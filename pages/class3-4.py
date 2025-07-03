import random  # 匯入random模組

# # random.randrange()  # 設定抽籤範圍的方式跟range()一樣
# print(random.randrange(7))  # 0~6
# print(random.randrange(1, 6))  # 1~6
# print(random.randrange(1, 6, 2))  # 1~6, 間隔2

# # random.randint()  # 設定抽籤範圍的方式一定要設定開始與結束且結束的數字會包含在內
# print(random.randint(1, 6))  # 1~6
import streamlit as st

st.title("猜數字遊戲")
ans = random.randint(1, 100)
while True:
    guess = int(st.number_input("請輸入 1 到 100 之間的數字: ", value=0))
    if guess < 1 or guess > 100:
        st.write("請輸入 1 到 100 之間的數字。")
        continue
    if guess < ans:
        st.write("再大一點")
        continue
    if guess > ans:
        st.write("再小一點")
        continue
    if guess == ans:
        st.write("猜中了")
        break
