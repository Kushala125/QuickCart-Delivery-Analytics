import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Business Question
# Which cities have the highest complaint rate?
# ==========================================

city_summary = (
    df.groupby("City")
      .agg(
          Total_Orders=("Complaint_Flag", "count"),
          Complaints=("Complaint_Flag", "sum")
      )
)

city_summary["Complaint_Rate (%)"] = (
    city_summary["Complaints"] /
    city_summary["Total_Orders"] * 100
).round(2)

city_summary = city_summary.sort_values(
    "Complaint_Rate (%)",
    ascending=False
)

print("=" * 65)
print("CUSTOMER COMPLAINT RATE BY CITY")
print("=" * 65)
print(city_summary)

city_summary.to_csv(
    "reports/complaint_rate_city.csv"
)

print("\n✅ Complaint Rate report saved successfully!")

# ==========================================
# Visualization
# ==========================================

plt.figure(figsize=(10,6))

ax = sns.barplot(
    data=city_summary.reset_index(),
    x="Complaint_Rate (%)",
    y="City",
    palette="Reds_r"
)

# Add labels
for i, value in enumerate(city_summary["Complaint_Rate (%)"]):
    ax.text(
        value + 0.05,
        i,
        f"{value:.2f}%",
        va="center",
        fontsize=10
    )

plt.title(
    "Customer Complaint Rate by City",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Complaint Rate (%)", fontsize=13)
plt.ylabel("City", fontsize=13)

plt.grid(axis="x", linestyle="--", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "screenshots/complaint_rate_city.png",
    dpi=300
)

plt.show()

print("\n✅ Chart saved successfully!")