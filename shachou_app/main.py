import streamlit as st
from datetime import datetime
import base64

st.set_page_config(page_title="社長秘書エリカ", layout="wide")

# === base64で直接画像をHTMLに埋め込む ===
def show_center_image_from_path():
    # base64に変換（今回のアップ画像をコードに直接埋め込むかURL化が必要）
    image_path = "https://drive.google.com/uc?id=YOUR_IMAGE_ID"  # ←ここだけ差し替えればOK
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
        <img src="{image_path}" class="erika-center-img">
    """, unsafe_allow_html=True)

# === 共通スタイル ===
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

# === ヘッダー ===
now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
st.markdown(f"""
## 🏢 &NEXT合同会社 ｜ 社長秘書エリカ
### 🕒 現在時刻（日本時間）：{now}
""")

# === 全身画像中央表示 ===
show_center_image_from_path()

# === 入力セクション ===
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
