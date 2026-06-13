/* ============================================================
   webbackground-growth-3d — 실시간 2.5D WebGL 성장 지도
   Three.js r128 + GSAP 3 / 모바일 60fps 목표
   ============================================================ */
(function () {
"use strict";

/* ---------------- CONFIG (비즈니스 숫자는 여기서만) ---------------- */
const CONFIG = {
  YEAR_S: 2.4,            // 1년이 흐르는 시간(초)
  HOLD_S: 3.5,            // 완성 후 정지(초)
  years:  [2026, 2027, 2028, 2029, 2030, 2031],
  stores: [90, 240, 420, 660, 900, 1500],
  revenue:[3, 9, 24, 54, 90, 135],        // $M
  brands: [3, 15, 36, 63, 96, 135],       // 직영+협력 합계
  // 호치민 중심 점등 반경(월드 단위) — 매년 약 2배 확장 (5배 광역)
  glowRadii: [3.5, 7, 14, 26, 42, 62],
  FPS_CAP: 24,            // 배경용 프레임 캡
  baseOpacity: 1.0,       // 캔버스 밝기
};

/* ---------------- 좌표계: SVG 지도 좌표 → 월드 ---------------- */
const S = 0.02, CX = 190, CY = 395, TOP = 0.3;   // 지도 두께 0.3
const W = (x, y) => [(x - CX) * S, (y - CY) * S]; // [wx, wz]
const BASE_FINAL_STORES = 500;
const STORE_SCALE = CONFIG.stores[CONFIG.stores.length - 1] / BASE_FINAL_STORES;
const MAP_AREA_BOOST = 3;                       // 직전 대비 지도 점유 면적 약 50% 축소
const MAP_CAMERA_FILL = 1;
const EXTRA_BUILDING_DENSITY = 4.4;
const BUILDING_DENSITY = Math.max(1, Math.min(14,
  Math.round(STORE_SCALE * EXTRA_BUILDING_DENSITY)));
const LIGHT_BOOST = Math.min(1.55, 1 + (STORE_SCALE - 1) * 0.25);
const FLOW_DOTS = Math.min(9, 2 + Math.ceil(BUILDING_DENSITY / 2));
const FINAL_MAP_VIEWPORT_FILL = 0.5;           // 최종 프레임은 지도 전체가 화면 절반 수준
const FINAL_DIST_MUL = 1 / FINAL_MAP_VIEWPORT_FILL;
const INITIAL_DIST_MUL = FINAL_DIST_MUL + 0.35; // 첫 화면은 베트남 전체가 안정적으로 보이는 거리
const BUILDING_FOOTPRINT_MUL = 1.15;
const BUILDING_HEIGHT_MUL = 1.45;
const BUILDING_CLUSTER_MUL = 0.5;

let _seed = 20260612;
function rng(){ _seed|=0; _seed=_seed+0x6D2B79F5|0;
  let t=Math.imul(_seed^_seed>>>15,1|_seed);
  t=t+Math.imul(t^t>>>7,61|t)^t; return ((t^t>>>14)>>>0)/4294967296; }

/* 베트남 외곽 폴리라인 (각진 윤곽, SVG와 동일) */
const VN = [[175,8],[205,4],[232,14],[252,30],[244,46],[270,52],[292,78],[285,100],
[300,112],[282,128],[255,132],[238,150],[232,140],[218,158],[210,150],[198,172],
[206,188],[192,206],[200,226],[188,242],[205,268],[222,292],[238,320],[252,344],
[270,360],[288,372],[302,386],[296,400],[316,418],[330,440],[342,466],[354,496],
[360,524],[358,552],[344,580],[326,604],[312,624],[296,640],[276,656],[258,672],
[248,690],[236,706],[212,724],[196,744],[172,762],[150,778],[134,766],[140,742],
[128,728],[148,708],[158,690],[150,672],[170,648],[196,612],[228,564],[258,524],
[270,488],[262,452],[248,418],[234,388],[218,356],[202,328],[190,300],[172,272],
[150,248],[128,228],[102,212],[78,198],[58,178],[40,150],[28,124],[18,100],
[34,80],[28,58],[50,44],[74,42],[96,30],[120,22],[148,12]];

const VN_WORLD = VN.map(([x, y]) => W(x, y));
function pointInVietnam(x, z) {
  let inside = false;
  for (let i = 0, j = VN_WORLD.length - 1; i < VN_WORLD.length; j = i++) {
    const [xi, zi] = VN_WORLD[i];
    const [xj, zj] = VN_WORLD[j];
    const crosses = ((zi > z) !== (zj > z)) &&
      (x < (xj - xi) * (z - zi) / ((zj - zi) || 1e-9) + xi);
    if (crosses) inside = !inside;
  }
  return inside;
}
function pointWithInsetInVietnam(x, z, inset) {
  return pointInVietnam(x, z) &&
    pointInVietnam(x - inset, z - inset) &&
    pointInVietnam(x + inset, z - inset) &&
    pointInVietnam(x - inset, z + inset) &&
    pointInVietnam(x + inset, z + inset);
}

/* 도시: [지도x, 지도y, 점등연도(0-base), 빌딩수, 규모] */
const CITIES = [
  [240,668, 0, 4, 1.00, "HCMC"],      // 2026 호치민 중심
  [252,652, 1, 2, 0.55],              // 2027 광역권 (비엔호아)
  [252,690, 1, 2, 0.50],              //      (붕따우)
  [216,688, 1, 1, 0.40],              //      (롱안)
  [195,700, 2, 2, 0.60, "CAN THO"],   // 2028 남부
  [160,710, 2, 1, 0.40],              //      (락자)
  [312,612, 2, 1, 0.45],              //      (달랏)
  [336,576, 2, 1, 0.50],              //      (나트랑)
  [290,392, 3, 3, 0.70, "DA NANG"],   // 2029 중부
  [276,366, 3, 1, 0.45],              //      (후에)
  [340,500, 3, 1, 0.40],              //      (꾸이년)
  [198,126, 4, 3, 0.80, "HANOI"],     // 2030 북부
  [240,145, 4, 2, 0.55, "HAI PHONG"],
  [198,198, 4, 1, 0.40],              //      (타인호아)
  [188,256, 5, 1, 0.38],              // 2031 전역
  [230,310, 5, 1, 0.36],
  [288,540, 5, 1, 0.36],
  [160,690, 5, 1, 0.34],
  [222,92,  4, 1, 0.36],              // 북부 보강
  [166,116, 4, 1, 0.32],
  [196,224, 5, 1, 0.34],              // 북중부 보강
  [230,286, 5, 1, 0.32],
  [262,430, 3, 2, 0.44],              // 중부·고원 보강
  [314,474, 3, 1, 0.36],
  [326,540, 4, 1, 0.36],
  [282,590, 4, 1, 0.34],
  [230,632, 2, 1, 0.38],              // 남부 보강
  [286,662, 3, 1, 0.34],
  [220,716, 5, 1, 0.30],
  [174,732, 5, 1, 0.30],
];

/* 네트워크 라인: [도시idx A, 도시idx B, 등장연도] */
const LINKS = [
  [0,1,1],[0,2,1],[0,3,1],
  [0,4,2],[4,5,2],[0,6,2],[6,7,2],
  [0,8,3],[8,9,3],[8,10,3],
  [8,11,4],[11,12,4],[11,13,4],
  [11,14,5],[0,15,5],[8,16,5],[4,17,5],
];

/* ---------------- 기본 셋업 ---------------- */
const root = document.getElementById("growth-bg");
function purgeGrowthHud() {
  if (!root) return;
  root.querySelectorAll(
    ".hud-year,.hud-stores,.hud-side,.hud-revenue,.hud-brands,#hudYear,#hudStores,#hudRevenue,#hudBrands"
  ).forEach(el => el.remove());
  root.querySelectorAll("*").forEach(el => {
    if (el.tagName === "CANVAS" || el.classList.contains("veil-vignette") ||
        el.classList.contains("veil-loop") || el.classList.contains("fps")) return;
    const text = (el.textContent || "").replace(/\s+/g, " ").trim();
    if (/^(300|60|30)$/i.test(text) ||
        /^(TOTAL STORES|COLLABS|PARTNERS)$/i.test(text)) el.remove();
  });
}
purgeGrowthHud();
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true,
  powerPreference: "low-power" });
