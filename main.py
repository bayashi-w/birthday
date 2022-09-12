import streamlit as st
from PIL import Image
import time


st.title('質問に答えてください')
name = st.text_input('あなたの名前は？')
st.text('例：山田太郎')
age = st.slider('あなたの年齢は？', 0 ,100, 50) 

if st.button('内容を確定する。' ):
        if age == 25 and name == '菊野麗菜':
            latest_iteration = st.empty()
            bar = st.progress(0)
            for i in range(100):
                latest_iteration.text(f'{i+1}')
                bar.progress(i + 1)
                time.sleep(0.01)
            st.header('誕生日おめでとう！！！')
            img = Image.open('IMG.jpg')
            st.image(img, use_column_width=True)           
        else:
            st.error('エラー：どちら様ですか？')
            
            


