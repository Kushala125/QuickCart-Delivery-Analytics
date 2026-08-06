import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Create Age Groups
# ==========================================

bins = [18, 25, 35, 45, 55, 65, 75]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65",
    "66-74"
]

df["Age_Group"] = pd.cut(
    df["Customer_Age"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# ==========================================
# Summary
# ==========================================

summary = (
    df.groupby("Age_Group")["Order_Value_USD"]
      .agg(["count", "mean", "median", "max"])
      .round(2)
)

print("=" * 60)
print("ORDER VALUE BY CUSTOMER AGE GROUP")
print("=" * 60)

print(summary)

summary.to_csv(
    "reports/customer_age_order_value.csv"
)

print("\n✅ Summary saved successfully!")

# ==========================================
# Violin Plot
# ==========================================

plt.figure(figsize=(11,6))

sns.violinplot(
    data=df,
    x="Age_Group",
    y="Order_Value_USD",
    inner="box"
)

plt.title(
    "Order Value Distribution by Customer Age Group",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Customer Age Group", fontsize=13)
plt.ylabel("Order Value (USD)", fontsize=13)

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "screenshots/customer_age_order_value.png",
    dpi=300
)

plt.show()

print("\n✅ Violin Plot saved successfully!")