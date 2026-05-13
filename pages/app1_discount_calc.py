import streamlit as st

# ================= CSS =================
st.markdown("""
<style>

/* พื้นหลัง */
.stApp {
    background-color: #f5f7fb;
}

/* กล่องหลัก */
.main-container {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

/* หัวข้อ */
h1 {
    color: #1e293b;
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

/* input */
div[data-baseweb="input"] input {
    border-radius: 10px;
    border: 1px solid #cbd5e1;
    padding: 10px;
    font-size: 18px;
    color: black;
    background-color: white;
}

/* ปุ่ม */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: none;
    background-color: #2563eb;
    color: white;
    font-size: 16px;
    font-weight: bold;
    padding: 10px;
}

/* hover ปุ่ม */
.stButton > button:hover {
    background-color: #1d4ed8;
}

/* metric */
[data-testid="metric-container"] {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    padding: 15px;
    border-radius: 12px;
}

/* ตัวหนังสือ metric */
[data-testid="metric-container"] label {
    color: #475569 !important;
}

[data-testid="metric-container"] div {
    color: black !important;
}

/* กล่องแจ้งเตือน */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= UI =================

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("💰 ระบบคำนวณส่วนลดร้านค้า")
st.info("คำนวณส่วนลดลูกค้าตามยอดการสั่งซื้อสะสม")

# รับข้อมูล
total_bill = st.number_input(
    "กรุณากรอกยอดซื้อรวม (บาท):",
    min_value=0.0,
    step=100.0
)

# คำนวณ
if total_bill >= 1000:
    discount_rate = 0.15
elif total_bill >= 500:
    discount_rate = 0.10
else:
    discount_rate = 0.00

discount_amount = total_bill * discount_rate
net_price = total_bill - discount_amount

# ปุ่มคำนวณ
if st.button("🧮 คำนวณยอดสุทธิ"):
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ยอดซื้อรวม", f"{total_bill:,.2f} บาท")
        st.write(f"ส่วนลดที่ได้รับ: {discount_rate*100:.0f}%")

    with col2:
        st.metric(
            "ยอดชำระจริง",
            f"{net_price:,.2f} บาท",
            delta=f"-{discount_amount:,.2f} บาท"
        )

    if discount_rate > 0:
        st.success(f"คุณได้รับส่วนลด {discount_amount:,.2f} บาท")
    else:
        st.warning("ยอดซื้อไม่ถึงเกณฑ์รับส่วนลด")

# ปุ่มกลับ
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")

st.markdown('</div>', unsafe_allow_html=True)
