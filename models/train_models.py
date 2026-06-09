import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import joblib

df = pd.read_csv("dataset/customers.csv")

# Create a target column for demo purposes
df["Churn"] = (df["Spending Score (1-100)"] < 40).astype(int)

X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    eval_metric="logloss"
)

model.fit(X_train_scaled, y_train)

joblib.dump(model, "models/xgb_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model saved successfully!")