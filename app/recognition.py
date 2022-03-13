import streamlit as st
import io
import requests
from PIL import Image
from PIL import ImageDraw
import pandas as pd


# UI
add_selectbox = st.sidebar.selectbox("メニュー", ("画像認識/顔検出","画像認識/物体検出(準備中)",  "リアルタイム画像認識/物体検出(準備中)"))
st.title('顔認証アプリ（PC版）')

"""
###### 下記に画像をアップロードしてください（jpgのみの対応です）

"""

# /UI

# subscription_keyとURLの設定
subscription_key = '2a27e11cacae4ca0aa27fe68c84feb1e'
assert subscription_key

face_api_url = 'https://face-recognition-app.cognitiveservices.azure.com/face/v1.0/detect'
# /subscription_keyとURLの設定


# ファイルのアップロードから結果の出力まで
uploaded_file = st.file_uploader("Choose an image...", type='jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    #画像の展開→バイナリーデータによる展開
    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue()

    #APIをたたくための設定
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key
    }    
    params = {
        'returnFaceId': 'true',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise', 
    }

    response = requests.post(face_api_url, params=params, headers=headers, data=binary_img)

    #レスポンスから結果をもってきて、レクタングルデータを抽出
    results = response.json()
    for result in results:
        rect = result['faceRectangle']
        attr = result['faceAttributes']

    #描画画像に描画をする
        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])], fill=None, outline='green', width=5)
        draw.text((rect['left']+rect['width'], rect['top']), str(attr['gender']), fill = (255, 0, 0))
        draw.text((rect['left']+rect['width'], rect['top']+15), str(attr['age']), fill = (255, 0, 0))

    st.image(img, caption='Uploaded Image.', use_column_width=True )
# /ファイルのアップロードから結果の出力まで

# UI②
"""
######
"""
if st.checkbox('使い方'):
    """
    □　上記の”Browse files”ボタンをクリックし、任意の画像を選択してください。
    \n □　選択してから2~3秒後に、画像の中の「顔」とそれらに紐づく「性別」と「年齢」が判定されます。
    \n ※アップロードされた画像をデータベース等に保存する機能は実装していないため、お気軽にご使用ください！！
    """

# /UI②
