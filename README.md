Absolutely! Here's the improved version of your `README.md` without emojis and written in a more natural, human tone:

---

# Caprae Capital – Pre-Work Assignment

This repository contains my submission for Caprae Capital’s AI-Readiness Pre-Screening Challenge.

## Feature: Lead Scoring & Prioritization

The task was to build on top of an existing lead generation tool ([saasquatchleads.com](https://www.saasquatchleads.com)) by adding a feature to help sales teams quickly identify high-value leads through an automated scoring system.

---

## Contents

| File                | Description                              |
| ------------------- | ---------------------------------------- |
| lead\_scoring.ipynb | Jupyter notebook with the scoring logic  |
| app.py              | Streamlit app for uploading and scoring  |
| mock-data.csv       | Sample dataset for testing               |
| report.md           | A short summary of the feature and logic |
| requirements.txt    | List of required Python libraries        |

---

## How It Works

Leads are scored based on:

* Revenue (normalized to millions)
* Relevance of the industry (with extra weight for tech and finance)
* Presence of contact information (email or phone number adds extra points)

The final list is sorted by score, making it easy to prioritize outreach to high-potential leads.

---

## Two Ways to Try It Out

### 1. Jupyter Notebook

1. Open `lead_scoring.ipynb` in Jupyter
2. Run all cells
3. View the sorted list of scored leads

### 2. Streamlit Web App

To run the interactive web interface:

pip install -r requirements.txt
streamlit run app.py

You can use the included `mock-data.csv` or upload your own CSV file.

---

## Sample CSV

The repository includes a sample file (`mock-data.csv`) with 10 realistic leads for demo purposes. You can modify or replace this file to test with your own data.

---

## Submission Highlights

* Solid business logic for prioritizing leads
* Lightweight and easy to extend
* Includes a simple web app for better usability
* Built with Caprae Capital’s focus on practical, results-driven AI in mind

---

Let me know if you'd like a PDF version or GitHub styling suggestions!
