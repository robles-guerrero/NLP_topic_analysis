import streamlit as st
import pandas as pd
import numpy as np

import tensorflow as tf 
import tensorflow_hub as hub
import numpy as np

import tensorflow_text as text
import plotly.express as px

from PIL import Image



#st.set_page_config(layout='wide')

st.markdown("<h1 style='text-align: center; color: black;'>Moderator 3000 recharged</h1>", unsafe_allow_html=True)
#st.title('Moderator 3000 recharged')

#print(check)
#model = pickle.load()
# model= joblib.load('Skynet.pkl')
# with open('Skynet.pkl', 'rb') as f:
#     data = pickle.load(f)





@st.cache 
def load_model():
    path = 'C:/Users/Consultant/Documents/Python_Scripts/model_news_topics_bert/model_news_topics_bert'
    model = tf.saved_model.load(path)
    return model

# model = tf.saved_model.load('model_news_topics_bert')
# path = r"C:\Users\Consultant\PycharmProjects\pythonProject\Project\model_news_topics_bert"
# # assert os.path.isfile(path)
# with open(path, "r") as f:
#     model = tf.saved_model.load(f)
# with open('model_news_topics_bert') as f:
#     model = tf.saved_model.load(f)



def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


#_max_width_()
#"C:\Users\Consultant\Downloads\800px-President_Barack_Obama.jpg"

col1,col2,col3 = st.columns(3)
image=Image.open('C:/Users/Consultant/Downloads/politics.jfif')
image2=Image.open('C:/Users/Consultant/Downloads/download.png')
image3=Image.open('C:/Users/Consultant/Downloads/stonkss.jfif')


col1.image(image.resize((300,300)),use_column_width=True)
col2.image(image2.resize((300,300)),use_column_width=True)
col3.image(image3.resize((300,300)),use_column_width=True)

model=load_model()

st.subheader('Post')
test_text = st.text_input('Insert comment here')

review = st.button('Submit')

if review:
    #st.info('Result')
    test = np.argmax(model([test_text]))
    #st.success('The value is {}'.format(test))

    if test == 0:
        st.header('Politics')
    elif test == 1:
        st.header('Economy')
    elif test == 2:
        st.header('Tech')