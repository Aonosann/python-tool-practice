import streamlit as st

# ページのタイトル
st.title("📝 単語カウンター")

# 説明文
st.write("テキストを入力すると、単語数を数えます！")

# テキスト入力エリア
text = st.text_area("ここにテキストを入力してください", height=200)

# ボタンを押したらカウント
if st.button("カウントする"):
    if text:
        # 単語数をカウント（スペースで分割）
        words = text.split()
        word_count = len(words)
        
        # 結果を表示
        st.success(f"🔢 単語数: {word_count}")
    else:
        st.warning("テキストを入力してください！")