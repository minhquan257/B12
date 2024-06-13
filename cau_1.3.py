import streamlit as st
from PyDictionary import PyDictionary
import random

# Khởi tạo từ điển PyDictionary
dictionary = PyDictionary()

# Danh sách các từ mẫu (bạn có thể mở rộng danh sách này)
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Hàm để tạo từ ngẫu nhiên
def get_random_word():
    return random.choice(words)

# Tiêu đề của ứng dụng
st.title("Random Words Generator")

# Nút để tạo từ ngẫu nhiên
if st.button("Generate"):
    random_word = get_random_word()
    meaning = dictionary.meaning(random_word)
    if meaning:
        meaning_str = ', '.join([f"{key}: {', '.join(values)}" for key, values in meaning.items()])
    else:
        meaning_str = "Meaning not found."
else:
    random_word = "-"
    meaning_str = "-"

# Hiển thị từ và ý nghĩa
st.write("## Random Word")
st.write(f"### {random_word}")
st.write(f"**Meaning:** {meaning_str}")

# Hướng dẫn người dùng
st.write("Click the **Generate** button to generate new word")
