這裡是一份簡單易懂、適合國中生的 Python 筆記整理，幫助你複習今天上課學到的內容：

---

# 🐍 Python 基礎指令筆記（國中版）

## ✅ 比較運算子（判斷兩個東西的關係）

```python
print(1 == 1)  # 是不是相等 → True
print(1 != 1)  # 是不是不相等 → False
print(1 > 1)   # 是不是大於 → False
print(1 < 1)   # 是不是小於 → False
print(1 >= 1)  # 是不是大於等於 → True
print(1 <= 1)  # 是不是小於等於 → True
```

📌 注意：比較運算會回傳 `True`（真）或 `False`（假）

---

## 🔗 邏輯運算子（用來組合判斷）

```python
print(True and True)    # 兩個都是真的 → True
print(True and False)   # 有一個是假的 → False
print(False and False)  # 全部都是假的 → False

print(not True)   # 把 True 變成 False → False
print(not False)  # 把 False 變成 True → True
```

---

## 🧮 運算優先順序（誰先算？）

1. `()` 括號內的最先算
2. `**` 次方
3. `* / // %` 乘、除、整除、取餘數
4. `+ -` 加減
5. `== != > < >= <=` 比較大小
6. `not` 非（邏輯反轉）
7. `and` 並且
8. `or` 或者

---

## 🔐 密碼門（使用 if 判斷）

```python
password = input("請輸入密碼: ")

if password == "1234":
    print("歡迎 danny")
elif password == "5678":
    print("歡迎 dog")
elif password == "0000":
    print("歡迎 admin")
else:
    print("密碼錯誤")
```

📌 重點解釋：

- `if`：如果符合條件，就執行對應內容
- `elif`（else if）：如果前面不符合，才會檢查這裡
- `else`：以上都不符合，就執行這段

✅ 使用 `elif` 可以避免重複判斷，效率比較高喔！

---

## 🌐 使用 Streamlit 製作互動網頁

> Streamlit 是一個讓你快速做出互動網頁的小工具

### 🎮 數字輸入 + 成績判斷

```python
number = st.number_input("請輸入數字", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是: {number}")

if number >= 90:
    st.write("成績達 A")
elif number > 80:
    st.write("成績達 B")
elif number > 70:
    st.write("成績達 C")
elif number > 60:
    st.write("成績達 D")
else:
    st.write("成績達 F")
```

#123
📌 說明：

- `st.number_input`：在網頁上顯示一個可以輸入數字的格子
- `step`：每次加減的單位
- `min_value / max_value`：可以輸入的範圍

---

### 🎉 按鈕互動

```python
if st.button("點我"):
    st.balloons()  # 會噴出氣球動畫

if st.button("按我", key="snow"):
    st.snow()  # 會出現雪花動畫
```

📌 說明：

- `st.button("文字")`：在網頁上顯示一個按鈕
- `key`：讓不同按鈕有不同的名字
- 按鈕被點時會執行後面的動畫程式

---

這就是你今天學到的 Python 重點內容！💪
繼續加油，學會這些之後，你就能做出自己的小遊戲或互動網站了喔！

如果你還有不懂的地方，歡迎再問我 😊
