import streamlit as st
import numpy as np
import pandas as pd

st.title('MÔ HÌNH PHÂN LOẠI CẢM XÚC TIẾNG VIỆT')
st.header('Bộ dữ liệu')

data = pd.read_csv('uit-vsfc.csv')
df = pd.DataFrame(data)
st.dataframe(df)



st.header('Mô hình')
st.markdown('Mô hình phân loại đã xây dựng sử dụng kiến trúc base_v2  của [PhoBERT](%s).' %\
            'https://github.com/VinAIResearch/PhoBERT', unsafe_allow_html=True )
st.header('Dự đoán cảm xúc')
st.text_input('Nhập 1 câu tiếng Việt:', '')