import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Startup Analysis')

df=pd.read_csv('startup_cleaned.csv')

def load_investor_details(investor):
    st.title(investor)
    # load the last 5 investments
    st.subheader('last 5 Investments')
    last_5=df[df['Investors'].str.contains(investor)].sort_values(by='date',ascending=False).head(5)
    st.dataframe(last_5)    

    col1,col2=st.columns(2)
    with col1:
        # load the biggest_investment
        st.subheader('Biggest Investments')
        big_series=df[df['Investors'].str.contains(investor)].groupby('startup').sum('amount').sort_values(by='amount',ascending=False)
        st.dataframe(big_series)
        fig,ax=plt.subplots()
        ax.bar(big_series.index,big_series['amount'])
        st.pyplot(fig)
    
    with col2:
        # load the verticals invested.
        st.subheader('verticals Invested')
        verticals_series=df[df['Investors'].str.contains(investor)].groupby('vertical').sum('amount').sort_values(by='amount',ascending=False)
        st.dataframe(verticals_series)
        fig,ax=plt.subplots()   
        ax.pie(verticals_series['amount'], labels=verticals_series.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    


st.sidebar.title('Startup Funding Analysis')

option=st.sidebar.selectbox('select One',['Overall Analyis','Startup', 'Investor'])

if option=='Overall Analysis':
    st.title('Overall Analysis')
elif  option=='Startup':
    st.sidebar.selectbox('select One',df['startup'].unique())
    bt1=st.sidebar.button('find startup details')
    st.title('Startup Analysis')
else:
    selected_investor=st.sidebar.selectbox('select One',sorted(set(df['Investors'].str.split(',').sum())))
    bt2=st.sidebar.button('find Investors details')
    if bt2:
        load_investor_details(selected_investor)
        
    




