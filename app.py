import streamlit as st
import pandas as pd

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Delhivery Logistics Intelligence",
    layout="wide"
)

# ---------------------------------
# LOAD DATA
# ---------------------------------

hub_audit = pd.read_csv("data/hub_audit.csv")
corridor_breach = pd.read_csv("data/corridor_breach.csv")
final_recommendations = pd.read_csv("data/final_recommendations.csv")

# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Network Analysis",
        "FTL vs Carting",
        "Business Impact"
    ]
)

# =================================
# OVERVIEW
# =================================

if page == "Overview":

    st.title("Delhivery Logistics Intelligence System")

    st.markdown(
        """
        Graph-based network intelligence framework for:
        - ETA Optimization
        - Bottleneck Detection
        - Corridor Analysis
        - FTL vs Carting Recommendations
        """
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Nodes", "1657")
    col2.metric("Edges", "2783")
    col3.metric("Graph ETA MAE", "35.76")
    col4.metric("Revenue Recovery", "₹1.12 Cr")

# =================================
# NETWORK ANALYSIS
# =================================

elif page == "Network Analysis":

    st.title("Network Analysis")

    st.subheader("Top Bottleneck Hubs")

    st.dataframe(
        hub_audit.sort_values(
            "bottleneck_score",
            ascending=False
        ).head(10)
    )

    st.bar_chart(
        hub_audit
        .sort_values(
            "bottleneck_score",
            ascending=False
        )
        .head(10)
        .set_index("hub")["bottleneck_score"]
    )

    st.subheader("Top Delayed Corridors")

    st.dataframe(
        corridor_breach
        .sort_values(
            "sla_breach_contribution",
            ascending=False
        )
        .head(10)
    )

    st.bar_chart(
        corridor_breach
        .sort_values(
            "sla_breach_contribution",
            ascending=False
        )
        .head(10)
        .set_index("source_center")[
            "sla_breach_contribution"
        ]
    )

# =================================
# FTL VS CARTING
# =================================

elif page == "FTL vs Carting":

    st.title("FTL vs Carting Recommendation Framework")

    st.markdown(
        """
        The ML framework recommends whether a corridor
        should use FTL or Carting based on:

        - Distance
        - Historical Delay
        - Shipment Volume
        - Network Centrality
        - Corridor Characteristics
        """
    )

    st.subheader("Sample Corridor Recommendations")

    st.dataframe(
        final_recommendations.head(20)
    )

# =================================
# BUSINESS IMPACT
# =================================

elif page == "Business Impact":

    st.title("Business Impact")

    col1, col2 = st.columns(2)

    col1.metric(
        "Top 3 Hub Breach Contribution",
        "40.67%"
    )

    col2.metric(
        "Late Delivery Reduction",
        "8.13%"
    )

    st.metric(
        "Revenue Recovered",
        "₹1.12 Cr"
    )

    st.markdown("---")

    st.subheader("Strategy Recommendations")

    st.markdown(
        """
        ### Top Bottleneck Hubs

        1. IND000000ACB
        2. IND562132AAA
        3. IND501359AAE
        4. IND160002AAC
        5. IND712311AAA

        ### Recommended Actions

        - Facility Upgrade at IND000000ACB
        - Parallel Routing near IND562132AAA
        - FTL Shift on high-delay corridors
        - Capacity Expansion at major bottlenecks

        ### Expected Outcome

        - 8.13% reduction in late deliveries
        - ₹1.12 Cr revenue recovered
        """
    )