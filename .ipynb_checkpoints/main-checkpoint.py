import streamlit as st
from PIL import Image

st.title('顔認証アプリ')

"""
#### 下記に画像をアップロードしてください（jpegのみの対応です）

"""

uploaded_file = st.file_uploader("Choose an image...", type='jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True )



