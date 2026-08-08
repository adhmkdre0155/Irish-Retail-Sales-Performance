-- ============================================================
-- Irish Retail Sales Performance Dashboard — Analysis Queries
-- Table: sales (loaded from retail_sales_clean.csv)
-- ============================================================

-- 1. Monthly revenue by store
SELECT
    Store,
    Month,
    ROUND(SUM(Sales), 2)  AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) * 1.0 / SUM(Sales), 4) AS MarginPct
FROM sales
GROUP BY Store, Month
ORDER BY Store, Month;

-- 2. Top 10 sub-categories by total margin (profit)
SELECT
    Category,
    SubCategory,
    ROUND(SUM(Sales), 2)  AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(SUM(Profit) * 1.0 / SUM(Sales), 4) AS MarginPct
FROM sales
GROUP BY Category, SubCategory
ORDER BY Profit DESC
LIMIT 10;

-- 3. Year-over-year revenue growth by store (window function)
WITH yearly AS (
    SELECT Store, Year, ROUND(SUM(Sales), 2) AS Revenue
    FROM sales
    GROUP BY Store, Year
)
SELECT
    Store,
    Year,
    Revenue,
    LAG(Revenue) OVER (PARTITION BY Store ORDER BY Year) AS PrevYearRevenue,
    ROUND(
        (Revenue - LAG(Revenue) OVER (PARTITION BY Store ORDER BY Year)) * 100.0
        / LAG(Revenue) OVER (PARTITION BY Store ORDER BY Year), 2
    ) AS YoY_Growth_Pct
FROM yearly
ORDER BY Store, Year;

-- 4. Store vs. category performance matrix (used for the Cork/Electronics finding)
SELECT
    Store,
    Category,
    ROUND(SUM(Sales), 2)  AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    ROUND(AVG(MarginPct), 4) AS AvgMarginPct
FROM sales
GROUP BY Store, Category
ORDER BY Category, Revenue DESC;

-- 5. Quarterly revenue trend (for the Executive Overview KPI cards)
SELECT
    Quarter,
    ROUND(SUM(Sales), 2)  AS Revenue,
    ROUND(SUM(Profit), 2) AS Profit,
    COUNT(DISTINCT OrderID) AS Orders
FROM sales
GROUP BY Quarter
ORDER BY Quarter;

-- 6. Cork vs Dublin, Electronics category only — the headline insight query
SELECT
    Store,
    ROUND(SUM(Sales), 2) AS ElectronicsRevenue,
    ROUND(SUM(Profit), 2) AS ElectronicsProfit
FROM sales
WHERE Category = 'Electronics' AND Store IN ('Cork', 'Dublin')
GROUP BY Store;
