import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/delivery_data.csv")
weather_delivery = (
    df.groupby("Weather_Condition")["Delivery_Time_Min"]
      .mean()
      .round(2)
)

plt.figure(figsize=(8,5))

plt.plot(
    weather_delivery.index,
    weather_delivery.values,
    marker="o",
    linewidth=3
)

plt.title("Average Delivery Time by Weather")
plt.xlabel("Weather Condition")
plt.ylabel("Average Delivery Time (Minutes)")
plt.grid(True)

plt.savefig("screenshots/delivery_time_by_weather.png", dpi=300)

plt.show()