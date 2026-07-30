import pandas as pd

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/delivery_data.csv")

# ==========================================
# EDA-001
# Business Question:
# Which city generates the highest revenue?
# ==========================================

city_revenue = (
    df.groupby("City")["Revenue_USD"]
      .sum()
      .sort_values(ascending=False)
)

print("=" * 50)
print("TOTAL REVENUE BY CITY")
print("=" * 50)
print(city_revenue)

city_revenue.to_csv("reports/revenue_by_city.csv")

print("\n✅ Revenue by City report saved successfully!")

# ==========================================
# EDA-002
# Business Question:
# Which restaurant type generates the highest revenue?
# ==========================================

restaurant_revenue = (
    df.groupby("Restaurant_Type")["Revenue_USD"]
      .sum()
      .sort_values(ascending=False)
)

print("\n" + "=" * 50)
print("TOTAL REVENUE BY RESTAURANT TYPE")
print("=" * 50)
print(restaurant_revenue)

restaurant_revenue.to_csv("reports/revenue_by_restaurant_type.csv")

print("\n✅ Revenue by Restaurant Type report saved successfully!")

# ==========================================
# EDA-003
# Business Question:
# Which customer segment generates the highest revenue?
# ==========================================

customer_revenue = (
    df.groupby("Customer_Type")["Revenue_USD"]
      .sum()
      .sort_values(ascending=False)
)

print("\n" + "=" * 50)
print("TOTAL REVENUE BY CUSTOMER TYPE")
print("=" * 50)
print(customer_revenue)

customer_revenue.to_csv("reports/revenue_by_customer_type.csv")

print("\n✅ Revenue by Customer Type report saved successfully!")

# ==========================================
# EDA-004
# Business Question:
# How are delivery times distributed?
# ==========================================

print("\n" + "=" * 50)
print("DELIVERY TIME ANALYSIS")
print("=" * 50)

delivery_time = df["Delivery_Time_Min"]

print(f"Average Delivery Time : {delivery_time.mean():.2f} minutes")
print(f"Median Delivery Time  : {delivery_time.median():.2f} minutes")
print(f"Minimum Delivery Time : {delivery_time.min()} minutes")
print(f"Maximum Delivery Time : {delivery_time.max()} minutes")
print(f"Most Common Time      : {delivery_time.mode()[0]} minutes")

# ==========================================
# EDA-005
# Business Question:
# Does traffic level affect delivery time?
# ==========================================

traffic_delivery = (
    df.groupby("Traffic_Level")["Delivery_Time_Min"]
      .mean()
      .round(2)
      .sort_values()
)

print("\n" + "=" * 50)
print("AVERAGE DELIVERY TIME BY TRAFFIC LEVEL")
print("=" * 50)
print(traffic_delivery)

traffic_delivery.to_csv("reports/delivery_time_by_traffic.csv")

print("\n✅ Delivery Time by Traffic report saved successfully!")

# ==========================================
# EDA-006
# Business Question:
# Does weather affect delivery time?
# ==========================================

weather_delivery = (
    df.groupby("Weather_Condition")["Delivery_Time_Min"]
      .mean()
      .round(2)
      .sort_values()
)

print("\n" + "=" * 50)
print("AVERAGE DELIVERY TIME BY WEATHER")
print("=" * 50)
print(weather_delivery)

weather_delivery.to_csv("reports/delivery_time_by_weather.csv")

print("\n✅ Delivery Time by Weather report saved successfully!")
#Does delivery distance affect delivery time?
correlation = df["Delivery_Distance_KM"].corr(df["Delivery_Time_Min"])
print("\n" + "=" * 50)
print("DELIVERY DISTANCE VS DELIVERY TIME CORRELATION")
print("=" * 50)
print(f"Correlation: {correlation: .2f}")
if correlation > 0.7:
    print("There is a strong positive correlation between delivery distance and delivery time.")
elif correlation > 0.5:
    print("There is a moderate positive correlation between delivery distance and delivery time.")
else:
    print("Weak or no relationship.")
distance_summary = (
    df[["Delivery_Distance_KM", "Delivery_Time_Min"]]
      .describe()
)
print("\nSummary Statistics")
print(distance_summary)

distance_summary.to_csv(
    "reports/distance_delivery_summary.csv"
)

print("\n✅ Distance vs Delivery report saved successfully!")
#Do customer complaints lead to refunds?
# ==========================================
# EDA-008
# Business Question:
# Do customer complaints lead to refunds?
# ==========================================

