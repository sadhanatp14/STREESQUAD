import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.metrics import r2_score

# ==============================
# PATHS
# ==============================
DATA_PATH = "DATA/SYNTHETIC/SHGMASTERDATASET.csv"
MODEL_PATH = "BACKEND/APP/MODELS/"

os.makedirs(MODEL_PATH, exist_ok=True)

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded:", df.shape)

# ==============================
# COMMON CLEANING
# ==============================
df.fillna(0, inplace=True)

# ==============================
# FEATURE GROUPS
# ==============================

FINANCIAL_FEATURES = [
    "AVG_MONTHLY_SAVINGS",
    "SAVINGS_STD",
    "SAVINGS_REGULARITY_PCT",
    "EMI_MISS_RATE",
    "AVG_REPAYMENT_DELAY"
]

STABILITY_FEATURES = [
    "ATTENDANCE_AVG",
    "ATTENDANCE_STD",
    "MEMBER_DROPOUT_RATE",
    "MEETING_REGULARITY",
    "LEADERSHIP_CHANGES"
]

GROWTH_FEATURES = [
    "SAVINGS_GROWTH_RATE",
    "LOAN_UTILIZATION_SCORE",
    "LOAN_TO_SAVINGS_RATIO",
    "INCOME_STABILITY_PROXY"
]

BEHAVIOR_FEATURES = [
    "SUDDEN_SAVINGS_JUMP",
    "ATTENDANCE_DROP_FLAG",
    "PAST_DEFAULT_FLAG"
]

# ==============================
# TARGETS
# ==============================

TARGET_FINANCIAL = "FINANCIAL_DISCIPLINE_SCORE"
TARGET_STABILITY = "STABILITY_SCORE"
TARGET_GROWTH = "GROWTH_READINESS_SCORE"

# ==============================
# TRAIN FUNCTION
# ==============================
def train_regression_model(X, y, name):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=6,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(f"{name} R2 Score:", round(r2_score(y_test, preds), 3))

    joblib.dump(model, f"{MODEL_PATH}/{name}.pkl")
    print(f"Saved: {name}.pkl")


# ==============================
# MODEL 1: FINANCIAL DISCIPLINE
# ==============================
train_regression_model(
    df[FINANCIAL_FEATURES],
    df[TARGET_FINANCIAL],
    "FINANCIALDISCIPLINE"
)

# ==============================
# MODEL 2: STABILITY
# ==============================
train_regression_model(
    df[STABILITY_FEATURES],
    df[TARGET_STABILITY],
    "STABILITY"
)

# ==============================
# MODEL 3: GROWTH READINESS
# ==============================
train_regression_model(
    df[GROWTH_FEATURES],
    df[TARGET_GROWTH],
    "GROWTH"
)

# ==============================
# MODEL 4: BEHAVIORAL SAFETY
# ==============================
behavior_model = IsolationForest(
    n_estimators=150,
    contamination=0.1,
    random_state=42
)

behavior_model.fit(df[BEHAVIOR_FEATURES])

joblib.dump(behavior_model, f"{MODEL_PATH}/BEHAVIOR.pkl")
print("Saved: BEHAVIOR.pkl")

print("✅ ALL MODELS TRAINED AND SAVED SUCCESSFULLY")