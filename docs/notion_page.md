# 📊 Irish Retail Sales Performance Dashboard

**Type:** Data Analyst project · **Tools:** Excel, SQL, Power BI-style dashboard (Chart.js) · **Status:** Complete

[🔗 Live interactive dashboard](#) · [🔗 GitHub repository](#) · [📄 Insights memo (PDF)](#)

---

### The problem
A multi-store Irish retailer needs visibility into which stores, categories, and periods are underperforming so management can reallocate stock and staff — instead of relying on manual, reactive monthly reporting.

### Business context
Retail chains in Ireland run on thin margins, and weekly self-serve reporting removes the decision lag that monthly head-office reporting creates.

### Dataset
Simulated Irish multi-store dataset — 6,500 cleaned transactions (Jan 2024–Dec 2025) across **Dublin, Cork, Galway, Limerick** and 4 product categories. Built with deliberately messy source data (mixed date formats, duplicate rows, missing values) so the cleaning step is real, not decorative.

### What I did
1. **Cleaned** the raw data in Python (mirrors an Excel/Power Query workflow) — standardized 3 different date formats, removed 150 duplicate rows, and handled nulls in Discount/Profit with a documented assumption.
2. **Queried** the cleaned data in SQL — monthly revenue by store, top 10 sub-categories by profit, and year-over-year growth using window functions (`LAG() OVER`).
3. **Modeled** a formula-driven Excel dashboard (SUMIFS-based, not hardcoded) with KPI cards and two charts.
4. **Built** an interactive web dashboard with a toggleable trend line, category breakdown, and the headline finding highlighted directly on the page.

### 🔑 Key insight
> Electronics makes up **59–60%** of total revenue in Dublin, Galway, and Limerick — but only **43.7%** in Cork. This is a **Cork-specific gap**, not a city-size effect: Cork's Homeware share is actually *above* the other stores' average, so the issue is Electronics-specific.

### Recommendation
Audit Cork's Electronics range and stock depth, and run a targeted in-store promotion ahead of the Q4 seasonal peak — rather than reallocating floor space away from Electronics. Closing the gap is worth an estimated **€26,000+/year**.

### Business impact
Gives store managers a weekly self-serve view instead of a monthly backward-looking report, and gives Cork's management team a specific, quantified, and testable starting point for Q4 planning.

---

**CV / LinkedIn bullet:**
*Built an interactive Power BI-style sales dashboard analyzing €2.05M in simulated multi-store revenue across 4 Irish stores; identified a Cork-specific Electronics underperformance worth an estimated €26K/year in recoverable revenue.*

**Skills demonstrated:** Data cleaning · SQL (window functions) · Excel (formula-driven dashboards) · Data visualization · Root-cause analysis · Business recommendation writing
