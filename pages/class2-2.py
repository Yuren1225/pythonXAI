import streamlit as st

number = st.number_input("請輸入數字", step=1, min_value=0, max_value=100)
# step=10表示每次增加或減少10，min_vaule表示最小值，max_vaule表示最大值
st.write(f"你輸入的數字是: {number}")
if number >= 90:  # 成績達A
    st.write("成績達A")
elif number > 80:  # 成績達B
    st.write("成績達B")
elif number > 70:  # 成績達C
    st.write("成績達C")
elif number > 60:  # 成績達D
    st.write("成績達D")
else:  # 成績達F
    st.write("成績達F")

if st.button("點我"):
    st.balloons()  # 點擊按鈕後會顯示氣球動畫
if st.button("按我", key="snow"):
    st.snow()  # 點擊按鈕後會顯示雪花動畫
# st.button()可以在網頁上顯示一個按鈕，使用者可以點擊按鈕
# key式按鈕的識別名稱，可以用來區分不同按鈕
# 如果使用者點擊按鈕，st:button()會回傳true，否則回傳false