renderer.shadowMap.enabled = false;                       // 그림자 비활성
let DPR = Math.min(window.devicePixelRatio || 1, 2);
renderer.setPixelRatio(DPR);
root.prepend(renderer.domElement);
renderer.domElement.style.opacity = CONFIG.baseOpacity;
purgeGrowthHud();
new MutationObserver(purgeGrowthHud).observe(root, {
  childList: true,
  subtree: true,
  characterData: true
});

const scene = new THREE.Scene();
scene.fog = new THREE.Fog(0x0a142e, 30, 80);

const camera = new THREE.PerspectiveCamera(45, 1, 0.02, 100);
scene.add(new THREE.AmbientLight(0x3d5a96, 1.7));
const hemi = new THREE.HemisphereLight(0x6fa9ff, 0x061126, 0.65);
scene.add(hemi);
const dir = new THREE.DirectionalLight(0x8db4ec, 0.85);
dir.position.set(-6, 12, -4);
scene.add(dir);
const cityKey = new THREE.PointLight(0xffc97c, 1.25, 18, 2);
cityKey.position.set(1.0, 7.5, 5.8);
scene.add(cityKey);

/* ---------------- 베트남 지형 (extrude, 어두운 블루) ---------------- */
const shape = new THREE.Shape();
VN.forEach(([x, y], i) => {
  const px = (x - CX) * S, py = (CY - y) * S;
  i ? shape.lineTo(px, py) : shape.moveTo(px, py);
});
const landGeo = new THREE.ExtrudeGeometry(shape,
  { depth: TOP, bevelEnabled: false });
