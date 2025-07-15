import pandas as pd
import streamlit as st

# Title and description
st.title("🔍 Lead Scoring & Prioritization Tool")
st.markdown("""
This simple demo ranks leads based on:
- Revenue
- Industry relevance
- Contact info (email/phone)

Upload your own CSV or use the default mock data below.
""")

# Upload section
uploaded_file = st.file_uploader("📤 Upload Your CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame({
        'Company': ['Acme Corp', 'Beta Inc', 'Gamma LLC', 'Delta Ltd', 'Epsilon GmbH'],
        'Revenue': [5000000, 20000000, 12000000, 4000000, 25000000],
        'Industry': ['Tech', 'Finance', 'Health', 'Retail', 'Tech'],
        'Has_Email': [True, True, False, True, False],
        'Has_Phone': [False, True, True, False, True]
    })

# Industry weight mapping
industry_weights = {
    'Tech': 10,
    'Finance': 8,
    'Health': 6,
    'Retail': 4,
    'Other': 2
}

# Scoring logic
def score_lead(row):
    revenue_score = row['Revenue'] / 1_000_000
    industry_score = industry_weights.get(row['Industry'], industry_weights['Other'])
    contact_score = 0
    if row['Has_Email']: contact_score += 5
    if row['Has_Phone']: contact_score += 5
    return revenue_score + industry_score + contact_score

# Apply scoring
df['Lead_Score'] = df.apply(score_lead, axis=1)
df_sorted = df.sort_values(by='Lead_Score', ascending=False)

# Display results
st.subheader("📊 Prioritized Leads")
st.dataframe(df_sorted)

# Download button
st.download_button(
    label="⬇️ Download Prioritized Leads as CSV",
    data=df_sorted.to_csv(index=False),
    file_name="scored_leads.csv",
    mime="text/csv"
)
