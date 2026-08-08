"""
Cleaning step for the Irish Retail Sales Performance Dashboard project.
Mirrors what would be done in Excel/Power Query:
  1. Standardize inconsistent date formats to ISO (YYYY-MM-DD)
  2. Remove exact duplicate rows
  3. Handle nulls in Discount (assume 0 if missing) and Profit (recompute)
  4. Add derived columns used throughout the analysis (Month, Quarter, Margin%)
"""
import pandas as pd

df = pd.read_csv("retail_sales_raw.csv")
raw_rows = len(df)

# 1) Standardize dates — pandas' dateutil parser handles the mixed formats
df["OrderDate"] = pd.to_datetime(df["OrderDate"], dayfirst=True, format="mixed")

# 2) Remove exact duplicates
df = df.drop_duplicates()
deduped_rows = len(df)

# 3) Handle nulls
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce").fillna(0)

# Recompute Profit for any missing values using an estimated 65% cost ratio
# (documented assumption — flagged in the README/insights memo)
missing_profit_mask = df["Profit"].isna() | (df["Profit"] == "")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
estimated_profit = df["Sales"] * (1 - df["Discount"]) - (df["Sales"] * 0.65)
df.loc[df["Profit"].isna(), "Profit"] = estimated_profit[df["Profit"].isna()]
df["Profit"] = df["Profit"].round(2)

# 4) Derived columns
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)
df["Quarter"] = df["OrderDate"].dt.to_period("Q").astype(str)
df["Year"] = df["OrderDate"].dt.year
df["MarginPct"] = (df["Profit"] / df["Sales"]).round(4)

df = df.sort_values("OrderDate").reset_index(drop=True)
df.to_csv("retail_sales_clean.csv", index=False)

print(f"Raw rows:      {raw_rows}")
print(f"After dedupe:  {deduped_rows}  ({raw_rows - deduped_rows} duplicates removed)")
print(f"Final rows:    {len(df)}")
print(f"Nulls remaining -> Discount: {df['Discount'].isna().sum()}, Profit: {df['Profit'].isna().sum()}")
print(f"Date range: {df['OrderDate'].min().date()} to {df['OrderDate'].max().date()}")
