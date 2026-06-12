import fs from "node:fs";
import path from "node:path";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const domain = "https://www.globos.world";

const labels = {
  ko: {
    home: "홈",
    tower: "로컬 파트너",
    capabilities: "실행 영역",
    proof: "운영 근거",
    sitemap: "사이트맵",
    contact: "문의",
    inquiry: "문의하기",
    langOther: "EN",
    bestFor: "적합한 경우",
    scope: "실행 범위",
    flow: "진행 흐름",
    proofTitle: "운영 근거",
    related: "연결되는 실행 영역",
    ctaTitle: "현재 검토 중인 과제부터 정리해 드립니다.",
    ctaBody: "브랜드, 제품군, 목표 지역, 준비 단계, 우선 과제를 보내주시면 베트남에서 필요한 실행 순서를 정리해 드립니다.",
    ctaButton: "상담 문의하기",
    back: "비즈니스 영역 전체 보기",
    about: "회사소개",
    leaders: "경영진",
    vision: "비전&미션",
    org: "조직도",
    partnership: "로컬 파트너십 안내",
    partnershipStructure: "파트너십 구조",
    partnershipReason: "현지 실행 필요성",
    partnershipInfra: "운영 인프라",
    business: "제공가능 비즈니스 영역",
    businessFranchise: "프랜차이즈·F&B",
    businessLegal: "법인·인허가",
    businessMarketing: "쇼피·틱톡샵 마케팅",
    businessSourcing: "유통·소싱",
    businessSystems: "ERP·POS·배달",
    record: "운영 실적",
    recordCurrent: "운영 현황",
    recordFlow: "실행 프로세스",
    recordGuides: "베트남 진출 가이드",
    consultation: "상담 문의",
    email: "이메일"
  },
  en: {
    home: "Home",
    tower: "Local Partner",
    capabilities: "Services",
    proof: "Track Record",
    sitemap: "Site Map",
    contact: "Contact",
    inquiry: "Get in Touch",
    langOther: "KR",
    bestFor: "Best for",
    scope: "Execution scope",
    flow: "Operating flow",
    proofTitle: "Operating proof",
    related: "Related capabilities",
    ctaTitle: "Start with the bottleneck.",
    ctaBody: "Send the brand, product category, target area, and current constraint. We will map the operating sequence required for Vietnam.",
    ctaButton: "Request consultation",
    back: "View all business areas",
    about: "About",
    leaders: "Leadership",
    vision: "Vision & Mission",
    org: "Organization",
    partnership: "Local Partnership",
    partnershipStructure: "Partnership Structure",
    partnershipReason: "Why Local Execution",
    partnershipInfra: "Operating Infrastructure",
    business: "Business Areas",
    businessFranchise: "Franchise & F&B",
    businessLegal: "Company & Licensing",
    businessMarketing: "Shopee & TikTok Marketing",
    businessSourcing: "Distribution & Sourcing",
    businessSystems: "ERP, POS & Delivery",
    record: "Track Record",
    recordCurrent: "Operating Numbers",
    recordFlow: "Execution Flow",
    recordGuides: "Vietnam Entry Guides",
    consultation: "Consultation",
    email: "Email"
  }
};

