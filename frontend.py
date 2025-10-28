import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import backend as bk

st.set_page_config(page_title="Delhi Engineering College Recommender 🎓", page_icon="🎓", layout="wide")

st.title("🎓 Delhi Engineering College Recommendation System")
st.write("Find your best engineering college in Delhi based on your JEE percentile!")

percentile = st.slider("Enter your JEE Percentile:", 0.0, 100.0, 90.0)

tab1, tab2, tab3, tab4 = st.tabs(["🎯 Best Colleges", "📘 Backup Options", "📊 All Data", "📈 Trend Graph"])

with tab1:
    st.subheader("🎯 Colleges That Match You")
    res = bk.best_suited(percentile)
    if res.empty:
        st.warning("No colleges found for this percentile.")
    else:
        st.dataframe(res)

with tab2:
    st.subheader("📘 Easier (Backup) Colleges")
    res = bk.backup_options(percentile)
    if res.empty:
        st.info("No backup colleges found.")
    else:
        st.dataframe(res)

with tab3:
    st.subheader("📊 All Colleges & Cutoffs")
    st.dataframe(bk.show_all())

with tab4:
    st.subheader("📈 Yearly Cutoff Trends (Bar Graph)")
    trend = bk.get_full_trend_data()

    # Let user pick a college
    college_choice = st.selectbox("Select College:", ['DTU', 'NSIT', 'IIIT Delhi', 'IGDTUW'])

    # Create bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(trend['Year'], trend[college_choice], color='teal')

    ax.set_title(f"{college_choice} Cutoff Trend (2015–2027)", fontsize=14)
    ax.set_xlabel("Year")
    ax.set_ylabel("Cutoff Percentile")
    ax.set_ylim(60, 100)  # restrict Y-axis
    ax.set_xlim(2015, 2027)  # restrict X-axis range
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    st.pyplot(fig)

st.markdown("---")
st.caption("Developed by Ritesh Pathak | Subject: AI (843) | Guide Ms. Pooja & Ms. Deepshikha")

st.sidebar.title("🎓 DU College Recommender")
st.sidebar.markdown("💬 Find your best Delhi University colleges based on JEE percentile!!")
st.sidebar.markdown("""
 **Team Members**
- Ritesh Pathak (Programmer)
- Eshan Awasthi (Assistant Programmer)
- Pratyush Singh (File Management)
- Aditi Mishra (File Management)
- Ryan Naqvi (Useless)

 **Class:** 12th
 **School:** AMITY INTERNATIONAL SCHOOL, MAYUR VIHAR PHASE-1, DELHI-110091
 
 **Description:**  
 This AI project analyzes JEE percentile data to recommend the most suitable Delhi Engineering colleges for BTECH and predicts next year’s cutoff using Linear Regression.  
 It features an interactive frontend built using Streamlit.

""")