landGeo.rotateX(-Math.PI / 2);
function makeLandTexture() {
  const c = document.createElement("canvas");
  c.width = c.height = 256;
  const g = c.getContext("2d");
  const grad = g.createLinearGradient(0, 0, 256, 256);
  grad.addColorStop(0, "#2a4a8a");
  grad.addColorStop(0.5, "#1c3972");
  grad.addColorStop(1, "#0f285c");
  g.fillStyle = grad;
  g.fillRect(0, 0, 256, 256);
  for (let i = 0; i < 900; i++) {
    const a = 0.035 + rng() * 0.055;
    g.fillStyle = `rgba(180,215,255,${a})`;
    g.fillRect(rng() * 256, rng() * 256, 1 + rng() * 2, 1 + rng() * 2);
  }
  g.strokeStyle = "rgba(150,190,255,.08)";
  g.lineWidth = 1;
  for (let y = 18; y < 256; y += 26) {
    g.beginPath();
    for (let x = 0; x <= 256; x += 8) {
      const yy = y + Math.sin((x + y) * 0.04) * 4;
      x ? g.lineTo(x, yy) : g.moveTo(x, yy);
    }
    g.stroke();
  }
  const tex = new THREE.CanvasTexture(c);
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
  tex.repeat.set(1.5, 2.8);
  return tex;
}
const land = new THREE.Mesh(landGeo, new THREE.MeshPhongMaterial({
  color: 0x274980,
  emissive: 0x101f44,
  shininess: 18,
  map: makeLandTexture(),
  specular: 0x1d4a86
}));
scene.add(land);

// 윤곽선 (살짝 빛나는 에지 라인)
const edgePos = [];
VN.concat([VN[0]]).forEach(([x, y]) => {
  const [wx, wz] = W(x, y);
  edgePos.push(wx, TOP + 0.012, wz);
});
const edgeGeo = new THREE.BufferGeometry();
edgeGeo.setAttribute("position", new THREE.Float32BufferAttribute(edgePos, 3));
scene.add(new THREE.Line(edgeGeo, new THREE.LineBasicMaterial({
  color: 0x9cc4ff, transparent: true, opacity: 0.8 })));

const coastHalo = new THREE.Line(edgeGeo.clone(), new THREE.LineBasicMaterial({
  color: 0x6fb5ff,
  transparent: true,
  opacity: 0.16,
  blending: THREE.AdditiveBlending,
  depthWrite: false
}));
coastHalo.scale.set(1.018, 1, 1.018);
scene.add(coastHalo);

