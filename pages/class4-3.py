import streamlit as st  # 網頁
import os
import time

st.title("🛒 購物平台")  # 標題


image_folder = "image"
image_files = [
    f
    for f in os.listdir(image_folder)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))  # 找圖片
]


initial_product_info = {
    "apple.png": {"price": "$30", "stock": 10},
    "banana.png": {"price": "$20", "stock": 10},
    "bg.png": {"price": "$50", "stock": 10},  #
    "orange.png": {"price": "$25", "stock": 10},
}


if "product_info" not in st.session_state:
    st.session_state.product_info = (
        initial_product_info.copy()
    )  # 商品庫存存到session state


num_columns = st.number_input(
    "請輸入每列圖片數量 (欄位數)",
    min_value=1,
    max_value=5,
    value=3,
    step=1,  # 最大值和最小值和初始值
)

# 顯示圖片與資訊，每列最多 num_columns 欄
for i in range(0, len(image_files), num_columns):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        if i + j < len(image_files):
            image_file = image_files[i + j]
            with cols[j]:
                st.image(f"{image_folder}/{image_file}", use_container_width=True)

                info = st.session_state.product_info.get(
                    image_file, {"price": "未知", "stock": "未知"}
                )
                st.write(f"💰 價格: {info['price']}")
                st.write(f"📦 庫存: {info['stock']}")

                # 動態產生按鈕的 key
                button_key = f"buy_{image_file}"
                if st.button("🛍️ 購買", key=button_key):
                    if info["stock"] > 0:
                        st.session_state.product_info[image_file]["stock"] -= 1
                        st.success(f"已購買 {image_file}！")
                    else:
                        st.error("❌ 庫存不足！")
                    st.rerun()

# 分隔線
st.markdown("---")

# 新增商品庫存
st.header("➕ 新增商品庫存")

# 建立左右兩欄
col1, col2 = st.columns(2)

with col1:
    product_names = list(st.session_state.product_info.keys())
    selected_product = st.selectbox("選擇商品名稱", product_names)

with col2:
    quantity_to_add = st.selectbox("選擇要增加的數量", list(range(1, 11)))

# 確認按鈕
if st.button("✅ 確認新增庫存"):
    st.session_state.product_info[selected_product]["stock"] += quantity_to_add
    st.success(f"{selected_product} 的庫存已增加 {quantity_to_add}！")
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理
# 顯示所有商品目前庫存
st.subheader("📦 所有商品目前庫存")
for product, info in st.session_state.product_info.items():
    st.write(f"👉 **{product}** ：庫存 **{info['stock']}**")
