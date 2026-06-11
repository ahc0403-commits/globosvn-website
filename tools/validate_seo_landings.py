#!/usr/bin/env python3
"""Validate static SEO landing pages and search infrastructure."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://www.globos.world"
SLUGS = [
    "vietnam-market-entry",
    "vietnam-company-registration",
    "vietnam-cosmetics-registration",
    "vietnam-fnb-franchise-entry",
    "vietnam-ecommerce-entry",
    "vietnam-tiktok-shopee-marketing",
    "vietnam-distribution-logistics",
    "vietnam-sourcing",
]
CAPABILITY_SLUGS = [
    "franchise-expansion",
    "fb-market-entry",
    "direct-store-operations",
    "legal-advisory",
    "it-systems-development",
    "it-market-entry",
    "beauty-market-entry",
    "vietnam-sourcing",
    "marketing-services",
    "master-brand-acquisition",
]
REQUIRED_KO_TERMS = {
    "vietnam-market-entry": ["베트남 진출", "베트남 시장 진출", "베트남 진출 전략"],
    "vietnam-company-registration": ["베트남 법인 설립", "베트남 법인 설립 비용", "베트남 법인 설립 자본금"],
    "vietnam-cosmetics-registration": ["베트남 화장품 수출", "베트남 화장품 인허가", "베트남 화장품 제품등록"],
    "vietnam-fnb-franchise-entry": ["베트남 식당 창업", "베트남 카페 창업", "베트남 한식당 창업"],
    "vietnam-ecommerce-entry": ["베트남 쇼피 입점", "쇼피 베트남 판매", "베트남 틱톡샵 입점"],
    "vietnam-tiktok-shopee-marketing": ["베트남 틱톡 마케팅", "베트남 틱톡 광고", "베트남 인플루언서 마케팅"],
    "vietnam-distribution-logistics": ["베트남 유통업체", "베트남 통관대행", "베트남 수입관세"],
    "vietnam-sourcing": ["베트남 소싱", "베트남 소싱 업체", "베트남 식자재 유통"],
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_json_ld(content: str, path: Path) -> list:
    blocks = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', content, re.S)
    if not blocks:
        fail(f"{path} missing JSON-LD")
    parsed = []
    for block in blocks:
        try:
            value = json.loads(block)
        except json.JSONDecodeError as exc:
            fail(f"{path} invalid JSON-LD: {exc}")
        parsed.extend(value if isinstance(value, list) else [value])
    return parsed


def validate_page(lang: str, slug: str) -> None:
    path = ROOT / lang / slug / "index.html"
    if not path.exists():
        fail(f"missing {path}")
    content = path.read_text(encoding="utf-8")
    canonical = f"{DOMAIN}/{lang}/{slug}/"
    other = "en" if lang == "ko" else "ko"
    checks = [
        (f'<html class="scroll-smooth" lang="{lang}">' in content, "html lang"),
        ("<title>" in content and "</title>" in content, "title"),
        ('<meta name="description"' in content, "description"),
        (f'<link rel="canonical" href="{canonical}"' in content, "canonical"),
        (f'hreflang="{lang}" href="{canonical}"' in content, "self hreflang"),
        (f'hreflang="{other}" href="{DOMAIN}/{other}/{slug}/"' in content, "alternate hreflang"),
        ('hreflang="x-default"' in content, "x-default hreflang"),
        ("../../assets/fonts.css" in content, "shared fonts"),
        ("contact@globos.world" in content, "contact email"),
        ("FAQPage" in content, "FAQ schema"),
        ("BreadcrumbList" in content, "breadcrumb schema"),
        ("@type\": \"Service\"" in content, "service schema"),
        ("<details" in content, "visible FAQ"),
        ("Globos Holdings" in content, "brand"),
        ("in-house ERP" in content, "memory rule wording"),
    ]
    for ok, label in checks:
        if not ok:
            fail(f"{path} missing {label}")
    if lang == "ko":
        missing_terms = [term for term in REQUIRED_KO_TERMS[slug] if term not in content]
        if missing_terms:
            fail(f"{path} missing KO search terms: {missing_terms}")
    data = extract_json_ld(content, path)
    types = {item.get("@type") for item in data if isinstance(item, dict)}
    for required in {"Organization", "Service", "FAQPage", "BreadcrumbList"}:
        if required not in types:
            fail(f"{path} missing {required} JSON-LD")


def validate_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        fail("missing sitemap.xml")
    tree = ET.parse(path)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = {node.text for node in tree.findall(".//sm:loc", namespace)}
    for required_url in [f"{DOMAIN}/", f"{DOMAIN}/site-map", f"{DOMAIN}/contact"]:
        if required_url not in locs:
            fail(f"sitemap missing {required_url}")
    for lang in ("ko", "en"):
        for slug in SLUGS:
            url = f"{DOMAIN}/{lang}/{slug}/"
            if url not in locs:
                fail(f"sitemap missing {url}")
    for lang in ("ko", "en"):
        for slug in CAPABILITY_SLUGS:
            url = f"{DOMAIN}/{lang}/capabilities/{slug}"
            if url not in locs:
                fail(f"sitemap missing {url}")


def validate_site_map_page() -> None:
    path = ROOT / "site-map.html"
    if not path.exists():
        fail("missing site-map.html")
    content = path.read_text(encoding="utf-8")
    required = [
        "Globos Holdings 웹사이트의 전체 페이지",
        "id=\"directory\"",
        "id=\"entry-problems\"",
        "상황별 바로가기",
        "ko/vietnam-market-entry/",
        "en/vietnam-market-entry/",
        "ko/capabilities/franchise-expansion.html",
        "contact@globos.world",
    ]
    for needle in required:
        if needle not in content:
            fail(f"site-map.html missing {needle}")


def validate_robots() -> None:
    path = ROOT / "robots.txt"
    if not path.exists():
        fail("missing robots.txt")
    content = path.read_text(encoding="utf-8")
    if "Allow: /" not in content or f"Sitemap: {DOMAIN}/sitemap.xml" not in content:
        fail("robots.txt missing Allow or Sitemap")


def validate_home_links() -> None:
    content = (ROOT / "index.html").read_text(encoding="utf-8")
    for lang in ("ko", "en"):
        for slug in SLUGS:
            href = f"{lang}/{slug}/"
            if href not in content:
                fail(f"homepage missing internal link {href}")
    for slug in CAPABILITY_SLUGS:
        if f'data-capability-link="{slug}"' not in content:
            fail(f"homepage missing capability language link {slug}")


def validate_capability_pages() -> None:
    for lang in ("ko", "en"):
        other = "en" if lang == "ko" else "ko"
        for slug in CAPABILITY_SLUGS:
            path = ROOT / lang / "capabilities" / f"{slug}.html"
            if not path.exists():
                fail(f"missing {path}")
            content = path.read_text(encoding="utf-8")
            checks = [
                (f'<html class="scroll-smooth" lang="{lang}">' in content, "html lang"),
                (f'<link rel="canonical" href="{DOMAIN}/{lang}/capabilities/{slug}"' in content, "canonical"),
                (f'hreflang="{other}" href="{DOMAIN}/{other}/capabilities/{slug}"' in content, "alternate hreflang"),
                ("../../assets/fonts.css" in content, "shared fonts"),
                ("contact@globos.world" in content, "contact email"),
                ('"@type":"Service"' in content or '"@type": "Service"' in content, "service schema"),
                ("Globos Holdings" in content, "brand"),
            ]
            for ok, label in checks:
                if not ok:
                    fail(f"{path} missing {label}")
            if lang == "ko" and "베트남" not in content:
                fail(f"{path} missing Korean Vietnam copy")
            if lang == "en" and "Vietnam" not in content:
                fail(f"{path} missing English Vietnam copy")


def validate_vercel() -> None:
    content = (ROOT / "vercel.json").read_text(encoding="utf-8")
    for route in ["/ko/:slug", "/en/:slug", "/ko/capabilities/:slug", "/en/capabilities/:slug"]:
        if route not in content:
            fail(f"vercel.json missing rewrite {route}")


def main() -> None:
    for lang in ("ko", "en"):
        for slug in SLUGS:
            validate_page(lang, slug)
    validate_sitemap()
    validate_site_map_page()
    validate_robots()
    validate_home_links()
    validate_capability_pages()
    validate_vercel()
    print(f"Validated {len(SLUGS) * 2} SEO landing pages, {len(CAPABILITY_SLUGS) * 2} capability pages, sitemap, robots, homepage links, and Vercel rewrites")


if __name__ == "__main__":
    main()
