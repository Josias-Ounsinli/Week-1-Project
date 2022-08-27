from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="User experience analysis", layout="wide")

st.title('Data visualisation')
image1 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Distribution TP.png')
st.image(image1, caption='Average TP distribution throughout handset')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('Clustering on experience metrics')
image2 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Experience Cluster.png')
st.image(image2, caption='Clusters for experience metrics')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
