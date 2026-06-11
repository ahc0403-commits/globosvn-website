# Globos Holdings 웹사이트 인수인계서

이 문서는 Globos Holdings 웹사이트 작업을 다음 담당자에게 인수인계하기 위한 별도 문서입니다. 실제 사이트 프로젝트는 아래 경로에 있습니다.

## 1. 프로젝트 위치

- 로컬 프로젝트: `/Users/andreahn/Desktop/globosvn-website`
- 현재 Codex 대화 workspace와 다릅니다. 작업할 때는 반드시 위 프로젝트 폴더로 이동하세요.
- GitHub remote: `https://github.com/ahc0403-commits/globosvn-website.git`
- 기본 브랜치: `main`
- Vercel project: `globosvn-website`
- Vercel project id: `prj_ytmePoL2nWK0kc59Ei4XNLOJbP2E`
- Vercel team/org id: `team_4AfACJKDlP09zRqoJKce3Tib`

## 2. 현재 배포 상태

- Production domain: `https://www.globos.world`
- `https://globos.world`도 `https://www.globos.world/`로 정상 연결 확인됨.
- 최신 production deploy:
  - Vercel deployment URL: `https://globosvn-website-74kwc2al8-andres-projects-c63d3b09.vercel.app`
  - Vercel inspect URL: `https://vercel.com/andres-projects-c63d3b09/globosvn-website/8iRioNP4c5yXMHbDowHFD8SBGwBJ`
- 최신 Git commit:
  - `2030bf5 Fix secure contact form actions`
  - `main`과 `origin/main`이 같은 커밋을 가리키는 것까지 확인됨.

## 3. 최근 작업 요약

주요 목적은 기존 GLOBOSVN 웹사이트를 Globos Holdings 사이트로 정리하고, 사이트 구조/이미지/상호작용/링크/배포 상태를 안정화하는 것이었습니다.

완료된 작업:

- 회사명 전체 변경: `GLOBOSVN`, 기존 법인명 표기, `Global Architect Consulting` 잔재를 `Globos Holdings`로 통일.
- 이메일 전체 변경: `contact@globos.world`.
- 홈페이지 구조 재정리:
  - `Home / Model / Evidence / Capabilities / Process / Contact`
  - `#platform`, `#operating-data`, `#capabilities`, `#intelligence` 흐름으로 논리 구조 정리.
- 전문적인 이미지로 전면 교체:
  - 생성 이미지들은 `assets/images/generated/` 아래 WebP로 저장.
  - Legal 페이지는 데이터 이미지가 아니라 법률/문서 분위기의 이미지로 교체.
- 홈페이지 데이터 박스 상호작용 구현:
  - `data-insight-key` 버튼 클릭 시 `#operating-insight-panel` 내용과 CTA 링크가 바뀜.
- 클릭 가능한 것처럼 보이던 카드/아이콘 정리:
  - `cursor-pointer`만 있고 동작 없는 카드들을 실제 `<a>` 링크로 변경.
  - 푸터의 `language`, `share` 아이콘에도 실제 링크 부여.
- 폼 보안 경고 수정:
  - `action="mailto:..."`가 브라우저에서 "안전하지 않은 양식" 경고를 띄워서 제거.
  - 현재 폼 action은 `https://www.globos.world/contact`.
  - JS가 submit을 intercept한 뒤 `mailto:contact@globos.world?...`를 열어 이메일 클라이언트로 연결.

## 4. 주요 파일

- `index.html`
  - 홈페이지 전체.
  - 운영 모델, 데이터 박스, capabilities hub, process, footer, homepage contact CTA 포함.
  - 데이터 박스 JS와 mail form JS가 하단 inline script에 있음.
- `contact.html`
  - Contact 페이지.
  - 상세 문의 폼과 회사 정보 섹션 포함.
- `capabilities/*.html`
  - 총 10개 capability 상세 페이지.
  - 페이지별 이미지/링크/푸터/메일 링크 정리 완료.
- `assets/images/generated/*.webp`
  - 이번 작업에서 생성/교체한 시각 asset 12개.
- `vercel.json`
  - clean URL, capability rewrite, 보안 header 설정.
- `.gitignore`
  - `.vercel`을 ignore하도록 추가됨.

## 5. 생성 이미지 목록

- `assets/images/generated/home-execution-command.webp`
- `assets/images/generated/contact-confidential-inquiry.webp`
- `assets/images/generated/beauty-market-entry.webp`
- `assets/images/generated/direct-store-operations.webp`
- `assets/images/generated/fb-market-entry.webp`
- `assets/images/generated/franchise-expansion.webp`
- `assets/images/generated/it-market-entry.webp`
- `assets/images/generated/it-systems-operations.webp`
- `assets/images/generated/legal-advisory.webp`
- `assets/images/generated/marketing-services.webp`
- `assets/images/generated/master-brand-acquisition.webp`
- `assets/images/generated/vietnam-sourcing.webp`

## 6. 로컬 실행

정적 HTML 사이트입니다.