/* ---------------- 글로우 텍스처 (캔버스 1장 공유) ---------------- */
function makeGlowTexture() {
  const c = document.createElement("canvas");
  c.width = c.height = 128;
  const g = c.getContext("2d");
  const grad = g.createRadialGradient(64, 64, 0, 64, 64, 64);
  grad.addColorStop(0, "rgba(255,214,140,1)");
  grad.addColorStop(0.35, "rgba(120,170,250,.55)");
  grad.addColorStop(1, "rgba(60,110,220,0)");
  g.fillStyle = grad;
  g.fillRect(0, 0, 128, 128);
  return new THREE.CanvasTexture(c);
}
const glowTex = makeGlowTexture();

function makeRingTexture() {
  const c = document.createElement("canvas");
  c.width = c.height = 256;
  const g = c.getContext("2d");
  const grad = g.createRadialGradient(128, 128, 82, 128, 128, 128);
  grad.addColorStop(0, "rgba(255,205,112,0)");
  grad.addColorStop(0.58, "rgba(255,205,112,.06)");
  grad.addColorStop(0.78, "rgba(140,190,255,.46)");
  grad.addColorStop(0.88, "rgba(255,216,146,.34)");
  grad.addColorStop(1, "rgba(95,145,255,0)");
  g.fillStyle = grad;
  g.fillRect(0, 0, 256, 256);
  return new THREE.CanvasTexture(c);
}
const ringTex = makeRingTexture();

/* 호치민 중심 확장 글로우 (매년 ~2배) — 지면 위 평면 1장 */
const [hx, hz] = W(240, 668);
const spread = new THREE.Mesh(
  new THREE.PlaneGeometry(2, 2),
  new THREE.MeshBasicMaterial({ map: glowTex, transparent: true,
    opacity: 0.0, blending: THREE.AdditiveBlending, depthWrite: false }));
spread.rotation.x = -Math.PI / 2;
spread.scale.set(0.3, 0.3, 1);
spread.position.set(hx, TOP + 0.02, hz);
scene.add(spread);

/* 성장 파동: 호치민에서 전국으로 퍼지는 얇은 에너지 링 */
const waveGeo = new THREE.PlaneGeometry(2, 2);
const waves = [0, 1, 2].map(i => {
  const mat = new THREE.MeshBasicMaterial({
    map: ringTex,
    transparent: true,
    opacity: 0,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  });
  const wave = new THREE.Mesh(waveGeo, mat);
  wave.rotation.x = -Math.PI / 2;
  wave.position.set(hx, TOP + 0.035 + i * 0.002, hz);
  wave.scale.set(0.1, 0.1, 1);
  scene.add(wave);
  return wave;
});

/* ---------------- 도시 글로우 + 빌딩 ---------------- */
const boxGeo = new THREE.BoxGeometry(1, 1, 1);
boxGeo.translate(0, 0.5, 0);                    // 바닥 기준 스케일
const buildMatBlue  = new THREE.MeshPhongMaterial({
  color: 0x385fae, emissive: 0x203d83, shininess: 42, specular: 0x7097da });
const buildMatAmber = new THREE.MeshPhongMaterial({
  color: 0xb58231, emissive: 0x805516, shininess: 48, specular: 0xffc77b });
const windowMatBlue = new THREE.MeshBasicMaterial({
  color: 0xb7d5ff, transparent: true, opacity: 0.62,
  blending: THREE.AdditiveBlending, depthWrite: false,
  side: THREE.DoubleSide });
const windowMatAmber = new THREE.MeshBasicMaterial({
  color: 0xffd68b, transparent: true, opacity: 0.78,
  blending: THREE.AdditiveBlending, depthWrite: false,
  side: THREE.DoubleSide });
const capMat = new THREE.SpriteMaterial({
  map: glowTex, color: 0xffd28a, transparent: true, opacity: 0,
  blending: THREE.AdditiveBlending, depthWrite: false });

