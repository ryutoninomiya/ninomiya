# Streamlitライブラリをインポート
import streamlit as st
import random
saikoro = (1,2,3,4,5,6)

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('さいころ回そう')


saikorosuu = st.number_input("さいころの数を入力してください",min_value=0)

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('回す')
    st.write(f'さいころの数は、「{saikorosuu}」個です。')
    random_num=random.randint(saikoro)
    for random_num in range(saikorosuu):
        st.write(f'さいころの数字は、{random_num}')
    
