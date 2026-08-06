# ==========================================
# QuickCart Delivery Analytics
# Visualization 4
# Average Delivery Time by Traffic Level
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Average Delivery Time by Traffic Level
# ==========================================

traffic_delivery = (
    df.groupby("Traffic_Level")["Delivery_Time_Min"]
      .mean()
      .round(2)
      .sort_values()
)

print("=" * 50)
print("AVERAGE DELIVERY TIME BY TRAFFIC LEVEL")
print("=" * 50)
print(traffic_delivery)

# ==========================================
# Create Horizontal Bar Chart
# ==========================================

plt.figure(figsize=(10,6))

bars = plt.barh(
    traffic_delivery.index,
    traffic_delivery.values
)

plt.title(
    "Average Delivery Time by Traffic Level",
    fontsize=18
)

plt.xlabel(
    "Average Delivery Time (Minutes)",
    fontsize=14
)

plt.ylabel(
    "Traffic Level",
    fontsize=14
)

plt.grid(axis="x", linestyle="--", alpha=0.4)

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.2,
        bar.get_y() + bar.get_height()/2,
        f"{width:.2f}",
        va="center",
        fontsize=10
    )

plt.tight_layout()

plt.savefig(
    "screenshots/delivery_time_by_traffic.png",
    dpi=300
)

plt.close()

print("\n✅ Delivery Time by Traffic chart saved successfully!")