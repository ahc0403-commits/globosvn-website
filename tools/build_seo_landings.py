#!/usr/bin/env python3
"""Generate static SEO landing pages for Globos Holdings."""
from __future__ import annotations

import html
import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://www.globos.world"
CONTACT_EMAIL = "contact@globos.world"


PAGES = [
    {
        "slug": "vietnam-market-entry",
        "ko_title": "베트남 진출 컨설팅 | 시장 진출 전략과 현지 운영 실행",
        "en_title": "Vietnam Market Entry Consulting | Strategy to Local Execution",
        "ko_description": "베트남 진출, 베트남 시장 진출 전략, 법인 설립, 인허가, 유통, 마케팅, 점포 운영을 현지 실행 구조로 연결하는 Globos Holdings 솔루션.",
        "en_description": "Globos Holdings supports Vietnam market entry with market strategy, entity setup coordination, licensing, distribution, marketing localization, store operations, ERP, POS, and delivery infrastructure.",
        "ko_h1": "베트남 진출, 전략보다 중요한 현지 실행팀.",
        "en_h1": "Vietnam market entry needs an execution structure, not just a strategy deck.",
        "ko_intro": "시장성은 있어도 법인, 인허가, 유통, 마케팅, 점포 운영에서 막히는 브랜드를 위한 현지 실행팀. 2024년부터 베트남 점포를 운영해 온 Globos Holdings의 실행 기반.",
        "en_intro": "Companies entering Vietnam must evaluate market fit, company setup, licensing, distribution, marketing, and operating infrastructure together. Globos Holdings connects market-entry strategy to local execution through active Vietnam operations.",
        "ko_problem": "주요 검색 의도는 베트남 진출 전략, 진출 컨설팅, 한국 기업 진출 사례, 실패 사례. 핵심 병목은 보고서보다 현지에서 움직이는 운영 구조.",
        "en_problem": "Searchers compare Vietnam market-entry strategy, consulting, Korean company examples, and failure cases. The real failure point is often not research, but the absence of local execution structure.",
        "keywords": ["베트남 진출", "베트남 시장 진출", "베트남 진출 전략", "베트남 진출 컨설팅", "Vietnam market entry", "Vietnam market entry strategy"],
        "services_ko": ["시장 진입 가설과 현지 실행 범위 정리", "법인 설립, 인허가, 유통, 마케팅, 점포 운영 경로 설계", "ERP, SaaS POS, 배달 앱 기반을 포함한 운영 모델 연결"],
        "services_en": ["Clarify market-entry assumptions and execution scope", "Map entity setup, licensing, distribution, marketing, and store operations", "Connect ERP, SaaS POS, and delivery infrastructure into the operating model"],
        "faqs_ko": [
            ["베트남 진출 전 우선 확인 사항", "시장 규모보다 현지 운영 주체, 법적 구조, 유통 구조, 마케팅 실행 구조 우선 확인."],
            ["Globos Holdings와 단순 컨설팅의 차이", "2024년부터 베트남 실제 점포 운영. ERP, POS, 배달 앱 기반을 갖춘 실행형 운영 파트너."],
            ["적합 업종", "F&B, 프랜차이즈, 뷰티, 리테일, 이커머스, 유통형 브랜드."],
            ["초기 상담 준비 자료", "브랜드 소개, 목표 지역, 제품과 서비스, 예상 투자 범위, 필요한 현지 기능."],
        ],
        "faqs_en": [
            ["What should be checked first before entering Vietnam?", "Before market size, companies should confirm who will operate locally and how legal, distribution, marketing, and store execution will work."],
            ["How is Globos Holdings different from a presentation-only consultant?", "Globos Holdings operates stores in Vietnam and connects strategy to ERP, POS, delivery, and local operating routines."],
            ["Which industries fit this service?", "F&B, franchise, beauty, retail, ecommerce, and distribution-driven brands are the strongest fit."],
            ["What should we prepare for the first consultation?", "Prepare your brand profile, target region, products or services, investment range, and required local functions."],
        ],
    },
    {
        "slug": "vietnam-company-registration",
        "ko_title": "베트남 법인 설립 | 비용, 자본금, 외투법인, 대표사무소",
        "en_title": "Vietnam Company Registration | Cost, Capital, Representative Office",
        "ko_description": "베트남 법인 설립 절차, 비용, 자본금, 외투법인, 대표사무소, 사업자등록, 투자허가, 영업허가를 사업 실행 관점으로 정리한 솔루션.",
        "en_description": "Vietnam company registration support covering setup process, capital, foreign-invested company structure, representative office, business registration, investment licensing, and operating readiness.",
        "ko_h1": "베트남 법인 설립, 비용표보다 중요한 운영 구조.",
        "en_h1": "Vietnam company registration starts with the business structure, not only the filing checklist.",
        "ko_intro": "법인만 세워도 사업은 움직이지 않는 베트남 시장. 외투법인, 대표사무소, 투자허가, 영업허가를 실제 운영 방식과 함께 보는 설립 구조.",
        "en_intro": "Company setup, foreign-invested structures, representative offices, business registration, investment licensing, and operating permits depend on business type and operating model. Globos Holdings coordinates advisory support with execution planning.",
        "ko_problem": "주요 검색 의도는 베트남 법인 설립 비용, 절차, 자본금, 대행업체. 실제 출발점은 사업 운영 형태와 허가 범위.",
        "en_problem": "Searchers look for Vietnam company setup cost, process, capital, and service providers, but the real decision starts with how the business will operate.",
        "keywords": ["베트남 법인 설립", "베트남 법인 설립 비용", "베트남 법인 설립 자본금", "베트남 외투법인", "Vietnam company registration", "business setup cost in Vietnam"],
        "services_ko": ["법인 설립 목적과 업종별 실행 구조 정리", "외투법인, 대표사무소, 사업자등록, 투자허가 검토 조율", "세무, 회계, 노무, 법률 지원 조직 연결"],
        "services_en": ["Clarify the purpose of company setup and industry-specific structure", "Coordinate review of FIE, representative office, business registration, and investment licensing", "Connect tax, accounting, labor, and legal support functions"],
        "faqs_ko": [
            ["베트남 법인 설립 비용", "업종, 자본금, 외국인 투자 구조, 인허가 범위에 따른 변동."],
            ["대표사무소와 법인 차이", "대표사무소는 영업 활동 제한 가능성. 법인은 매출 발생과 운영 범위 확대. 업종별 검토 필요."],
            ["외투법인 자본금 기준", "업종과 허가 조건에 따른 요구 자본금 판단."],
            ["법률 서비스 범위", "법률 판단은 현지 전문가 조율. Globos Holdings는 사업 실행 구조와 운영 준비 연결."],
        ],
        "faqs_en": [
            ["Is Vietnam company setup cost fixed?", "No. Cost varies by industry, capital structure, foreign investment form, and licensing scope."],
            ["How is a representative office different from a company?", "A representative office usually has limited commercial activity, while a company can support broader revenue and operations."],
            ["Is there a capital requirement for a foreign-invested company?", "Capital expectations can vary by industry and licensing conditions."],
            ["Does Globos Holdings provide legal advice directly?", "Legal determinations are coordinated with local professionals while Globos Holdings connects the business and operating structure."],
        ],
    },
    {
        "slug": "vietnam-cosmetics-registration",
        "ko_title": "베트남 화장품 인허가 | 제품등록, 인증, 라벨링, 통관",
        "en_title": "Vietnam Cosmetics Registration | Notification, Labeling, Customs",
        "ko_description": "베트남 화장품 수출, 인증, 인허가, 제품등록, 위생허가, 라벨링, CFS, PIF, 통관, 유통업체 연결을 포함한 시장 진입 절차.",
        "en_description": "Vietnam cosmetics registration and market-entry support covering product notification, labeling, CFS, PIF, customs clearance, import coordination, and distributor readiness.",
        "ko_h1": "베트남 화장품 진출, 제품등록부터 유통까지.",
        "en_h1": "Vietnam cosmetics entry requires registration, labeling, customs, and distribution to move together.",
        "ko_intro": "인증 하나로 끝나지 않는 화장품 수출. 성분, 제품등록, 라벨링, CFS와 PIF, 수입자, 통관, 유통 채널의 동시 준비.",
        "en_intro": "Cosmetics export does not end with one approval. Ingredients, product notification, labeling, CFS/PIF, importer coordination, customs, and distribution channels must move together.",
        "ko_problem": "주요 검색 의도는 베트남 화장품 수출, 인증, 인허가, 제품등록, 위생허가, 라벨링, 통관. 실제 실행은 하나의 출시 흐름.",
        "en_problem": "Searchers separate cosmetics export, certification, registration, labeling, and customs, but execution works as one launch flow.",
        "keywords": ["베트남 화장품 수출", "베트남 화장품 인허가", "베트남 화장품 제품등록", "베트남 화장품 라벨링", "Vietnam cosmetics registration", "Vietnam cosmetic product notification"],
        "services_ko": ["제품별 인허가/등록 준비 항목 정리", "라벨링, CFS, PIF, 통관 요구사항 조율", "유통업체, 이커머스, 마케팅 실행 경로 연결"],
        "services_en": ["Map registration and notification requirements by product", "Coordinate labeling, CFS, PIF, and customs requirements", "Connect distribution, ecommerce, and marketing execution routes"],
        "faqs_ko": [
            ["베트남 화장품 제품등록 필요성", "시장 판매 전 제품별 등록 또는 통지 절차 검토 필요."],
            ["화장품 라벨링 현지화", "베트남 판매용 현지 라벨 요건과 표시 문구 검토."],
            ["CFS와 PIF 검토", "제품 유형과 수출/등록 절차에 따른 CFS, PIF 등 문서 검토."],
            ["등록 이후 유통 연결", "등록 준비 이후 유통, 쇼피와 틱톡샵, 마케팅 경로 연결 검토."],
        ],
        "faqs_en": [
            ["Is product notification required for Vietnam cosmetics?", "In most market-sale cases, product-level notification or registration review is needed before launch."],
            ["Does labeling need localization?", "Yes. Vietnam sales require local labeling and claim review."],
            ["Are CFS and PIF required?", "Depending on product type and procedure, CFS, PIF, and related documentation may be required."],
            ["Can distribution be connected after registration?", "Globos Holdings connects registration preparation with distribution, Shopee/TikTok Shop, and marketing routes."],
        ],
    },
    {
        "slug": "vietnam-fnb-franchise-entry",
        "ko_title": "베트남 식당 창업과 F&B 프랜차이즈 진출 | 카페, 한식당, 매장 운영",
        "en_title": "Vietnam F&B Franchise Entry | Restaurant, Cafe, Korean Food Launch",
        "ko_description": "베트남 식당 창업, 카페 창업, 한식당 창업, 외식업 진출, 프랜차이즈 창업을 점포 운영, 인력, POS, 배달, 공급망 관점으로 지원.",
        "en_description": "Vietnam F&B and franchise entry support for restaurants, cafes, Korean food brands, store operations, staffing, POS workflows, delivery readiness, and supply chain setup.",
        "ko_h1": "베트남 식당과 카페 창업, 오픈보다 중요한 운영 지속성.",
        "en_h1": "Vietnam restaurant and cafe entry is about operating durability, not only opening day.",
        "ko_intro": "오픈보다 어려운 일은 매일 같은 품질로 운영되는 매장. 입지, 인허가, 인력, 원부자재, POS, 배달, 마케팅, 점포 SOP를 함께 묶는 현지 실행 구조.",
        "en_intro": "Vietnam F&B entry requires location, licensing, staffing, ingredients, POS, delivery, marketing, and store SOPs to work together. Globos Holdings designs the local execution structure from real store operations.",
        "ko_problem": "주요 검색 의도는 베트남 창업 현실, 식당 창업, 카페 창업, 한식당 창업, 프랜차이즈 창업. 실제 병목은 오픈 후 운영 통제.",
        "en_problem": "Searchers look for restaurant, cafe, Korean food, and franchise entry, but the bottleneck is usually post-launch operating control.",
        "keywords": ["베트남 식당 창업", "베트남 카페 창업", "베트남 한식당 창업", "베트남 외식업 진출", "Vietnam restaurant business", "Vietnam F&B market entry"],
        "services_ko": ["F&B 브랜드 현지화와 매장 오픈 경로 설계", "점포 SOP, 인력 운영, POS, 배달 앱 준비", "식자재, 공급망, 마케팅, 프랜차이즈 전개 연결"],
        "services_en": ["Design F&B localization and store launch route", "Prepare store SOPs, staffing routines, POS, and delivery readiness", "Connect ingredients, supply chain, marketing, and franchise rollout"],
        "faqs_ko": [
            ["베트남 식당 창업 핵심 리스크", "오픈보다 인력, 원가, 공급망, 현장 관리, 배달 운영의 흔들림."],
            ["카페와 한식당 지원 범위", "카페, 한식당, F&B 프랜차이즈 운영 모델 검토."],
            ["점포 운영 구조", "브랜드, 지역, 운영 범위에 따른 직접 운영, 공동 운영, 운영 컨설팅 검토."],
            ["배달앱 운영 포함 범위", "배달 운영 흐름과 POS, 주문, 정산 루틴 검토."],
        ],
        "faqs_en": [
            ["What is the biggest risk in Vietnam restaurant entry?", "The larger risk is not opening day, but staffing, cost control, supply chain, field management, and delivery operations."],
            ["Can cafes and Korean restaurants be supported?", "Yes. Cafe, Korean restaurant, and F&B franchise models can be reviewed."],
            ["Can store operations be handled locally?", "Depending on brand, region, and scope, direct operation, co-operation, or operating advisory models can be reviewed."],
            ["Is delivery app operation included?", "Delivery workflows, POS/order routines, and settlement flows are reviewed together."],
        ],
    },
    {
        "slug": "vietnam-ecommerce-entry",
        "ko_title": "베트남 쇼피 라자다 틱톡샵 진출 | 입점, 판매, 셀러 운영",
        "en_title": "Vietnam Ecommerce Entry | Shopee, Lazada, TikTok Shop Seller Operations",
        "ko_description": "베트남 쇼피 입점, 라자다 입점, 틱톡샵 입점, 온라인 판매, 셀러 운영, 상품 등록, 현지 마케팅, 물류와 통관 연결 지원.",
        "en_description": "Vietnam ecommerce entry support for Shopee, Lazada, TikTok Shop, seller operations, product listing, local marketing, fulfillment, customs, and distributor coordination.",
        "ko_h1": "베트남 온라인 판매, 쇼피 라자다 틱톡샵 운영 구조.",
        "en_h1": "Vietnam ecommerce entry starts with Shopee, Lazada, and TikTok Shop operating structure.",
        "ko_intro": "상품 등록만으로 끝나지 않는 쇼피, 라자다, 틱톡샵 운영. 현지 셀러 구조, 콘텐츠, 광고, 물류, 통관, CS, 정산 루틴까지 연결되는 판매 구조.",
        "en_intro": "Shopee, Lazada, and TikTok Shop entry is not just product listing. Seller structure, content, ads, logistics, customs, customer service, and settlement routines must be prepared.",
        "ko_problem": "주요 검색 의도는 쇼피 베트남 판매, 베트남 쇼피 입점, 라자다 입점방법, 베트남 틱톡샵. 핵심 의도는 마케팅보다 판매 운영.",
        "en_problem": "Searchers look for Shopee Vietnam selling, Lazada entry, and TikTok Shop Vietnam. This intent is closer to commercial operation than general marketing.",
        "keywords": ["베트남 쇼피 입점", "쇼피 베트남 판매", "베트남 라자다 입점", "베트남 틱톡샵 입점", "TikTok Shop Vietnam", "Shopee Vietnam seller"],
        "services_ko": ["쇼피, 라자다, 틱톡샵 입점 가능성 검토", "상품 등록, 콘텐츠, 광고, CS, 정산 운영 구조 설계", "물류, 통관, 유통, 마케팅 실행과 연결"],
        "services_en": ["Review Shopee, Lazada, and TikTok Shop entry feasibility", "Design listing, content, ads, CS, and settlement routines", "Connect logistics, customs, distribution, and marketing execution"],
        "faqs_ko": [
            ["한국 회사의 베트남 쇼피 입점", "셀러 구조, 현지 사업자, 상품군, 물류 방식 기준 가능성 검토."],
            ["틱톡샵 베트남의 성격", "마케팅 채널이자 판매 채널. 콘텐츠와 라이브커머스의 판매 운영 연결 구조."],
            ["라자다와 쇼피 동시 운영", "상품군, 운영 인력, 마케팅 예산 기준 우선순위 설정."],
            ["Globos Holdings 지원 범위", "입점 구조, 상품 등록, 현지 운영 루틴, 마케팅, 물류와 통관 연결 검토."],
        ],
        "faqs_en": [
            ["Can a Korean company sell on Shopee Vietnam?", "Feasibility depends on seller structure, local entity, product category, and logistics model."],
            ["Is TikTok Shop Vietnam marketing or sales?", "It is both: content and live commerce are directly connected to sales operations."],
            ["Should Lazada and Shopee be operated together?", "Priority should depend on category, operating team, and marketing budget."],
            ["What does Globos Holdings support?", "We review entry structure, listing, local operating routines, marketing, and logistics/customs connection."],
        ],
    },
    {
        "slug": "vietnam-tiktok-shopee-marketing",
        "ko_title": "베트남 틱톡 쇼피 마케팅 | 광고, 인플루언서, 라이브커머스",
        "en_title": "Vietnam TikTok and Shopee Marketing | Ads, Influencers, Live Commerce",
        "ko_description": "베트남 틱톡 마케팅, 틱톡 광고, 틱톡샵 대행, 쇼피 마케팅, SNS 마케팅, 인플루언서, 라이브커머스 실행 구조 지원.",
        "en_description": "Vietnam TikTok, Shopee, influencer, SNS, live commerce, and ecommerce marketing support connected to sales execution and local brand localization.",
        "ko_h1": "베트남 마케팅, 틱톡 쇼피 인플루언서 판매 전환.",
        "en_h1": "Vietnam marketing must connect TikTok, Shopee, influencers, and sales conversion.",
        "ko_intro": "단순 광고 집행보다 중요한 채널별 판매 구조와 콘텐츠 현지화. 틱톡 광고, 틱톡샵, 쇼피 캠페인, 인플루언서, 라이브커머스가 실제 매출로 이어지는 운영 구조.",
        "en_intro": "Vietnam online marketing is not only ad buying. Channel-specific sales structure and content localization matter. TikTok ads, TikTok Shop, Shopee campaigns, influencers, and live commerce must connect to sales operations.",
        "ko_problem": "주요 검색 의도는 베트남 틱톡 마케팅, 틱톡 광고, 틱톡 대행, 쇼피 마케팅, 베트남 인플루언서 마케팅. 채널별 운영법 필요.",
        "en_problem": "Searchers look for Vietnam TikTok marketing, TikTok ads, TikTok agency, Shopee marketing, and influencer marketing. Each channel needs a distinct operating method.",
        "keywords": ["베트남 틱톡 마케팅", "베트남 틱톡 광고", "베트남 쇼피 마케팅", "베트남 인플루언서 마케팅", "Vietnam TikTok marketing", "Shopee Vietnam marketing agency"],
        "services_ko": ["틱톡, 쇼피, SNS 채널별 캠페인 구조 설계", "인플루언서, 숏폼, 라이브커머스 실행 조율", "이커머스 판매, 매장 방문, 브랜드 런칭 목표와 연결"],
        "services_en": ["Design campaign structures by TikTok, Shopee, and SNS channel", "Coordinate influencer, short-form, and live commerce execution", "Connect campaigns to ecommerce sales, store visits, and brand launch goals"],
        "faqs_ko": [
            ["베트남 틱톡 마케팅 적합 브랜드", "뷰티, F&B, 리테일, 소비재 등 시각 콘텐츠와 구매 전환 연결 업종."],
            ["쇼피 마케팅과 틱톡 마케팅 병행", "제품군에 따라 차이. 인지도와 판매 전환 연결 목적의 통합 설계."],
            ["인플루언서 섭외 포함 범위", "캠페인 목적과 예산 기준 현지 인플루언서와 콘텐츠 실행 구조 검토."],
            ["광고 대행과의 차이", "단순 광고 집행보다 판매 운영, 콘텐츠, 채널 전략 통합 검토."],
        ],
        "faqs_en": [
            ["Which brands fit Vietnam TikTok marketing?", "Beauty, F&B, retail, and consumer brands that benefit from visual content and conversion fit well."],
            ["Should Shopee and TikTok marketing be planned together?", "Often yes, especially when awareness and sales conversion need to connect."],
            ["Can influencer execution be included?", "Depending on campaign goals and budget, local influencer and content execution can be reviewed."],
            ["Is this only ad agency work?", "No. We connect advertising with sales operations, content, and channel strategy."],
        ],
    },
    {
        "slug": "vietnam-distribution-logistics",
        "ko_title": "베트남 유통 통관 물류 | 유통업체, 통관대행, 수입관세",
        "en_title": "Vietnam Distribution, Customs, and Logistics | Distributor and Import Support",
        "ko_description": "베트남 유통업체, 유통망, 유통채널, 통관, 통관대행, 통관 비용, 수입통관, 수입관세, 물류업체, 냉장 물류 실행 구조.",
        "en_description": "Vietnam distribution, customs clearance, import duties, logistics partners, distributor coordination, warehousing, cold chain, and route-to-market support.",
        "ko_h1": "베트남 유통, 업체 리스트보다 중요한 통관과 판매 채널 구조.",
        "en_h1": "Vietnam distribution is not a vendor list. It is the structure from customs to sales channels.",
        "ko_intro": "제품을 베트남에 들여오는 일과 실제로 판매되는 일 사이의 간격. 통관, 수입자, 관세, 창고, 물류, 유통업체, 판매 채널을 묶는 실행 경로.",
        "en_intro": "For products to enter Vietnam, customs, importer coordination, duties, warehousing, logistics, distributors, and sales channels must connect. Globos Holdings reviews practical routes to market after entry.",
        "ko_problem": "주요 검색 의도는 베트남 유통업체, 유통망, 통관대행, 수입관세, 물류업체. 핵심 병목은 기능 분리로 인한 일정과 원가 흔들림.",
        "en_problem": "Searchers look for distributors, customs brokers, import duties, and logistics companies. If these functions move separately, launch timing and cost control suffer.",
        "keywords": ["베트남 유통업체", "베트남 유통망", "베트남 통관대행", "베트남 수입관세", "베트남 물류업체", "Vietnam distributor"],
        "services_ko": ["제품군별 유통 경로와 수입 구조 검토", "통관, 관세, 물류, 창고, 냉장 물류 실행 조율", "오프라인 유통, 이커머스, 매장 운영 채널 연결"],
        "services_en": ["Review route-to-market and import structure by product category", "Coordinate customs, duties, logistics, warehousing, and cold chain execution", "Connect offline distribution, ecommerce, and store operating channels"],
        "faqs_ko": [
            ["베트남 유통업체만으로 충분한지 여부", "수입자, 통관, 관세, 물류, 판매 채널의 동시 검토 필요."],
            ["통관 비용 산정 기준", "제품군, HS 코드, 서류, 검사 여부, 물류 방식 기준 변동."],
            ["냉장 물류와 식품 유통", "제품군과 지역 기준 식자재, 냉장, 매장 공급망 검토."],
            ["화장품 유통 포함 범위", "인허가, 라벨링, 통관, 유통업체 검토의 동시 진행 필요."],
        ],
        "faqs_en": [
            ["Is finding a distributor enough?", "No. Importer, customs, duties, logistics, and sales channels must be reviewed together."],
            ["How is customs cost determined?", "It can vary by category, HS code, documents, inspection, and logistics method."],
            ["Can cold chain or food distribution be reviewed?", "Depending on product and region, ingredient, cold chain, and store supply routes can be reviewed."],
            ["Does this include cosmetics distribution?", "Cosmetics require registration, labeling, customs, and distributor review together."],
        ],
    },
    {
        "slug": "vietnam-sourcing",
        "ko_title": "베트남 소싱 | 제조, 식자재, 공급망, 현지 파트너 발굴",
        "en_title": "Vietnam Sourcing | Manufacturing, Ingredients, Supply Chain, Local Partners",
        "ko_description": "베트남 소싱 업체, 제조 소싱, 식자재 유통, 현지 공급망, 파트너 발굴, 점포 운영용 공급처 개발 지원.",
        "en_description": "Vietnam sourcing support for manufacturing, ingredients, supplier development, local partner discovery, supply chain coordination, and store-operation needs.",
        "ko_h1": "베트남 소싱, 가격 비교보다 중요한 운영 가능한 공급망.",
        "en_h1": "Vietnam sourcing is not only price comparison. It is building an operating supply chain.",
        "ko_intro": "업체 리스트보다 중요한 실제 납품 가능성. 품질, 납기, 통관, 물류, 매장 공급, 정산, 지속 운영 가능성까지 보는 공급망 설계.",
        "en_intro": "Sourcing does not end with factory or supplier lists. Quality, delivery, customs, logistics, store supply, settlement, and continuity must be reviewed together.",
        "ko_problem": "주요 검색 의도는 베트남 소싱, 소싱 업체, 제조공장, 식자재 유통. 브랜드 운영 핵심은 실제 납품 가능한 공급망.",
        "en_problem": "Searchers look for sourcing agents, factories, and ingredient distribution. Brand operations need suppliers that can actually deliver consistently.",
        "keywords": ["베트남 소싱", "베트남 소싱 업체", "베트남 제조 소싱", "베트남 식자재 유통", "Vietnam sourcing agent", "Vietnam supplier development"],
        "services_ko": ["제품과 브랜드 운영에 필요한 공급처 조건 정리", "제조, 식자재, 부자재, 물류 연결 가능성 검토", "점포 운영, 유통, 이커머스 판매와 연결되는 공급망 설계"],
        "services_en": ["Clarify supplier requirements for product and brand operations", "Review manufacturing, ingredients, packaging, and logistics feasibility", "Design supply chains connected to store operations, distribution, and ecommerce sales"],
        "faqs_ko": [
            ["베트남 소싱 업체 리스트", "단순 리스트보다 제품 조건, 품질, 납기, 물류 가능성 기준 검토."],
            ["식자재 유통 포함 범위", "F&B 운영용 식자재, 부자재, 매장 공급망 검토."],
            ["제조 소싱과 유통 소싱 차이", "제조 소싱은 생산처 중심. 유통 소싱은 판매와 운영 채널에 맞춘 공급 구조 중심."],
            ["소싱 이후 운영 연결", "공급처 개발과 점포 운영, 유통, 물류, 이커머스 판매의 연결 검토."],
        ],
        "faqs_en": [
            ["Do you provide supplier lists?", "Rather than simple lists, suppliers are reviewed by product requirements, quality, delivery, and logistics feasibility."],
            ["Is ingredient distribution included?", "For F&B operations, ingredients, packaging, and store supply routes can be reviewed."],
            ["How are manufacturing sourcing and distribution sourcing different?", "Manufacturing sourcing focuses on production, while distribution sourcing focuses on supply structures for sales and operations."],
            ["Can sourcing connect to operations?", "Yes. Supplier development should connect to store operations, distribution, logistics, and ecommerce sales."],
        ],
    },
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def lang_path(lang: str, slug: str) -> str:
    return f"/{lang}/{slug}/"


def abs_url(lang: str, slug: str) -> str:
    return f"{DOMAIN}{lang_path(lang, slug)}"


def render_json_ld(page: dict, lang: str) -> str:
    is_ko = lang == "ko"
    slug = page["slug"]
    title = page["ko_title"] if is_ko else page["en_title"]
    description = page["ko_description"] if is_ko else page["en_description"]
    faqs = page["faqs_ko"] if is_ko else page["faqs_en"]
    services = page["services_ko"] if is_ko else page["services_en"]
    data = [
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "@id": f"{DOMAIN}/#organization",
            "name": "Globos Holdings",
            "url": DOMAIN + "/",
            "email": CONTACT_EMAIL,
            "foundingDate": "2024",
            "areaServed": ["Vietnam", "South Korea"],
            "knowsAbout": page["keywords"],
        },
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "@id": f"{abs_url(lang, slug)}#service",
            "name": title,
            "description": description,
            "provider": {"@id": f"{DOMAIN}/#organization"},
            "areaServed": ["Vietnam", "South Korea"],
            "serviceType": services,
            "url": abs_url(lang, slug),
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "@id": f"{abs_url(lang, slug)}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in faqs
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Globos Holdings", "item": DOMAIN + "/"},
                {"@type": "ListItem", "position": 2, "name": "SEO Landing", "item": abs_url(lang, slug)},
            ],
        },
    ]
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_page(page: dict, lang: str) -> str:
    is_ko = lang == "ko"
    other = "en" if is_ko else "ko"
    slug = page["slug"]
    title = page["ko_title"] if is_ko else page["en_title"]
    description = page["ko_description"] if is_ko else page["en_description"]
    h1 = page["ko_h1"] if is_ko else page["en_h1"]
    intro = page["ko_intro"] if is_ko else page["en_intro"]
    problem = page["ko_problem"] if is_ko else page["en_problem"]
    services = page["services_ko"] if is_ko else page["services_en"]
    faqs = page["faqs_ko"] if is_ko else page["faqs_en"]
    keywords = page["keywords"]
    html_lang = "ko" if is_ko else "en"
    home_href = "../../index.html"
    contact_href = "../../contact.html"
    lang_label = "English" if is_ko else "한국어"
    eyebrow = "검색 의도별 실행 랜딩" if is_ko else "Search-intent execution landing"
    overview_label = "핵심 검색어" if is_ko else "Primary search phrases"
    proof_label = "운영 증거" if is_ko else "Operating proof"
    proof_text = (
        "2024년 베트남 운영 개시. 현재 8개 점포 운영. 파트너사 20여 개사 기반. 2030년까지 300개 점포와 파트너사 50개 목표. in-house ERP, SaaS POS, 배달 앱 기반의 실제 운영 구조."
        if is_ko
        else "Globos Holdings began Vietnam operations in 2024, currently operates 8 stores, works with 20+ partner firms, and targets 300 stores with 50 partner firms by 2030. in-house ERP, SaaS POS, and delivery app infrastructure are connected to the operating model."
    )
    can_do = "지원 범위" if is_ko else "What Globos Holdings supports"
    search_problem = "검색 의도" if is_ko else "The problem searchers are actually trying to solve"
    faq_title = "핵심 체크포인트" if is_ko else "Frequently Asked Questions"
    cta_title = "베트남에서 막히는 지점 공유." if is_ko else "Share the Vietnam execution bottleneck first."
    cta_body = (
        "브랜드, 제품군, 목표 지역, 현재 준비 단계, 가장 막히는 지점. 그 지점에서 시작하는 다음 실행 경로."
        if is_ko
        else "Send your brand, product category, target region, current preparation stage, and bottleneck. We will map the next execution route."
    )
    cta_button = "문의" if is_ko else "Contact Globos Holdings"
    nav_guides = "SEO 랜딩" if is_ko else "SEO landings"
    nav_contact = "문의" if is_ko else "Contact"
    related_title = "관련 랜딩" if is_ko else "Related landing pages"
    all_pages = [
        (
            p["slug"],
            p["ko_title"].split(" | ")[0] if is_ko else p["en_title"].split(" | ")[0],
        )
        for p in PAGES
        if p["slug"] != slug
    ][:4]
    related_links = "\n".join(
        f'<a class="rounded-sm border border-line bg-white p-4 text-sm font-bold text-ink hover:border-navy" href="../{rel_slug}/">{esc(label)}</a>'
        for rel_slug, label in all_pages
    )
    keyword_tags = "\n".join(
        f'<li class="rounded-sm border border-line bg-white px-3 py-2 text-sm font-bold text-navy">{esc(keyword)}</li>'
        for keyword in keywords
    )
    service_items = "\n".join(
        f'<li class="flex gap-3"><span class="material-symbols-outlined mt-1 text-base text-cobalt" aria-hidden="true">check_circle</span><span>{esc(item)}</span></li>'
        for item in services
    )
    faq_items = "\n".join(
        f"""
        <details class="rounded-sm border border-line bg-white p-5">
          <summary class="cursor-pointer font-headline text-lg font-bold text-ink">{esc(q)}</summary>
          <p class="mt-4 leading-7 text-slatecopy">{esc(a)}</p>
        </details>
        """
        for q, a in faqs
    )
    json_ld = render_json_ld(page, lang)
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html class="scroll-smooth" lang="{html_lang}">
        <head>
          <meta charset="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>{esc(title)}</title>
          <meta name="description" content="{esc(description)}" />
          <meta name="robots" content="index, follow" />
          <link rel="canonical" href="{abs_url(lang, slug)}" />
          <link rel="alternate" hreflang="{lang}" href="{abs_url(lang, slug)}" />
          <link rel="alternate" hreflang="{other}" href="{abs_url(other, slug)}" />
          <link rel="alternate" hreflang="x-default" href="{abs_url('en', slug)}" />
          <meta property="og:type" content="website" />
          <meta property="og:title" content="{esc(title)}" />
          <meta property="og:description" content="{esc(description)}" />
          <meta property="og:url" content="{abs_url(lang, slug)}" />
          <meta property="og:site_name" content="Globos Holdings" />
          <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
          <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&amp;display=swap" rel="stylesheet" />
          <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css" rel="stylesheet" />
          <link href="../../assets/fonts.css" rel="stylesheet" />
          <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet" />
          <script>
            tailwind.config = {{
              theme: {{
                extend: {{
                  colors: {{
                    ink: '#071a31',
                    navy: '#002147',
                    cobalt: '#0b4d8f',
                    fog: '#f4f6f7',
                    line: '#d8dde3',
                    brass: '#c8a45d',
                    mint: '#5db79e',
                    slatecopy: '#5c6672'
                  }},
                  fontFamily: {{
                    body: ['Montserrat', 'sans-serif'],
                    headline: ['Montserrat', 'sans-serif'],
                    label: ['Montserrat', 'sans-serif'],
                    korean: ['Pretendard', 'sans-serif']
                  }},
                  boxShadow: {{ firm: '0 24px 60px rgba(0, 33, 71, 0.12)' }},
                  borderRadius: {{ DEFAULT: '0.125rem', sm: '0.125rem' }}
                }}
              }}
            }};
          </script>
          <style>
            :root {{ color-scheme: light; }}
            * {{ letter-spacing: 0 !important; }}
            body {{ background: #f4f6f7; color: #071a31; }}
            .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 350, 'GRAD' 0, 'opsz' 24; line-height: 1; }}
          </style>
          <script type="application/ld+json">
        {json_ld}
          </script>
        </head>
        <body class="font-body antialiased">
          <header class="sticky top-0 z-50 border-b border-line bg-white/95 backdrop-blur">
            <nav class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-5 py-4 lg:px-8" aria-label="Primary navigation">
              <a class="brand-name font-headline text-xl font-bold text-navy sm:text-2xl" href="{home_href}">Globos Holdings</a>
              <div class="hidden items-center gap-6 text-sm font-bold text-slatecopy md:flex">
                <a class="hover:text-navy" href="{home_href}#capabilities">{nav_guides}</a>
                <a class="hover:text-navy" href="{contact_href}">{nav_contact}</a>
              </div>
              <a class="rounded-sm border border-line bg-fog px-4 py-2 text-xs font-extrabold text-navy hover:border-navy" href="../../{other}/{slug}/">{lang_label}</a>
            </nav>
          </header>
          <main>
            <section class="bg-white">
              <div class="mx-auto grid max-w-7xl gap-10 px-5 py-16 lg:grid-cols-[1fr_360px] lg:px-8 lg:py-24">
                <div>
                  <p class="mb-6 text-xs font-extrabold uppercase text-cobalt">{eyebrow}</p>
                  <h1 class="font-headline text-4xl font-bold leading-tight text-ink md:text-6xl">{esc(h1)}</h1>
                  <p class="mt-7 max-w-3xl text-lg leading-8 text-slatecopy">{esc(intro)}</p>
                  <div class="mt-9 flex flex-col gap-3 sm:flex-row">
                    <a class="primary-action inline-flex items-center justify-center gap-2 rounded-sm bg-navy px-7 py-4 text-sm font-extrabold text-white hover:bg-cobalt" href="{contact_href}">{cta_button}<span class="material-symbols-outlined text-lg" aria-hidden="true">arrow_forward</span></a>
                    <a class="secondary-action inline-flex items-center justify-center gap-2 rounded-sm border border-line bg-white px-7 py-4 text-sm font-extrabold text-navy hover:border-navy" href="{home_href}">Globos Holdings</a>
                  </div>
                </div>
                <aside class="rounded-sm border border-line bg-fog p-6 shadow-firm">
                  <p class="text-xs font-extrabold uppercase text-cobalt">{overview_label}</p>
                  <ul class="mt-5 flex flex-wrap gap-2">
                    {keyword_tags}
                  </ul>
                </aside>
              </div>
            </section>

            <section class="border-y border-line bg-fog py-14">
              <div class="mx-auto grid max-w-7xl gap-8 px-5 lg:grid-cols-2 lg:px-8">
                <article class="rounded-sm border border-line bg-white p-7">
                  <h2 class="font-headline text-3xl font-bold text-ink">{search_problem}</h2>
                  <p class="mt-5 leading-8 text-slatecopy">{esc(problem)}</p>
                </article>
                <article class="rounded-sm border border-line bg-white p-7">
                  <h2 class="font-headline text-3xl font-bold text-ink">{proof_label}</h2>
                  <p class="mt-5 leading-8 text-slatecopy">{proof_text}</p>
                </article>
              </div>
            </section>

            <section class="bg-white py-14">
              <div class="mx-auto grid max-w-7xl gap-10 px-5 lg:grid-cols-[0.85fr_1.15fr] lg:px-8">
                <div>
                  <h2 class="font-headline text-3xl font-bold text-ink">{can_do}</h2>
                  <p class="mt-5 leading-8 text-slatecopy">{esc(description)}</p>
                </div>
                <ul class="grid gap-4 text-base leading-7 text-slatecopy">
                  {service_items}
                </ul>
              </div>
            </section>

            <section class="border-y border-line bg-fog py-14">
              <div class="mx-auto max-w-5xl px-5 lg:px-8">
                <h2 class="font-headline text-3xl font-bold text-ink">{faq_title}</h2>
                <div class="mt-8 grid gap-3">
                  {faq_items}
                </div>
              </div>
            </section>

            <section class="bg-white py-14">
              <div class="mx-auto grid max-w-7xl gap-8 px-5 lg:grid-cols-[1fr_1fr] lg:px-8">
                <div class="rounded-sm border border-line bg-[#071a31] p-8 text-white">
                  <h2 class="font-headline text-3xl font-bold">{cta_title}</h2>
                  <p class="mt-4 leading-8 text-white/70">{cta_body}</p>
                  <a class="primary-action mt-7 inline-flex items-center gap-2 rounded-sm bg-brass px-6 py-4 text-sm font-extrabold text-navy" href="{contact_href}">{cta_button}<span class="material-symbols-outlined text-lg" aria-hidden="true">mail</span></a>
                </div>
                <div>
                  <h2 class="font-headline text-2xl font-bold text-ink">{related_title}</h2>
                  <div class="mt-5 grid gap-3">
                    {related_links}
                  </div>
                </div>
              </div>
            </section>
          </main>
          <footer class="border-t border-line bg-white py-10">
            <div class="mx-auto flex max-w-7xl flex-col gap-4 px-5 text-sm text-slatecopy lg:flex-row lg:items-center lg:justify-between lg:px-8">
              <a class="brand-name font-headline text-2xl font-bold text-navy" href="{home_href}">Globos Holdings</a>
              <div class="flex flex-col gap-2 lg:text-right">
                <a class="hover:text-navy" href="mailto:{CONTACT_EMAIL}?subject=Globos Holdings Website Inquiry">{CONTACT_EMAIL}</a>
                <p>© 2026 Globos Holdings. All rights reserved.</p>
              </div>
            </div>
          </footer>
        </body>
        </html>
        """
    )


def render_sitemap() -> str:
    urls = [
        f"{DOMAIN}/",
        f"{DOMAIN}/contact",
        *[abs_url(lang, page["slug"]) for lang in ("ko", "en") for page in PAGES],
        *[f"{DOMAIN}/capabilities/{slug}" for slug in [
            "direct-store-operations",
            "franchise-expansion",
            "master-brand-acquisition",
            "fb-market-entry",
            "beauty-market-entry",
            "vietnam-sourcing",
            "it-market-entry",
            "it-systems-development",
            "marketing-services",
            "legal-advisory",
        ]],
    ]
    items = "\n".join(
        f"  <url><loc>{esc(url)}</loc><changefreq>weekly</changefreq><priority>{'1.0' if url == DOMAIN + '/' else '0.8'}</priority></url>"
        for url in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>\n'


def write_pages() -> None:
    for lang in ("ko", "en"):
        for page in PAGES:
            directory = ROOT / lang / page["slug"]
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "index.html").write_text(render_page(page, lang), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(render_sitemap(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: https://www.globos.world/sitemap.xml\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_pages()
    print(f"Generated {len(PAGES) * 2} SEO landing pages, sitemap.xml, and robots.txt")
