import streamlit as st
import pandas as pd
import time

##text utility******

st.title('Startup Dashboard')
st.header('Hello world')
st.subheader('hi')
st.write('welcome to startup analysis')
st.markdown("""
           ### MY favorite Movies
           -  diya
            - love moctail
            - race 3""")

st.code("""
           def func(a):
            return a*2
        func(5) """)

st.latex('x^2+y^2+3=0')

#Display elements****

df=pd.DataFrame({
    'name':['likith','venki'],
    'lpa': [7.5,6.5]
})

st.dataframe(df)

st.metric('Revenue','3l','-3%')


import streamlit as st


email=st.text_input('enter email')
password=st.text_input('enter password')
gender=st.selectbox('select gender',['male','female','other'])

btn=st.button('login here')

#if button is clicked   
if btn:
    if email=='abhi@gmail.com' and password=='1234':
        st.success('Login Successful')
        st.write(gender)
        st.balloons()
    else:
        st.error('Login Failed')

st.json({
    'name':['likith','venki'],
    'lpa': [7.5,6.5]
}   )

st.image('our_lab.JPG')
st.video('class.mp4')

st.sidebar.title('Welcome')

col1,col2= st.columns(2)

with col1:
    st.image('our_lab.JPG')
with col2:
    st.image('our_lab.JPG')

st.error('login failed')
st.success('login successful')
st.info('just a info')
st.warning('just warning')

bar= st.progress(0)

for i in range(0,101):
    time.sleep(0.1)

email=st.text_input('Enter Email')
number=st.number_input('Enter age')
date=st.date_input('Enter date')


import streamlit as st
import pandas as pd

file=st.file_uploader('upload a csv file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())




