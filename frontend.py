import streamlit as st
import backend as bk

st.set_page_config(page_title="College Recommendation System", layout="wide")

st.title("Delhi College Recommendation System")
st.write("This tool suggests Delhi engineering colleges based on your JEE percentile.")

# User input
percentile = st.slider("Enter your JEE Percentile", 60, 100, 85)

# Navigation
tab1, tab2, tab3, tab4 = st.tabs([
    "Best Matches",
    "Additional Options",
    "All Colleges",
    "Cutoff Trend"
])

# Tab 1: Best matches
with tab1:
    st.subheader("Best Options for Your Percentile")
    result = bk.best_suited(percentile)
    st.dataframe(result, use_container_width=True)

# Tab 2: Additional options
with tab2:
    st.subheader("Other Nearby Options")
    result = bk.additional_options(percentile)
    st.dataframe(result, use_container_width=True)

# Tab 3: All colleges data
with tab3:
    st.subheader("All Colleges with 2025 Cutoffs")
    st.dataframe(bk.show_all_cutoffs(), use_container_width=True)

# Tab 4: Cutoff trend visualization
with tab4:
    st.subheader("JEE Advanced Cutoff Trend (2015–2025)")
    trend = bk.get_trend_data().sort_values(by="Year")
    st.line_chart(trend.set_index("Year")["Cutoff_Percentile"], height=400)
    st.caption("Displays JEE Advanced cutoff percentiles (2015–2025).")

# Footer
st.markdown("""
Project by Class 12 Students  
Subject: Artificial Intelligence (843)
""")

# Sidebar info
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
This AI project analyzes JEE percentile data to recommend suitable Delhi engineering colleges for B.Tech and visualizes cutoff trends using Streamlit.
""")
