# Irish Retail Sales Performance Dashboard

**Data Analyst portfolio project — Adham AlHers**
[Live interactive dashboard](./dashboard/index.html) · [LinkedIn](https://www.linkedin.com/in/adhamalhers/) · [Portfolio home](#)

## Problem statement
A multi-store Irish retailer needs visibility into which stores, categories, and periods are underperforming so management can reallocate stock and staff — instead of relying on manual, reactive monthly reporting.

## Business context
Retail chains in Ireland (multi-branch operators like Dunnes or SuperValu) run on thin margins. Weekly self-serve reporting removes decision lag that monthly head-office reports create.

## Dataset
A simulated Irish multi-store dataset (6,500 cleaned transactions, Jan 2024–Dec 2025) across **Dublin, Cork, Galway, and Limerick**, spanning Electronics, Homeware, Grocery, and Clothing categories. Generated with a deliberate, realistic data-quality problem set (mixed date formats, ~150 duplicate rows, ~3–4% missing Discount/Profit values) so the cleaning step is genuine rather than decorative. See `/data/generate_data.py` for full generation logic and documented assumptions.

## Tools
Python (pandas) for cleaning · SQL (SQLite) for analysis · Excel (openpyxl, formula-driven) for the KPI/pivot dashboard · Chart.js for the interactive web dashboard.

## Repository structure
```
├── data/
│   ├── generate_data.py        # Generates the raw simulated dataset
│   ├── clean_data.py           # Cleaning: dates, duplicates, nulls, derived columns
│   ├── retail_sales_raw.csv    # Raw (messy) data
│   └── retail_sales_clean.csv  # Cleaned, analysis-ready data
├── sql/
│   └── queries.sql             # Monthly revenue, top-10 SKUs, YoY growth (window functions)
├── excel/
│   └── Irish_Retail_Sales_Dashboard.xlsx   # Formula-driven KPI dashboard with charts
├── dashboard/
│   └── index.html              # Self-contained interactive web dashboard
└── docs/
    └── insights_memo.docx      # One-page findings memo
```

## Step-by-step approach
1. **Clean** — `data/clean_data.py` standardizes three inconsistent date formats to ISO, removes 150 exact-duplicate rows, fills missing discounts as 0, and re-estimates the ~2% of missing profit values using a documented 65% cost-ratio assumption.
2. **Analyze in SQL** — `sql/queries.sql` covers monthly revenue by store, the top 10 sub-categories by profit, and year-over-year growth by store using window functions (`LAG() OVER (PARTITION BY ...)`).
3. **Model in Excel** — `excel/Irish_Retail_Sales_Dashboard.xlsx` uses `SUMIFS` formulas (not hardcoded values) across a Data → Store_Summary → Category_Summary → Dashboard structure, with a KPI-card header row and two charts (clustered store revenue, Pareto profit chart).
4. **Visualize interactively** — `dashboard/index.html` is a self-contained (no external dependencies) HTML dashboard with a toggleable monthly trend line, a stacked category-by-store bar, a Pareto ranking, and the headline Cork finding, built to be hosted directly on GitHub Pages.

## Key insight
Electronics accounts for **59–60% of total revenue** in Dublin, Galway, and Limerick, but only **43.7% in Cork** — a Cork-specific gap of roughly 16 percentage points, not a city-size effect (confirmed by checking Cork's Homeware share, which is actually *above* the other stores' average). Closing that gap to the other-store average would add an estimated **€26,000+ per year** in Cork electronics revenue.

## Recommendation
Investigate Cork's Electronics range and stock depth and run a targeted in-store promotion ahead of Q4 — rather than reallocating floor space away from Electronics, since Cork already over-indexes on Homeware relative to the other three stores.

## Business impact
Replaces a monthly, backward-looking head-office report with a weekly self-serve dashboard store managers can act on directly — reducing decision lag and giving a concrete, quantified starting point for Cork's Q4 planning.
---
*Dataset is simulated for portfolio purposes. Methodology (cleaning logic, SQL, and formulas) is fully reproducible — see the scripts and workbook above.*
