# Caprae Capital Pre-Work Report
## Feature: Lead Scoring & Prioritization

### 🧠 Objective
The task was to identify a valuable feature enhancement for the lead generation tool [saasquatchleads.com](https://www.saasquatchleads.com) and implement it within a 5-hour coding window. I chose to create a **Lead Scoring and Prioritization** feature designed to help sales teams focus on the most valuable leads.

---

### 💡 Why This Feature?
The existing tool gathers leads from various sources, but it doesn't prioritize them. This makes it hard for sales teams to know which leads are most likely to convert. A lead scoring system introduces structure and allows sales reps to focus on **high-impact opportunities first** — improving efficiency and ROI.

---

### 🔍 Scoring Logic Summary

Each lead receives a numeric score based on:
- **Revenue**: Higher revenue = higher score (scaled by millions)
- **Industry**: Certain industries (like Tech, Finance) receive a weight bonus
- **Contact Info**: Leads with both email and phone receive additional score boosts


score = (revenue / 1_000_000) + industry_weight + contact_info_score

The leads are then sorted in descending order of score to surface the best opportunities first.

---

### ⚙️ Tools Used

* Python
* Jupyter Notebook
* Libraries: `pandas`, `numpy`

---

### ✅ Business Relevance

The feature simulates how AI or data logic can be used to **optimize B2B outreach**, making the lead generation process more strategic. This aligns closely with Caprae Capital’s emphasis on **practical AI implementation post-acquisition**.

---
