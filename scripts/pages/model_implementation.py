from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Model", layout="wide")

st.title('Learning curve of the model of satisfaction prediction')
image1 = Image.open('/home/jds98/10 Academy/Week 1/Week-1-Project/notebooks/Figures/learning curve.png')
st.image(image1, caption='Learning curve of the model')
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
