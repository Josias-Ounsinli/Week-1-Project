from statistics import mode
import sys
sys.path.insert(0, './scripts')

import streamlit as st
from multiapp import MultiApp
from pages import user_overview_analysis_page, user_engagement_analysis_page, user_experience_analysis_page, some_useful_data_page, final_data_and_some_visualization_page, user_satistfaction_analysis_page, model_implementation
# import your app modules here

st.set_page_config(page_title="TellCo Telecom Analytics", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# TellCo's User Analytics
### Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
### Modifications
\t- Page Folder Based Access
\t- Presentation changed to SideBar
""")

# Add all your application here
app.add_app("User overview analysis", user_overview_analysis_page.app)
app.add_app("User engagement analysis", user_engagement_analysis_page.app)
app.add_app("User experience analysis", user_experience_analysis_page.app)
app.add_app("User satisfaction analysis", user_satistfaction_analysis_page.app)
app.add_app("FFinal Data and brief viusalizations", final_data_and_some_visualization_page.app)
app.add_app("Some insighful data", some_useful_data_page.app)
app.add_app('Model', model_implementation.app)

# The main app
app.run()