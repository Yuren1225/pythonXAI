import streamlit as st
import openai  # pip install openai
from dotenv import load_dotenv
import time

load_dotenv()  # 載入.env檔案內容

# 設定API金鑰
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 初始化對話紀錄
if "history" not in st.session_state:
    st.session_state.history = []

col1, col2, col3 = st.columns(3)
with col1:
    st.write("請用繁體中文進行後續對話")
with col2:
    gpt_names = ["gpt-4o-mini", "gpt-4-0613", "gpt-4-32k", "gpt-4-32k-0613"]
    selected_product = st.selectbox("AI模型", gpt_names)
with col3:
    # st.button("清空記錄", key="button1")
    if st.button("清空記錄", key="button1"):
        st.session_state.history = []

        st.rerun()


# 聊天輸入框
prompt = st.chat_input("請輸入你的問題")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()  # 重新整理

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "請用繁體中文進行後續對話"}]
    + st.session_state.history,
)
assistant_message = response.choices[0].message.content
st.session_state.history.append({"role": "assistant", "content": assistant_message})

# 用迴圈顯示聊天泡泡

for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
