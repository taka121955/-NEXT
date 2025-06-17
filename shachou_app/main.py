import streamlit as st
from datetime import datetime
import base64
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="社長秘書エリカ", layout="wide")

# === 白石えりか画像を中央・大きく表示 ===
def show_center_image(uploaded_image):
    img = Image.open(uploaded_image)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    st.markdown(f"""
        <style>
        .erika-center-img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 40%;
            max-width: 300px;
        }}
        @media (max-width: 768px) {{
            .erika-center-img {{
                width: 70%;
            }}
        }}
        </style>
        <img src="data:image/png;base64,{img_str}" class="erika-center-img">
    """, unsafe_allow_html=True)

# === 共通スタイル（フォントなど） ===
st.markdown("""
    <style>
    section[data-testid="stSidebar"] > div:first-child {
        height: 100vh;
        overflow-y: auto;
    }
    .stTextInput > div > input {
        text-align: center;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# === 上部ヘッダー ===
now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
st.markdown(f"""
## 🏢 &NEXT合同会社 ｜ 社長秘書エリカ
### 🕒 現在時刻（日本時間）：{now}
""")

# === 中央に白石えりかの画像を表示 ===
show_center_image("C218EBE1-DA82-44F7-83DE-74C4DE20DEC3.jpeg")

# === 入力エリア ===
st.markdown("---")
st.markdown("### 💬 白石えりか（社長秘書）")
st.markdown("#### 📢 社長、ご用件をどうぞ。")

command = st.text_input("社長のご指示を入力してください", label_visibility="collapsed")
if st.button("📨 指示を送信"):
    if command.strip():
        st.success(f"📎 指示内容：**{command}** を受け付けました。")
        st.info("📌 エリカが対応準備中です。")
    else:
        st.warning("⚠️ ご指示が未入力です。")

st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
