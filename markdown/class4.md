這是一份針對國中程度整理的 Python 筆記，會用簡單的語言來說明每個功能與用法。你可以當作學習紀錄，也可以複習用喔！

---

# 🐍 Python 初學筆記（國中版）

---

## 📂 檔案讀取與關閉

### 方法一：手動開檔與關檔

```python
f = open("pages/test.txt", "r")  # 開啟檔案（r代表讀取模式）
content = f.read()              # 讀取檔案內容
f.close()                       # 關閉檔案
print(content)                  # 顯示內容
```

### 方法二：用 `with` 自動幫你關好檔案

```python
with open("pages/test.txt", "r") as f:
    content = f.read()
print(content)
```

🔹 用 `with` 的好處是檔案會自動關起來，不會忘記！

---

## 🔁 call by value vs call by reference

### 🔹 call by value（值複製）

```python
a = 1
b = a
b = 2
print(a, b)  # ➜ a還是1，b變成2
```

### 🔹 call by reference（記憶體共用）

```python
a = [1, 2, 3]
b = a
b[0] = 9
print(a, b)  # ➜ a和b都變了
```

📝 小結：

- 數字等基本資料型態會複製一份（value）
- 清單 list 會共用記憶體位置（reference）

---

## 📋 list（清單）的基本操作

### 加東西：`append()`

```python
L = [1, 2, 3]
L.append(4)
print(L)  # ➜ [1, 2, 3, 4]
```

### 移除元素的方法

1️⃣ 用 `remove()` 移除指定內容（只會移掉第一個）

```python
L = ["a", "b", "a"]
L.remove("a")
print(L)  # ➜ ["b", "a"]
```

2️⃣ 用 `pop()` 移除某個位置的元素

```python
L = ["a", "b", "c"]
L.pop(1)      # 移除 index=1 的元素 "b"
L.pop()       # 不寫 index 的話，移除最後一個
print(L)
```

---

## 🎈Streamlit 前端應用

Streamlit 是讓我們做漂亮網頁介面的工具。

### 基本元件：按鈕、文字、輸入框

```python
import streamlit as st

st.title("我的網頁")
st.button("點我！")
text = st.text_input("請輸入文字")
st.write(f"你輸入的是：{text}")
```

### 使用 columns 排版（像表格一樣）

```python
col1, col2 = st.columns([1, 2])  # 左1份，右2份寬
with col1:
    st.button("按鈕1")
with col2:
    st.write("這是右邊的內容")
```

### 迴圈自動產生多個欄位

```python
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

---

## 🧠 session_state 記住資料

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("加1"):
    st.session_state.ans1 += 1

st.write(f"現在的值是: {st.session_state.ans1}")
```

👉 可以用來記住按鈕按了幾次！

---

## ➕ 算術指定運算子（a += b 這種）

| 寫法      | 意思                |
| --------- | ------------------- |
| a += 1    | a = a + 1           |
| a -= 1    | a = a - 1           |
| a \*= 2   | a = a × 2           |
| a /= 2    | a = a ÷ 2           |
| a \*\*= 2 | a = a 的平方        |
| a %= 2    | a 除以 2 的餘數     |
| a //= 2   | a 除以 2 的整數部分 |

---

## 🧮 運算優先順序（誰先算）

從優先順序高 ➜ 低：

1. `()` 括號先
2. `**` 次方
3. `* / // %` 乘除
4. `+ -` 加減
5. `== != > < >= <=` 比較
6. `not`
7. `and`
8. `or`
9. `= += -= ...` 指定

---

## 🔁 while 迴圈

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### `break` 用來跳出迴圈

```python
while True:
    guess = int(input("猜數字（1~100）："))
    if guess == 42:
        print("猜中了！")
        break
```

---

## 🎲 猜數字遊戲（搭配 `random`）

```python
import random
ans = random.randint(1, 100)

while True:
    guess = int(input("猜1到100之間的數字："))

    if guess < ans:
        print("再大一點")
    elif guess > ans:
        print("再小一點")
    else:
        print("猜對了！")
        break
```

---

## 📖 字典 dict（key - value）

字典的意思就像是資料的「對應表」。

```python
d = {1: "a", 2: "b", 3: "c"}
```

### 成績表範例

```python
grades = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63], "英文": [93, 83, 73]},
    "小華": {"國文": [86, 76, 66], "數學": [81, 71, 61], "英文": [91, 81, 71]},
}
```

查詢範例：

```python
print(grades["小明"]["數學"])       # ➜ [85, 75, 65]
print(grades["小美"]["英文"][0])   # ➜ 93
print(grades["小華"]["國文"][1])   # ➜ 76
```

---

希望這份筆記有幫助你複習今天的上課內容！如果還想看更多範例或圖解，也可以再問我 😊
