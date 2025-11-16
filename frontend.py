import streamlit as st
import backend as bk
import altair as alt

st.set_page_config(page_title="Delhi College Rec System", layout="wide")

st.title("Delhi College Recommendation System")
st.write("Suggests colleges based on your JEE percentile.")

percentile = st.slider("Select Your JEE Percentile", 80, 100, 90)


tab1, tab2, tab3, tab4 = st.tabs(["Best Matches","Additional Options","All Colleges","Cutoff Trend"])


# ----------------- TAB 1 -------------------
with tab1:
    st.subheader("Best Matches for Your Percentile")
    result = bk.best_suited(percentile)

    if result is not None and not result.empty:
        st.dataframe(result.reset_index(drop=True), use_container_width=True)
    else:
        st.warning("No matching colleges found for this percentile.")


# ----------------- TAB 2 -------------------
with tab2:
    st.subheader("Additional Options")
    result = bk.additional_options(percentile)
    st.dataframe(result.reset_index(drop=True), use_container_width=True)


# ----------------- TAB 3 -------------------
with tab3:
    st.subheader("All Colleges Cutoffs")
    st.dataframe(bk.show_all_cutoffs(), use_container_width=True)


# ----------------- TAB 4 -------------------
with tab4:
    st.subheader("JEE Advanced Cutoff Trend (2015–2025)")

    trend = bk.get_trend_data()

    chart = (
        alt.Chart(trend)
        .mark_line(point=True)
        .encode(
            x=alt.X("Year:O", title="Year"),
            y=alt.Y("Cutoff_Percentile:Q", 
                    title="Percentile (80-100)", 
                    scale=alt.Scale(domain=[80,100])),
            tooltip=["Year", "Cutoff_Percentile"]
        )
        .properties(width=700, height=400, title="Cutoff Trend")
    )

    st.altair_chart(chart, use_container_width=False)


# ----------------- Footer -------------------
st.markdown("Project by Class 12 Students. Subject: Artificial Intelligence (843)")

st.sidebar.title("Project Info")
st.sidebar.markdown("""
**Team Members**  
- Ritesh Pathak  
- Eshan Awasthi  
- Pratyush Singh  
- Aditi Mishra  
- Ryan Naqvi

**School:** AMITY INTERNATIONAL SCHOOL, MAYUR VIHAR, DELHI -110091
""")