const cityNodes = CITIES.map(([mx, my, year, nBld, size], ci) => {
  const [wx, wz] = W(mx, my);
  const group = new THREE.Group();
  group.position.set(wx, TOP, wz);
  scene.add(group);

  // 도시 글로우 스프라이트 (약하게)
  const glow = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex,
    transparent: true, opacity: 0, blending: THREE.AdditiveBlending,
    depthWrite: false }));
  glow.scale.set(size * 1.5 * LIGHT_BOOST, size * 1.5 * LIGHT_BOOST, 1);
  glow.position.y = 0.05;
  group.add(glow);

  // 빌딩: stores 최종 목표가 커질수록 밀도도 같이 증가
  const builds = [];
  const visualBldCount = Math.max(2, Math.round(nBld * BUILDING_DENSITY));
  const cluster = size * (0.55 + BUILDING_DENSITY * 0.145) * BUILDING_CLUSTER_MUL;
  for (let b = 0; b < visualBldCount; b++) {
    const isHub = ci === 0;
    const m = new THREE.Mesh(boxGeo, isHub ? buildMatAmber : buildMatBlue);
    const w = (0.08 + rng() * 0.10) * BUILDING_FOOTPRINT_MUL;
    const d = (0.08 + rng() * 0.11) * BUILDING_FOOTPRINT_MUL;
    m.scale.set(w, (0.018 + rng() * 0.026) * BUILDING_HEIGHT_MUL, d);
    m.rotation.y = (rng() - 0.5) * 0.45;
    const inset = Math.max(w, d) * 0.68;
    let ox = 0, oz = 0;
    for (let attempt = 0; attempt < 18; attempt++) {
      const candidateX = (rng() - 0.5) * cluster;
      const candidateZ = (rng() - 0.5) * cluster;
      if (pointWithInsetInVietnam(wx + candidateX, wz + candidateZ, inset)) {
        ox = candidateX;
        oz = candidateZ;
        break;
      }
    }
    m.position.set(ox, 0, oz);

    const winMat = isHub ? windowMatAmber : windowMatBlue;
    const windowStrip = new THREE.Mesh(new THREE.PlaneGeometry(0.44, 0.72), winMat);
    windowStrip.position.set(0, 0.58, 0.505);
    windowStrip.scale.set(0.28 + rng() * 0.18, 0.55 + rng() * 0.30, 1);
    m.add(windowStrip);

    const cap = new THREE.Sprite(capMat.clone());
    cap.position.set(0, 1.05, 0);
    const capSize = Math.max(0.65, 1.55 / Math.sqrt(BUILDING_DENSITY / 4));
    cap.scale.set(capSize, capSize, 1);
    m.add(cap);

    group.add(m);
    builds.push({ mesh: m, cap, heightBias: (0.75 + rng() * 0.65 + (isHub ? 0.22 : 0)) * BUILDING_HEIGHT_MUL });
  }

  const halo = new THREE.Mesh(new THREE.PlaneGeometry(2, 2),
    new THREE.MeshBasicMaterial({ map: ringTex, transparent: true, opacity: 0,
      blending: THREE.AdditiveBlending, depthWrite: false }));
  halo.rotation.x = -Math.PI / 2;
  halo.position.y = 0.028;
  halo.scale.set(size * 0.25, size * 0.25, 1);
  group.add(halo);

  return { year, size, glow, builds, halo };
});

/* ---------------- 네트워크 라인 ---------------- */
const linkLines = LINKS.map(([a, b, year]) => {
  const A = CITIES[a], B = CITIES[b];
  const [ax, az] = W(A[0], A[1]), [bx, bz] = W(B[0], B[1]);
  const mid = new THREE.Vector3((ax+bx)/2, TOP + 0.5 +
    Math.hypot(bx-ax, bz-az) * 0.10, (az+bz)/2);   // 살짝 떠오르는 아치
  const curve = new THREE.QuadraticBezierCurve3(
    new THREE.Vector3(ax, TOP + 0.04, az), mid,
    new THREE.Vector3(bx, TOP + 0.04, bz));
  const geo = new THREE.BufferGeometry().setFromPoints(curve.getPoints(32));
  const mat = new THREE.LineBasicMaterial({ color: 0x78b8ff,
    transparent: true, opacity: 0, blending: THREE.AdditiveBlending,
    depthWrite: false });
  const line = new THREE.Line(geo, mat);
  scene.add(line);

  const flow = [];
  for (let i = 0; i < FLOW_DOTS; i++) {
    const pMat = new THREE.SpriteMaterial({ map: glowTex, color: 0xffd28a,
      transparent: true, opacity: 0, blending: THREE.AdditiveBlending,
      depthWrite: false });
    const p = new THREE.Sprite(pMat);
    p.scale.set(0.26, 0.26, 1);
    p.userData.phase = rng();
    scene.add(p);
    flow.push(p);
  }
  const state = { active: 0 };
  return { year, mat, curve, flow, state, speed: 0.09 + rng() * 0.05 };
});

