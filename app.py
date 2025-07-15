import pandas as pd
import streamlit as st

# ----------- PAGE CONFIG ----------- #
st.set_page_config(page_title="Lead Scoring Tool", page_icon="📊", layout="wide")

# ----------- SIDEBAR --------------- #
with st.sidebar:
    st.title("🧠 Lead Scoring Tool")
    st.markdown("Score and prioritize business leads based on:")
    st.markdown("- Revenue")
    st.markdown("- Industry")
    st.markdown("- Contact info availability")
    st.markdown("---")
    st.markdown("💡 Tip: Upload your own lead CSV or use our demo below.")
    st.caption("Built with ❤️ for Caprae Capital Pre-Work Assignment")

# ----------- MAIN TITLE ----------- #
st.markdown("<h1 style='text-align: center;'>🔍 Lead Scoring & Prioritization</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Identify high-impact leads with a smart scoring model.</p>", unsafe_allow_html=True)

# ----------- UPLOAD SECTION ----------- #
st.subheader("📤 Upload a CSV File (or use demo data below)")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# ----------- SAMPLE DATA ----------- #
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ CSV uploaded successfully!")
else:
    st.info("🔁 No CSV uploaded. Using default mock dataset.")
    df = pd.DataFrame({
        'Company': ['Acme Corp', 'Beta Inc', 'Gamma LLC', 'Delta Ltd', 'Epsilon GmbH'],
        'Revenue': [5000000, 20000000, 12000000, 4000000, 25000000],
        'Industry': ['Tech', 'Finance', 'Health', 'Retail', 'Tech'],
        'Has_Email': [True, True, False, True, False],
        'Has_Phone': [False, True, True, False, True]
    })

# ----------- INDUSTRY WEIGHTS ----------- #
industry_weights = {
    'Tech': 10,
    'Finance': 8,
    'Health': 6,
    'Retail': 4,
    'Other': 2
}

# ----------- SCORING FUNCTION ----------- #
def score_lead(row):
    revenue_score = row['Revenue'] / 1_000_000
    industry_score = industry_weights.get(row['Industry'], industry_weights['Other'])
    contact_score = 0
    if row['Has_Email']:
        contact_score += 5
    if row['Has_Phone']:
        contact_score += 5
    return revenue_score + industry_score + contact_score

# Apply scoring
df['Lead_Score'] = df.apply(score_lead, axis=1)
df['Lead_Score'] = df['Lead_Score'].round(2)  # Make it pretty
df_sorted = df.sort_values(by='Lead_Score', ascending=False)

# ----------- DISPLAY RESULTS ----------- #
st.subheader("📊 Prioritized Leads (High to Low)")
st.dataframe(df_sorted.style.format({"Revenue": "${:,.0f}", "Lead_Score": "{:.2f}"}), use_container_width=True)

# ----------- DOWNLOAD BUTTON ----------- #
st.download_button(
    label="⬇️ Download Prioritized Leads (CSV)",
    data=df_sorted.to_csv(index=False),
    file_name="scored_leads.csv",
    mime="text/csv"
)

# ----------- BONUS: Industry Scoring Info ----------- #
with st.expander("📘 View Industry Scoring Criteria"):
    st.markdown("""
    **Industry Weights:**
    - Tech: 10
    - Finance: 8
    - Health: 6
    - Retail: 4
    - Other: 2

    **Contact Info:**
    - +5 points for Email
    - +5 points for Phone
    """)

# ----------- Footer ----------- #
st.markdown("---")
st.caption("Made by [Your Name] · Streamlit Demo · Caprae Capital · © 2025")
