import pandas as pd
import numpy as np
import random

np.random.seed(42)

NUM_SHGS = 800   # good size for ML + fast training

regions = ["Rural-North", "Rural-South", "Rural-East", "Rural-West"]

data = []

for i in range(NUM_SHGS):
    shg_id = f"SHG_{1000+i}"
    formation_year = random.randint(2012, 2023)
    shg_age = 2024 - formation_year
    group_size = random.randint(8, 20)
    region = random.choice(regions)
    bank_linked = random.choice([0, 1])

    # -------------------------------
    # FINANCIAL DISCIPLINE
    # -------------------------------
    avg_monthly_savings = np.random.normal(2500, 800)
    avg_monthly_savings = max(500, avg_monthly_savings)

    savings_std = np.random.uniform(200, 1200)
    savings_regularity = np.random.uniform(60, 100)

    total_internal_lending = avg_monthly_savings * random.randint(6, 18)

    emi_miss_rate = np.clip(np.random.beta(2, 8), 0, 1)
    avg_repayment_delay = max(0, np.random.normal(4, 6))

    # -------------------------------
    # STABILITY & CONTINUITY
    # -------------------------------
    attendance_avg = np.random.uniform(60, 100)
    attendance_std = np.random.uniform(2, 15)
    member_dropout_rate = np.clip(np.random.beta(1.5, 6), 0, 0.4)
    meeting_regularity = np.random.uniform(70, 100)
    leadership_changes = random.randint(0, 4)

    # -------------------------------
    # GROWTH READINESS
    # -------------------------------
    savings_growth_rate = np.random.uniform(-0.05, 0.35)
    loan_utilization_score = np.random.uniform(40, 100)
    loan_to_savings_ratio = np.random.uniform(0.3, 2.5)
    income_stability_proxy = np.random.uniform(50, 100)

    # -------------------------------
    # BEHAVIORAL SAFETY
    # -------------------------------
    anomaly_score = np.random.uniform(0, 1)
    sudden_savings_jump = random.choice([0, 1])
    attendance_drop_flag = random.choice([0, 1])
    past_default_flag = random.choice([0, 1])

    # -------------------------------
    # SYNTHETIC TARGET SCORES
    # -------------------------------
    financial_discipline_score = np.clip(
        100
        - (emi_miss_rate * 50)
        - (savings_std / 50)
        + (savings_regularity * 0.3),
        0, 100
    )

    stability_score = np.clip(
        attendance_avg
        - (attendance_std * 1.2)
        - (member_dropout_rate * 40)
        - (leadership_changes * 3),
        0, 100
    )

    growth_readiness_score = np.clip(
        (savings_growth_rate * 120)
        + (loan_utilization_score * 0.6)
        - (loan_to_savings_ratio * 8),
        0, 100
    )

    behavioral_safety_score = np.clip(
        100
        - (anomaly_score * 60)
        - (attendance_drop_flag * 15)
        - (past_default_flag * 25),
        0, 100
    )

    final_credit_score = np.clip(
        0.30 * financial_discipline_score
        + 0.25 * stability_score
        + 0.20 * growth_readiness_score
        + 0.15 * behavioral_safety_score
        + 0.10 * np.random.uniform(40, 100),
        0, 100
    )

    data.append([
        shg_id, region, formation_year, shg_age, group_size, bank_linked,
        avg_monthly_savings, savings_std, savings_regularity, total_internal_lending,
        emi_miss_rate, avg_repayment_delay,
        attendance_avg, attendance_std, member_dropout_rate,
        meeting_regularity, leadership_changes,
        savings_growth_rate, loan_utilization_score, loan_to_savings_ratio,
        income_stability_proxy,
        anomaly_score, sudden_savings_jump, attendance_drop_flag, past_default_flag,
        financial_discipline_score, stability_score,
        growth_readiness_score, behavioral_safety_score, final_credit_score
    ])

columns = [
    "SHG_ID", "REGION", "FORMATION_YEAR", "SHG_AGE_YEARS", "GROUP_SIZE", "BANK_LINKED",
    "AVG_MONTHLY_SAVINGS", "SAVINGS_STD", "SAVINGS_REGULARITY_PCT", "TOTAL_INTERNAL_LENDING",
    "EMI_MISS_RATE", "AVG_REPAYMENT_DELAY",
    "ATTENDANCE_AVG", "ATTENDANCE_STD", "MEMBER_DROPOUT_RATE",
    "MEETING_REGULARITY", "LEADERSHIP_CHANGES",
    "SAVINGS_GROWTH_RATE", "LOAN_UTILIZATION_SCORE", "LOAN_TO_SAVINGS_RATIO",
    "INCOME_STABILITY_PROXY",
    "ANOMALY_SCORE", "SUDDEN_SAVINGS_JUMP", "ATTENDANCE_DROP_FLAG", "PAST_DEFAULT_FLAG",
    "FINANCIAL_DISCIPLINE_SCORE", "STABILITY_SCORE",
    "GROWTH_READINESS_SCORE", "BEHAVIORAL_SAFETY_SCORE", "FINAL_CREDIT_SCORE"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("SHGMASTERDATASET.csv", index=False)

print("✅ SHGMASTERDATASET.csv generated successfully!")

