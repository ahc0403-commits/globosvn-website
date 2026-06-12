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
        "ko_description": "베트남 진출을 준비하는 브랜드를 위해 법인 설립, 인허가, 유통, 마케팅, 점포 운영을 실제 현지 운영 관점에서 함께 정리합니다.",
        "en_description": "Globos Holdings supports Vietnam market entry with market strategy, entity setup coordination, licensing, distribution, marketing localization, store operations, ERP, POS, and delivery infrastructure.",
        "ko_h1": "베트남 진출, 보고서보다 현지에서 움직일 팀이 먼저입니다.",
        "en_h1": "Vietnam market entry needs an execution structure, not just a strategy deck.",
        "ko_intro": "베트남 시장이 좋아 보여도, 막상 시작하려면 법인, 인허가, 유통, 마케팅, 매장 운영이 한꺼번에 걸립니다. Globos Holdings는 2025년 설립 이후 실제 운영 기반을 쌓으며 그 과정을 같이 정리합니다.",
        "en_intro": "Companies entering Vietnam must evaluate market fit, company setup, licensing, distribution, marketing, and operating infrastructure together. Globos Holdings connects market-entry strategy to local execution through active Vietnam operations.",
        "ko_problem": "계획 단계에서는 베트남 진출 전략, 시장 진출, 컨설팅을 검토합니다. 실행 단계에서는 법인, 인허가, 유통, 운영을 현지에서 누가 연결하고 관리할지가 핵심입니다.",
        "en_problem": "Planning usually begins with Vietnam market-entry strategy, consulting, Korean company examples, and failure cases. Execution depends on who connects company setup, licensing, distribution, and daily operations locally.",
        "keywords": ["베트남 진출", "베트남 시장 진출", "베트남 진출 전략", "베트남 진출 컨설팅", "Vietnam market entry", "Vietnam market entry strategy"],
        "services_ko": ["우리 브랜드가 베트남에서 팔릴 수 있는지 먼저 정리", "법인 설립, 인허가, 유통, 마케팅, 점포 운영을 한 흐름으로 검토", "ERP, SaaS POS, 배달 앱까지 고려한 운영 방식 설계"],
        "services_en": ["Clarify market-entry assumptions and execution scope", "Map entity setup, licensing, distribution, marketing, and store operations", "Connect ERP, SaaS POS, and delivery infrastructure into the operating model"],
        "faqs_ko": [
            ["베트남 진출 전 우선 확인 사항", "시장 규모만 볼 것이 아니라 현지에서 누가 운영할지, 법인과 인허가가 어떤 방식으로 맞는지, 유통과 마케팅을 어떻게 시작할지 먼저 확인해야 합니다."],
            ["Globos Holdings와 단순 컨설팅의 차이", "Globos Holdings는 2025년 설립 이후 베트남에서 실제 점포 운영 기반을 쌓고 있습니다. ERP, POS, 배달 앱 기반까지 함께 보는 현지 운영 파트너입니다."],
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
        "ko_h1": "베트남 법인 설립, 서류보다 사업 방식이 먼저입니다.",
        "en_h1": "Vietnam company registration starts with the business structure, not only the filing checklist.",
        "ko_intro": "베트남 법인 설립은 비용표만 보고 결정하기 어렵습니다. 어떤 업종으로, 어떤 허가를 받아, 실제로 어떻게 매출을 만들 것인지에 따라 설립 방식이 달라집니다.",
        "en_intro": "Company setup, foreign-invested structures, representative offices, business registration, investment licensing, and operating permits depend on business type and operating model. Globos Holdings coordinates advisory support with execution planning.",
        "ko_problem": "계획 단계에서는 설립 비용, 절차, 자본금, 외투법인 구조를 검토합니다. 실행 단계에서는 실제 사업 모델에 맞는 허가 범위와 운영 구조를 먼저 정리해야 합니다.",
        "en_problem": "Planning usually begins with company setup cost, process, capital, and foreign-invested structures. Execution starts with the operating model and the licensing scope required for revenue.",
        "keywords": ["베트남 법인 설립", "베트남 법인 설립 비용", "베트남 법인 설립 자본금", "베트남 외투법인", "Vietnam company registration", "business setup cost in Vietnam"],
        "services_ko": ["법인을 왜 세우는지와 어떤 업종으로 운영할지 정리", "외투법인, 대표사무소, 사업자등록, 투자허가 검토 조율", "세무, 회계, 노무, 법률 지원이 필요한 지점 연결"],
        "services_en": ["Clarify the purpose of company setup and industry-specific structure", "Coordinate review of FIE, representative office, business registration, and investment licensing", "Connect tax, accounting, labor, and legal support functions"],
        "faqs_ko": [
            ["베트남 법인 설립 비용", "업종, 자본금, 외국인 투자 구조, 인허가 범위에 따른 변동."],
            ["대표사무소와 법인 차이", "대표사무소는 영업 활동 제한 가능성. 법인은 매출 발생과 운영 범위 확대. 업종별 검토 필요."],
            ["외투법인 자본금 기준", "업종과 허가 조건에 따른 요구 자본금 판단."],
            ["법률 서비스 범위", "법률 판단은 현지 전문가와 함께 확인합니다. Globos Holdings는 사업 방식과 운영 준비가 법인 설립과 맞게 이어지도록 조율합니다."],
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
        "ko_h1": "베트남 화장품 진출, 제품등록 이후 판매까지 봐야 합니다.",
        "en_h1": "Vietnam cosmetics entry requires registration, labeling, customs, and distribution to move together.",
        "ko_intro": "화장품은 제품등록만 끝났다고 바로 팔리는 시장이 아닙니다. 성분, 라벨링, CFS와 PIF, 수입자, 통관, 유통 채널까지 같이 준비되어야 합니다.",
        "en_intro": "Cosmetics export does not end with one approval. Ingredients, product notification, labeling, CFS/PIF, importer coordination, customs, and distribution channels must move together.",
        "ko_problem": "계획 단계에서는 화장품 수출, 인허가, 제품등록, 라벨링, 통관을 각각 검토합니다. 실행 단계에서는 이 과정이 출시 일정과 유통 계획 안에서 하나로 연결되어야 합니다.",
        "en_problem": "Planning separates cosmetics export, certification, registration, labeling, and customs. Execution works only when the full launch flow connects to distribution and sales timing.",
        "keywords": ["베트남 화장품 수출", "베트남 화장품 인허가", "베트남 화장품 제품등록", "베트남 화장품 라벨링", "Vietnam cosmetics registration", "Vietnam cosmetic product notification"],
        "services_ko": ["제품별 등록과 인허가 준비 항목 정리", "라벨링, CFS, PIF, 통관 요구사항 확인", "유통업체, 쇼피, 틱톡샵, 마케팅 판매 흐름 연결"],
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
        "ko_intro": "베트남에서 식당이나 카페를 여는 것보다 어려운 일은 오픈 이후입니다. 입지, 인허가, 인력, 식자재, POS, 배달, 마케팅, 매장 SOP가 매일 같이 돌아가야 합니다.",
        "en_intro": "Vietnam F&B entry requires location, licensing, staffing, ingredients, POS, delivery, marketing, and store SOPs to work together. Globos Holdings designs the local execution structure from real store operations.",
        "ko_problem": "계획 단계에서는 식당, 카페, 한식당, 프랜차이즈 창업 가능성을 검토합니다. 실행 단계에서는 오픈 이후의 인력, 식자재, 품질, POS, 배달 운영이 더 큰 과제가 됩니다.",
        "en_problem": "Planning begins with restaurant, cafe, Korean food, and franchise entry feasibility. Execution is shaped by staffing, ingredients, quality control, POS, delivery, and post-launch management.",
        "keywords": ["베트남 식당 창업", "베트남 카페 창업", "베트남 한식당 창업", "베트남 외식업 진출", "Vietnam restaurant business", "Vietnam F&B market entry"],
        "services_ko": ["F&B 브랜드 현지화와 매장 오픈 경로 설계", "점포 SOP, 인력 운영, POS, 배달 앱 준비", "식자재, 공급망, 마케팅, 프랜차이즈 전개 연결"],
        "services_en": ["Design F&B localization and store launch route", "Prepare store SOPs, staffing routines, POS, and delivery readiness", "Connect ingredients, supply chain, marketing, and franchise rollout"],
        "faqs_ko": [
            ["베트남 식당 창업 핵심 리스크", "오픈보다 인력, 원가, 공급망, 현장 관리, 배달 운영의 흔들림."],
            ["카페와 한식당 지원 범위", "카페, 한식당, F&B 프랜차이즈 운영 모델 검토."],
            ["점포 운영 방식", "브랜드와 지역, 투자 범위에 따라 직접 운영, 공동 운영, 운영 컨설팅 방식을 함께 검토합니다."],
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
        "ko_h1": "베트남 온라인 판매, 입점보다 운영이 더 중요합니다.",
        "en_h1": "Vietnam ecommerce entry starts with Shopee, Lazada, and TikTok Shop operating structure.",
        "ko_intro": "쇼피, 라자다, 틱톡샵은 상품만 올린다고 팔리는 채널이 아닙니다. 현지 셀러 구조, 콘텐츠, 광고, 물류, 통관, CS, 정산까지 같이 봐야 합니다.",
        "en_intro": "Shopee, Lazada, and TikTok Shop entry is not just product listing. Seller structure, content, ads, logistics, customs, customer service, and settlement routines must be prepared.",
        "ko_problem": "계획 단계에서는 쇼피, 라자다, 틱톡샵 입점을 검토합니다. 실행 단계에서는 상품 등록, 콘텐츠, 광고, 주문 처리, 정산을 현지에서 지속 운영할 수 있어야 합니다.",
        "en_problem": "Planning begins with Shopee, Lazada, and TikTok Shop entry. Execution requires listing, content, ads, order handling, customer service, and settlement to run continuously.",
        "keywords": ["베트남 쇼피 입점", "쇼피 베트남 판매", "베트남 라자다 입점", "베트남 틱톡샵 입점", "TikTok Shop Vietnam", "Shopee Vietnam seller"],
        "services_ko": ["쇼피, 라자다, 틱톡샵 입점 가능성 검토", "상품 등록, 콘텐츠, 광고, CS, 정산 운영 방식 정리", "물류, 통관, 유통, 마케팅을 판매 흐름에 맞게 연결"],
        "services_en": ["Review Shopee, Lazada, and TikTok Shop entry feasibility", "Design listing, content, ads, CS, and settlement routines", "Connect logistics, customs, distribution, and marketing execution"],
        "faqs_ko": [
            ["한국 회사의 베트남 쇼피 입점", "셀러 구조, 현지 사업자, 상품군, 물류 방식 기준 가능성 검토."],
            ["틱톡샵 베트남의 성격", "마케팅 채널이자 판매 채널. 콘텐츠와 라이브커머스의 판매 운영 연결 구조."],
            ["라자다와 쇼피 동시 운영", "상품군, 운영 인력, 마케팅 예산 기준 우선순위 설정."],
            ["Globos Holdings 지원 범위", "입점 방식, 상품 등록, 현지 운영 루틴, 마케팅, 물류와 통관 연결을 함께 검토합니다."],
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
        "ko_description": "베트남 틱톡 마케팅, 틱톡 광고, 틱톡샵 대행, 쇼피 마케팅, 인플루언서, 라이브커머스를 실제 판매 흐름과 연결합니다.",
        "en_description": "Vietnam TikTok, Shopee, influencer, SNS, live commerce, and ecommerce marketing support connected to sales execution and local brand localization.",
        "ko_h1": "베트남 마케팅, 조회수보다 판매가 중요합니다.",
        "en_h1": "Vietnam marketing must connect TikTok, Shopee, influencers, and sales conversion.",
        "ko_intro": "베트남에서 마케팅은 광고를 켜는 것만으로 끝나지 않습니다. 틱톡 광고, 틱톡샵, 쇼피 캠페인, 인플루언서, 라이브커머스가 실제 매출로 이어지도록 설계해야 합니다.",
        "en_intro": "Vietnam online marketing is not only ad buying. Channel-specific sales structure and content localization matter. TikTok ads, TikTok Shop, Shopee campaigns, influencers, and live commerce must connect to sales operations.",
        "ko_problem": "계획 단계에서는 틱톡 광고, 쇼피 마케팅, 인플루언서 운영을 검토합니다. 실행 단계에서는 채널별 콘텐츠, 라이브커머스, 광고비, 판매 전환 구조를 함께 관리해야 합니다.",
        "en_problem": "Planning begins with TikTok ads, Shopee marketing, agency support, and influencer campaigns. Execution requires channel-specific content, live commerce, media spend, and conversion management.",
        "keywords": ["베트남 틱톡 마케팅", "베트남 틱톡 광고", "베트남 쇼피 마케팅", "베트남 인플루언서 마케팅", "Vietnam TikTok marketing", "Shopee Vietnam marketing agency"],
        "services_ko": ["틱톡, 쇼피, SNS 채널별 캠페인 구조 설계", "인플루언서, 숏폼, 라이브커머스 실행 조율", "이커머스 판매, 매장 방문, 브랜드 런칭 목표와 연결"],
        "services_en": ["Design campaign structures by TikTok, Shopee, and SNS channel", "Coordinate influencer, short-form, and live commerce execution", "Connect campaigns to ecommerce sales, store visits, and brand launch goals"],
        "faqs_ko": [
            ["베트남 틱톡 마케팅 적합 브랜드", "뷰티, F&B, 리테일, 소비재처럼 영상 콘텐츠와 구매가 자연스럽게 이어지는 브랜드가 잘 맞습니다."],
            ["쇼피 마케팅과 틱톡 마케팅 병행", "제품군에 따라 다르지만, 인지도와 구매 전환을 함께 만들려면 두 채널을 같이 설계하는 편이 좋습니다."],
            ["인플루언서 섭외 포함 범위", "캠페인 목적과 예산에 따라 현지 인플루언서와 콘텐츠 제작 방식을 함께 검토합니다."],
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
        "ko_description": "베트남 유통업체, 유통망, 통관대행, 통관 비용, 수입관세, 물류업체, 냉장 물류까지 실제 판매 흐름에 맞춰 함께 검토합니다.",
        "en_description": "Vietnam distribution, customs clearance, import duties, logistics partners, distributor coordination, warehousing, cold chain, and route-to-market support.",
        "ko_h1": "베트남 유통, 업체 리스트만으로는 부족합니다.",
        "en_h1": "Vietnam distribution is not a vendor list. It is the structure from customs to sales channels.",
        "ko_intro": "제품을 베트남에 들여오는 일과 실제로 판매되는 일 사이에는 생각보다 많은 단계가 있습니다. 통관, 수입자, 관세, 창고, 물류, 유통업체, 판매 채널을 같이 봐야 합니다.",
        "en_intro": "For products to enter Vietnam, customs, importer coordination, duties, warehousing, logistics, distributors, and sales channels must connect. Globos Holdings reviews practical routes to market after entry.",
        "ko_problem": "계획 단계에서는 유통업체, 유통망, 통관대행, 수입관세, 물류업체를 각각 검토합니다. 실행 단계에서는 일정, 원가, 재고, 채널 입점을 하나의 프로세스로 관리해야 합니다.",
        "en_problem": "Planning often separates distributors, customs brokers, import duties, and logistics companies. Execution suffers unless timing, cost, inventory, and channel entry are managed as one process.",
        "keywords": ["베트남 유통업체", "베트남 유통망", "베트남 통관대행", "베트남 수입관세", "베트남 물류업체", "Vietnam distributor"],
        "services_ko": ["제품군별 유통 경로와 수입 방식 검토", "통관, 관세, 물류, 창고, 냉장 물류 확인", "오프라인 유통, 이커머스, 매장 판매 채널 연결"],
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
        "ko_h1": "베트남 소싱, 싸게 찾는 것보다 꾸준히 받는 것이 중요합니다.",
        "en_h1": "Vietnam sourcing is not only price comparison. It is building an operating supply chain.",
        "ko_intro": "베트남 소싱은 업체 리스트를 받는 것으로 끝나지 않습니다. 품질, 납기, 통관, 물류, 매장 공급, 정산, 지속 가능성까지 봐야 실제 운영에 쓸 수 있습니다.",
        "en_intro": "Sourcing does not end with factory or supplier lists. Quality, delivery, customs, logistics, store supply, settlement, and continuity must be reviewed together.",
        "ko_problem": "계획 단계에서는 소싱 업체, 제조 소싱, 식자재 유통을 검토합니다. 실행 단계에서는 품질, 납기, 단가, 반복 공급이 가능한 현지 공급망을 확보해야 합니다.",
        "en_problem": "Planning begins with sourcing agents, factories, and ingredient distribution. Execution depends on quality, delivery timing, price control, and a supply base that can repeat.",
        "keywords": ["베트남 소싱", "베트남 소싱 업체", "베트남 제조 소싱", "베트남 식자재 유통", "Vietnam sourcing agent", "Vietnam supplier development"],
        "services_ko": ["제품과 브랜드 운영에 맞는 공급처 조건 정리", "제조, 식자재, 부자재, 물류 연결 가능성 확인", "점포 운영, 유통, 이커머스 판매까지 이어지는 공급망 설계"],
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


def object_particle(value: str) -> str:
    stripped = value.strip()
    if not stripped:
        return "을"
    code = ord(stripped[-1])
    if 0xAC00 <= code <= 0xD7A3 and (code - 0xAC00) % 28 == 0:
        return "를"
    return "을"


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
            "foundingDate": "2025",
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
    home_href = f"../../index.html?lang={'ko' if is_ko else 'en'}"
    contact_href = "../../contact.html"
    lang_label = "English" if is_ko else "한국어"
    eyebrow = "계획을 실행으로 바꾸는 지점" if is_ko else "From planning to execution"
    overview_label = "초기 검토 키워드" if is_ko else "Initial review keywords"
    landing_name = page["ko_title"].split(" | ")[0] if is_ko else page["en_title"].split(" | ")[0]
    geo_label = "실행 관점 요약" if is_ko else "Execution summary"
    geo_title = f"{landing_name} 실행 요약" if is_ko else f"{landing_name} execution summary"
    geo_body = (
        f"Globos Holdings는 {landing_name}{object_particle(landing_name)} 자료 검토 단계에 머무르게 두지 않고, 베트남 현지에서 바로 확인해야 할 실행 과제로 정리합니다. 법인, 인허가, 유통, 운영, 마케팅, 시스템 중 먼저 풀어야 할 범위를 함께 확인합니다."
        if is_ko
        else f"Globos Holdings treats {landing_name} as an execution agenda, not a research note. We map the first operating gap across company setup, licensing, distribution, store operations, marketing, and systems."
    )
    proof_label = "운영 실적" if is_ko else "Operating proof"
    proof_text = (
        "2025년 설립 이후 베트남에서 직접 운영 기반을 쌓고 있습니다. 현재 8개 점포를 운영하고, 한국 협업 프로젝트 2개를 진행 중입니다. 2030년까지 300개 점포와 협업 브랜드/파트너 30개를 목표로 in-house ERP, SaaS POS, 배달 앱 기반을 함께 키우고 있습니다."
        if is_ko
        else "Founded in 2025, Globos Holdings currently operates 8 stores, runs 2 Korea collaboration projects, and targets 300 stores with 30 collaboration brands/partners by 2030. in-house ERP, SaaS POS, and delivery app infrastructure are connected to the operating model."
    )
    can_do = "지원 가능 범위" if is_ko else "What Globos Holdings supports"
    search_problem = "계획과 실행의 Gap" if is_ko else "The Gap Between Planning and Execution"
    faq_title = "상담 전 주요 질문" if is_ko else "Frequently Asked Questions"
    cta_title = "현재 준비 상황부터 정리해 드립니다." if is_ko else "Start with the execution gap."
    cta_body = (
        "브랜드, 제품군, 목표 지역, 준비 단계, 가장 먼저 풀어야 할 과제를 알려주시면 필요한 실행 범위와 진행 순서를 정리해 드립니다."
        if is_ko
        else "Send your brand, product category, target region, current preparation stage, and the first issue to solve. We will map the next execution route."
    )
    cta_button = "문의하기" if is_ko else "Contact Globos Holdings"
    nav_guides = "사이트맵" if is_ko else "Site map"
    nav_contact = "문의" if is_ko else "Contact"
    nav_about = "회사소개" if is_ko else "About"
    nav_leaders = "경영진" if is_ko else "Leadership"
    nav_vision = "비전&미션" if is_ko else "Vision & Mission"
    nav_org = "조직도" if is_ko else "Organization"
    nav_partnership = "로컬 파트너십 안내" if is_ko else "Local Partnership"
    nav_partnership_structure = "파트너십 구조" if is_ko else "Partnership Structure"
    nav_partnership_reason = "현지 실행 필요성" if is_ko else "Why Local Execution"
    nav_partnership_infra = "운영 인프라" if is_ko else "Operating Infrastructure"
    nav_business = "제공가능 비즈니스 영역" if is_ko else "Business Areas"
    nav_business_franchise = "F&B/화장품/IT 서비스" if is_ko else "F&B, beauty, and IT services"
    nav_business_legal = "베트남 현지 법률 기반 서비스" if is_ko else "Vietnam legal-based services"
    nav_business_marketing = "온·오프라인 마케팅 채널/인프라" if is_ko else "Online/offline marketing channels"
    nav_business_sourcing = "유통·소싱" if is_ko else "Distribution & Sourcing"
    nav_business_systems = "자체 IT 인프라" if is_ko else "In-house IT infrastructure"
    nav_record = "운영 실적" if is_ko else "Track Record"
    nav_record_current = "운영 현황" if is_ko else "Operating Numbers"
    nav_record_flow = "실행 프로세스" if is_ko else "Execution Flow"
    nav_record_guides = "베트남 진출 가이드" if is_ko else "Vietnam Entry Guides"
    nav_consult = "상담 문의" if is_ko else "Consultation"
    nav_email = "이메일" if is_ko else "Email"
    related_title = "같이 보면 좋은 페이지" if is_ko else "Related landing pages"
    flow_title = "일하는 순서" if is_ko else "Execution flow"
    flow_body = (
        "시장 검토는 하나의 주제에서 시작되지만, 현지 실행은 법인, 인허가, 유통, 운영, 시스템이 순서대로 맞물려야 합니다."
        if is_ko
        else "Market review may begin with one topic, but local execution works only when legal, licensing, distribution, operations, and systems connect in order."
    )
    keyword_title = "시장 검토의 출발점" if is_ko else "Where market review begins"
    dashboard_title = "운영 기반" if is_ko else "Operating base"
    dashboard_subtitle = (
        "현재 운영 현황과 2030년 확장 목표를 함께 제시합니다."
        if is_ko
        else "Live operating numbers and the 2030 expansion vision shown together."
    )
    operations_started = "회사 설립" if is_ko else "Company founded"
    now_label = "현재" if is_ko else "Now"
    stores_label = "운영 점포" if is_ko else "stores"
    partners_label = "한국 협업" if is_ko else "Korea collaboration"
    firms_label = "프로젝트" if is_ko else "projects"
    target_label = "2030 목표" if is_ko else "2030 target"
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
    flow_cards = "\n".join(
        f"""
        <article class="rounded-sm border border-line bg-white p-5">
          <p class="text-xs font-extrabold uppercase text-cobalt">{idx:02d}</p>
          <h3 class="mt-3 font-headline text-xl font-bold text-ink">{esc(item)}</h3>
          <div class="mt-5 h-2 overflow-hidden rounded-sm bg-fog">
            <span class="landing-bar block h-full bg-brass" style="width: {min(92, 46 + idx * 14)}%"></span>
          </div>
        </article>
        """
        for idx, item in enumerate(services, 1)
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
            .landing-bar {{ animation: landingBar 3.8s ease-in-out infinite alternate; transform-origin: left; }}
            .landing-pulse {{ animation: landingPulse 2.4s ease-in-out infinite; }}
            .nav-group {{ position: relative; }}
            .nav-trigger {{ display: inline-flex; align-items: center; border-radius: 0.125rem; padding: 0.625rem 0.5rem; color: #5c6672; transition: color 160ms ease, background-color 160ms ease; }}
            .nav-trigger:hover, .nav-trigger:focus-visible, .nav-group:focus-within .nav-trigger {{ color: #002147; background: #f4f6f7; outline: none; }}
            .nav-panel {{ position: absolute; left: 0; top: calc(100% + 0.5rem); z-index: 60; min-width: 230px; border: 1px solid #d8dde3; background: rgba(255,255,255,.98); padding: .5rem; box-shadow: 0 18px 42px rgba(7, 26, 49, .12); opacity: 0; visibility: hidden; transform: translateY(6px); transition: opacity 160ms ease, transform 160ms ease, visibility 160ms ease; }}
            .nav-group:hover .nav-panel, .nav-group:focus-within .nav-panel {{ opacity: 1; visibility: visible; transform: translateY(0); }}
            .nav-panel a {{ display: block; border-radius: 0.125rem; padding: .75rem .85rem; font-size: .8125rem; font-weight: 700; color: #5c6672; white-space: nowrap; }}
            .nav-panel a:hover, .nav-panel a:focus-visible {{ color: #002147; background: #f4f6f7; outline: none; }}
            .mobile-menu-button {{ display: inline-flex; align-items: center; justify-content: center; width: 42px; height: 42px; border: 1px solid #d8dde3; background: #fff; color: #002147; transition: border-color 160ms ease, background-color 160ms ease, transform 160ms ease; }}
            .mobile-menu-button:hover, .mobile-menu-button:focus-visible {{ border-color: #002147; background: #f4f6f7; transform: translateY(-1px); outline: none; }}
            .mobile-nav-panel {{ max-height: calc(100dvh - 73px); overflow-y: auto; border-top: 1px solid #d8dde3; background: rgba(255,255,255,.98); box-shadow: 0 20px 60px rgba(7,26,49,.12); }}
            .mobile-nav-panel[hidden] {{ display: none !important; }}
            .mobile-nav-panel a {{ display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #edf0f3; padding: .95rem 1.25rem; font-size: .9375rem; font-weight: 800; color: #071a31; }}
            .mobile-nav-panel a:hover, .mobile-nav-panel a:focus-visible {{ background: #f4f6f7; color: #0b4d8f; outline: none; }}
            body.mobile-nav-open {{ overflow: hidden; }}
            @media (min-width: 1024px) {{ .mobile-menu-button, .mobile-nav-panel {{ display: none !important; }} }}
            @keyframes landingBar {{ from {{ transform: scaleX(.52); opacity: .58; }} to {{ transform: scaleX(1); opacity: 1; }} }}
            @keyframes landingPulse {{ 0%, 100% {{ opacity: .45; transform: scale(1); }} 50% {{ opacity: 1; transform: scale(1.12); }} }}
            @media (prefers-reduced-motion: reduce) {{ .landing-bar, .landing-pulse {{ animation: none; }} }}
          </style>
          <script type="application/ld+json">
        {json_ld}
          </script>
        </head>
        <body class="font-body antialiased">
          <header class="sticky top-0 z-50 border-b border-line bg-white/95 backdrop-blur">
            <nav class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-5 py-4 lg:px-8" aria-label="Primary navigation">
              <a class="brand-name font-headline text-xl font-bold text-navy sm:text-2xl" href="{home_href}">Globos Holdings</a>
              <div class="hidden items-center gap-1 text-sm font-bold text-slatecopy lg:flex">
                <div class="nav-group">
                  <a class="nav-trigger" href="{home_href}#leadership">{nav_about}</a>
                  <div class="nav-panel" aria-label="{nav_about} submenu">
                    <a href="{home_href}#leadership">{nav_leaders}</a>
                    <a href="{home_href}#mission-vision">{nav_vision}</a>
                    <a href="{home_href}#organization">{nav_org}</a>
                  </div>
                </div>
                <div class="nav-group">
                  <a class="nav-trigger" href="{home_href}#local-partner">{nav_partnership}</a>
                  <div class="nav-panel" aria-label="{nav_partnership} submenu">
                    <a href="{home_href}#local-partner">{nav_partnership_structure}</a>
                    <a href="{home_href}#why-globos">{nav_partnership_reason}</a>
                    <a href="{home_href}#operating-system">{nav_partnership_infra}</a>
                  </div>
                </div>
                <div class="nav-group">
                  <a class="nav-trigger" href="{home_href}#capabilities">{nav_business}</a>
                  <div class="nav-panel" aria-label="{nav_business} submenu">
                    <a href="../../{lang}/capabilities/franchise-expansion.html">{nav_business_franchise}</a>
                    <a href="../../{lang}/capabilities/legal-advisory.html">{nav_business_legal}</a>
                    <a href="../../{lang}/capabilities/marketing-services.html">{nav_business_marketing}</a>
                    <a href="../../{lang}/capabilities/vietnam-sourcing.html">{nav_business_sourcing}</a>
                    <a href="../../{lang}/capabilities/it-systems-development.html">{nav_business_systems}</a>
                  </div>
                </div>
                <div class="nav-group">
                  <a class="nav-trigger text-navy" href="{home_href}#proof">{nav_record}</a>
                  <div class="nav-panel" aria-label="{nav_record} submenu">
                    <a href="{home_href}#proof">{nav_record_current}</a>
                    <a href="{home_href}#execution-flow">{nav_record_flow}</a>
                    <a href="{home_href}#seo-landings">{nav_record_guides}</a>
                  </div>
                </div>
                <div class="nav-group">
                  <a class="nav-trigger" href="{contact_href}">{nav_contact}</a>
                  <div class="nav-panel" aria-label="{nav_contact} submenu">
                    <a href="{contact_href}">{nav_consult}</a>
                    <a href="mailto:contact@globos.world?subject=Globos Holdings Website Inquiry">{nav_email}</a>
                    <a href="../../site-map.html">{nav_guides}</a>
                  </div>
                </div>
              </div>
              <div class="flex items-center gap-2">
                <a class="rounded-sm border border-line bg-fog px-4 py-2 text-xs font-extrabold text-navy hover:border-navy" href="../../{other}/{slug}/">{lang_label}</a>
                <button class="mobile-menu-button lg:hidden" type="button" data-mobile-toggle aria-controls="mobile-menu" aria-expanded="false" aria-label="Open navigation">
                  <span class="material-symbols-outlined text-xl" aria-hidden="true">menu</span>
                </button>
              </div>
            </nav>
            <div id="mobile-menu" class="mobile-nav-panel lg:hidden" data-mobile-menu hidden>
              <a href="{home_href}#leadership"><span>{nav_about}</span><span class="material-symbols-outlined text-lg" aria-hidden="true">arrow_forward</span></a>
              <a href="{home_href}#local-partner"><span>{nav_partnership}</span><span class="material-symbols-outlined text-lg" aria-hidden="true">arrow_forward</span></a>
              <a href="{home_href}#capabilities"><span>{nav_business}</span><span class="material-symbols-outlined text-lg" aria-hidden="true">arrow_forward</span></a>
              <a href="{home_href}#proof"><span>{nav_record}</span><span class="material-symbols-outlined text-lg" aria-hidden="true">arrow_forward</span></a>
              <a href="{contact_href}"><span>{nav_contact}</span><span class="material-symbols-outlined text-lg" aria-hidden="true">north_east</span></a>
            </div>
          </header>
          <main>
            <section class="bg-white">
              <div class="mx-auto grid max-w-7xl gap-10 px-5 py-16 lg:grid-cols-[1fr_410px] lg:px-8 lg:py-24">
                <div>
                  <p class="mb-6 text-xs font-extrabold uppercase text-cobalt">{eyebrow}</p>
                  <h1 class="font-headline text-4xl font-bold leading-tight text-ink md:text-6xl">{esc(h1)}</h1>
                  <p class="mt-7 max-w-3xl text-lg leading-8 text-slatecopy">{esc(intro)}</p>
                  <div class="mt-9 flex flex-col gap-3 sm:flex-row">
                    <a class="primary-action inline-flex items-center justify-center gap-2 rounded-sm bg-navy px-7 py-4 text-sm font-extrabold text-white hover:bg-cobalt" href="{contact_href}">{cta_button}<span class="material-symbols-outlined text-lg" aria-hidden="true">arrow_forward</span></a>
                    <a class="secondary-action inline-flex items-center justify-center gap-2 rounded-sm border border-line bg-white px-7 py-4 text-sm font-extrabold text-navy hover:border-navy" href="{home_href}">Globos Holdings</a>
                  </div>
                </div>
                <aside class="rounded-sm border border-line bg-[#071a31] p-6 text-white shadow-firm">
                  <p class="text-xs font-extrabold uppercase text-white/50">{dashboard_title}</p>
                  <h2 class="mt-3 font-headline text-3xl font-bold">{proof_label}</h2>
                  <p class="mt-3 text-sm leading-7 text-white/65">{dashboard_subtitle}</p>
                  <div class="mt-6 grid gap-3">
                    <div class="rounded-sm border border-white/10 bg-white/10 p-4">
                      <p class="text-xs uppercase text-white/45">2025</p>
                      <p class="mt-1 font-headline text-2xl font-bold">{operations_started}</p>
                    </div>
                    <div class="grid grid-cols-2 gap-3">
                      <div class="rounded-sm border border-white/10 bg-white/10 p-4">
                        <p class="text-xs uppercase text-white/45">{now_label}</p>
                        <p class="mt-1 font-headline text-3xl font-bold">8</p>
                        <p class="text-xs text-white/55">{stores_label}</p>
                      </div>
                      <div class="rounded-sm border border-white/10 bg-white/10 p-4">
                        <p class="text-xs uppercase text-white/45">{partners_label}</p>
                        <p class="mt-1 font-headline text-3xl font-bold">2</p>
                        <p class="text-xs text-white/55">{firms_label}</p>
                      </div>
                    </div>
                    <div class="rounded-sm border border-white/10 bg-white/10 p-4">
                      <div class="flex items-center justify-between gap-3">
                        <p class="font-bold">{target_label}</p>
                        <p class="font-headline text-3xl font-bold text-brass">300</p>
                      </div>
                      <div class="mt-4 h-2 overflow-hidden rounded-sm bg-white/10">
                        <span class="landing-bar block h-full bg-brass"></span>
                      </div>
                    </div>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs font-bold">
                      <span class="landing-pulse rounded-sm bg-white/10 px-2 py-3">ERP</span>
                      <span class="landing-pulse rounded-sm bg-white/10 px-2 py-3" style="animation-delay: .25s">POS</span>
                      <span class="landing-pulse rounded-sm bg-white/10 px-2 py-3" style="animation-delay: .5s">Delivery</span>
                    </div>
                  </div>
                </aside>
              </div>
            </section>

            <section class="border-y border-line bg-fog py-10">
              <div class="mx-auto max-w-7xl px-5 lg:px-8">
                <div class="grid gap-6 lg:grid-cols-[320px_1fr] lg:items-center">
                  <div>
                    <p class="text-xs font-extrabold uppercase text-cobalt">{overview_label}</p>
                    <h2 class="mt-3 font-headline text-3xl font-bold text-ink">{keyword_title}</h2>
                  </div>
                  <ul class="flex flex-wrap gap-2">
                    {keyword_tags}
                  </ul>
                </div>
              </div>
            </section>

            <section id="geo-answer" class="bg-white py-12">
              <div class="mx-auto max-w-7xl px-5 lg:px-8">
                <div class="rounded-sm border border-line bg-fog p-6 md:p-8">
                  <p class="text-xs font-extrabold uppercase text-cobalt">{geo_label}</p>
                  <h2 class="mt-3 font-headline text-3xl font-bold leading-tight text-ink">{esc(geo_title)}</h2>
                  <p class="mt-4 max-w-4xl leading-8 text-slatecopy">{esc(geo_body)}</p>
                </div>
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
              <div class="mx-auto max-w-7xl px-5 lg:px-8">
                <div class="max-w-3xl">
                  <h2 class="font-headline text-3xl font-bold text-ink">{flow_title}</h2>
                  <p class="mt-5 leading-8 text-slatecopy">{flow_body}</p>
                </div>
                <div class="mt-8 grid gap-4 md:grid-cols-3">
                  {flow_cards}
                </div>
              </div>
            </section>

            <section class="bg-white py-14">
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
                <a class="hover:text-navy" href="../../site-map.html">{nav_guides}</a>
                <p>© 2026 Globos Holdings. All rights reserved.</p>
              </div>
            </div>
          </footer>
          <script>
            const mobileToggle = document.querySelector('[data-mobile-toggle]');
            const mobileMenu = document.querySelector('[data-mobile-menu]');
            function closeMobileMenu() {{
              if (!mobileMenu || !mobileToggle) return;
              mobileMenu.hidden = true;
              mobileToggle.setAttribute('aria-expanded', 'false');
              mobileToggle.querySelector('.material-symbols-outlined').textContent = 'menu';
              document.body.classList.remove('mobile-nav-open');
            }}
            mobileToggle?.addEventListener('click', () => {{
              const willOpen = mobileMenu.hidden;
              mobileMenu.hidden = !willOpen;
              mobileToggle.setAttribute('aria-expanded', String(willOpen));
              mobileToggle.querySelector('.material-symbols-outlined').textContent = willOpen ? 'close' : 'menu';
              document.body.classList.toggle('mobile-nav-open', willOpen);
            }});
            document.querySelectorAll('[data-mobile-menu] a').forEach((link) => link.addEventListener('click', closeMobileMenu));
            window.addEventListener('resize', () => {{ if (window.innerWidth >= 1024) closeMobileMenu(); }});
          </script>
        </body>
        </html>
        """
    )


def render_sitemap() -> str:
    capability_slugs = [
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
    ]
    urls = [
        f"{DOMAIN}/",
        f"{DOMAIN}/site-map",
        f"{DOMAIN}/contact",
        *[abs_url(lang, page["slug"]) for lang in ("ko", "en") for page in PAGES],
        *[f"{DOMAIN}/{lang}/capabilities/{slug}" for lang in ("ko", "en") for slug in capability_slugs],
        *[f"{DOMAIN}/capabilities/{slug}" for slug in capability_slugs],
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
