import streamlit as st

# ================= CSS =================
st.markdown("""
<style>

/* พื้นหลังหลัก */
.stApp {
    background: linear-gradient(to right, #eef2ff, #f8fafc);
}

/* กล่อง input */
div[data-baseweb="input"] input {
    border-radius: 12px;
    border: 2px solid #6366f1;
    padding: 10px;
    font-size: 18px;
}

/* ปุ่ม */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: none;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 12px;
    transition: 0.3s;
}

/* เอฟเฟกต์ตอนเอาเมาส์ชี้ */
.stButton > button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #4338ca, #6d28d9);
}

/* metric card */
[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #e5e7eb;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* หัวข้อ */
h1 {
    color: #312e81;
    text-align: center;
    font-weight: 800;
}

/* กล่อง info */
.stAlert {
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)

# ================= UI =================
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

# แสดงผล
if st.button("🧮 คำนวณยอดสุทธิ"):
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ยอดซื้อรวม", f"{total_bill:,.2f} บาท")
        st.write(f"🎁 ส่วนลดที่ได้รับ ({discount_rate*100:.0f}%)")

    with col2:
        st.metric(
            "ยอดชำระจริง",
            f"{net_price:,.2f} บาท",
            delta=f"-{discount_amount:,.2f}"
        )

    if discount_rate > 0:
        st.success(f"คุณได้รับส่วนลดทั้งหมด {discount_amount:,.2f} บาท 🎉")
    else:
        st.warning("ยอดซื้อไม่ถึงเกณฑ์รับส่วนลด")

# ปุ่มกลับ
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")
