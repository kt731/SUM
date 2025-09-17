import streamlit as st
import pandas as pd

st.set_page_config(page_title="Subset Sum Finder", layout="centered")

st.title("⚡ Tìm nhanh 1 tổ hợp số có tổng = số mong muốn")

# Upload file Excel
uploaded_file = st.file_uploader("📂 Upload file Excel (.xlsx)", type=["xlsx"])

# Nhập số mục tiêu
target = st.number_input("Nhập số mong muốn:", min_value=0, value=14)

def subset_sum(numbers, target):
    dp = {0: []}  # tổng 0 thì có tổ hợp rỗng
    for num in numbers:
        new_dp = dp.copy()
        for s, comb in dp.items():
            new_sum = s + num
            if new_sum <= target and new_sum not in new_dp:
                new_dp[new_sum] = comb + [num]
                if new_sum == target:
                    return new_dp[new_sum]  # ✅ dừng ngay khi tìm thấy
        dp = new_dp
    return None

if uploaded_file:
    try:
        # Đọc dữ liệu từ Excel
        df = pd.read_excel(uploaded_file)

        st.write("📑 Dữ liệu trong file:")
        st.dataframe(df)

        # Chọn cột chứa số
        col = st.selectbox("Chọn cột chứa số:", df.columns)

        numbers = df[col].dropna().astype(int).tolist()

        st.write(f"✅ Đã lấy {len(numbers)} số từ cột **{col}**")

        if st.button("🔍 Tìm tổ hợp nhanh"):
            result = subset_sum(numbers, target)

            if result:
                st.success(f"✅ Tìm thấy 1 tổ hợp có tổng = {target}: {result}")
            else:
                st.error("❌ Không tìm thấy tổ hợp nào phù hợp.")
    except Exception as e:
        st.error(f"⚠️ Lỗi đọc file: {e}")
else:
    st.info("⬆️ Vui lòng upload file Excel trước.")
