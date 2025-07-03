# # # call by value
# # a = 1
# # b = a  # 複製a的值給b
# # b = 2
# # print(a, b)

# # # call by reference
# # a = [1, 2, 3]
# # b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
# # b[0] = 2
# # print(a, b)

# # # list的append
# # L = [1, 2, 3]
# # L.append(4)  # 把4加到L的最後面
# # print()
# # # list的移除元素有兩種
# # # 1.使用remove可以移除指定的元素
# # L = ["a", "b", "c", "d", "e"]
# # L.remove("a")  # 移除第一個a
# # # 代表remove會從頭開始找到苻和的元素就會移除
# # # 如果想要移除所有符合的，可以使用迴圈
# # for i in L:
# #     if i == a:
# #         L.remove(i)
# # # 2.使用pop，可以移除指定的index元素
# # L = ["a", "b", "c", "d", "a"]
# # L.pop(0)  # 移除index 0的元素
# # # 代表pop會移除指定的index的元素
# # # #如果不指定index，則會移除最後一個元素
# # L.pop()  # 移除最後一個元素
# # print(L)


# # import streamlit as st

# # st.title("欄位元件")
# # col1, col2 = st.columns(2)  # 2columns
# # col1.button("按鈕1", key="btn1")  # 在col1中建立一個類似St.button("按鈕1")
# # col2.button("按鈕2", key="btn2")  # 在col2中建立一個類似St.button("按鈕2")

# # # 2columns可以用比例來設定每個column的寬度,將比例放到list中
# # col1, col2 = st.columns([1, 2])
# # col1.button("按鈕1", key="btn3")  # 在col1中建立一個類似St.button("按鈕1")
# # col2.button("按鈕2", key="btn4")  # 在col2中建立一個類似St.button("按鈕2")

# # # 3columns
# # col1, col2, col3 = st.columns([1, 2, 3])
# # col1.button("按鈕1", key="btn5")  # 在col1中建立一個類似St.button("按鈕1")
# # col2.button("按鈕2", key="btn6")  # 在col2中建立一個類似St.button("按鈕2")
# # col3.button("按鈕3", key="btn7")  # 在col3中建立一個類似St.button("按鈕3")

import streamlit as st

# col1, col2 = st.columns([1, 2])
# with col1:  # 在col1中使用with語句放更多東西
#     if st.button("按鈕1", key="btn8"):  # 在col1中建立一個按鈕
#         st.balloons()  # 在col1中建立一個氣球
#     st.write("這是col1")  # 在col1中建立一個文字
# with col2:  # 在col中使用with語句放更多東西
#     st.button("按鈕2", key="btn9")  # 在col1中建立一個按鈕
#     st.write("這是col2")  # 在col2中建立一個文字

# # 多個columns可以使用for迴圈來建立
# cols = st.columns(4)  # 4columns, cols[0]...cols[3]
# for i in range(len(cols)):
#     with cols[i]:
#         st.button(f"按鈕{i+1}", key=f"btn{i+10}")  # 在cols[i]中建立一個按鈕類似
#     # st.balloons()  # 在cols[i]中建立一個氣球

# st.write("---")
# st.title("columns排列元件效果比較")
# # 2columns
# col1, col2 = st.columns(2)
# with col1:
#     st.button("按鈕1", key="1")
#     st.button("按鈕2", key="2")
#     st.button("按鈕3", key="3")
# with col2:
#     st.write("這是col2")
#     st.write("這是col2")
#     st.write("這是col2")

# st.write("---")

# for i in range(3):
#     col1, col2 = st.columns(2)
#     with col1:
#         st.button(f"按鈕{i+1}", key=f"{i+4}")
#     with col2:
#         st.write(f"這是col2_{i+1}")

# st.write("---")
# st.title("文字輸入元件")
# # st.text_input指令格式st.text_input(輸入欄位的標題,value="顯示預設文字")
# text = st.text_input("請輸入文字", value="顯示預設文字")
# st.write(f"你輸入的文字是: {text}")

st.write("---")
st.title("session_state")

if "ans1" not in st.session_state:  # 如果沒有answer這個變數
    st.session_state.ans1 = 1  # 將answer變數的值設為1
if st.button("按下去ans+1", key="ans2"):  # 如果按下了按鈕
    st.session_state.ans1 = st.session_state.ans1 + 1  # 將answer變數的值加1
st.write(f"answer = {st.session_state.ans1}")  # 印出answer變數的值
