import streamlit as st
import pandas as pd
import plotly.express as px

from models.segmentation import run_segmentation
from models.churn_prediction import predict_churn
from models.purchase_prediction import predict_purchase
from models.recommendation import get_recommendations
def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.set_page_config(page_title="AI Customer Intelligence",
                    layout="wide",
                    initial_sidebar_state="expanded"
                    )

st.title("🧠 AI-Driven Customer Segmentation System")

# Load dataset
df = pd.read_csv("dataset/customers.csv")

# Sidebar menu
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Customers", "Segmentation", "Prediction", "Recommendation"]
)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.title("📊 AI Customer Intelligence Dashboard")

    df = pd.read_csv("dataset/customers.csv")

    # ---------------- KPI METRICS ----------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Total Customers", len(df))

    with col2:
        st.metric("💰 Avg Income", round(df["Annual Income (k$)"].mean(), 2))

    with col3:
        st.metric("🛒 Avg Spending", round(df["Spending Score (1-100)"].mean(), 2))

    with col4:
        high_risk = len(df[df["Spending Score (1-100)"] < 40])
        st.metric("⚠️ High Risk", high_risk)

    st.markdown("---")

    # ---------------- CHART 1 ----------------
    st.subheader("📈 Income vs Spending Pattern")

    fig1 = px.scatter(
        df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color="Age",
        size="Age",
        title="Customer Segmentation View"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ---------------- CHART 2 ----------------
    st.subheader("📊 Age Distribution")

    fig2 = px.histogram(
        df,
        x="Age",
        nbins=10,
        title="Customer Age Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- CUSTOMERS ----------------
elif menu == "Customers":
    st.subheader("📋 Customer Data")
    st.dataframe(df)

# ---------------- SEGMENTATION ----------------
elif menu == "Segmentation":
    st.subheader("🧠 Customer Segmentation (K-Means)")

    clustered_df = run_segmentation()

    fig = px.scatter(
        clustered_df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color="Cluster",
        title="Customer Clusters"
    )

    st.plotly_chart(fig)
    st.dataframe(clustered_df)

# ---------------- PREDICTION ----------------
elif menu == "Prediction":
    st.subheader("🔮 XGBoostPrediction System")

    age = st.number_input("Age", 18, 100)
    income = st.number_input("Annual Income", 10, 200)
    score = st.number_input("Spending Score", 1, 100)

    if st.button("Predict Churn(XGBoost)"):
        from models.churn_prediction import predict_churn
        result = predict_churn(age, income, score)
        st.success(result)

# ---------------- RECOMMENDATION ----------------
elif menu == "Recommendation":
    st.subheader("🎯 Recommendation Engine")

    cid = st.text_input("Customer ID")

    if st.button("Get Recommendations"):
        result = get_recommendations(cid)
        for item in result:
            st.write("✔", item)