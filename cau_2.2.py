import streamlit as st
import time
import webbrowser as wb


st.title('Đăng nhập')
username = st.text_input('Username', '')
password = st.text_input('Password', '', type='password')

if st.button('Đăng nhập'):
    if username == '20520710' and password == '2002':
        st.write('Đăng nhập thành công')
        time.sleep(3)
        st.balloons()
        st.success('Chào mừng bạn quay lại!')
        time.sleep(2)
        wb.open('https://www.uit.edu.vn/')
    else:
        st.error('Sai tên đăng nhập hoặc mật khẩu')