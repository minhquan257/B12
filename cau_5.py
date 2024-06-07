import streamlit as st
import numpy as np
import pandas as pd

st.title('My first ...')
st.header('Header ...')
st.text('Đây là text')
st.markdown('Markdown đây **anh em ơi**')
st.write('Còn dưới đây là latex')
st.latex(r'''a + b = 3''')
st.write(12345)
# Sửa lại dấu "" thành '' và ngược lại
st.code("""
        def(hello):
                print('Hello world!')
        """, language='python', line_numbers=True)
st.write('Hiển thị luôn cả chart')

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(data)