const services = [
  {
    slug: "franchise-expansion",
    asset: "franchise-expansion",
    icon: "storefront",
    ko: {
      title: "프랜차이즈 베트남 확장",
      eyebrow: "Franchise Expansion",
      meta: "베트남 프랜차이즈 진출, 운영자 통제, 매장 오픈, 다점포 확장 구조를 설계하는 Globos Holdings 실행 영역.",
      lead: "한국에서 검증된 브랜드를 베트남에서 반복 가능한 매장 모델로 바꾸는 일. 계약보다 중요한 것은 누가 열고, 누가 관리하고, 어떤 숫자로 확장할지입니다.",
      bestFor: ["베트남에 첫 매장을 준비하는 프랜차이즈 본사", "현지 운영자나 마스터 파트너 구조가 필요한 브랜드", "가맹 계약보다 실제 운영 통제가 더 걱정되는 회사", "다점포 확장 기준을 처음부터 잡고 싶은 팀"],
      scope: ["시장성과 상권 기준 검토", "마스터 운영권·파트너 구조 설계", "오픈 순서, 교육, SOP, POS 기준 정리", "다점포 확장 로드맵과 리포팅 체계"],
      flow: ["브랜드와 메뉴 구조 검토", "현지 운영 방식과 법적 구조 정리", "1호점 오픈 기준과 운영 루틴 설계", "성과 지표 확인 후 확장 순서 결정"],
      proof: "Globos Holdings는 베트남에서 8개 점포를 운영하며 매장, 인력, POS, 배달, 정산 루틴을 직접 다루고 있습니다."
    },
    en: {
      title: "Franchise Expansion in Vietnam",
      eyebrow: "Franchise Expansion",
      meta: "Vietnam franchise expansion, operator control, store launch, and multi-unit operating structure by Globos Holdings.",
      lead: "Turning a proven brand into a repeatable Vietnam store model. The real question is not only who signs the contract, but who opens, controls, reports, and scales the stores.",
      bestFor: ["Franchise headquarters preparing a first Vietnam location", "Brands needing a local operator or master partner structure", "Teams concerned about field control after contract signing", "Companies that want multi-store governance from day one"],
      scope: ["Market fit and trade-area criteria", "Master operating rights and partner structure", "Launch sequence, training, SOP, and POS standards", "Expansion roadmap and reporting cadence"],
      flow: ["Review brand and menu architecture", "Define local operating and legal structure", "Design first-store launch standards and routines", "Validate metrics before multi-store expansion"],
      proof: "Globos Holdings operates 8 stores in Vietnam and manages the daily routines behind staffing, POS, delivery, settlement, and reporting."
    },
    related: ["direct-store-operations", "fb-market-entry", "legal-advisory"]
  },
  {
    slug: "fb-market-entry",
    asset: "fb-market-entry",
    icon: "restaurant",
    ko: {
      title: "F&B 브랜드 런칭",
      eyebrow: "F&B Brand Launch",
      meta: "베트남 식당, 카페, 한식당, F&B 프랜차이즈 진출을 위한 매장 오픈과 운영 실행 지원.",
      lead: "F&B는 오픈보다 운영이 어렵습니다. 메뉴 현지화, 식자재, 인력, SOP, POS, 배달, 품질 기준이 처음부터 맞아야 합니다.",
      bestFor: ["식당·카페·한식 브랜드의 베트남 진출", "현지 식자재와 공급처가 필요한 브랜드", "배달 앱과 매장 운영을 같이 준비하는 팀", "오픈 후 품질 유지가 걱정되는 본사"],
      scope: ["메뉴와 가격 현지화", "식자재·공급처·물류 구조", "매장 오픈 체크리스트와 교육", "POS, 배달, 품질 리포팅 기준"],
      flow: ["브랜드와 메뉴 적합성 검토", "입지와 공급망 기준 수립", "오픈 준비, 인력 교육, 운영 테스트", "매출·원가·품질 리포트로 안정화"],
      proof: "직영점 운영 경험을 기반으로 F&B 매장의 매출, 원가, 인력, 배달 흐름을 한 화면에서 관리하는 구조를 갖추고 있습니다."
    },
    en: {
      title: "F&B Brand Launch in Vietnam",
      eyebrow: "F&B Brand Launch",
      meta: "Store opening and operating execution for restaurants, cafes, Korean food brands, and F&B franchises entering Vietnam.",
      lead: "In F&B, launch day is not the hardest part. Menu localization, ingredients, staffing, SOP, POS, delivery, and quality control must fit together from the start.",
      bestFor: ["Restaurant, cafe, and Korean food brands entering Vietnam", "Brands needing local ingredients and suppliers", "Teams preparing store operations and delivery together", "Headquarters worried about quality after opening"],
      scope: ["Menu and price localization", "Ingredients, suppliers, and logistics structure", "Store opening checklist and staff training", "POS, delivery, and quality reporting standards"],
      flow: ["Review brand and menu fit", "Set location and supply criteria", "Prepare opening, train staff, test operations", "Stabilize with sales, cost, and quality reporting"],
      proof: "Our own store operations provide the basis for managing F&B revenue, cost, staffing, delivery, and quality in one operating view."
    },
    related: ["franchise-expansion", "direct-store-operations", "marketing-services"]
  },
  {
    slug: "direct-store-operations",
    asset: "direct-store-operations",
    icon: "dashboard",
    ko: {
      title: "직영점 운영 대행",
      eyebrow: "Direct Store Operations",
      meta: "베트남 직영점 운영, 인력, SOP, POS, 원가, 배달, 매장 리포팅을 관리하는 운영 대행 서비스.",
      lead: "브랜드가 베트남에 들어온 뒤 가장 필요한 것은 매장을 매일 굴리는 팀입니다. 운영 대행은 현장, 숫자, 개선 루틴을 함께 맡는 일입니다.",
      bestFor: ["베트남 현지 매장을 직접 관리하기 어려운 본사", "매장 리포트와 손익 관리를 원하는 브랜드", "현장 인력과 품질 기준을 잡아야 하는 팀", "운영 안정화 후 확장을 검토하는 회사"],
      scope: ["점포 운영 관리와 인력 루틴", "SOP, 서비스, 품질 점검", "매출, 원가, 재고, 인건비 리포팅", "배달 채널과 정산 관리"],
      flow: ["현재 매장 상태 진단", "운영 기준과 리포트 형식 합의", "현장 루틴 적용과 개선", "성과 지표 기반 확장 여부 판단"],
      proof: "8개 운영 점포를 통해 실제 매장 리듬, 이슈 대응, 원가 관리, 리포팅 구조를 검증하고 있습니다."
    },
    en: {
      title: "Direct Store Operations",
      eyebrow: "Direct Store Operations",
      meta: "Vietnam store operation management covering staffing, SOP, POS, costs, delivery, and performance reporting.",
      lead: "After market entry, a brand needs a team that runs the store every day. Store operations means field control, numbers, and improvement routines handled together.",
      bestFor: ["Headquarters unable to manage Vietnam stores directly", "Brands needing store reporting and P&L visibility", "Teams setting staff and quality standards", "Companies stabilizing operations before expansion"],
      scope: ["Store management and staff routines", "SOP, service, and quality checks", "Sales, cost, inventory, and labor reporting", "Delivery channel and settlement management"],
      flow: ["Diagnose current store condition", "Align operating standards and report format", "Apply routines and improve field execution", "Decide expansion based on performance indicators"],
      proof: "Our 8 operating stores validate the daily rhythm, issue handling, cost control, and reporting structure required in Vietnam."
    },
    related: ["it-systems-development", "fb-market-entry", "franchise-expansion"]
  },
  {
    slug: "legal-advisory",
    asset: "legal-advisory",
    icon: "gavel",
    ko: {
      title: "법인 설립·인허가 자문",
      eyebrow: "Legal & Licensing",
      meta: "베트남 법인 설립, 사업자등록, 투자허가, 제품등록, 계약 구조, 현지 전문가 조율 지원.",
      lead: "법률 자문은 서류만 끝내는 일이 아닙니다. 실제 사업 모델에 맞는 법인, 인허가, 계약, 운영 구조가 함께 맞아야 합니다.",
      bestFor: ["베트남 법인 설립 경로가 불명확한 회사", "제품등록, 영업허가, 투자허가가 필요한 브랜드", "계약과 현지 운영 구조를 함께 봐야 하는 본사", "전문가 조율을 내부에서 하기 어려운 팀"],
      scope: ["법인 형태와 투자 구조 검토", "사업자등록, 허가, 제품등록 일정 관리", "계약, 파트너, 운영 책임 구조 정리", "현지 법률·회계·행정 전문가 조율"],
      flow: ["사업 모델과 필요한 허가 확인", "법인·계약·제품등록 경로 설계", "전문가와 서류 진행 관리", "운영 시작 전 리스크 점검"],
      proof: "법인과 인허가를 운영과 분리하지 않고, 매장·유통·이커머스 실행 순서 안에서 검토합니다."
    },
    en: {
      title: "Legal and Licensing Advisory",
      eyebrow: "Legal & Licensing",
      meta: "Vietnam entity setup, business registration, investment permits, product registration, contract structure, and local professional coordination.",
      lead: "Legal advisory is not only paperwork. Entity setup, permits, contracts, and operating responsibility must fit the actual business model.",
      bestFor: ["Companies unclear about Vietnam entity setup", "Brands needing product registration, business permits, or investment permits", "Headquarters reviewing contracts and local operating structure together", "Teams needing coordination across local professionals"],
      scope: ["Entity type and investment structure review", "Business registration, permits, and product registration schedule", "Contract, partner, and operating responsibility structure", "Coordination with legal, accounting, and administrative specialists"],
      flow: ["Confirm business model and permits required", "Design entity, contract, and registration route", "Coordinate professionals and filing process", "Check operating risk before launch"],
      proof: "We review legal and licensing work inside the operating sequence for stores, distribution, and ecommerce, not as a separate document exercise."
    },
    related: ["it-market-entry", "beauty-market-entry", "vietnam-sourcing"]
  },
  {
    slug: "it-systems-development",
    asset: "it-systems-operations",
    icon: "database",
    ko: {
      title: "ERP·POS·배달 시스템",
      eyebrow: "ERP / POS / Delivery",
      meta: "베트남 매장 운영을 위한 ERP, SaaS POS, 배달 앱, 재고, 주문, 정산, 리포팅 시스템 구축.",
      lead: "점포가 늘어날수록 감으로 관리할 수 없습니다. 매출, 원가, 재고, 주문, 정산, 리포팅이 같은 데이터 기준으로 움직여야 합니다.",
      bestFor: ["매장 수 증가에 맞춰 시스템이 필요한 브랜드", "POS, ERP, 배달 주문, 정산이 분리된 회사", "본사에서 베트남 매장 숫자를 보고 싶은 팀", "프랜차이즈 확장을 준비하는 운영 조직"],
      scope: ["SaaS POS 운영 기준", "ERP 기반 매출·재고·원가 관리", "배달 주문과 정산 흐름 연결", "대시보드와 리포팅 구조"],
      flow: ["현재 운영 데이터 확인", "POS·ERP·배달 연결 범위 정의", "매장별 입력·정산 루틴 적용", "본사 리포트와 확장 지표 운영"],
      proof: "자체 ERP, SaaS POS, 배달 앱 기반을 운영 점포에 맞춰 준비했고, 확장 시 데이터 통제 기반으로 사용합니다."
    },
    en: {
      title: "ERP, POS, and Delivery Systems",
      eyebrow: "ERP / POS / Delivery",
      meta: "ERP, SaaS POS, delivery app, inventory, orders, settlement, and reporting systems for Vietnam store operations.",
      lead: "As stores increase, intuition is not enough. Sales, costs, inventory, orders, settlement, and reporting need to move from the same data standard.",
      bestFor: ["Brands needing systems as store count grows", "Companies with disconnected POS, ERP, delivery, and settlement flows", "Headquarters requiring visibility into Vietnam store numbers", "Operations teams preparing franchise expansion"],
      scope: ["SaaS POS operating standards", "ERP-based sales, inventory, and cost management", "Delivery order and settlement connection", "Dashboard and reporting structure"],
      flow: ["Audit current operating data", "Define POS, ERP, and delivery connection scope", "Apply store-level input and settlement routines", "Operate headquarters reporting and expansion metrics"],
      proof: "Globos Holdings has prepared in-house ERP, SaaS POS, and delivery app infrastructure aligned to active store operations."
    },
    related: ["direct-store-operations", "franchise-expansion", "marketing-services"]
  },
  {
    slug: "it-market-entry",
    asset: "it-market-entry",
    icon: "public",
    ko: {
      title: "베트남 시장 진출",
      eyebrow: "Vietnam Market Entry",
      meta: "베트남 시장 진출, 법인 설립, 인허가, 유통, 운영, 마케팅, 시스템까지 한 번에 정리하는 실행 경로.",
      lead: "베트남 진출은 시장 조사로 끝나지 않습니다. 법인, 인허가, 유통, 운영, 판매 채널, 시스템을 한 흐름으로 정리해야 실행이 시작됩니다.",
      bestFor: ["베트남 진출 여부를 처음 검토하는 브랜드", "사업 모델은 있지만 현지 실행 순서가 없는 회사", "법인, 유통, 매장, 온라인 판매를 같이 봐야 하는 팀", "투자 전 실행 리스크를 확인하고 싶은 본사"],
      scope: ["시장 진입 경로와 우선순위 정리", "법인·인허가·유통·운영 연결", "현지 파트너와 실행 일정 관리", "초기 운영 지표와 확장 가능성 검토"],
      flow: ["브랜드와 제품군 진단", "진입 방식과 필수 허가 확인", "운영·유통·판매 채널 설계", "초기 실행 범위와 예산 정리"],
      proof: "2024년 베트남에서 시작해 현재 8개 점포와 20여 개 파트너사 기반으로 진입 이후 운영까지 연결합니다."
    },
    en: {
      title: "Vietnam Market Entry",
      eyebrow: "Vietnam Market Entry",
      meta: "Vietnam market entry route covering entity setup, licensing, distribution, operations, marketing, and systems.",
      lead: "Vietnam market entry does not end with research. Entity setup, permits, distribution, operations, sales channels, and systems must be organized into one execution path.",
      bestFor: ["Brands evaluating Vietnam for the first time", "Companies with a business model but no local execution sequence", "Teams that need entity, distribution, store, and online sales reviewed together", "Headquarters checking execution risk before investment"],
      scope: ["Market-entry route and priority setting", "Entity, licensing, distribution, and operations connection", "Local partner and execution schedule management", "Initial operating metrics and scale potential review"],
      flow: ["Diagnose brand and product category", "Confirm entry mode and required permits", "Design operations, distribution, and sales channels", "Define initial scope and budget"],
      proof: "Since starting Vietnam operations in 2024, Globos Holdings connects market entry to actual operations through 8 stores and 20+ partner firms."
    },
    related: ["legal-advisory", "vietnam-sourcing", "marketing-services"]
  },
  {
    slug: "beauty-market-entry",
    asset: "beauty-market-entry",
    icon: "science",
    ko: {
      title: "뷰티·소비재 시장 진출",
      eyebrow: "Beauty Market Entry",
      meta: "베트남 화장품, 뷰티, 소비재 브랜드의 제품등록, 라벨링, 통관, 유통, 쇼피·틱톡샵 판매 실행.",
      lead: "뷰티와 소비재는 제품등록 이후가 더 중요합니다. 통관, 유통, 쇼피, 틱톡샵, 콘텐츠, 판매 전환이 이어져야 시장 진입이 됩니다.",
      bestFor: ["화장품·뷰티·소비재를 베트남에 수출하려는 브랜드", "제품등록 이후 판매 채널이 필요한 회사", "쇼피와 틱톡샵 운영을 같이 준비하는 팀", "유통사와 온라인 판매를 동시에 검토하는 본사"],
      scope: ["제품등록, 라벨링, 통관 일정", "유통사, 리테일, 온라인 채널 검토", "쇼피·틱톡샵 입점과 운영", "콘텐츠, 광고, 판매 전환 루틴"],
      flow: ["제품군과 규제 요건 확인", "등록·라벨링·통관 경로 정리", "채널별 판매 구조 설계", "마케팅과 정산 루틴 운영"],
      proof: "인허가와 판매 채널을 분리하지 않고, 등록 이후 실제 판매까지 이어지는 운영 경로로 설계합니다."
    },
    en: {
      title: "Beauty and Consumer Goods Market Entry",
      eyebrow: "Beauty Market Entry",
      meta: "Vietnam market entry for cosmetics, beauty, and consumer brands covering registration, labeling, customs, distribution, Shopee, and TikTok Shop.",
      lead: "For beauty and consumer goods, the work after product registration matters most. Customs, distribution, Shopee, TikTok Shop, content, and conversion must connect.",
      bestFor: ["Cosmetics, beauty, and consumer brands exporting to Vietnam", "Companies needing sales channels after product registration", "Teams preparing Shopee and TikTok Shop operations", "Headquarters reviewing distributors and online sales together"],
      scope: ["Product registration, labeling, and customs schedule", "Distributor, retail, and online channel review", "Shopee and TikTok Shop setup and operation", "Content, ads, and sales conversion routines"],
      flow: ["Confirm product category and regulatory requirements", "Map registration, labeling, and customs route", "Design sales structure by channel", "Operate marketing and settlement routines"],
      proof: "We design the route from registration to actual sales, connecting licensing, distribution, ecommerce, and marketing as one process."
    },
    related: ["legal-advisory", "marketing-services", "vietnam-sourcing"]
  },
  {
    slug: "vietnam-sourcing",
    asset: "vietnam-sourcing",
    icon: "local_shipping",
    ko: {
      title: "베트남 소싱·공급망",
      eyebrow: "Vietnam Sourcing",
      meta: "베트남 소싱, 공급처 개발, 식자재, 제조, 통관, 물류, 창고, 유통 연결 지원.",
      lead: "소싱은 공급처 목록을 받는 일이 아닙니다. 품질, 가격, 납기, 통관, 보관, 판매 채널까지 이어져야 실제 공급망이 됩니다.",
      bestFor: ["베트남 현지 공급처가 필요한 브랜드", "식자재, 제조, 물류 구조를 찾아야 하는 F&B 회사", "유통·통관·창고를 같이 검토하는 팀", "기존 공급망을 베트남으로 확장하려는 본사"],
      scope: ["공급처 발굴과 조건 검토", "품질, 가격, MOQ, 납기 확인", "통관, 창고, 물류 연결", "유통사와 판매 채널 연계"],
      flow: ["품목과 품질 기준 정의", "후보 공급처 검토와 조건 협의", "샘플·가격·물류 가능성 확인", "운영 루틴과 리스크 관리"],
      proof: "매장 운영과 유통 경험을 바탕으로 공급처를 실제 판매·운영 흐름 안에서 검토합니다."
    },
    en: {
      title: "Vietnam Sourcing and Supply Chain",
      eyebrow: "Vietnam Sourcing",
      meta: "Vietnam sourcing, supplier development, ingredients, manufacturing, customs, logistics, warehousing, and distribution connection.",
      lead: "Sourcing is not a supplier list. Quality, price, lead time, customs, storage, and sales channels must connect before it becomes a real supply chain.",
      bestFor: ["Brands needing Vietnam-based suppliers", "F&B companies sourcing ingredients, manufacturing, or logistics", "Teams reviewing distribution, customs, and warehousing together", "Headquarters expanding supply chains into Vietnam"],
      scope: ["Supplier discovery and condition review", "Quality, price, MOQ, and lead-time check", "Customs, warehouse, and logistics connection", "Distributor and sales-channel linkage"],
      flow: ["Define item and quality standards", "Review supplier candidates and negotiate terms", "Confirm sample, price, and logistics feasibility", "Manage operating routine and risk"],
      proof: "We review suppliers inside the actual sales and operating flow, backed by store operations and local distribution experience."
    },
    related: ["legal-advisory", "fb-market-entry", "direct-store-operations"]
  },
  {
    slug: "marketing-services",
    asset: "marketing-services",
    icon: "campaign",
    ko: {
      title: "틱톡·쇼피 마케팅 운영",
      eyebrow: "Marketing & Ecommerce",
      meta: "베트남 틱톡 마케팅, 쇼피 마케팅, 인플루언서, 라이브커머스, 콘텐츠, 광고, 판매 전환 운영.",
      lead: "베트남 마케팅은 조회수만으로 끝나면 의미가 없습니다. 쇼피, 틱톡샵, 콘텐츠, 광고, 라이브커머스가 판매와 정산까지 이어져야 합니다.",
      bestFor: ["쇼피·틱톡샵 판매를 시작하는 브랜드", "현지 콘텐츠와 인플루언서 운영이 필요한 회사", "광고보다 판매 전환이 중요한 팀", "온라인 판매와 오프라인 유통을 같이 키우려는 본사"],
      scope: ["틱톡·쇼피 채널 운영", "콘텐츠, 인플루언서, 라이브커머스", "광고 집행과 판매 전환 관리", "CS, 리뷰, 정산, 리포팅"],
      flow: ["채널과 상품 우선순위 설정", "콘텐츠와 캠페인 운영 계획", "광고·라이브·인플루언서 실행", "판매, CS, 정산 데이터로 개선"],
      proof: "마케팅을 별도 캠페인이 아니라 판매 채널 운영, 재고, 정산, 리포팅 안에서 관리합니다."
    },
    en: {
      title: "TikTok and Shopee Marketing Operations",
      eyebrow: "Marketing & Ecommerce",
      meta: "Vietnam TikTok marketing, Shopee marketing, influencers, live commerce, content, ads, and sales conversion operations.",
      lead: "Vietnam marketing is not useful if it stops at views. Shopee, TikTok Shop, content, ads, and live commerce must connect to sales and settlement.",
      bestFor: ["Brands starting Shopee or TikTok Shop sales", "Companies needing local content and influencer operations", "Teams focused on conversion over impressions", "Headquarters growing online sales with offline distribution"],
      scope: ["TikTok and Shopee channel operations", "Content, influencers, and live commerce", "Advertising and conversion management", "CS, reviews, settlement, and reporting"],
      flow: ["Set channel and product priorities", "Plan content and campaign operations", "Execute ads, live commerce, and influencer work", "Improve through sales, CS, and settlement data"],
      proof: "We manage marketing inside sales-channel operations, inventory, settlement, and reporting rather than as a separate campaign."
    },
    related: ["beauty-market-entry", "fb-market-entry", "it-systems-development"]
  },
  {
    slug: "master-brand-acquisition",
    asset: "master-brand-acquisition",
    icon: "handshake",
    ko: {
      title: "파트너·브랜드 개발",
      eyebrow: "Partner Development",
      meta: "베트남 현지 파트너, 운영자, 공급처, 유통사, 브랜드 도입, 마스터 운영권 개발.",
      lead: "베트남에서 좋은 파트너는 명함으로 찾는 것이 아닙니다. 브랜드 목표, 운영 책임, 수익 구조, 확장 계획이 맞아야 오래 갑니다.",
      bestFor: ["현지 파트너나 운영자를 찾아야 하는 브랜드", "마스터 운영권이나 브랜드 도입 구조를 검토하는 회사", "유통사, 공급처, 운영사를 동시에 봐야 하는 팀", "장기 확장 파이프라인이 필요한 본사"],
      scope: ["파트너 후보 발굴과 조건 검토", "운영 책임과 수익 구조 정리", "브랜드 도입, 마스터 권리, 계약 방향", "확장 파이프라인과 관리 기준"],
      flow: ["브랜드 목표와 파트너 요건 정의", "후보 검토와 운영 적합성 확인", "권리·책임·수익 구조 협의", "성과 기준과 확장 단계 관리"],
      proof: "20여 개 파트너사 네트워크와 현장 운영 경험을 기반으로 실제 실행 가능한 관계를 설계합니다."
    },
    en: {
      title: "Partner and Brand Development",
      eyebrow: "Partner Development",
      meta: "Vietnam local partner, operator, supplier, distributor, brand introduction, and master operating rights development.",
      lead: "A good Vietnam partner is not found through a business card. Brand goals, operating responsibility, profit structure, and expansion plan must fit.",
      bestFor: ["Brands looking for local partners or operators", "Companies reviewing master rights or brand introduction structures", "Teams evaluating distributors, suppliers, and operators together", "Headquarters needing long-term expansion pipelines"],
      scope: ["Partner candidate sourcing and condition review", "Operating responsibility and profit structure", "Brand introduction, master rights, and contract direction", "Expansion pipeline and management standards"],
      flow: ["Define brand goals and partner requirements", "Review candidates and operating fit", "Align rights, responsibilities, and profit structure", "Manage performance standards and expansion stages"],
      proof: "Our 20+ partner-firm network and field operating experience help us design relationships that can actually execute."
    },
    related: ["franchise-expansion", "vietnam-sourcing", "legal-advisory"]
  }
];

