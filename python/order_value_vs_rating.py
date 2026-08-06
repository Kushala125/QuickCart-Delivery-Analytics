import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Correlation
# ==========================================

correlation = np.corrcoef(
    df["Order_Value_USD"],
    df["Customer_Rating"]
)[0,1]

print("="*60)
print("ORDER VALUE VS CUSTOMER RATING")
print("="*60)
print(f"Correlation : {correlation:.4f}")

# ==========================================
# Regression Plot
# ==========================================

plt.figure(figsize=(10,6))

sns.regplot(
    data=df,
    x="Order_Value_USD",
    y="Customer_Rating",
    scatter_kws={
        "alpha":0.30,
        "s":15
    },
    line_kws={
        "color":"red",
        "linewidth":3
    }
)

plt.title(
    "Order Value vs Customer Rating",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Order Value (USD)", fontsize=13)
plt.ylabel("Customer Rating", fontsize=13)

plt.grid(alpha=0.3)

plt.text(
    0.02,
    0.95,
    f"Correlation = {correlation:.3f}",
    transform=plt.gca().transAxes,
    bbox=dict(facecolor="white")
)

plt.tight_layout()

plt.savefig(
    "screenshots/order_value_vs_rating.png",
    dpi=300
)

plt.show()

print("\n✅ Chart saved successfully!")