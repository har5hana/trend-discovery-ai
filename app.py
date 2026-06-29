import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="Trend Discovery AI",
    page_icon="⭐️",
    layout="wide"
)

st.title("Trend Discovery AI")
st.caption("All current trends around the world" \
"")

# --------------------------------
# DATABASE CONNECTION
# --------------------------------
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TrendDiscoveryAI;"
    "Trusted_Connection=yes;"
)

# --------------------------------
# LOAD DATA
# --------------------------------
trends_df = pd.read_sql("""
SELECT *
FROM Trends
ORDER BY Frequency DESC
""", conn)

articles_df = pd.read_sql("""
SELECT TOP 50 *
FROM NewsArticles
ORDER BY Id DESC
""", conn)

# --------------------------------
# SIDEBAR
# --------------------------------
st.sidebar.title("⚙ Filters")

source_filter = st.sidebar.selectbox(
    "Source",
    ["All Sources", "Google News"]
)

refresh = st.sidebar.button("🔄 Refresh Data")

# --------------------------------
# KPI CARDS
# --------------------------------
total_articles = len(articles_df)

total_trends = len(trends_df)

top_keyword = (
    trends_df.iloc[0]["Keyword"]
    if not trends_df.empty
    else "N/A"
)

avg_frequency = (
    round(trends_df["Frequency"].mean(), 2)
    if not trends_df.empty
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Articles",
    total_articles
)

col2.metric(
    "Keywords",
    total_trends
)

col3.metric(
    "Top Trend",
    top_keyword
)

col4.metric(
    "Avg Score",
    avg_frequency
)

st.divider()

# --------------------------------
# TREND CHART
# --------------------------------
st.subheader("Top Trending Topics")

top_trends = trends_df.head(15)

fig = px.bar(
    top_trends,
    x="Keyword",
    y="Frequency",
    text="Frequency"
)

fig.update_layout(
    height=500,
    xaxis_title="Keyword",
    yaxis_title="Frequency"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------
# TOP KEYWORDS TABLE
# --------------------------------
col_left, col_right = st.columns([1, 1])

with col_left:

    st.subheader("Top Keywords")

    st.dataframe(
        top_trends,
        use_container_width=True
    )

with col_right:

    st.subheader("Top 10 Keywords")

    keyword_counts = top_trends[
        ["Keyword", "Frequency"]
    ].copy()

    st.dataframe(
        keyword_counts,
        use_container_width=True
    )

st.divider()

# --------------------------------
# LATEST HEADLINES
# --------------------------------
st.subheader("Latest Headlines")

display_articles = articles_df[
    ["Title"]
].copy()

st.dataframe(
    display_articles,
    use_container_width=True,
    height=400
)

# --------------------------------
# FOOTER
# --------------------------------
st.markdown("---")
st.caption(
    "By Harshana - \t" \
    "GitHub @har5hana"
)