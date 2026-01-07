import numpy as np

# ======================================================
# UTILITY FUNCTIONS
# ======================================================

def safe_mean(values):
    if not values or len(values) == 0:
        return 0.0
    return float(np.mean(values))


def safe_std(values):
    if not values or len(values) == 0:
        return 0.0
    return float(np.std(values))


def clamp(value, min_val=0, max_val=100):
    return max(min(value, max_val), min_val)


# ======================================================
# FINANCIAL DISCIPLINE FEATURES
# ======================================================

def compute_financial_features(raw):
    """
    Expected raw keys:
    - monthly_savings (list)
    - emi_missed (int)
    - repayment_delay_days (list)
    """

    savings = raw.get("monthly_savings", [])
    missed_emi = raw.get("emi_missed", 0)
    delays = raw.get("repayment_delay_days", [])

    avg_savings = safe_mean(savings)
    savings_std = safe_std(savings)

    regular_months = sum(1 for s in savings if s > 0)
    savings_regularity_pct = (regular_months / max(len(savings), 1)) * 100

    emi_miss_rate = missed_emi / max(len(savings), 1)
    avg_repayment_delay = safe_mean(delays)

    return {
        "AVG_MONTHLY_SAVINGS": avg_savings,
        "SAVINGS_STD": savings_std,
        "SAVINGS_REGULARITY_PCT": clamp(savings_regularity_pct),
        "EMI_MISS_RATE": clamp(emi_miss_rate * 100),
        "AVG_REPAYMENT_DELAY": avg_repayment_delay
    }


# ======================================================
# STABILITY FEATURES
# ======================================================

def compute_stability_features(raw):
    """
    Expected raw keys:
    - attendance_pct (list)
    - member_dropouts (int)
    - group_size (int)
    - meeting_frequency (int)
    - leadership_changes (int)
    """

    attendance = raw.get("attendance_pct", [])
    dropouts = raw.get("member_dropouts", 0)
    group_size = max(raw.get("group_size", 1), 1)

    attendance_avg = safe_mean(attendance)
    attendance_std = safe_std(attendance)

    dropout_rate = dropouts / group_size
    meeting_regularity = raw.get("meeting_frequency", 0)
    leadership_changes = raw.get("leadership_changes", 0)

    return {
        "ATTENDANCE_AVG": clamp(attendance_avg),
        "ATTENDANCE_STD": attendance_std,
        "MEMBER_DROPOUT_RATE": clamp(dropout_rate * 100),
        "MEETING_REGULARITY": meeting_regularity,
        "LEADERSHIP_CHANGES": leadership_changes
    }


# ======================================================
# GROWTH READINESS FEATURES
# ======================================================

def compute_growth_features(raw):
    """
    Expected raw keys:
    - monthly_savings (list)
    - total_loan_taken (float)
    - income_proxy (list)
    """

    savings = raw.get("monthly_savings", [])
    total_loan = raw.get("total_loan_taken", 0)
    income = raw.get("income_proxy", [])

    if len(savings) > 1:
        growth_rate = (savings[-1] - savings[0]) / max(savings[0], 1)
    else:
        growth_rate = 0

    loan_utilization_score = 1 if total_loan > 0 else 0
    loan_to_savings_ratio = total_loan / max(sum(savings), 1)

    income_stability = 100 - safe_std(income)

    return {
        "SAVINGS_GROWTH_RATE": clamp(growth_rate * 100),
        "LOAN_UTILIZATION_SCORE": loan_utilization_score * 100,
        "LOAN_TO_SAVINGS_RATIO": clamp(loan_to_savings_ratio * 100),
        "INCOME_STABILITY_PROXY": clamp(income_stability)
    }


# ======================================================
# BEHAVIORAL SAFETY FEATURES
# ======================================================

def compute_behavior_features(raw):
    """
    Expected raw keys:
    - monthly_savings (list)
    - attendance_pct (list)
    - past_default (bool)
    """

    savings = raw.get("monthly_savings", [])
    attendance = raw.get("attendance_pct", [])

    sudden_savings_jump = 1 if len(savings) > 1 and savings[-1] > 2 * savings[-2] else 0
    attendance_drop = 1 if len(attendance) > 1 and attendance[-1] < 0.7 * attendance[-2] else 0
    past_default_flag = 1 if raw.get("past_default", False) else 0

    return {
        "SUDDEN_SAVINGS_JUMP": sudden_savings_jump,
        "ATTENDANCE_DROP_FLAG": attendance_drop,
        "PAST_DEFAULT_FLAG": past_default_flag
    }


# ======================================================
# MASTER FEATURE PIPELINE
# ======================================================

def build_feature_vector(raw_input):
    """
    Combines all feature groups into one dict
    """

    features = {}
    features.update(compute_financial_features(raw_input))
    features.update(compute_stability_features(raw_input))
    features.update(compute_growth_features(raw_input))
    features.update(compute_behavior_features(raw_input))

    return features
