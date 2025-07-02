這裡是幫你整理的 **Python 課堂筆記**，使用簡單、容易懂的國中程度用詞。你可以拿來當作學習回顧的重點整理 👇

---

## 🌀 `for` 迴圈是什麼？

- `for` 是用來「重複做某件事」的工具。
- 它會搭配 `in` 和 `range()` 使用。
- 例如：

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

## 🎯 小練習：印出 1 到使用者輸入的數字

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

- 就像一個裝了很多東西的箱子。

```python
print([1, 2, 3])  # 有三個數字
print([1, 2, 3, ["a", "b", "c"]])  # 也可以放進其他 List
```

### 🧐 怎麼看 List 裡面的東西？

- 用「編號」來找（編號從 0 開始）：

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