/* ---------------- 약한 트윙클 파티클 ---------------- */
const TWINKLE_N = Math.round(95 * Math.min(3.2, STORE_SCALE));
const tw = new Float32Array(TWINKLE_N * 3);
for (let i = 0; i < TWINKLE_N; i++) {
  // 점등된 지역 위주로 흩뿌림 (전국 범위, 지면 위)
  const c = CITIES[Math.floor(rng() * CITIES.length)];
  const [wx, wz] = W(c[0], c[1]);
  tw[i*3]   = wx + (rng() - 0.5) * 1.6;
  tw[i*3+1] = TOP + 0.15 + rng() * 0.8;
  tw[i*3+2] = wz + (rng() - 0.5) * 1.6;
}
const twGeo = new THREE.BufferGeometry();
twGeo.setAttribute("position", new THREE.BufferAttribute(tw, 3));
const twMat = new THREE.PointsMaterial({ color: 0x9fc4ff, size: 0.05,
  transparent: true, opacity: 0, blending: THREE.AdditiveBlending,
  depthWrite: false });
const twinkles = new THREE.Points(twGeo, twMat);
scene.add(twinkles);

/* ---------------- 카메라: 베트남 전체를 유지하는 상부 줌 ---------------- */
const camState = { distMul: INITIAL_DIST_MUL, targetZ: 0.0, azim: -0.012, el: 1.50, orbit: 0 };
let baseDist = 22;
function frameCamera() {
  const aspect = root.clientWidth / Math.max(root.clientHeight, 1);
  camera.aspect = aspect;
  const halfH = 8.6, halfW = 4.2;                  // 지도 + 여백
  const t = Math.tan(THREE.MathUtils.degToRad(45 / 2));
  baseDist = Math.max(halfH / t, halfW / (t * aspect)) * 1.08 * MAP_CAMERA_FILL;
  camera.updateProjectionMatrix();
}
function updateCamera(t) {
  const el = camState.el;                           // 내려다보는 각 (다이브하며 완만해짐)
  const d = baseDist * camState.distMul;
  const drift = Math.max(0, 1 - camState.distMul) * 0.12;
  const close = THREE.MathUtils.clamp((0.12 - camState.distMul) / 0.087, 0, 1);
  const targetY = TOP + close * 1.35;
  const closeLift = close * 3.7;
  const az = camState.azim + Math.sin(t * 0.33) * 0.015 + camState.orbit;
  const tz = camState.targetZ + Math.sin(t * 0.18) * drift;
  const tx = Math.cos(t * 0.21) * drift * 0.45;
  camera.position.set(
    tx + Math.sin(az) * Math.cos(el) * d,
    targetY + Math.sin(el) * d + Math.sin(t * 0.43) * drift + closeLift,
    tz + Math.cos(el) * Math.cos(az) * d);
  camera.lookAt(tx, targetY + Math.sin(t * 0.27) * 0.03, tz);
  camera.rotation.z += Math.sin(t * 0.3) * 0.008 * Math.min(1, drift * 8);
}

/* ---------------- DOM ---------------- */
const $ = s => root.querySelector(s);
const finale = $("#finale");

/* ---------------- GSAP 타임라인 ---------------- */
const Y = CONFIG.YEAR_S, N = CONFIG.years.length;
const veil = $(".veil-loop");
const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

const tl = gsap.timeline({ repeat: reduced ? 0 : -1, paused: true,
  onRepeat: () => { gsap.set(veil, { opacity: 1 });
                    linkLines.forEach(l => {
                      l.state.active = 0;
                      l.flow.forEach(p => { p.material.opacity = 0; });
                    });
                    waves.forEach(w => { w.material.opacity = 0; });
                    gsap.to(veil, { opacity: 0, duration: 0.9, delay: 0.05 }); } });