```bash
cd /Users/andreahn/Desktop/globosvn-website
python3 -m http.server 4173
```

브라우저:

```text
http://127.0.0.1:4173/index.html
```

현재 Codex 작업 중에는 위 URL로 로컬 서버를 확인했습니다.

## 7. 검증했던 항목

반복적으로 아래를 확인했습니다.

- `rg`로 예전 회사명 잔여 검색:
  - `GLOBOSVN`
  - `globosvn`
  - `CÔNG TY TNHH`
  - `COMPANY LIMITED`
  - `CO., LTD`
  - `Global Architect`
- 클릭/링크 감사:
  - HTML 12개
  - 앵커 219개
  - 버튼 15개
  - 폼 2개
  - 이미지 32개
  - JS 동적 href 13개
  - 로컬 타깃 242개
  - 최종 issue 0건
- inline script 문법 검사:
  - 최종 script issue 0건
- 공개 사이트 확인:
  - `https://www.globos.world`
  - `https://www.globos.world/contact`
  - `https://www.globos.world/capabilities/legal-advisory`
  - 주요 image asset 200 OK
- 폼 보안 경고 수정 후 공개 HTML 확인:
  - homepage form action: `https://www.globos.world/contact`
  - contact form action: `https://www.globos.world/contact`
  - `action="mailto:..."`와 `enctype="text/plain"`은 제거됨.

## 8. 배포 방법

GitHub push:

```bash
cd /Users/andreahn/Desktop/globosvn-website
git status -sb
git add <files>
git commit -m "Message"
git push origin main
```

Vercel production deploy:

```bash
cd /Users/andreahn/Desktop/globosvn-website
vercel deploy --prod --yes
```

배포 후 확인:

```bash
curl -L -sS -o /dev/null -w '%{http_code} %{url_effective}\n' https://www.globos.world
curl -L -sS https://www.globos.world | rg -n '<title>|Globos Holdings|GLOBOSVN|Global Architect'
curl -L -sS https://www.globos.world/contact | rg -n '<form|action="mailto:|action="https://www.globos.world/contact"|enctype="text/plain"'
```

## 9. 현재 주의할 점

- 폼은 백엔드 제출이 아니라 `mailto:` 기반입니다.
  - 브라우저 경고를 없애기 위해 form action은 HTTPS로 두고, JS에서 submit을 막은 뒤 mail client를 엽니다.
  - 사용자의 컴퓨터에 이메일 클라이언트가 없으면 문의 제출 경험이 약할 수 있습니다.
  - 장기적으로는 Formspree, Vercel Functions, Supabase, Resend 같은 실제 form backend를 붙이는 것이 좋습니다.
- Browser/Node runtime에서 보이는 `Statsig` / `oaistatsig.com` Cloudflare 경고는 Codex 브라우저 도구 자체의 외부 telemetry 관련 노이즈입니다. 사이트 앱 오류로 보지 않았습니다.
- `.vercel/project.json`은 로컬에는 있지만 `.gitignore`에 의해 커밋하지 않습니다.
- 이 사이트는 Tailwind CDN/Google Fonts/Material Symbols CDN을 사용합니다. 완전한 offline build 구조는 아닙니다.

## 10. 다음 작업 추천

우선순위 높은 순서:

1. 실제 문의 백엔드 붙이기.
   - 현재 mailto 방식은 임시/가벼운 방식입니다.
   - `contact@globos.world`로 안정적으로 이메일을 받으려면 serverless form endpoint를 추가하세요.
2. 모바일 QA.
   - 특히 긴 브랜드명 `Globos Holdings`가 nav/header에서 좁은 화면에 잘 맞는지 재확인.
3. SEO/Open Graph 정리.
   - title은 바뀌었지만 description/meta/OG image는 더 다듬을 여지가 있습니다.
4. 회사 법인 정보 확정.
   - 기존 베트남 법인명 표기를 모두 `Globos Holdings`로 단순화했습니다.
   - 실제 법인명/주소/사업자 정보가 따로 있으면 contact/footer에 다시 반영해야 합니다.
5. capabilities 페이지 디자인 톤 통일.
   - 기능상 링크와 이미지가 정상화되었지만, 각 페이지의 원래 템플릿 톤이 조금씩 다릅니다.

## 11. 최근 커밋 히스토리

```text
2030bf5 Fix secure contact form actions
12a32be Refresh Globos Holdings website
899a2cb Initial commit: GLOBOSVN corporate website - 12 pages (home, contact, 10 capabilities)
```

## 12. 작업 시작 체크리스트

Claude가 이어받을 때 먼저 실행:

```bash
cd /Users/andreahn/Desktop/globosvn-website
git status -sb
git log -3 --oneline --decorate
curl -L -sS -o /dev/null -w '%{http_code} %{url_effective}\n' https://www.globos.world
```

문제 재현이 필요하면:

```bash
python3 -m http.server 4173
```

그리고 브라우저에서:

```text
http://127.0.0.1:4173/index.html
http://127.0.0.1:4173/contact.html
```
