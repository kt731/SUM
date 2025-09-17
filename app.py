import streamlit as st
from itertools import combinations

st.set_page_config(page_title="Subset Sum Finder", layout="centered")

st.title("🔢 Tìm tổ hợp số có tổng bằng số mong muốn")

# Nhập danh sách số
numbers_input = st.text_input(
    "Nhập danh sách số (cách nhau bởi dấu cách):",
    "2 4 6 8 10"
)

# Nhập số mục tiêu
target = st.number_input("Nhập số mong muốn:", min_value=0, value=14)

def find_combinations(numbers, target):
    results = []
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            if sum(combo) == target:
                results.append(combo)
    return results

if st.button("🔍 Tìm tổ hợp"):
    try:
        numbers = list(map(int, numbers_input.split()))
        results = find_combinations(numbers, target)

        if results:
            st.success(f"✅ Tìm thấy {len(results)} tổ hợp có tổng = {target}:")
            for combo in results:
                st.write(combo)
        else:
            st.error("❌ Không tìm thấy tổ hợp nào phù hợp.")
    except ValueError:
        st.error("⚠️ Vui lòng nhập đúng định dạng số (cách nhau bằng dấu cách).")
