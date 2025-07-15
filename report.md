# Caprae Capital Pre-Work Report  
## Feature Developed: Lead Scoring & Prioritization

### Objective  
As part of the AI-Readiness Pre-Screening Challenge, I analyzed the existing lead generation platform [saasquatchleads.com](https://www.saasquatchleads.com) to identify a practical enhancement that could deliver tangible value to users within a 5-hour development window.

I chose to develop a **Lead Scoring and Prioritization** feature that helps sales teams quickly identify and focus on their highest-value leads.

---

### Rationale  
While the current platform effectively aggregates potential leads, it treats all leads equally — lacking a mechanism to distinguish high-potential opportunities from lower-priority ones. This results in inefficiencies for users relying on the tool for outbound sales.

By introducing a lead scoring system, the platform can better align with the needs of sales professionals who want to prioritize outreach based on business potential. This added layer of intelligence transforms a static lead list into a more actionable, insight-driven resource.

---

### Scoring Methodology  

Each lead is assigned a numeric score calculated from the following factors:

- **Revenue**: Normalized by millions — higher revenue suggests greater deal size and interest.
- **Industry**: Weighted based on relevance to SaaS sales (e.g., Tech = high weight, Retail = lower weight).
- **Contact Availability**: Additional points are added if both email and phone contact information are present.

**Formula used**:

Score = (Revenue / 1,000,000) + Industry Weight + Contact Info Bonus


The final dataset is sorted by this score to produce a prioritized lead list.

---

### Tools & Technologies  
- Python  
- Jupyter Notebook  
- `pandas`, `numpy`  

---

### Business Impact  
This feature helps reduce time spent on low-quality leads, improves targeting, and introduces structure to the lead management process. It demonstrates a simple yet powerful way to apply data scoring within a sales workflow — consistent with Caprae Capital’s focus on enabling AI-readiness in real-world business operations.

---