complaint_refund = (
    pd.crosstab(
        df["Complaint_Flag"],
        df["Refund_Flag"],
        margins=True
    )
)

print("\n" + "=" * 50)
print("COMPLAINT VS REFUND")
print("=" * 50)
print(complaint_refund)

complaint_refund.to_csv(
    "reports/complaint_vs_refund.csv"
)

print("\n Complaint vs Refund report saved successfully!")
#ow does revenue change month by month?
# ==========================================
# EDA-009
# Business Question:
# How does revenue change month by month?
# ==========================================

monthly_revenue = (
    df.groupby("Month")["Revenue_USD"]
      .sum()
      .sort_index()
)

print("\n" + "=" * 50)
print("MONTHLY REVENUE")
print("=" * 50)
print(monthly_revenue)

monthly_revenue.to_csv(
    "reports/monthly_revenue.csv"
)

print("\n✅ Monthly Revenue report saved successfully!")
#"Are customers generally happy with our service? What's our average rating, and how are ratings distributed?"
# ==========================================
# EDA-010
# Business Question:
# How satisfied are our customers?
# ==========================================

print("\n" + "=" * 50)
print("CUSTOMER RATING ANALYSIS")
print("=" * 50)

ratings = df["Customer_Rating"]

print(f"Average Rating : {ratings.mean():.2f}")
print(f"Median Rating  : {ratings.median():.2f}")
print(f"Highest Rating : {ratings.max()}")
print(f"Lowest Rating  : {ratings.min()}")

rating_distribution = (
    df["Customer_Rating"]
      .value_counts()
      .sort_index()
)

print("\nRating Distribution")
print(rating_distribution)

rating_distribution.to_csv(
    "reports/customer_rating_distribution.csv"
)

print("\n✅ Customer Rating report saved successfully!")
#Which business metrics are most strongly related to each other?
numerical_columns = [
    "Customer_Age",
    "Delivery_Distance_KM",
    "Delivery_Time_Min",
    "Order_Value_USD",
    "Item_Count",
    "Revenue_USD",
    "Profit_USD",
    "Demand_Score"
]
correlation_matrix = df[numerical_columns].corr()
print("\n" + "=" * 50)
print("CORRELATION MATRIX")
print("=" * 50)
print(correlation_matrix.round(2))
correlation_matrix.to_csv(
    "reports/correlation_matrix.csv"
)

print("\nCorrelation Matrix report saved successfully!")
#What are the key business KPIs for QuickCart?
# ==========================================
# EDA-012
# Executive KPI Summary
# ==========================================

print("\n" + "=" * 50)
print("EXECUTIVE KPI SUMMARY")
print("=" * 50)

total_orders = len(df)
total_revenue = df["Revenue_USD"].sum()
total_profit = df["Profit_USD"].sum()

average_order_value = df["Order_Value_USD"].mean()
average_delivery_time = df["Delivery_Time_Min"].mean()
average_customer_rating = df["Customer_Rating"].mean()

complaint_rate = (df["Complaint_Flag"].eq("Yes").mean()) * 100
refund_rate = (df["Refund_Flag"].eq("Yes").mean()) * 100

print(f"Total Orders            : {total_orders:,}")
print(f"Total Revenue (USD)     : ${total_revenue:,.2f}")
print(f"Total Profit (USD)      : ${total_profit:,.2f}")
print(f"Average Order Value     : ${average_order_value:.2f}")
print(f"Average Delivery Time   : {average_delivery_time:.2f} minutes")
print(f"Average Customer Rating : {average_customer_rating:.2f}")
print(f"Complaint Rate          : {complaint_rate:.2f}%")
print(f"Refund Rate             : {refund_rate:.2f}%")

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Orders",
        "Total Revenue",
        "Total Profit",
        "Average Order Value",
        "Average Delivery Time",
        "Average Customer Rating",
        "Complaint Rate (%)",
        "Refund Rate (%)"
    ],
    "Value": [
        total_orders,
        round(total_revenue, 2),
        round(total_profit, 2),
        round(average_order_value, 2),
        round(average_delivery_time, 2),
        round(average_customer_rating, 2),
        round(complaint_rate, 2),
        round(refund_rate, 2)
    ]
})

kpi_summary.to_csv(
    "reports/executive_kpi_summary.csv",
    index=False
)

print("\n✅ Executive KPI Summary saved successfully!")