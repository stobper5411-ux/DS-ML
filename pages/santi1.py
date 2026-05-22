import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore') # ตั้งค่าให้ละเว้นคำเตือนที่อาจเกิดขึ้น

def clean_redbull_data_beautiful(data_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Performs a comprehensive data cleaning process on the Red Bull sales dataset,
    including handling duplicates, inconsistent values, missing data, and noisy data.

    Args:
        data_raw (pd.DataFrame): The raw DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame with standardized and validated data.
    """
    df = data_raw.copy()
    print(f"\n--- เริ่มต้นทำความสะอาดข้อมูล (Initial Rows: {len(df):,}) ---")

    # --- STEP 1: Duplicate Data — ข้อมูลซ้ำ ---
    initial_rows_dup = len(df)
    df = df.drop_duplicates()
    if len(df) < initial_rows_dup:
        print(f"✅ จัดการข้อมูลซ้ำ: ลบไป {initial_rows_dup - len(df):,} แถว (เหลือ {len(df):,} แถว)")
    else:
        print("ℹ️ ไม่พบ Exact Duplicate ในข้อมูลนี้")

    # --- STEP 2: Inconsistent Data — ข้อมูลที่ไม่สอดคล้องกัน ---
    # 2.1 Standardize 'Region' Column
    df['Region'] = df['Region'].str.strip().str.lower() # แปลงเป็นตัวพิมพ์เล็กและลบช่องว่างส่วนเกิน
    region_mapping = {
        'th-central': 'TH-Central', 'th central': 'TH-Central',
        'thailand central': 'TH-Central', 'thailand-central': 'TH-Central',
        'thailand': 'TH-Central',
        'usa-east': 'USA-East', 'us east': 'USA-East',
        'united states east': 'USA-East', 'u.s.a.': 'USA-East',
        'europe-eu': 'Europe-EU', 'eu': 'Europe-EU',
        'europe': 'Europe-EU', 'european union': 'Europe-EU',
        'asia-pacific': 'Asia-Pacific', 'asia-pac': 'Asia-Pacific',
        'apac': 'Asia-Pacific', 'asia pacific': 'Asia-Pacific'
    }
    df['Region'] = df['Region'].replace(region_mapping) # แทนที่ค่าตาม mapping ที่กำหนด
    df['Region'] = df['Region'].str.upper() # แปลงให้เป็นตัวพิมพ์ใหญ่ทั้งหมดเพื่อความสอดคล้อง

    # 2.2 Standardize 'Product_Variant' Column
    df['Product_Variant'] = df['Product_Variant'].str.strip().str.lower() # แปลงเป็นตัวพิมพ์เล็กและลบช่องว่างส่วนเกิน
    product_variant_mapping = {
        'original blue': 'Original Blue', 'original  blue': 'Original Blue',
        'krating daeng 250': 'Krating Daeng 250',
        'red edition': 'Red Edition',
        'sugarfree': 'Sugarfree', 'sugar free': 'Sugarfree',
        'sugarfree ': 'Sugarfree', 'sugar-free': 'Sugarfree',
        'tropical edition': 'Tropical Edition', 'tropical  edition': 'Tropical Edition',
        'tropical': 'Tropical Edition',
    }
    df['Product_Variant'] = df['Product_Variant'].replace(product_variant_mapping) # แทนที่ค่าตาม mapping ที่กำหนด

    # 2.3 Standardize 'Channel' Column
    df['Channel'] = df['Channel'].str.strip().str.lower() # แปลงเป็นตัวพิมพ์เล็กและลบช่องว่างส่วนเกิน
    channel_mapping = {
        'social media': 'Social Media', 'social_media': 'Social Media',
        'tv ad': 'TV Ad', 'tv ads': 'TV Ad',
        'tv advertisement': 'TV Ad', 'television ad': 'TV Ad',
        'in-store promo': 'In-store Promo',
        'f1 sponsorship': 'F1 Sponsorship',
        'extreme sports': 'Extreme Sports'
    }
    df['Channel'] = df['Channel'].replace(channel_mapping) # แทนที่ค่าตาม mapping ที่กำหนด
    # แปลงตัวอักษรแรกเป็นพิมพ์ใหญ่สำหรับคำอื่นๆ ที่อาจไม่ได้อยู่ใน mapping
    df['Channel'] = df['Channel'].apply(lambda x: x.title() if isinstance(x, str) else x)

    # 2.4 Convert 'Date' Column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='mixed') # แปลงสตริงวันที่เป็นวัตถุ datetime
    print("✅ จัดการ Inconsistent Data และแปลง 'Date' เป็น datetime แล้ว")

    # --- STEP 3: Missing Data — ข้อมูลที่หายไป ---
    missing_before = df.isnull().sum().sum()
    if missing_before > 0:
        # เติมค่าว่างใน 'Marketing_Spend' ด้วยค่ามัธยฐาน (median) เนื่องจากอาจมี outlier
        median_marketing = df['Marketing_Spend'].median()
        df['Marketing_Spend'] = df['Marketing_Spend'].fillna(median_marketing)

        # เติมค่าว่างใน 'Customer_Score' ด้วยค่ามัธยฐาน (median) เนื่องจากเป็นคะแนน
        median_score = df['Customer_Score'].median()
        df['Customer_Score'] = df['Customer_Score'].fillna(median_score)
        print(f"✅ จัดการ Missing Data: เติม {missing_before:,} ค่าด้วย Median")
    else:
        print("ℹ️ ไม่พบ Missing Data ในข้อมูลนี้")

    # --- STEP 4: Noisy Data — ข้อมูลผิดพลาด (ตาม Business Logic) ---
    initial_rows_noisy = len(df)
    # กรองข้อมูลตามกฎทางธุรกิจ (Business Logic):
    # - 'Unit_Price' ต้องมากกว่า 0
    # - 'Units_Sold' ต้องมากกว่า 0
    # - 'Marketing_Spend' ต้องไม่ติดลบ (มากกว่าหรือเท่ากับ 0)
    # - 'Customer_Score' ต้องอยู่ระหว่าง 1 ถึง 10
    df = df[df['Unit_Price'] > 0]
    df = df[df['Units_Sold'] > 0]
    df = df[df['Marketing_Spend'] >= 0]
    df = df[(df['Customer_Score'] >= 1) & (df['Customer_Score'] <= 10)]

    if len(df) < initial_rows_noisy:
        print(f"✅ จัดการ Noisy Data: ลบไป {initial_rows_noisy - len(df):,} แถว (เหลือ {len(df):,} แถว)")
    else:
        print("ℹ️ ไม่พบ Noisy Data ที่ขัดแย้งกับ Business Logic")

    # --- STEP 5: Outlier Detection (และหมายเหตุการจัดการ) ---
    # ใน Workshop นี้ เราจะเพียงแค่ตรวจจับ Outliers แต่จะไม่ทำการปรับค่าด้วย Winsorize หรือวิธีอื่น ๆ
    # เนื่องจากต้องพิจารณาบริบททางธุรกิจอย่างรอบคอบว่า Outlier เป็นข้อมูลผิดพลาดหรือข้อมูลจริงที่มีความสำคัญ
    print("ℹ️ ตรวจสอบ Outliers (ไม่มีการปรับค่าตามบริบท Business Logic ของ Workshop)")

    print(f"--- ทำความสะอาดข้อมูลเสร็จสิ้น (Final Rows: {len(df):,}) ---")
    return df

# --- สาธิตการใช้งานฟังก์ชัน --- 
# โหลดข้อมูลดิบ (สมมติว่า df_raw ถูกโหลดมาแล้วจากการอัปโหลดไฟล์)
# cleaned_df_santi1 = clean_redbull_data_beautiful(df_raw)

# print("\n--- สรุปผลการทำความสะอาดโดย Santi1.py ---")
# print(f"ขนาดข้อมูลก่อนทำความสะอาด: {df_raw.shape[0]:,} แถว, {df_raw.shape[1]} คอลัมน์")
# print(f"ขนาดข้อมูลหลังทำความสะอาด: {cleaned_df_santi1.shape[0]:,} แถว, {cleaned_df_santi1.shape[1]} คอลัมน์")

# print("\n### ข้อมูลที่ทำความสะอาดแล้ว (5 แถวแรกจาก Santi1.py):")
# display(cleaned_df_santi1.head())
