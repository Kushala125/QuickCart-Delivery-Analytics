import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Select Numeric Columns
# ==========================================

numeric_df = df.select_dtypes(include=np.number)

# ==========================================
# Correlation Matrix
# ==========================================

corr = numeric_df.corr()

print("=" * 70)
print("CORRELATION MATRIX")
print("=" * 70)

print(corr.round(2))

corr.to_csv("reports/correlation_matrix.csv")

print("\n✅ Correlation Matrix saved successfully!")

# ==========================================
# Heatmap
# ==========================================

plt.figure(figsize=(14,10))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    square=True
)

plt.title(
    "Correlation Heatmap of Numerical Features",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    "screenshots/correlation_heatmap.png",
    dpi=300
)

plt.show()

print("\n✅ Correlation Heatmap saved successfully!")