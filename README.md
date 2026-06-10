AI-Driven Customer Segmentation and Analytics System
WEBLINK: https://project-1-ai-driven-2.onrender.com
📌 Project Overview

The AI-Driven Customer Segmentation and Analytics System is a machine learning-powered application that helps businesses analyze customer behavior, identify customer segments, predict churn risk, estimate purchase likelihood, and generate personalized recommendations.

The system uses K-Means Clustering for customer segmentation and XGBoost for predictive analytics. An interactive dashboard built with Streamlit provides real-time visualizations and insights for business decision-making.

🎯 Problem Statement

Businesses often struggle to understand customer behavior from large datasets. Traditional analytics provide static reports and fail to deliver actionable insights.

This project addresses these challenges by:

Segmenting customers into meaningful groups
Predicting customer churn
Predicting purchase behavior
Providing recommendation insights
Visualizing customer trends through an interactive dashboard
🚀 Features
🧠 Customer Segmentation
Uses K-Means Clustering
Groups customers based on:
Age
Annual Income
Spending Score

📊 Interactive Dashboard
Customer overview metrics
Income and spending analysis
Age distribution visualization
Cluster visualization

⚠️ Churn Prediction
Uses XGBoost Classifier
Predicts customer churn risk
Displays churn probability
🛒 Purchase Prediction
Estimates customer purchase likelihood
Uses machine learning-based scoring

🎯 Recommendation System
Generates product recommendations
Helps improve customer engagement

📈 Data Visualization
Interactive Plotly charts
Responsive dashboard
Customer segment analysis

🛠️ Technologies Used
Technology	Purpose
Python	Backend Development
Streamlit	User Interface
Pandas	Data Processing
NumPy	Numerical Computation
Scikit-Learn	Machine Learning
XGBoost	Predictive Modeling
Plotly	Interactive Visualization
Joblib	Model Serialization

📂 Project Structure
project/
│
├── app.py
│
├── dataset/
│   └── customers.csv
│
├── models/
│   ├── segmentation.py
│   ├── churn_prediction.py
│   ├── purchase_prediction.py
│   ├── recommendation.py
│   ├── train_models.py
│   ├── xgb_model.pkl
│   └── scaler.pkl
│
├── static/
│   └── css/
│       └── style.css
│
├── requirements.txt
│
└── README.md
⚙️ Machine Learning Models
1. Customer Segmentation

Algorithm:

K-Means Clustering

Features:

Age
Annual Income
Spending Score

Output:

Customer Cluster Assignment
2. Churn Prediction

Algorithm:

XGBoost Classifier

Features:

Age
Annual Income
Spending Score

Output:

High Risk
Medium Risk
Low Risk
3. Recommendation System

Recommendation engine suggests products based on customer profiles and behavioral patterns.

📊 Dashboard Components
KPI Cards
Total Customers
Average Income
Average Spending Score
High-Risk Customers
Charts
Customer Distribution
Income vs Spending Analysis
Age Distribution
Customer Segmentation Plot
Tables
Customer Dataset
Clustered Customer Data

📁 Dataset Description

The dataset contains:

Column	Description
CustomerID	Unique customer identifier
CustomerName	Customer name
Age	Customer age
Annual Income (k$)	Annual income
Spending Score (1-100)	Spending behavior score

Example:

CustomerID,CustomerName,Age,Annual Income (k$),Spending Score (1-100)
1,Aarav,21,22,21
2,Vihaan,24,29,32
3,Aditya,27,36,43

📈 Workflow
Customer Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
K-Means Clustering
        │
        ▼
Customer Segments
        │
        ▼
XGBoost Prediction
        │
        ├── Churn Prediction
        │
        └── Purchase Prediction
        │
        ▼
Recommendation Engine
        │
        ▼
Streamlit Dashboard

🎯 Benefits
Better customer understanding
Improved marketing strategies
Increased customer retention
Data-driven business decisions
Personalized customer engagement
Revenue growth opportunities

🔮 Future Enhancements
Real-time data integration
Customer Lifetime Value (CLV) prediction
Deep Learning-based recommendation system
Automated model retraining
Cloud deployment
Power BI integration
Advanced analytics dashboard

👩‍💻 Author

Rajeswari Kakumanu

Project Title
AI-Driven Customer Segmentation and Analytics System Using K-Means Clustering and XGBoost
