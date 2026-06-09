import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_segmentation():
    df = pd.read_csv("dataset/customers.csv")

    X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    return df