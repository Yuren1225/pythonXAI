import streamlit as st

# st.title("數字金字塔")
# number = st.number_input("請輸入一個整數", value=0, step=1)
# for i in range(1, number + 1):
#     st.write(str(i) * i)

st.title("箭頭金字塔")
num = st.number_input(
    "請輸入一個整數",
    value=0,
    step=1,
)
s = ""
for i in range(1, num + 1):
    space = " " * (num - i)
    star = "*" * (2 * i - 1)
    s = s + space + star + "\n"

for i in range(num):

    s = s + " " * (num - 1) + "*" + "\n"
st.write(f"```\n{s}```")
