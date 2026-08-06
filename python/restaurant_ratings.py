
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
# Which restaurant type receives the highest ratings?
# ==========================================

rating_summary = (
    df.groupby("Restaurant_Type")["Customer_Rating"]
      .agg(["count", "mean", "median", "min", "max"])
      .round(2)
      .sort_values("mean", ascending=False)
)

print("=" * 65)
print("CUSTOMER RATINGS BY RESTAURANT TYPE")
print("=" * 65)

print(rating_summary)

rating_summary.to_csv(
    "reports/restaurant_rating_summary.csv"
)

print("\n✅ Restaurant Rating Summary saved successfully!")

# ==========================================
# Box Plot
# ==========================================

plt.figure(figsize=(11,6))

sns.boxplot(
    data=df,
    x="Restaurant_Type",
    y="Customer_Rating",
    palette="Set2"
)

plt.title(
    "Customer Rating Distribution by Restaurant Type",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Restaurant Type", fontsize=13)
plt.ylabel("Customer Rating", fontsize=13)

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "screenshots/restaurant_ratings_boxplot.png",
    dpi=300
)

plt.show()

print("\n✅ Restaurant Ratings Box Plot saved successfully!")