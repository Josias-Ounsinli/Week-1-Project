from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="User satisfaction analysis", layout="wide")

st.title('Learning curve of the model of satisfaction prediction')
image1 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/learning curve.png')
st.image(image1, caption='Learning curve of the model')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('Clustering on experience metrics')
image2 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/satisfaction_clusters.png')
st.image(image2, caption='Clusters for satisfactions')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('Satisfaction frequencies')
image3 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/satisfaction classes.png')
st.image(image3, caption='Classes for satisfactions')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