const bySlug = Object.fromEntries(services.map((service) => [service.slug, service]));

function esc(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
}

function list(items) {
  return items.map((item) => `<li class="flex gap-3"><span class="mt-2 h-2 w-2 shrink-0 rounded-full bg-brass"></span><span>${esc(item)}</span></li>`).join("\n");
}

function relatedCards(service, lang) {
  return service.related.map((slug) => {
    const target = bySlug[slug];
    return `<a class="group rounded-sm border border-white/12 bg-white/[0.08] p-5 transition hover:bg-white hover:text-ink" href="${slug}.html">
      <span class="material-symbols-outlined text-brass transition group-hover:text-cobalt" aria-hidden="true">${target.icon}</span>
      <strong class="mt-4 block font-headline text-xl">${esc(target[lang].title)}</strong>
      <span class="mt-3 inline-flex items-center gap-2 text-sm font-bold">${esc(labels[lang].back)}<span class="material-symbols-outlined text-base" aria-hidden="true">north_east</span></span>
    </a>`;
  }).join("\n");
}

function page(service, lang) {
  const t = service[lang];
  const l = labels[lang];
  const other = lang === "ko" ? "en" : "ko";
  const otherLabel = labels[lang].langOther;
  const canonical = `${domain}/${lang}/capabilities/${service.slug}`;
  const alternate = `${domain}/${other}/capabilities/${service.slug}`;
  const homeUrl = `../../index.html?lang=${lang}`;
  const imagePath = `../../assets/images/generated/${service.asset}.webp`;
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": t.title,
    "provider": { "@type": "Organization", "name": "Globos Holdings", "url": domain },
    "areaServed": ["Vietnam", "South Korea"],
    "serviceType": t.eyebrow,
    "description": t.meta,
    "url": canonical
  };
  return `<!DOCTYPE html>
<html class="scroll-smooth" lang="${lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>${esc(t.title)} | Globos Holdings</title>
  <meta name="description" content="${esc(t.meta)}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="${canonical}" />
  <link rel="alternate" hreflang="${lang}" href="${canonical}" />
  <link rel="alternate" hreflang="${other}" href="${alternate}" />
  <link rel="alternate" hreflang="x-default" href="${domain}/en/capabilities/${service.slug}" />
  <meta property="og:title" content="${esc(t.title)} | Globos Holdings" />
  <meta property="og:description" content="${esc(t.meta)}" />
  <meta property="og:url" content="${canonical}" />
  <meta property="og:type" content="website" />
  <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&amp;display=swap" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css" rel="stylesheet" />
  <link href="../../assets/fonts.css" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet" />
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: { ink: '#071a31', navy: '#002147', cobalt: '#0b4d8f', fog: '#f4f6f7', line: '#d8dde3', brass: '#c8a45d', mint: '#5db79e', slatecopy: '#5c6672' },
          fontFamily: { body: ['Montserrat', 'sans-serif'], headline: ['Montserrat', 'sans-serif'], korean: ['Pretendard', 'sans-serif'] },
          borderRadius: { DEFAULT: '0.125rem', sm: '0.125rem' },
          boxShadow: { firm: '0 24px 60px rgba(0, 33, 71, 0.12)' }
        }
      }
    };
  </script>
  <style>
    :root { color-scheme: light; }
    * { letter-spacing: 0 !important; }
    body { background: #f4f6f7; color: #071a31; }
    .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 350, 'GRAD' 0, 'opsz' 24; line-height: 1; }
    .section-label { display: inline-flex; align-items: center; gap: 10px; font-size: 11px; font-weight: 800; text-transform: uppercase; color: #0b4d8f; }
    .section-label::before { content: ''; width: 34px; height: 2px; background: #c8a45d; }
    .hover-lift { transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease, background-color 180ms ease, color 180ms ease; }
    .hover-lift:hover, .hover-lift:focus-visible { transform: translateY(-3px); box-shadow: 0 18px 42px rgba(7, 26, 49, .14), 0 2px 10px rgba(7, 26, 49, .05); outline: none; }
    .nav-group { position: relative; }
    .nav-trigger { display: inline-flex; align-items: center; border-radius: 0.125rem; padding: 0.625rem 0.5rem; color: #5c6672; transition: color 160ms ease, background-color 160ms ease; }
    .nav-trigger:hover, .nav-trigger:focus-visible, .nav-group:focus-within .nav-trigger { color: #002147; background: #f4f6f7; outline: none; }
    .nav-panel { position: absolute; left: 0; top: calc(100% + 0.5rem); z-index: 60; min-width: 230px; border: 1px solid #d8dde3; background: rgba(255,255,255,.98); padding: .5rem; box-shadow: 0 18px 42px rgba(7, 26, 49, .12); opacity: 0; visibility: hidden; transform: translateY(6px); transition: opacity 160ms ease, transform 160ms ease, visibility 160ms ease; }
    .nav-group:hover .nav-panel, .nav-group:focus-within .nav-panel { opacity: 1; visibility: visible; transform: translateY(0); }
    .nav-panel a { display: block; border-radius: 0.125rem; padding: .75rem .85rem; font-size: .8125rem; font-weight: 700; color: #5c6672; white-space: nowrap; }
    .nav-panel a:hover, .nav-panel a:focus-visible { color: #002147; background: #f4f6f7; outline: none; }
  </style>
  <script type="application/ld+json">${JSON.stringify(jsonLd)}</script>
</head>
<body class="font-body antialiased">
  <header class="fixed left-0 top-0 z-50 w-full border-b border-line/80 bg-white/95 backdrop-blur">
    <nav class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-5 py-4 lg:px-8" aria-label="Primary navigation">
      <a class="brand-name font-headline text-xl font-bold text-navy sm:text-2xl" href="${homeUrl}" aria-label="Globos Holdings home">Globos Holdings</a>
      <div class="hidden items-center gap-1 text-sm font-bold text-slatecopy lg:flex">
        <div class="nav-group">
          <a class="nav-trigger" href="${homeUrl}#leadership">${esc(l.about)}</a>
          <div class="nav-panel" aria-label="${esc(l.about)} submenu">
            <a href="${homeUrl}#leadership">${esc(l.leaders)}</a>
            <a href="${homeUrl}#mission-vision">${esc(l.vision)}</a>
            <a href="${homeUrl}#organization">${esc(l.org)}</a>
          </div>
        </div>
        <div class="nav-group">
          <a class="nav-trigger" href="${homeUrl}#local-partner">${esc(l.partnership)}</a>
          <div class="nav-panel" aria-label="${esc(l.partnership)} submenu">
            <a href="${homeUrl}#local-partner">${esc(l.partnershipStructure)}</a>
            <a href="${homeUrl}#why-globos">${esc(l.partnershipReason)}</a>
            <a href="${homeUrl}#operating-system">${esc(l.partnershipInfra)}</a>
          </div>
        </div>
        <div class="nav-group">
          <a class="nav-trigger text-navy" href="${homeUrl}#capabilities">${esc(l.business)}</a>
          <div class="nav-panel" aria-label="${esc(l.business)} submenu">
            <a href="../../${lang}/capabilities/franchise-expansion.html">${esc(l.businessFranchise)}</a>
            <a href="../../${lang}/capabilities/legal-advisory.html">${esc(l.businessLegal)}</a>
            <a href="../../${lang}/capabilities/marketing-services.html">${esc(l.businessMarketing)}</a>
            <a href="../../${lang}/capabilities/vietnam-sourcing.html">${esc(l.businessSourcing)}</a>
            <a href="../../${lang}/capabilities/it-systems-development.html">${esc(l.businessSystems)}</a>
          </div>
        </div>
        <div class="nav-group">
          <a class="nav-trigger" href="${homeUrl}#proof">${esc(l.record)}</a>
          <div class="nav-panel" aria-label="${esc(l.record)} submenu">
            <a href="${homeUrl}#proof">${esc(l.recordCurrent)}</a>
            <a href="${homeUrl}#execution-flow">${esc(l.recordFlow)}</a>
            <a href="${homeUrl}#seo-landings">${esc(l.recordGuides)}</a>
          </div>
        </div>
        <div class="nav-group">
          <a class="nav-trigger" href="../../contact.html">${esc(l.contact)}</a>
          <div class="nav-panel" aria-label="${esc(l.contact)} submenu">
            <a href="../../contact.html">${esc(l.consultation)}</a>
            <a href="mailto:contact@globos.world?subject=Globos Holdings Website Inquiry">${esc(l.email)}</a>
            <a href="../../site-map.html">${esc(l.sitemap)}</a>
          </div>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <a class="rounded-sm border border-line bg-fog px-3 py-2 text-xs font-extrabold text-slatecopy hover:border-navy hover:text-navy" href="../../${other}/capabilities/${service.slug}.html">${otherLabel}</a>
      </div>
    </nav>
  </header>

  <main class="pt-[73px]">
    <section class="relative overflow-hidden bg-white">
      <div class="mx-auto grid min-h-[calc(100vh-73px)] max-w-7xl items-center gap-12 px-5 py-14 lg:grid-cols-[0.92fr_1.08fr] lg:px-8">
        <div>
          <p class="section-label mb-7">${esc(t.eyebrow)}</p>
          <h1 class="font-headline text-4xl font-bold leading-[1.05] text-ink sm:text-5xl md:text-7xl">${esc(t.title)}</h1>
          <p class="mt-7 max-w-2xl text-base leading-8 text-slatecopy md:text-xl">${esc(t.lead)}</p>
          <div class="mt-9 flex flex-col gap-3 sm:flex-row">
            <a class="hover-lift inline-flex items-center justify-center gap-3 rounded-sm bg-navy px-7 py-4 text-sm font-extrabold text-white hover:bg-cobalt" href="../../contact.html">${esc(l.ctaButton)}<span class="material-symbols-outlined text-lg" aria-hidden="true">mail</span></a>
            <a class="hover-lift inline-flex items-center justify-center gap-3 rounded-sm border border-line bg-white px-7 py-4 text-sm font-extrabold text-navy hover:border-navy" href="${homeUrl}#capabilities">${esc(l.back)}<span class="material-symbols-outlined text-lg" aria-hidden="true">arrow_back</span></a>
          </div>
        </div>
        <div class="relative overflow-hidden rounded-sm border border-line bg-[#071a31] p-4 shadow-firm">
          <img class="aspect-[4/3] w-full rounded-sm object-cover" src="${imagePath}" alt="${esc(t.title)}" />
          <div class="absolute inset-x-4 bottom-4 grid gap-3 sm:grid-cols-3">
            <div class="rounded-sm bg-white/95 p-4 text-ink"><p class="text-xs font-extrabold uppercase text-cobalt">2024</p><p class="mt-1 font-headline text-xl font-bold">${lang === "ko" ? "베트남 시작" : "Vietnam start"}</p></div>
            <div class="rounded-sm bg-white/95 p-4 text-ink"><p class="text-xs font-extrabold uppercase text-cobalt">8</p><p class="mt-1 font-headline text-xl font-bold">${lang === "ko" ? "운영 점포" : "stores"}</p></div>
            <div class="rounded-sm bg-white/95 p-4 text-ink"><p class="text-xs font-extrabold uppercase text-cobalt">20+</p><p class="mt-1 font-headline text-xl font-bold">${lang === "ko" ? "파트너사" : "partners"}</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="border-y border-line bg-fog py-16">
      <div class="mx-auto grid max-w-7xl gap-8 px-5 lg:grid-cols-3 lg:px-8">
        <article class="rounded-sm bg-white p-6 shadow-sm">
          <p class="text-xs font-extrabold uppercase text-cobalt">${esc(l.bestFor)}</p>
          <ul class="mt-6 grid gap-4 text-sm leading-7 text-slatecopy">${list(t.bestFor)}</ul>
        </article>
        <article class="rounded-sm bg-white p-6 shadow-sm">
          <p class="text-xs font-extrabold uppercase text-cobalt">${esc(l.scope)}</p>
          <ul class="mt-6 grid gap-4 text-sm leading-7 text-slatecopy">${list(t.scope)}</ul>
        </article>
        <article class="rounded-sm bg-[#071a31] p-6 text-white shadow-firm">
          <p class="text-xs font-extrabold uppercase text-brass">${esc(l.proofTitle)}</p>
          <p class="mt-6 text-base leading-8 text-white/70">${esc(t.proof)}</p>
        </article>
      </div>
    </section>

    <section class="bg-white py-16">
      <div class="mx-auto max-w-7xl px-5 lg:px-8">
        <div class="grid gap-10 lg:grid-cols-[0.7fr_1.3fr] lg:items-start">
          <div>
            <p class="section-label mb-6">${esc(l.flow)}</p>
            <h2 class="font-headline text-4xl font-bold leading-tight text-ink md:text-5xl">${esc(l.ctaTitle)}</h2>
            <p class="mt-6 text-lg leading-8 text-slatecopy">${esc(l.ctaBody)}</p>
          </div>
          <div class="grid gap-4 md:grid-cols-2">
            ${t.flow.map((step, index) => `<div class="rounded-sm border border-line bg-fog p-5">
              <p class="text-xs font-extrabold uppercase text-cobalt">${String(index + 1).padStart(2, "0")}</p>
              <h3 class="mt-4 font-headline text-2xl font-bold text-ink">${esc(step)}</h3>
            </div>`).join("\n")}
          </div>
        </div>
      </div>
    </section>

    <section class="bg-[#071a31] py-16 text-white">
      <div class="mx-auto grid max-w-7xl gap-8 px-5 lg:grid-cols-[360px_1fr] lg:px-8">
        <div>
          <p class="mb-6 text-xs font-extrabold uppercase text-brass">${esc(l.related)}</p>
          <h2 class="font-headline text-4xl font-bold leading-tight">${esc(l.capabilities)}</h2>
        </div>
        <div class="grid gap-4 md:grid-cols-3">${relatedCards(service, lang)}</div>
      </div>
    </section>
  </main>

  <footer class="bg-white py-10">
    <div class="mx-auto flex max-w-7xl flex-col gap-6 px-5 lg:flex-row lg:items-end lg:justify-between lg:px-8">
      <div>
        <a class="brand-name font-headline text-3xl font-bold text-navy" href="${homeUrl}">Globos Holdings</a>
        <p class="mt-3 max-w-xl text-sm leading-7 text-slatecopy">${esc(t.meta)}</p>
      </div>
      <div class="flex flex-col gap-2 text-sm text-slatecopy lg:text-right">
        <a class="hover:text-navy" href="mailto:contact@globos.world?subject=Globos Holdings Website Inquiry">contact@globos.world</a>
        <a class="hover:text-navy" href="../../contact.html">${esc(l.contact)}</a>
        <p>© 2026 Globos Holdings. All rights reserved.</p>
      </div>
    </div>
  </footer>
</body>
</html>
`;
}

function redirectPage(service) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex, follow" />
  <title>${esc(service.en.title)} | Globos Holdings</title>
  <meta http-equiv="refresh" content="0; url=../en/capabilities/${service.slug}.html" />
  <script>
    const language = localStorage.getItem('globos-language') === 'ko' ? 'ko' : 'en';
    window.location.replace('../' + language + '/capabilities/${service.slug}.html');
  </script>
</head>
<body>
  <p>Redirecting to <a href="../en/capabilities/${service.slug}.html">${esc(service.en.title)}</a>.</p>
</body>
</html>
`;
}

for (const lang of ["ko", "en"]) {
  fs.mkdirSync(path.join(root, lang, "capabilities"), { recursive: true });
}

for (const service of services) {
  for (const lang of ["ko", "en"]) {
    fs.writeFileSync(path.join(root, lang, "capabilities", `${service.slug}.html`), page(service, lang));
  }
  fs.writeFileSync(path.join(root, "capabilities", `${service.slug}.html`), redirectPage(service));
}

console.log(`Generated ${services.length * 2} localized capability pages and ${services.length} compatibility redirects.`);
