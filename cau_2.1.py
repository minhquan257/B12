import streamlit as st

# Tiêu đề của ứng dụng
st.title("Website tính toán")

# Nhập hai số thực
num1 = st.number_input("Số đầu tiên", format="%f")
num2 = st.number_input("Số thứ hai", format="%f")

# Tính toán
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Vô cùng"

# Hiển thị kết quả
st.write("### Results")
st.write(f"**Tổng:** {sum_result}")
st.write(f"**Hiệu:** {difference_result}")
st.write(f"**Tích:** {product_result}")
st.write(f"**Thương:** {quotient_result}")