CONFIG.years.forEach((_, i) => {
  const t = i * Y;
  // 호치민 중심 글로우 ~2배 확장
  tl.to(spread.scale, { x: CONFIG.glowRadii[i], y: CONFIG.glowRadii[i],
    duration: Y * 1.1, ease: "power1.inOut" }, t);
  if (i === 0) tl.to(spread.material, { opacity: 0.30 * LIGHT_BOOST, duration: Y }, t);

  const wave = waves[i % waves.length];
  tl.set(wave.scale, { x: 0.4, y: 0.4 }, t + 0.05);
  tl.set(wave.material, { opacity: 0.38 }, t + 0.05);
  tl.to(wave.scale, { x: CONFIG.glowRadii[i] * 1.05, y: CONFIG.glowRadii[i] * 1.05,
    duration: Y * 0.92, ease: "power2.out" }, t + 0.05);
  tl.to(wave.material, { opacity: 0, duration: Y * 0.75,
    ease: "power1.in" }, t + Y * 0.25);

  // 카메라: 시작은 베트남 전체, 끝은 전체 윤곽을 최대한 유지하는 상부 줌
  const k = (i + 1) / N;
  tl.to(camState, {
    distMul: INITIAL_DIST_MUL - (INITIAL_DIST_MUL - FINAL_DIST_MUL) * k,
    targetZ: 0.0 + 0.12 * k,
    el:      1.50 - 0.028 * k,
    azim:    -0.012 + 0.016 * k,
    orbit:    Math.sin(k * Math.PI) * 0.004,
    duration: Y, ease: "power1.inOut" }, t);
});

// 도시 점등 + 빌딩 성장 (점등 이후 매년 계속 자람)
cityNodes.forEach(c => {
  const t0 = c.year * Y + 0.2;
  tl.to(c.glow.material, { opacity: Math.min(0.92, 0.7 * LIGHT_BOOST), duration: 0.8 }, t0);
  tl.set(c.halo.scale, { x: c.size * 0.35, y: c.size * 0.35 }, t0);
  tl.to(c.halo.material, { opacity: Math.min(0.55, 0.34 * LIGHT_BOOST), duration: 0.18 }, t0);
  tl.to(c.halo.scale, { x: c.size * 2.2 * LIGHT_BOOST, y: c.size * 2.2 * LIGHT_BOOST,
    duration: 1.05, ease: "power2.out" }, t0);
  tl.to(c.halo.material, { opacity: 0, duration: 0.8,
    ease: "power1.in" }, t0 + 0.25);
  c.builds.forEach(b => {
    for (let y = c.year; y < N; y++) {
      const storeBoost = 0.82 + Math.sqrt(CONFIG.stores[y] / BASE_FINAL_STORES) * 0.28;
      const grown = (0.34 + (y - c.year + 1) * 0.36 * c.size * b.heightBias) * storeBoost;
      tl.to(b.mesh.scale, { y: grown, duration: Y * 0.9, ease: "power1.inOut" },
        y * Y + 0.25);
      tl.to(b.cap.material, { opacity: Math.min(0.42, 0.18 + grown * 0.08),
        duration: Y * 0.5 }, y * Y + 0.38);
    }
  });
});

// 네트워크 라인 (은은하게)
linkLines.forEach(l => {
  tl.to(l.mat, { opacity: Math.min(0.82, 0.62 * LIGHT_BOOST), duration: 1.0 }, l.year * Y + 0.5);
  tl.to(l.state, { active: 1, duration: 0.8, ease: "power1.out" },
    l.year * Y + 0.55);
});

// 트윙클: 2027부터 아주 약하게
tl.to(twMat, { opacity: Math.min(0.68, 0.45 * LIGHT_BOOST), duration: 2 }, Y);

// 피날레 문구: 지도 위 2초 겹침 (페이드인 0.4 + 유지 1.2 + 페이드아웃 0.4)
const F = N * Y + 0.6;
tl.to(finale, { opacity: 1, duration: 0.4, ease: "power1.out" }, F);
tl.to(finale, { opacity: 0, duration: 0.4, ease: "power1.in"  }, F + 1.6);

