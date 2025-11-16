import streamlit as st
import pandas as pd
import backend as bk

st.set_page_config(page_title="College Recommendation System", layout="wide")

st.title("Delhi College Recommendation System")
st.write("This tool suggests engineering colleges based on your JEE percentile.")

percentile = st.slider("Enter your JEE Percentile", 60, 100, 85)

tab1, tab2, tab3, tab4 = st.tabs([
    "Best Matches",
    "Additional Options",
    "All Colleges",
    "Cutoff Trend"
])

with tab1:
    st.subheader("Best Options for Your Percentile")
    result = bk.best_suited(percentile)
    st.dataframe(result, use_container_width=True)

with tab2:
    st.subheader("Additional Options")
    result = bk.additional_options(percentile)
    st.dataframe(result, use_container_width=True)

with tab3:
    st.subheader("All Colleges with 2025 Cutoffs")
    st.dataframe(bk.show_all_cutoffs(), use_container_width=True)

with tab4:
    st.subheader("Cutoff Trend (2015–2025)")
    trend = bk.get_trend_data()
    st.line_chart(trend.set_index("Year"))

st.markdown("""
Project by Class 12 Students  
Subject: Artificial Intelligence (843)  
""")

st.sidebar.title("Project Info")
st.sidebar.markdown("""
**Team Members**
- Ritesh Pathak  
- Eshan Awasthi  
- Pratyush Singh  
- Aditi Mishra  
- Ryan Naqvi  

**Class:** 12th  
**School:** AMITY INTERNATIONAL SCHOOL, MAYUR VIHAR PHASE-1, DELHI-110091  

**Description:**  
This AI project analyzes JEE percentile data to recommend suitable Delhi engineering colleges for B.Tech and predicts future cutoffs using Linear Regression.  
It features an interactive frontend built using Streamlit.
""")

