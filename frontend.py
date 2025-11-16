import streamlit as st
import backend as bk
import altair as alt

st.set_page_config(page_title="College Recommendation System", layout="wide")

st.title("Delhi College Recommendation System")
st.write("This tool recommends Delhi engineering colleges based on your JEE percentile.")

# User input
percentile = st.slider("Enter your JEE Percentile", 60, 100, 85)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Best Matches",
    "Additional Options",
    "All Colleges",
    "Cutoff Trend"
])

# Tab 1: Exact or closest matches (Top 20)
with tab1:
    st.subheader("Top 20 Best Match Colleges & Branches")
    result = bk.best_suited(percentile)
    if not result.empty:
        st.dataframe(result.reset_index(drop=True), use_container_width=True)
        st.caption("Showing up to 20 exact or closest matches for your percentile.")
    else:
        st.warning("No exact or close matches found.")

# Tab 2: Additional options (Top 30 below percentile)
with tab2:
    st.subheader("Top 30 Additional Suggestions")
    result = bk.additional_options(percentile)
    st.dataframe(result.reset_index(drop=True), use_container_width=True)
    st.caption("These cutoffs are slightly below your percentile.")

# Tab 3: All data
with tab3:
    st.subheader("All Colleges with 2025 Cutoffs")
    st.dataframe(bk.show_all_cutoffs(), use_container_width=True)

# Tab 4: Static (non-resizing) line graph for JEE trend
with tab4:
    st.subheader("JEE Advanced Cutoff Trend (2015–2025)")
    trend = bk.get_trend_data()

    chart = (
        alt.Chart(trend)
        .mark_line(point=True, color="steelblue")
        .encode(
            x=alt.X("Year:O", title="Year"),
            y=alt.Y("Cutoff_Percentile:Q", title="Cutoff Percentile (80–100)", scale=alt.Scale(domain=[80, 100])),
            tooltip=["Year", "Cutoff_Percentile"]
        )
        .properties(width=700, height=400, title="JEE Advanced Cutoff Trend")
        .configure_title(fontSize=16, anchor="middle")
        .configure_axis(labelFontSize=12, titleFontSize=13)
    )

    st.altair_chart(chart, use_container_width=False)

# Footer
st.markdown("""
Project by Class 12 Students  
Subject: Artificial Intelligence (843)
""")

# Sidebar
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
This AI project suggests best-suited Delhi engineering colleges based on JEE percentile and shows cutoff trends using Streamlit.
""")