// 완성 후 정지 + 페이드아웃 (onRepeat에서 페이드인)
tl.to({}, { duration: CONFIG.HOLD_S }, N * Y);
tl.to(veil, { opacity: 1, duration: 0.7 }, N * Y + CONFIG.HOLD_S - 0.7);

/* ---------------- 렌더 루프 + FPS 자동 강등 ---------------- */
const fpsEl = $(".fps");
if (new URLSearchParams(location.search).get("debug")) root.classList.add("debug");

let frames = 0, fpsT0 = performance.now(), degraded = 0, lowFpsHits = 0;
const qualityT0 = performance.now();
function autoQuality(fps) {
  if (performance.now() - qualityT0 < 4500) return; // 초기 컴파일/텍스처 업로드 구간 제외
  if (fps >= CONFIG.FPS_CAP - 5) {
    lowFpsHits = 0;
    return;
  }
  lowFpsHits++;
  if (lowFpsHits < 2 || degraded >= 2) return;
  lowFpsHits = 0;
  degraded++;
  if (degraded === 1) {                       // 1단계: 해상도 강등
    DPR = DPR > 1.25 ? 1.25 : 1; renderer.setPixelRatio(DPR);
    renderer.setSize(root.clientWidth, root.clientHeight, false);
  } else {                                    // 2단계: 트윙클 제거 + DPR 1
    DPR = 1; renderer.setPixelRatio(DPR);
    renderer.setSize(root.clientWidth, root.clientHeight, false);
    scene.remove(twinkles);
  }
  if (fpsEl) fpsEl.dataset.q = "Q-" + degraded;
}

const clock = new THREE.Clock();
const FRAME_MS = 1000 / CONFIG.FPS_CAP;
let lastFrame = 0;
function render(now) {
  requestAnimationFrame(render);
  if (now - lastFrame < FRAME_MS) return;     // 24fps 캡
  lastFrame = now;
  const t = clock.getElapsedTime();
  const expectedW = Math.round(root.clientWidth * DPR);
  const expectedH = Math.round(root.clientHeight * DPR);
  if (renderer.domElement.width !== expectedW || renderer.domElement.height !== expectedH) {
    renderer.setSize(root.clientWidth, root.clientHeight, false);
  }
  // 트윙클: 사인 기반 아주 약한 깜빡임
  twMat.size = 0.045 + Math.sin(t * 2.1) * 0.012;
  cityKey.intensity = (1.1 + Math.sin(t * 1.15) * 0.18) * LIGHT_BOOST;
  coastHalo.material.opacity = 0.13 + Math.sin(t * 0.8) * 0.045;
  linkLines.forEach(l => {
    if (l.state.active <= 0.01) {
      l.flow.forEach(p => { p.material.opacity = 0; });
      return;
    }
    l.flow.forEach((p, i) => {
      const u = (p.userData.phase + t * l.speed + i / FLOW_DOTS) % 1;
      p.position.copy(l.curve.getPointAt(u));
      p.material.opacity = l.state.active *
        Math.min(0.95, (0.26 + Math.sin(u * Math.PI) * 0.62) * LIGHT_BOOST);
      const s = 0.2 + Math.sin(u * Math.PI) * 0.18;
      p.scale.set(s, s, 1);
    });
  });
  updateCamera(t);
  renderer.render(scene, camera);

  frames++;
  const nowMs = performance.now();
  if (nowMs - fpsT0 >= 2000) {
    const fps = frames / ((nowMs - fpsT0) / 1000);
    if (fpsEl) fpsEl.textContent =
      `${fps.toFixed(0)} FPS · DPR ${DPR} ${fpsEl.dataset.q || ""}`;
    autoQuality(fps);
    frames = 0; fpsT0 = nowMs;
  }
}

function resize() {
  renderer.setSize(root.clientWidth, root.clientHeight);
  frameCamera();
}
window.addEventListener("resize", resize);
resize();

if (reduced) { tl.progress(1).pause();
  gsap.set(veil, { opacity: 0 }); gsap.set(finale, { opacity: 1 });
  updateCamera(0); renderer.render(scene, camera); }
else { tl.play(0); requestAnimationFrame(render); }

})();
