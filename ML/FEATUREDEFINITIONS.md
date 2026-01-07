# ✅ STEP 2: FEATURE DEFINITIONS

This file is **EXTREMELY IMPORTANT**.

Judges use this to decide:

* Whether your model is **just numbers**
* Or **financially grounded**

This goes into:

```
ML/FEATUREDEFINITIONS.md
```

You can **copy-paste this entire content**.

---

# 📘 FEATURE DEFINITIONS

## SHG Credit Health & Loan Readiness System

---

## 1️⃣ SHG PROFILE FEATURES

| Feature Name   | Description              | Source    | Why It Matters             |
| -------------- | ------------------------ | --------- | -------------------------- |
| SHG_ID         | Unique identifier of SHG | Synthetic | Entity tracking            |
| REGION         | Geographic region        | Synthetic | Peer comparison            |
| FORMATION_YEAR | Year SHG was formed      | Synthetic | Stability proxy            |
| SHG_AGE_YEARS  | Years since formation    | Derived   | Older SHGs are more stable |
| GROUP_SIZE     | Number of members        | Synthetic | Risk diversification       |
| BANK_LINKED    | Whether linked to bank   | Synthetic | Credit readiness           |

---

## 2️⃣ FINANCIAL DISCIPLINE FEATURES

| Feature Name           | Description             | Source     | Why It Matters           |
| ---------------------- | ----------------------- | ---------- | ------------------------ |
| AVG_MONTHLY_SAVINGS    | Average monthly savings | Synthetic  | Core repayment capacity  |
| SAVINGS_STD            | Variability in savings  | Engineered | Irregular savings = risk |
| SAVINGS_REGULARITY_PCT | % months saved          | Synthetic  | Discipline indicator     |
| TOTAL_INTERNAL_LENDING | Loans within SHG        | Synthetic  | Credit behavior          |
| EMI_MISS_RATE          | % EMIs missed           | Synthetic  | Default risk             |
| AVG_REPAYMENT_DELAY    | Avg days delayed        | Synthetic  | Liquidity stress         |

📌 **Used in:** Financial Discipline Model

---

## 3️⃣ GROUP STABILITY & CONTINUITY FEATURES

| Feature Name        | Description            | Source     | Why It Matters     |
| ------------------- | ---------------------- | ---------- | ------------------ |
| ATTENDANCE_AVG      | Avg meeting attendance | Synthetic  | Engagement         |
| ATTENDANCE_STD      | Attendance variability | Engineered | Inconsistency risk |
| MEMBER_DROPOUT_RATE | % members leaving      | Synthetic  | Group instability  |
| MEETING_REGULARITY  | Meetings held (%)      | Synthetic  | Governance quality |
| LEADERSHIP_CHANGES  | Leader changes         | Synthetic  | Control risk       |

📌 **Used in:** Stability Scoring

---

## 4️⃣ GROWTH READINESS FEATURES

| Feature Name           | Description           | Source    | Why It Matters          |
| ---------------------- | --------------------- | --------- | ----------------------- |
| SAVINGS_GROWTH_RATE    | YoY savings growth    | Synthetic | Capacity expansion      |
| LOAN_UTILIZATION_SCORE | Loan usage efficiency | Synthetic | Productive usage        |
| LOAN_TO_SAVINGS_RATIO  | Debt load             | Derived   | Over-leverage detection |
| INCOME_STABILITY_PROXY | Income consistency    | Synthetic | Cashflow predictability |

📌 **Used in:** Growth Readiness Model

---

## 5️⃣ BEHAVIORAL SAFETY FEATURES

| Feature Name         | Description             | Source     | Why It Matters     |
| -------------------- | ----------------------- | ---------- | ------------------ |
| ANOMALY_SCORE        | Unusual behavior index  | Engineered | Fraud / misuse     |
| SUDDEN_SAVINGS_JUMP  | Sharp change flag       | Synthetic  | Data manipulation  |
| ATTENDANCE_DROP_FLAG | Attendance anomaly      | Synthetic  | Internal conflict  |
| PAST_DEFAULT_FLAG    | Prior default indicator | Synthetic  | Strong risk signal |

📌 **Used in:** Anomaly Detection

---

## 6️⃣ TARGET VARIABLES (For Training)

| Target Name                | Meaning                      |
| -------------------------- | ---------------------------- |
| FINANCIAL_DISCIPLINE_SCORE | Payment & savings discipline |
| STABILITY_SCORE            | Group continuity strength    |
| GROWTH_READINESS_SCORE     | Ability to scale credit      |
| BEHAVIORAL_SAFETY_SCORE    | Risk-free behavior           |
| FINAL_CREDIT_SCORE         | Composite readiness score    |

📌 **Note:** Final score is **advisory only**, not automated approval.

---

## 7️⃣ LEGAL & ETHICAL NOTES

✔ No individual PII
✔ Group-level analytics only
✔ Advisory output
✔ Explainable scores
✔ No automated lending decision

---

## 🎯 WHY JUDGES LIKE THIS FILE

* Financial logic ✔
* Clear causality ✔
* Transparency ✔
* Legal safety ✔
* Break-phase defensibility ✔

---




