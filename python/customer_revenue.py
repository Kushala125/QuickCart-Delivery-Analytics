import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/delivery_data.csv")
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