import streamlit as st

st.set_page_config(page_title="DS & ML Boot Camp", layout="wide", page_icon="🚀")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=IBM+Plex+Sans+Thai:wght@300;400;500;600&display=swap');

/* ─── Reset & Base ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0f;
    color: #e8e8f0;
    font-family: 'IBM Plex Sans Thai', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 20% 10%, rgba(99,102,241,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(16,185,129,0.12) 0%, transparent 55%),
        #0a0a0f;
}

/* Hide default Streamlit chrome */
#MainMenu, header, footer, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
.block-container { padding: 2rem 3rem 4rem !important; max-width: 1100px !important; }

/* ─── Hero ─── */
.hero-wrap {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
    padding: 3.5rem 0 1rem;
}
.hero-eyebrow {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #6ee7b7;
    background: rgba(16,185,129,0.12);
    border: 1px solid rgba(16,185,129,0.3);
    padding: 0.3rem 0.9rem;
    border-radius: 100px;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.6rem, 6vw, 4.2rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    color: #f0f0fa;
}
.hero-title span {
    background: linear-gradient(135deg, #6366f1 0%, #06b6d4 50%, #10b981 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1.05rem;
    font-weight: 300;
    color: #9494b8;
    margin-top: 0.25rem;
    max-width: 560px;
    line-height: 1.7;
}
.badge-row {
    display: flex;
    gap: 0.75rem;
    margin-top: 0.5rem;
    flex-wrap: wrap;
}
.badge {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.3rem 0.85rem;
    border-radius: 6px;
    border: 1px solid;
}
.badge-indigo { color: #a5b4fc; border-color: rgba(99,102,241,0.4); background: rgba(99,102,241,0.08); }
.badge-cyan   { color: #67e8f9; border-color: rgba(6,182,212,0.4);  background: rgba(6,182,212,0.08); }
.badge-green  { color: #6ee7b7; border-color: rgba(16,185,129,0.4); background: rgba(16,185,129,0.08); }

/* ─── Divider ─── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.4), rgba(6,182,212,0.4), transparent);
    margin: 2rem 0;
}

/* ─── Section header ─── */
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #6366f1;
    margin-bottom: 1rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #e8e8f0;
    margin-bottom: 1.5rem;
}

/* ─── Cards ─── */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    overflow: hidden;
}
.card {
    background: #0e0e18;
    padding: 1.6rem 1.8rem;
    position: relative;
    transition: background 0.2s;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    opacity: 0;
    transition: opacity 0.2s;
}
.card:hover { background: #12121f; }
.card:hover::before { opacity: 1; }

.card-icon {
    font-size: 1.8rem;
    margin-bottom: 0.8rem;
    display: block;
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #e8e8f0;
    margin-bottom: 0.4rem;
}
.card-desc {
    font-size: 0.82rem;
    color: #7070a0;
    line-height: 1.55;
}
.card-tag {
    display: inline-block;
    font-size: 0.65rem;
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 0.9rem;
    padding: 0.2rem 0.65rem;
    border-radius: 4px;
    border: 1px solid;
}

/* ─── Buttons ─── */
.stButton > button {
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.75rem 1.8rem !important;
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
    border: none !important;
    cursor: pointer !important;
    width: 100% !important;
}

/* Primary button (first) */
div[data-testid="column"]:nth-child(1) .stButton > button {
    background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
    color: #fff !important;
    box-shadow: 0 0 20px rgba(99,102,241,0.35) !important;
}
div[data-testid="column"]:nth-child(1) .stButton > button:hover {
    background: linear-gradient(135deg, #7c7ff5, #6366f1) !important;
    box-shadow: 0 0 32px rgba(99,102,241,0.55) !important;
    transform: translateY(-2px) !important;
}

/* Secondary button */
div[data-testid="column"]:nth-child(2) .stButton > button {
    background: rgba(16,185,129,0.1) !important;
    color: #6ee7b7 !important;
    border: 1px solid rgba(16,185,129,0.35) !important;
}
div[data-testid="column"]:nth-child(2) .stButton > button:hover {
    background: rgba(16,185,129,0.18) !important;
    box-shadow: 0 0 24px rgba(16,185,129,0.25) !important;
    transform: translateY(-2px) !important;
}

/* ─── Footer ─── */
.footer {
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255,255,255,0.06);
    font-size: 0.75rem;
    color: #444466;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.footer span { color: #6366f1; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-eyebrow">🚀 STOBPER32 · Intensive Workshop</div>
    <div class="hero-title">Data Science &<br><span>Machine Learning</span></div>
    <div class="hero-sub">
        หลักสูตร Boot Camp แบบเข้มข้น 7 วัน เรียนรู้จากการปฏิบัติจริง
        ครอบคลุมตั้งแต่พื้นฐาน Python ไปจนถึง ML Model ขั้นสูง
    </div>
    <div class="badge-row">
        <div class="badge badge-indigo">7 Days</div>
        <div class="badge badge-cyan">Hands-on</div>
        <div class="badge badge-green">Project-based</div>
    </div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ── Day 1 Cards ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-label">📅 Day 1</div>
<div class="section-title">การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python</div>

<div class="cards-grid">
    <div class="card" style="--accent1:#6366f1;--accent2:#06b6d4;">
        <span class="card-icon">💰</span>
        <div class="card-title">ระบบคำนวณส่วนลดตามยอดซื้อ</div>
        <div class="card-desc">ฝึกใช้ logic เงื่อนไข, ฟังก์ชัน และโครงสร้างข้อมูล
        เพื่อสร้างระบบคำนวณส่วนลดแบบ tier-based</div>
        <div class="card-tag" style="color:#a5b4fc;border-color:rgba(99,102,241,0.35);background:rgba(99,102,241,0.08);">
            Python Logic
        </div>
    </div>
    <div class="card" style="--accent1:#10b981;--accent2:#06b6d4;">
        <span class="card-icon">🧹</span>
        <div class="card-title">ทำความสะอาดข้อมูล</div>
        <div class="card-desc">เรียนรู้เทคนิค Data Cleaning ด้วย pandas
        จัดการ missing values, duplicates และ outliers</div>
        <div class="card-tag" style="color:#6ee7b7;border-color:rgba(16,185,129,0.35);background:rgba(16,185,129,0.08);">
            Pandas · EDA
        </div>
    </div>
</div>

<div class="divider"></div>
""", unsafe_allow_html=True)

# ── Buttons ───────────────────────────────────────────────────────────────────
st.markdown("<div class='section-label'>⚡ เปิดแอปพลิเคชัน</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
        st.switch_page("pages/app1_discount_calc.py")

with col2:
    if st.button("🧹 ทำความสะอาดข้อมูล"):
        st.switch_page("pages/santi.py")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div>Boot Camp · Data Science & Machine Learning · <span>STOBPER32</span></div>
    <div>Day 1 / 7 — Python Fundamentals</div>
</div>
""", unsafe_allow_html=True)
