# ASSUMPTIONS.md

## Project: THEHACKHUB – SHG Credit Health & Loan Readiness System

This document outlines the **assumptions** made while designing the dataset, ML models, scoring logic, and system behavior.
These assumptions are required because **real SHG data is sensitive, fragmented, and not publicly available at scale**.

---

## 1. Definition of a Self Help Group (SHG)

* An SHG is assumed to be a **community-based group of 5–20 members**
* Members meet **at least once per month**
* SHGs practice:

  * Regular savings
  * Internal lending
  * External borrowing (banks / MFIs / government schemes)

---

## 2. Purpose of the System

The system is designed to:

* Evaluate **credit health** of SHGs
* Assess **loan readiness**, not loan approval
* Provide:

  * Risk-aware scoring
  * Explainable insights
  * Improvement recommendations

⚠️ **Final loan sanctioning remains a human decision**

---

## 3. Credit Health Definition

An SHG is considered **credit healthy** if it demonstrates:

1. **Financial Discipline**

   * Regular savings
   * Timely repayments
2. **Group Stability**

   * Consistent participation
   * Low dropout risk
3. **Growth Readiness**

   * Increasing savings
   * Productive loan utilization
4. **Behavioral Safety**

   * Low default probability
   * Stable historical behavior

---

## 4. Time Horizon Assumptions

* Minimum historical data required: **12 months**
* Maximum considered history: **36 months**
* Recent behavior (last 6–12 months) is weighted more heavily than older data

---

## 5. Savings Behavior Assumptions

* Savings are assumed to be:

  * Monthly
  * Fixed or semi-variable
* High variance in savings indicates **financial stress**
* Missed savings > 3 months is considered **high risk**

---

## 6. Loan & Repayment Assumptions

* Loans are assumed to be:

  * Group loans
  * Equal responsibility among members
* EMI delays:

  * ≤ 5 days → acceptable
  * 6–15 days → warning
  * > 15 days → high risk
* Repeated missed installments are stronger risk signals than one-time delays

---

## 7. Meeting & Participation Assumptions

* Meetings occur **monthly**
* Attendance:

  * ≥ 80% → stable group
  * 60–79% → moderate risk
  * < 60% → unstable group
* Irregular meetings reflect **organizational weakness**

---

## 8. Group Stability Assumptions

* Member dropout rate:

  * ≤ 10% annually → stable
  * > 20% annually → unstable
* Older SHGs are assumed to be more stable than newly formed groups

---

## 9. Growth Readiness Assumptions

* Growth is indicated by:

  * Increasing savings trend
  * Efficient loan utilization
  * Ability to absorb higher loan amounts
* Stagnant or declining savings indicates low growth readiness

---

## 10. Behavioral Risk Assumptions

* Past behavior is assumed to be the **best predictor of future risk**
* SHGs with consistent repayment but one-time shocks are **not penalized heavily**
* Sudden behavior changes are treated as risk flags

---

## 11. Data Availability Assumptions

* Real-world data sources (NRLM, NABARD) are:

  * Aggregated
  * Delayed
  * Incomplete
* Therefore:

  * Synthetic data is used for prototyping
  * Feature distributions are designed to resemble realistic rural finance patterns

---

## 12. Data Authenticity Assumptions

* User-entered data is assumed to be **self-reported**
* System mitigates false data by:

  * Logical validation
  * Range checks
  * Trend consistency checks
* Future versions may integrate:

  * Bank APIs
  * Government portals
  * Audit mechanisms

---

## 13. Scoring Interpretation Assumptions

* Scores are normalized to **0–100**
* Score interpretation:

  * 80–100 → Strong credit health
  * 60–79 → Moderate, improvable
  * 40–59 → High risk
  * < 40 → Not loan-ready
* Scores are **advisory**, not deterministic

---

## 14. Scheme Compatibility Assumptions

* Different loan schemes have different eligibility thresholds
* Loan eligibility depends on:

  * Score
  * Loan amount
  * Risk category
* Scheme mapping is rule-based, not ML-based (for transparency)

---

## 15. Ethical & Fairness Assumptions

* The system does **not discriminate** based on:

  * Region
  * Gender
  * Caste
* All decisions are explainable
* SHGs can improve scores through behavior change

---

## 16. Scope Limitations

This prototype does NOT:

* Replace banks or MFIs
* Automatically sanction loans
* Guarantee accuracy on real-world deployment

It **demonstrates feasibility**, transparency, and scalability.

---

## 17. Future Enhancements (Out of Scope)

* Integration with government databases
* Real-time bank transaction ingestion
* Mobile app for SHG members
* Auto-remediation suggestions

---

✅ **This document governs dataset creation, ML training, scoring logic, and UI behavior.**

---



