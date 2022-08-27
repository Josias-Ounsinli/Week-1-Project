from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="User engagement analysis", layout="wide")

st.title('Data visualisation')
image1 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/top10_users_sessions_freq.png')
st.image(image1, caption='Top frequent customers (sessions frequency)')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image2 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/top10_users_dur_ms.png')
st.image(image2, caption='Top 10 customers (sessions duration)')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image3 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/top10_users_total_traffic.png')
st.image(image3, caption='Top 10 customers (total traffic)')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('Clustering using engagement metrics')
image4 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/metrics_clusters.png')
st.image(image4, caption='Clusters on engagement metrics')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('Top 3 applications used')
image5 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Top3 applications.png')
st.image(image5, caption='Top 3 applications used')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('Clustering using applications total traffic')
image6 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Elbow method.png')
st.image(image6, caption='Elbow method: Maximum number of clusters')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image7 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/plot_cluters4.png')
st.image(image7, caption='Clusters on applications using')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
