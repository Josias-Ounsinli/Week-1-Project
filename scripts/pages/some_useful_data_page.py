import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Some insighful data", layout="wide")

st.title('1. Top 10 engaged customers data')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Top 10 customers for engagement metrics.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('2. Top 10 engaged customers (on applications) data')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Top 10 customers per application.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('3. Top 10 satisfied customers')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Top satisfied customers.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('4. Top values for experience metrics')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Experience_metrics_top_values.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('5. Satisfaction clusters data')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Satisfaction cluster_data.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('6. Engagements metrics with clusters')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Engagement metrics with cluster.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('7. Engagements metrics (on applications) with clusters')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Engagement metrics with cluster for applications.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('8. Experience metrics clusters data')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Experience_metrics_clusters_data.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('9. Preprocessed data used for the model')
df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Processed data used for the model.csv')
st.dataframe(df)
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
