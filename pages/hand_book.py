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

# 123
