# ==========================================
# QuickCart Delivery Analytics
# Visualization 1 & 2
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Visualization 1
# Revenue by City
# ==========================================

city_revenue = (
    df.groupby("City")["Revenue_USD"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

bars = plt.bar(
    city_revenue.index,
    city_revenue.values
)

plt.title("Revenue by City", fontsize=18)
plt.xlabel("City", fontsize=14)
plt.ylabel("Revenue (USD)", fontsize=14)

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"${height:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    "screenshots/revenue_by_city.png",
    dpi=300
)

plt.show()

print("✅ Revenue by City chart saved successfully!")

# ==========================================
# Visualization 2
# Revenue by Restaurant Type
# ==========================================

restaurant_revenue = (
    df.groupby("Restaurant_Type")["Revenue_USD"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

bars = plt.bar(
    restaurant_revenue.index,
    restaurant_revenue.values
)

plt.title("Revenue by Restaurant Type", fontsize=18)
plt.xlabel("Restaurant Type", fontsize=14)
plt.ylabel("Revenue (USD)", fontsize=14)

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"${height:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    "screenshots/revenue_by_restaurant_type.png",
    dpi=300
)

plt.show()

print("✅ Revenue by Restaurant Type chart saved successfully!")
##
# ==========================================
# QuickCart Delivery Analytics
# Visualization 3
# Revenue by Customer Type (Pie Chart)
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# Revenue by Customer Type
# ==========================================

# ==========================================
# Visualization 3
# Business Question:
# Which customer segment generates the highest revenue?
# ==========================================

customer_revenue = (
    df.groupby("Customer_Type")["Revenue_USD"]
      .sum()
      .sort_values(ascending=False)
)

# ==========================================
# Create Pie Chart
# ==========================================

plt.figure(figsize=(8, 8))

plt.pie(
    customer_revenue.values,
    labels=customer_revenue.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Revenue Share by Customer Type",
    fontsize=18
)

# Makes the pie chart perfectly circular
plt.axis("equal")

plt.tight_layout()

# Save the chart
plt.savefig(
    "screenshots/revenue_by_customer_type.png",
    dpi=300
)

# Close the figure instead of showing it
plt.close()

print("✅ Revenue by Customer Type chart saved successfully!")