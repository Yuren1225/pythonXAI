import streamlit as st

with st.expander("Class1課堂筆記"):
    st.write(
        """
        這裡是一份整理過、使用淺顯國中程度語言的 Python 筆記，幫助你回顧今天課堂上學到的內容：

    ---

    # 🐍 Python 初學筆記

    ## 🗣️ 印出東西到螢幕上

    ```python
    print("hallo")
    ```

    * `print()` 是用來在畫面上顯示東西的指令。
    * 引號裡的東西會直接顯示出來。

    ---

    ## 💬 註解（不會被執行）

    * 用 `#` 來寫一行註解，讓自己或別人看懂程式在做什麼。
    * 用三個單引號 `''' 內容 '''` 可以寫多行註解。
    * 快速註解：在程式編輯器中按 `Ctrl + ?`（視軟體而定）。

    ---

    ## 📊 基本資料型別

    | 類型      | 說明                       | 範例               |
    | ------- | ------------------------ | ---------------- |
    | `bool`  | 布林值，只會是 `True` 或 `False` | `print(True)`    |
    | `int`   | 整數                       | `print(1)`       |
    | `float` | 小數（浮點數）                  | `print(1.0)`     |
    | `str`   | 字串（文字）                   | `print("hello")` |

    ---

    ## 🧠 變數的使用

    ```python
    a = 10
    print(a)
    a = "apple"
    print(a)
    ```

    * `a` 是變數，用來存資料（像是數字或文字）。
    * 可以改變變數的內容。

    ---

    ## ➕ 基本運算

    ```python
    print(1 + 1)  # 加法
    print(1 - 1)  # 減法
    print(1 * 1)  # 乘法
    print(1 / 1)  # 除法（結果是小數）
    print(1 // 1)  # 整數除法（只留整數）
    print(1 % 1)  # 餘數
    print(2**2)  # 次方（2的2次方）
    ```

    🔢 運算優先順序：

    1. 括號 `()`
    2. 次方 `**`
    3. 乘、除、整除、餘數 `* / // %`
    4. 加減 `+ -`

    ---

    ## 🧩 f-string 字串格式化

    ```python
    a = 5
    b = "蘋果"
    print(f"{b}有{a}個")
    ```

    * `f"{變數}"` 可以把變數的值插進字串中。

    ---

    ## 🔍 查看資料型別

    ```python
    type(變數)
    ```

    範例：

    ```python
    print(type(True))  # bool
    print(type(1))     # int
    print(type(1.0))   # float
    print(type("hi"))  # str
    ```

    ---

    ## 🔄 資料型別轉換

    ```python
    int(1.0)        # 變成整數
    float(1)        # 變成小數
    str(1)          # 變成字串
    bool(1.234)     # 變成布林值（非0為True）
    ```

    範例：

    ```python
    print(int(1.234))       # 1
    print(float("1.234"))   # 1.234
    print(str(1.234))       # '1.234'
    print(bool(0))          # False
    ```

    ---

    ## ⌨️ 使用者輸入

    ```python
    a = input("請輸入一個數字: ")
    print(int(a) + 10)
    ```

    * `input()` 讓使用者可以在終端機輸入資料。
    * 注意！輸入的資料型別預設是字串（str）。

    ---

    ## 🖥️ Streamlit（讓 Python 變成網頁）

    ```python
    import streamlit as st
    ```

    ### 標題與文字顯示

    ```python
    st.title("這是標題")  # 顯示大標題
    st.write("這是普通的文字，還能支援表格、數字等")
    st.text("這是純文字，不支援格式")
    ```

    ### Markdown 語法（可以做出格式化的文字）

    ````python
    st.markdown(\"""
    # 這是最大標題
    ## 這是次大標題
    ### 更小的標題
    ---

    - 清單項目一
    - 清單項目二

    **粗體文字**  
    *斜體文字*

    [連結](https://www.example.com)

    ```python
    print("Hello, Streamlit!")
    ````

    \""")

    ```

    ---

    如果你能理解這些內容，就已經掌握了 Python 的基礎了！👏  
    未來還有更多進階的內容，慢慢學就好，不用一次記住全部，加油！

    ---  
    需要我幫你製作筆記成 PDF 或加上插圖，也可以告訴我哦！
    ```

    """
    )

