
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="VoltRelay Network Performance",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("VoltRelay_Q1_Submission.csv")

df["month"] = pd.to_datetime(df["month"])

# -----------------------------
# Title
# -----------------------------
st.title("⚡ VoltRelay Network Performance Dashboard")

st.markdown(
    "### Q1 — Network Performance Over Time"
)

st.caption(
    "Analysis period: January 2024 – June 2025"
)

# -----------------------------
# KPI calculations
# -----------------------------
total_swaps = df["completed_swaps"].sum()
total_revenue = df["revenue"].sum()
average_failure = df["failure_rate"].mean()
latest_margin = df.iloc[-1]["contribution_margin_per_swap"]

# -----------------------------
# KPI cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Completed Swaps",
        f"{total_swaps:,.0f}"
    )

with col2:
    st.metric(
        "Total Revenue",
        f"₹{total_revenue:,.0f}"
    )

with col3:
    st.metric(
        "Average Failure Rate",
        f"{average_failure:.2f}%"
    )

with col4:
    st.metric(
        "Latest Margin / Swap",
        f"₹{latest_margin:.2f}"
    )

st.divider()

# -----------------------------
# Completed swaps
# -----------------------------
st.subheader("1. Completed Swaps Over Time")

fig1 = px.line(
    df,
    x="month",
    y="completed_swaps",
    markers=True,
    labels={
        "month": "Month",
        "completed_swaps": "Completed Swaps"
    }
)

fig1.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -----------------------------
# Revenue
# -----------------------------
st.subheader("2. Revenue Over Time")

fig2 = px.line(
    df,
    x="month",
    y="revenue",
    markers=True,
    labels={
        "month": "Month",
        "revenue": "Revenue (INR)"
    }
)

fig2.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------------
# Failure rate
# -----------------------------
st.subheader("3. Failure Rate Over Time")

fig3 = px.line(
    df,
    x="month",
    y="failure_rate",
    markers=True,
    labels={
        "month": "Month",
        "failure_rate": "Failure Rate (%)"
    }
)

fig3.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -----------------------------
# Contribution margin
# -----------------------------
st.subheader("4. Contribution Margin per Swap")

fig4 = px.line(
    df,
    x="month",
    y="contribution_margin_per_swap",
    markers=True,
    labels={
        "month": "Month",
        "contribution_margin_per_swap":
            "Contribution Margin / Swap (INR)"
    }
)

fig4.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# -----------------------------
# Key findings
# -----------------------------
st.divider()

st.subheader("Key Findings")

st.markdown("""
- Completed swaps increased substantially during the analysis period.
- Monthly revenue increased alongside network activity.
- Failure rates were generally around 2.6–2.7% in many months, with noticeable spikes in selected periods.
- Contribution margin per completed swap increased over the analysis period.
""")

# -----------------------------
# Monthly data
# -----------------------------
with st.expander("View Monthly Data"):
    display_df = df.copy()
    display_df["month"] = display_df["month"].dt.strftime("%Y-%m")
    st.dataframe(
        display_df,
        use_container_width=True
    )
