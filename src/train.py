# src/train.py
import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("data/student_data.csv")

X = df[["age", "studytime", "absences", "G1", "G2"]]
y = df["G3"]

# Identify column types
numeric_features = X.select_dtypes(include=["int64", "float64"]).columns
categorical_features = X.select_dtypes(include=["object"]).columns

# Preprocessing
numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# Full Pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Hyperparameter tuning
param_grid = {
    "regressor__n_estimators": [100, 200],
    "regressor__max_depth": [None, 10, 20]
}

grid = GridSearchCV(model, param_grid, cv=5, scoring="r2")
grid.fit(X_train, y_train)

# Evaluate
y_pred = grid.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
save_path = "../student-performance-ml/models/student_model.pkl"

print("Current working directory:", os.getcwd())
print("Saving to:", os.path.abspath(save_path))

joblib.dump(grid.best_estimator_, save_path)
print("Model saved successfully!")