"""
Generates a simulated Irish multi-store retail sales dataset.
Intentionally includes duplicates, nulls, and inconsistent date formats
so the cleaning step in the portfolio project is genuine, not decorative.
"""
import random
import csv
from datetime import date, timedelta

random.seed(42)

STORES = ["Dublin", "Cork", "Galway", "Limerick"]
STORE_WEIGHT = [0.42, 0.24, 0.19, 0.15]  # Dublin biggest, Limerick smallest

CATEGORIES = {
    "Electronics": ["Headphones", "Laptops", "Mobile Accessories", "Smart Home", "TVs"],
    "Homeware": ["Kitchenware", "Bedding", "Furniture", "Lighting", "Storage"],
    "Grocery": ["Fresh Produce", "Bakery", "Beverages", "Snacks", "Dairy"],
    "Clothing": ["Menswear", "Womenswear", "Kidswear", "Footwear", "Accessories"],
}

# Base price ranges per category (EUR)
PRICE_RANGE = {
    "Electronics": (25, 650),
    "Homeware": (10, 300),
    "Grocery": (2, 40),
    "Clothing": (8, 120),
}

# Cork Electronics is deliberately weakened to create a genuine findable insight
def store_category_multiplier(store, category):
    if store == "Cork" and category == "Electronics":
        return 0.55  # underperformance signal to be discovered in analysis
    if store == "Dublin":
        return 1.15
    if store == "Limerick" and category == "Grocery":
        return 1.2  # local strength
    return 1.0

start = date(2024, 1, 1)
end = date(2025, 12, 31)
days = (end - start).days

rows = []
order_id = 100000

date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]  # inconsistent formats to clean

for _ in range(6500):
    order_id += 1
    d = start + timedelta(days=random.randint(0, days))
    # seasonal boost: Nov-Dec (+40%), summer dip in Aug (-15%)
    seasonal = 1.4 if d.month in (11, 12) else (0.85 if d.month == 8 else 1.0)

    store = random.choices(STORES, weights=STORE_WEIGHT, k=1)[0]
    category = random.choice(list(CATEGORIES.keys()))
    subcat = random.choice(CATEGORIES[category])

    mult = store_category_multiplier(store, category) * seasonal
    lo, hi = PRICE_RANGE[category]
    unit_price = round(random.uniform(lo, hi), 2)
    quantity = random.choice([1, 1, 1, 2, 2, 3, 4])
    discount = random.choice([0, 0, 0, 0.05, 0.10, 0.15, 0.20])

    sales = round(unit_price * quantity * mult, 2)
    cost_ratio = random.uniform(0.55, 0.75)  # cost as % of sales before discount
    profit = round(sales * (1 - discount) - (sales * cost_ratio), 2)

    # Randomly write date in an inconsistent format (needs cleaning)
    fmt = random.choice(date_formats)
    date_str = d.strftime(fmt)

    # Randomly null out discount or profit (~4% of rows) to simulate real dirty data
    discount_val = "" if random.random() < 0.03 else discount
    profit_val = "" if random.random() < 0.02 else profit

    rows.append([order_id, date_str, store, category, subcat,
                 sales, quantity, discount_val, profit_val])

# Inject ~150 exact duplicate rows (common real-world export error)
dupes = random.sample(rows, 150)
rows.extend(dupes)
random.shuffle(rows)

header = ["OrderID", "OrderDate", "Store", "Category", "SubCategory",
          "Sales", "Quantity", "Discount", "Profit"]

with open("retail_sales_raw.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)

print(f"Generated {len(rows)} raw rows (including {len(dupes)} intentional duplicates).")
