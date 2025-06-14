# main.py
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="社長秘書エリカ", layout="centered")

# 現在時刻（日本時間）
jst_now = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')

st.markdown(f"### 🧭 &NEXT合同会社 ｜ 社長秘書エリカ")
st.markdown(f"🕒 現在時刻（日本時間）：**{jst_now}**")
st.markdown("---")

# チャット風UI
st.markdown("#### 💬 白石えりか（社長秘書）")
st.info("社長、ご用件をどうぞ。")

user_input = st.text_input("💼 社長のご指示を入力してください", "")

if user_input:
    st.success(f"かしこまりました。ご指示「{user_input}」を受け付けました。")
    if "会議室" in user_input:
        st.markdown("[👉 経営幹部会議室へ移動](./会議室)")
    elif "予定" in user_input:
        st.markdown("📅 今週の予定：\n- 6/15（金）15:00 経営会議\n- 6/16（土）AI研修")
    elif "履歴書" in user_input:
        st.markdown("🗂 社員の履歴書はこちら：[社員情報ページ（準備中）](#)")
    else:
        st.markdown("🔍 ご指示に基づく処理は現在準備中です。")

# フッター
st.markdown("---")
st.markdown("👩‍💼 制作者：小島崇彦")
