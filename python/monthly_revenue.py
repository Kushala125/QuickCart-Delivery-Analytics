import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Monthly Revenue
# ==========================================

monthly_revenue = (
    df.groupby("Month")["Revenue_USD"]
      .sum()
      .sort_index()
)

print("=" * 50)
print("MONTHLY REVENUE")
print("=" * 50)
print(monthly_revenue)

# ==========================================
# Lollipop Chart
# ==========================================

plt.figure(figsize=(12,6))

months = monthly_revenue.index.astype(str)
revenue = monthly_revenue.values

# Vertical lines ("sticks")
plt.vlines(
    x=months,
    ymin=0,
    ymax=revenue,
    linewidth=3
)

# Dots ("lollipops")
plt.scatter(
    months,
    revenue,
    s=180
)

# Value labels
for month, rev in zip(months, revenue):
    plt.text(
        month,
        rev,
        f"${rev:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.title("Monthly Revenue Trend", fontsize=18, weight="bold")
plt.xlabel("Month", fontsize=13)
plt.ylabel("Revenue (USD)", fontsize=13)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(
    "screenshots/monthly_revenue_lollipop.png",
    dpi=300
)

plt.show()

print("\n✅ Monthly Revenue Lollipop Chart saved successfully!")