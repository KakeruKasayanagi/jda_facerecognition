import streamlit as st
import pandas as pd
import numpy as np


st.title('Face Recogniton App')

st.write('DataFrame')
st.write(
    pd.DataFrame({
        '1st column':[1, 2, 3, 4],
        '2nd column':[10, 20, 30, 40]
    })
)


"""
# ここより下にチャートを記述
pandasがデータの可視化。numpyが数値の作成。
(Uえるのグラフ化にはstreamlit)
"""

if st.checkbox('Show DataFrame'):
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    st.line_chart(chart_df)

