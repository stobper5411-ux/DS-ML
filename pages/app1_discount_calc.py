import streamlit as st

# ================= PAGE =================
st.set_page_config(
    page_title="ระบบคำนวณส่วนลด",
    page_icon="💰",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>

/* พื้นหลัง */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* ซ่อนเมนู */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* กล่องหลัก */
.main-box {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    margin-top: 30px;
}

/* หัวข้อ */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
}

/* subtitle */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
    font-size: 18px;
}

/* input */
div[data-baseweb="input"] input {
    background-color: rgba(255,255,255,0.12);
    color: white;
    border: 2px solid rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 14px;
    font-size: 22px;
    font-weight: bold;
}

/* label */
label {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold;
}

/* ปุ่ม */
.stButton > button {
    width: 100%;
    border-radius: 15px;
    border: none;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 14px;
    transition: 0.3s;
}

/* hover */
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(59,130,246,0.4);
}

/* metric */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
}

/* metric text */
[data-testid="metric-container"] label {
    color: #cbd5e1 !important;
}

[data-testid="metric-container"] div {
    color: white !important;
}

/* success box */
.stSuccess {
    border-radius: 15px;
}

/* warning */
.stWarning {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ================= UI =================
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown('<div class="title">💰 ระบบคำนวณส่วนลด</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">คำนวณยอดสุทธิและส่วนลดลูกค้าอัตโนมัติ</div>',
    unsafe_allow_html=True
)

# input
total_bill = st.number_input(
    "กรอกยอดซื้อรวม (บาท)",
    min_value=0.0,
    step=100.0
)

# logic
if total_bill >= 1000:
    discount_rate = 0.15
elif total_bill >= 500:
    discount_rate = 0.10
else:
    discount_rate = 0.00

discount_amount = total_bill * discount_rate
net_price = total_bill - discount_amount

# button
if st.button("🧮 คำนวณยอดสุทธิ"):
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "ยอดซื้อรวม",
            f"{total_bill:,.2f} ฿"
        )

    with col2:
        st.metric(
            "ยอดชำระจริง",
            f"{net_price:,.2f} ฿",
            delta=f"-{discount_amount:,.2f}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if discount_rate > 0:
        st.success(
            f"🎉 ได้รับส่วนลด {discount_rate*100:.0f}% "
            f"คิดเป็นเงิน {discount_amount:,.2f} บาท"
        )
    else:
        st.warning("⚠️ ยอดซื้อยังไม่ถึงเกณฑ์รับส่วนลด")

st.markdown("<br>", unsafe_allow_html=True)

# home button
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")

st.markdown('</div>', unsafe_allow_html=True)
