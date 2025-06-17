import streamlit as st
from datetime import datetime

st.set_page_config(page_title="社長秘書エリカ", layout="wide")

# === CSSスタイル定義 ===
st.markdown("""
    <style>
    /* サイドバーのスクロール対応 */
    section[data-testid="stSidebar"] > div:first-child {
        height: 100vh;
        overflow-y: auto;
    }

    /* 入力欄の見た目調整 */
    .css-18e3th9 {padding: 1rem 2rem !important;}
    .css-1d391kg {padding-top: 0rem !important;}
    .css-ffhzg2 {text-align: center !important;}
    .stTextInput > div > input {
        text-align: center;
        font-size: 18px;
    }

    /* 白石えりかの全身画像を右下に表示 */
    .erika-img {
        position: fixed;
        bottom: 10px;
        right: 10px;
        width: 110px;
        z-index: 100;
        opacity: 0.95;
    }

    @media (max-width: 768px) {
        .erika-img {
            width: 80px;
        }
    }
    </style>

    <!-- 👇 画像の表示（画像IDを差し替えてください） -->
    <img src="https://drive.google.com/uc?id=YOUR_IMAGE_ID" class="erika-img">
""", unsafe_allow_html=True)

# === タイトル＆時刻表示 ===
now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
st.markdown(f"""
## 🏢 &NEXT合同会社 ｜ 社長秘書エリカ
### 🕒 現在時刻（日本時間）：{now}

---

### 💬 白石えりか（社長秘書）
#### 📢 社長、ご用件をどうぞ。
""")

# === 入力欄と送信ボタン ===
command = st.text_input("社長のご指示を入力してください", label_visibility="collapsed")
if st.button("📨 指示を送信"):
    if command.strip():
        st.success(f"📎 指示内容：**{command}** を受け付けました。")
        st.info("📌 エリカが対応準備中です。")
    else:
        st.warning("⚠️ ご指示が未入力です。")

# === 制作者名 ===
st.markdown("---")
st.markdown("👤 制作者：小島崇彦")
