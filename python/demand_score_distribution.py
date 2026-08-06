import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Business Question
# How is Demand Score distributed?
# ==========================================

print("=" * 60)
print("DEMAND SCORE SUMMARY")
print("=" * 60)

print(df["Demand_Score"].describe())

df["Demand_Score"].describe().to_csv(
    "reports/demand_score_summary.csv"
)

# ==========================================
# Histogram + KDE
# ==========================================

plt.figure(figsize=(10,6))

sns.histplot(
    data=df,
    x="Demand_Score",
    bins=30,
    kde=True,
    color="royalblue"
)

plt.title(
    "Demand Score Distribution",
    fontsize=18,
    weight="bold"
)

plt.xlabel("Demand Score")
plt.ylabel("Number of Orders")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "screenshots/demand_score_distribution.png",
    dpi=300
)

plt.show()

print("\n✅ Demand Score report saved successfully!")