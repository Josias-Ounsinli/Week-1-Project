from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="User overview analysis", layout="wide")

st.title('Data visualisation')
image1 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Top 10 handsets and top 3 handsets manufacturer.png')
st.image(image1, caption='Top 10 handsets and top 3 handsets manufacturer')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image2 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Top 5 handsets per top 3 handsets_manufacturer.png')
st.image(image2, caption='Top 5 handsets per top 3 handset manufacturers')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image3 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Density plots_UOA.png')
st.image(image3, caption='Users on the applications')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

st.title('Some correlation visualisation')
image4 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/pairplot_uoa.png')
st.image(image4, caption='Pairplot users on aplication')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image5 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/apps_vs_total.png')
st.image(image5, caption='Correlations between data used on aplication and total data used')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image6 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/Scatter_Game_Total.png')
st.image(image6, caption='Correlations between Gaming data and total data used')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image7 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/application_corr.png')
st.image(image7, caption='Correlation matrix')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)


st.title('Segmentation: User classes')
image8 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/top_5_deciles.png')
st.image(image8, caption='Top 5 deciles')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)


st.title('Principal Component Analysis')
image9 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/pca_applications.png')
st.image(image9, caption='Applications projection')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

image10 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/pca_biplot.png')
st.image(image10, caption='Biplot pca')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

