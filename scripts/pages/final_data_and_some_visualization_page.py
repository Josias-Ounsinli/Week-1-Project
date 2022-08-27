import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Final Data and brief viusalizations", layout="wide")

st.title('DataFrame of the final data')

df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Final table.csv')

st.dataframe(df)


def handsets(df):
    handsets = df['Handset Type'].value_counts()
    fig, ax = plt.subplots(figsize=(15, 8))
    st.title("1. Top 10 handsets used")
    handsets[:10].plot(ax=ax, kind='bar', color='red')
    st.pyplot(fig)
    

def topsatisf(df):
    top_satisfied = df[['MSISDN/Number', 'Satisfaction_scores']].sort_values(by=['Satisfaction_scores'], ascending=False)[:10]
    top_satisfied = top_satisfied.set_index('MSISDN/Number')

    fig, ax = plt.subplots(figsize=(15, 8))
    st.title("2. Top 10 satisfied customers")
    top_satisfied.plot(ax=ax, kind='bar', color='green')
    st.pyplot(fig)


def satisfaction(df):
    sat = df['satisfied'].value_counts()
    fig, ax = plt.subplots(figsize=(15, 8))
    st.title("3. Satisfaction classes")
    sat.plot(ax=ax, kind='bar', color='red')
    st.pyplot(fig)

st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
st.title("Data Visualizations")
handsets(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
topsatisf(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
satisfaction(df)

