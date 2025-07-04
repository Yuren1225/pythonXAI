好的，以下是我幫你整理好的筆記，用簡單、好懂的國中生用詞來說明今天學到的 Python 指令內容：

---

# 🎯 Python + Streamlit 學習筆記（簡單版）

## 📌 Streamlit 是什麼？

Streamlit 是一個可以快速做出「互動式網頁」的小工具，讓我們用 Python 就能做出漂亮的網頁！

---

## 🖼️ 一、圖片元件的使用

### 1️⃣ 顯示圖片

```python
import streamlit as st

st.title("圖片元件")
st.image("image/apple.png", width=300)  # 顯示圖片，寬度300
```

👉 `st.image` 是用來放圖片的指令，可以調整圖片大小。

---

### 2️⃣ 一次顯示多張圖片

```python
import os

image_folder = "image"
image_files = os.listdir(image_folder)  # 取得資料夾裡所有檔案
st.write(image_files)  # 顯示檔案清單

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=100)  # 顯示每張圖片
```

👉 `os.listdir` 會幫你找到指定資料夾裡的所有檔案。

---

### 3️⃣ 調整圖片大小（互動式）

```python
image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
```

👉 `st.number_input` 讓使用者自己決定圖片大小。

---

### 4️⃣ 自動適應寬度

```python
for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", use_container_width=True)
```

👉 `use_container_width=True` 會讓圖片自動填滿區塊。

---

## 🛒 二、購物平台（互動式小遊戲）

### 1️⃣ 設定商品資料

```python
initial_product_info = {
    "apple.png": {"price": "$30", "stock": 10},
    "banana.png": {"price": "$20", "stock": 10},
}
```

👉 我們用「字典」記錄每個商品的「價格」和「庫存」。

---

### 2️⃣ 顯示多張商品圖片

```python
num_columns = st.number_input("請輸入每列圖片數量", min_value=1, max_value=5, value=3)

for i in range(0, len(image_files), num_columns):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        if i + j < len(image_files):
            image_file = image_files[i + j]
            with cols[j]:
                st.image(f"{image_folder}/{image_file}", use_container_width=True)
                # 顯示價格和庫存
```

👉 用 `st.columns` 把圖片排成一排，看起來更整齊。

---

### 3️⃣ 加入「購買」按鈕

```python
if st.button("🛍️ 購買", key=f"buy_{image_file}"):
    if info["stock"] > 0:
        st.session_state.product_info[image_file]["stock"] -= 1
        st.success(f"已購買 {image_file}！")
    else:
        st.error("❌ 庫存不足！")
    st.rerun()
```

👉 每個商品旁邊都可以點「購買」，按下去庫存會變少。

---

### 4️⃣ 增加商品庫存

```python
selected_product = st.selectbox("選擇商品名稱", product_names)
quantity_to_add = st.selectbox("選擇要增加的數量", list(range(1, 11)))

if st.button("✅ 確認新增庫存"):
    st.session_state.product_info[selected_product]["stock"] += quantity_to_add
    st.success("庫存已增加！")
    st.rerun()
```

👉 可以自己選商品，增加庫存數量。

---

### 5️⃣ 顯示所有商品庫存

```python
for product, info in st.session_state.product_info.items():
    st.write(f"{product}：庫存 {info['stock']}")
```

👉 把所有商品的庫存一目了然顯示出來。

---

## 🤖 三、跟 AI 聊天

### 1️⃣ 設定 API 金鑰

```python
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = st.secrets["OPENAI_API_KEY"]
```

👉 這段程式讓我們可以使用 ChatGPT API。

---

### 2️⃣ 聊天對話記錄

```python
if "history" not in st.session_state:
    st.session_state.history = []

prompt = st.chat_input("請輸入你的問題")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()
```

👉 `st.chat_input` 讓使用者輸入問題，`st.session_state` 幫我們記錄對話。

---

### 3️⃣ 顯示 AI 回答

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "請用繁體中文進行後續對話"}] + st.session_state.history,
)

assistant_message = response.choices[0].message.content
st.session_state.history.append({"role": "assistant", "content": assistant_message})
```

👉 AI 會根據使用者輸入的內容，自動回應。

---

### 4️⃣ 顯示聊天泡泡

```python
for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
```

👉 讓聊天變得更像真的在跟 AI 說話。

---

## ⭐ 總結重點

1. `st.title()` 可以加標題
2. `st.image()` 可以放圖片
3. `st.button()` 可以加按鈕
4. `st.session_state` 可以記住資料
5. `os.listdir()` 幫你找資料夾裡的檔案
6. 用 ChatGPT API 可以讓你的網頁變得有智慧！

---

這樣的筆記應該會更容易懂了！如果你想，我可以幫你做成簡報版本。
