import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time
import plotly.graph_objects as go


df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [40,30,20,10]
})

df
x = 100
x
"""
#マジックコマンドを使ってみる
文字列を入力
```
import streamlit as pt
print('hellow streamlit')
```
"""

# df = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
# df

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)



#matplotlib
"""
#matplotlib
"""
fig = plt.figure(figsize=(10,5))
ax = plt.axes()
x = [10,210,301,440,500]
y = [10,20,30,40,50]
ax.plot(x,y)
st.pyplot(fig)

#インタラクティブ

#ボタン設置
"""
#ボタン設置
"""
option_button = st.button('ボタン')
if option_button == True:
    st.write('ボタンが押されました')
else:
    st.write('ボタンを押してください')

#ラジオボタン
"""
#ラジオボタン
"""
option_radio = st.radio(
    "好きな果物を選んでください",('りんご','バナナ','オレンジ','その他')
)
st.write('あなたが選んだ果物は',option_radio)

#チェックボックス
"""
#チェックボックス
"""
option_check = st.checkbox('DataFrameの表示')
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [40,30,20,10]
})
if option_check == True:
    st.write(df)

#セレクトボックス
"""
#セレクトボックス
"""
option_select = st.selectbox('どれか一つを選んでください',('A','B','C'))
st.write('あなたが選んだのは：', option_select)

#マルチセレクト
"""
#マルチセレクト
"""
option_multi = st.multiselect(
    '好きな色を選択してください',
    ['緑','黄色','赤','青'],
    ['黄色','赤']
)

#スライダー
"""
#スライダー
"""
age = st.slider('あなたの年齢を教えてください', min_value=0, max_value=130, step=1, value=20)
st.write('私の年齢は', age, 'です')

value = st.slider(
    '数値の範囲を入力してください',
     0.0, 100.0, (25.0, 75.0))
st.write('values', value)

#サイドバー
"""
#サイドバー
"""
#スライダー
height = st.sidebar.slider('あなたの身長を入力してください', min_value=0, max_value=200, step=1, value=170)
st.write('私の身長は', height, 'です')

#セレクトボックス
gender = st.sidebar.selectbox(
    'あなたの性別を教えてください',
    ['男性','女性'])
st.write('あなたの性別は：', gender)

#プログレスバー
"""
#プログレスバー
"""
progress_button = st.button('プログレスボタン')
if progress_button == True:
    st.write('処理を開始します')
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete+1)
    st.text('処理が終了しました')
else:
    st.write('プログレスボタンを押してください')

#ファイルアップロード
"""
#ファイルアップロード
"""
upload_file = st.file_uploader("ファイルアップロード", type='csv')
if upload_file:
    df_csv = pd.read_csv(upload_file,encoding='shift-jis')
    st.dataframe(df_csv)
    fig =  go.Figure(data=[
    go.Scatter(x= np.array(df_csv['売上日']),y= np.array(df_csv['mean']),name="mean"),
    go.Scatter(x= np.array(df_csv['売上日']),y= np.array(df_csv['0']),name="allseason"),
    go.Scatter(x= np.array(df_csv['売上日']),y= np.array(df_csv['1']),name="spring"),
    go.Scatter(x= np.array(df_csv['売上日']),y= np.array(df_csv['2']),name="summer"),
    go.Scatter(x= np.array(df_csv['売上日']),y= np.array(df_csv['3']),name="autumn"),
    go.Scatter(x= np.array(df_csv['売上日']),y= np.array(df_csv['4']),name="winter"),
    go.Scatter(x= np.array(df_csv['売上日']),y= np.array(df_csv['5']),name="other"),
    ])
    st.plotly_chart(fig, use_container_width=True)



    
    
