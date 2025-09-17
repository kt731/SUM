import streamlit as st
import pandas as pd
from itertools import combinations

st.set_page_config(page_title="Subset Sum Finder", layout="centered")

st.title("🔢 Tìm tổ hợp số từ file Excel")

# Upload file Excel
uploaded_file = st.file_uploader("📂 Upload file Excel (.xlsx)", type=["xlsx"])

# Nhập số mục tiêu
target = st.number_input("Nhập số mong muốn:", min_value=0, value=14)

def find_combinations(numbers, target):
    results = []
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            if sum(combo) == target:
                results.append(combo)
    return results

if uploaded_file:
    try:
        # Đọc dữ liệu từ Excel
        df = pd.read_excel(uploaded_file)

        st.write("📑 Dữ liệu trong file:")
        st.dataframe(df)

        # Cho phép chọn cột số
        col = st.selectbox("Chọn cột chứa số:", df.columns)

        numbers = df[col].dropna().astype(int).tolist()

        st.write(f"✅ Đã lấy {len(numbers)} số từ cột **{col}**")

        if st.button("🔍 Tìm tổ hợp"):
            results = find_combinations(numbers, target)

            if results:
                st.success(f"✅ Tìm thấy {len(results)} tổ hợp có tổng = {target}:")
                for combo in results:
                    st.write(combo)
            else:
                st.error("❌ Không tìm thấy tổ hợp nào phù hợp.")
    except Exception as e:
        st.error(f"⚠️ Lỗi đọc file: {e}")
else:
    st.info("⬆️ Vui lòng upload file Excel trước.")
