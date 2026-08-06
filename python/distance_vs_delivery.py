import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Correlation
# ==========================================

correlation = np.corrcoef(
    df["Delivery_Distance_KM"],
    df["Delivery_Time_Min"]
)[0,1]

print("=" * 60)
print("DELIVERY DISTANCE VS DELIVERY TIME")
print("=" * 60)
print(f"Correlation : {correlation:.4f}")

# ==========================================
# Hexbin Plot
# ==========================================

plt.figure(figsize=(10,7))

hb = plt.hexbin(
    df["Delivery_Distance_KM"],
    df["Delivery_Time_Min"],
    gridsize=35,
    cmap="viridis",
    mincnt=1
)

plt.colorbar(hb, label="Number of Deliveries")

plt.title(
    "Delivery Distance vs Delivery Time",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Delivery Distance (KM)", fontsize=13)
plt.ylabel("Delivery Time (Minutes)", fontsize=13)

plt.grid(alpha=0.3)

plt.text(
    1,
    115,
    f"Correlation = {correlation:.3f}",
    fontsize=11,
    bbox=dict(facecolor="white", alpha=0.8)
)

plt.tight_layout()

plt.savefig(
    "screenshots/delivery_distance_hexbin.png",
    dpi=300
)

plt.show()

print("\nHexbin chart saved successfully!")