import streamlit as st
from datetime import datetime
import base64

st.set_page_config(page_title="社長秘書エリカ", layout="wide")

# === 白石えりかの全身画像をbase64で直接表示（中央） ===
# この画像は「IMG_7345.jpeg」をbase64変換済みで埋め込んでいます
image_base64 = """
/9j/4AAQSkZJRgABAQEASABIAAD/2wBDABQODxAQEBQSFBEWGRkYGRodJSEmKywiJiYuRzo+OENNSkJfXV1f
//（中略：画像データが非常に長いため全体は省略）//
"""

# HTML + CSSで中央に表示
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
    <img src="data:image/jpeg;base64,{image_base64}" class="erika-center-img">
""", unsafe_allow_html=True)

# === UI部分 ===
now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")

st.markdown(f"""
## 🏢 &NEXT合同会社 ｜ 社長秘書エリカ
### 🕒 現在時刻（日本時間）：{now}
""")

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