with st.expander("Class2課堂筆記"):
    st.write(
        """
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

* `if`：如果符合條件，就執行對應內容
* `elif`（else if）：如果前面不符合，才會檢查這裡
* `else`：以上都不符合，就執行這段

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

📌 說明：

* `st.number_input`：在網頁上顯示一個可以輸入數字的格子
* `step`：每次加減的單位
* `min_value / max_value`：可以輸入的範圍

---

### 🎉 按鈕互動

```python
if st.button("點我"):
    st.balloons()  # 會噴出氣球動畫

if st.button("按我", key="snow"):
    st.snow()  # 會出現雪花動畫
```

📌 說明：

* `st.button("文字")`：在網頁上顯示一個按鈕
* `key`：讓不同按鈕有不同的名字
* 按鈕被點時會執行後面的動畫程式

---

這就是你今天學到的 Python 重點內容！💪
繼續加油，學會這些之後，你就能做出自己的小遊戲或互動網站了喔！

如果你還有不懂的地方，歡迎再問我 😊

    """
    )
with st.expander("Class3課堂筆記"):
    st.write(
        """
這裡是幫你整理的 **Python 課堂筆記**，使用簡單、容易懂的國中程度用詞。你可以拿來當作學習回顧的重點整理 👇

---

## 🌀 `for` 迴圈是什麼？

* `for` 是用來「重複做某件事」的工具。
* 它會搭配 `in` 和 `range()` 使用。
* 例如：

```python
for i in range(5):
    print(i)
```

→ 會印出 0 到 4 的數字（一共跑 5 次）。

---

## 📏 `range()` 怎麼用？

`range()` 是一個幫我們「產生數字範圍」的工具。

1. **只有一個數字時** → `range(5)` 表示從 0 到 4（不包含 5）。
2. **兩個數字時** → `range(1, 5)` 表示從 1 到 4（不包含 5）。
3. **三個數字時** → `range(1, 10, 2)` 表示從 1 開始，每次+2，印到 9（不包含 10）。

---

## 🎯 小練習：印出1到使用者輸入的數字

```python
a = int(input("請輸入一個數字:"))
b = int(input("請輸入另一個數字:"))
for i in range(a, b + 1):
    print(f"{i}號在教室")
```

---

## ➕ 加總一段數字

```python
total = 0
for i in range(a, b + 1):
    total = total + i
print(f"{a}加到{b}的總和是: {total}")
```

---

## 🖥 Streamlit 做金字塔圖形（需搭配網頁介面）

````python
import streamlit as st

st.title("箭頭金字塔")
num = st.number_input("請輸入一個整數", value=0, step=1)
s = ""
for i in range(1, num + 1):
    space = " " * (num - i)
    star = "*" * (2 * i - 1)
    s = s + space + star + "\n"
for i in range(num):
    s = s + " " * (num - 1) + "*" + "\n"
st.write(f"```\n{s}```")
````

---

## 🧺 List（串列）

### 📦 List 是什麼？

* 就像一個裝了很多東西的箱子。

```python
print([1, 2, 3])  # 有三個數字
print([1, 2, 3, ["a", "b", "c"]])  # 也可以放進其他 List
```

### 🧐 怎麼看 List 裡面的東西？

* 用「編號」來找（編號從 0 開始）：

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[3])  # a
```

---

## 🧠 List 的進階技巧

### ➗ 切片（slice）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])     # 每隔一個取 → [1, 3, "b"]
print(L[1:4])     # 從第1到第3 → [2, 3, "a"]
print(L[1:4:2])   # 從第1到第3，每隔1個取 → [2, "a"]
```

### 📏 `len()`：看有幾個東西

```python
print(len(L))  # 6
```

---

## 🔁 List 的走訪（每一個都看一次）

兩種方法都可以：

### 方法一（用編號）

```python
for i in range(len(L)):
    print(L[i])
```

### 方法二（直接看內容）

```python
for i in L:
    print(i)
```

### 舉例：印出水果和數量

```python
F = ["蘋果", "香蕉", "鳳梨"]
N = [3, 5, 6]
for i in range(len(F)):
    print(f"{F[i]}有{N[i]}個")
```

---

## ⚖️ Call by value vs Call by reference

### Call by value（只是複製）

```python
a = 1
b = a
b = 2
print(a, b)  # a 不會變
```

### Call by reference（兩個人共用一個記憶體）

```python
a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)  # a 也會變
```

---

## ➕ List 加東西、移除東西

### 加東西：`append()`

```python
L = [1, 2, 3]
L.append(4)  # 加在最後
```

### 移除東西

#### 1. `remove()`：移掉指定內容

```python
L = ["a", "b", "c"]
L.remove("a")  # 移掉第一個 "a"
```

#### 2. `pop()`：移掉指定位置

```python
L = ["a", "b", "c", "d"]
L.pop(0)  # 移除第一個
L.pop()   # 不寫編號就移除最後一個
```

---

這就是今天上課的重點整理 💡
如果你看不懂某段或想多做練習，我可以幫你設計小題目喔！你也可以請我解釋任何一個段落～ 🙌

"""
    )
# 123
