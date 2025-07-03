import streamlit as st
import time


if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

st.title("點餐機")

if "order" not in st.session_state:
    st.session_state.order = []  # 如果沒有order，就建立一個空的list
# st.text_input指令格式st.text_input(輸入欄位的標題,value="顯示預設文字")
text = st.text_input("請輸入餐點")
if st.button("加入", key="1"):
    st.session_state.order.append(text)

st.title("購物籃")
for i in range(len(st.session_state.order)):  # 做一個輪迴
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.order[i])
    with col2:
        if st.button("刪除", key=f"2{i}"):  # 刪除建
            st.session_state.order.pop(i)  # 把東西丟出
            st.rerun()  # 重新整理
