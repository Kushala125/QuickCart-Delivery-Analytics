import pandas as pd

# Read the dataset
df = pd.read_csv("data/raw/delivery_data.csv")

# Create the report file
with open("reports/data_assessment_report.txt", "w") as report:

    report.write("=" * 60 + "\n")
    report.write("QUICKCART DATA ASSESSMENT REPORT\n")
    report.write("=" * 60 + "\n\n")

    # Dataset Shape
    report.write("DATASET SHAPE\n")
    report.write("-" * 40 + "\n")
    report.write(f"Rows    : {df.shape[0]}\n")
    report.write(f"Columns : {df.shape[1]}\n\n")

    # Column Names
    report.write("COLUMN NAMES\n")
    report.write("-" * 40 + "\n")

    for column in df.columns:
        report.write(f"{column}\n")

    report.write("\n")

    # Data Types
    report.write("DATA TYPES\n")
    report.write("-" * 40 + "\n")
    report.write(df.dtypes.to_string())

    report.write("\n\n")

    # Missing Values
    report.write("MISSING VALUES\n")
    report.write("-" * 40 + "\n")
    report.write(df.isnull().sum().to_string())

    report.write("\n\n")

    # Duplicate Rows
    report.write("DUPLICATE ROWS\n")
    report.write("-" * 40 + "\n")
    report.write(f"{df.duplicated().sum()}")

    report.write("\n\n")

    # Summary Statistics
    report.write("SUMMARY STATISTICS\n")
    report.write("-" * 40 + "\n")
    report.write(df.describe().to_string())

    report.write("\n\n")

    # Customer Types
    report.write("CUSTOMER TYPES\n")
    report.write("-" * 40 + "\n")
    report.write(df["Customer_Type"].value_counts().to_string())

    report.write("\n\n")

    # Restaurant Types
    report.write("RESTAURANT TYPES\n")
    report.write("-" * 40 + "\n")
    report.write(df["Restaurant_Type"].value_counts().to_string())

    report.write("\n\n")

    # Cities
    report.write("CITY DISTRIBUTION\n")
    report.write("-" * 40 + "\n")
    report.write(df["City"].value_counts().to_string())

    report.write("\n\n")

    # Weather
    report.write("WEATHER CONDITIONS\n")
    report.write("-" * 40 + "\n")
    report.write(df["Weather_Condition"].value_counts().to_string())

    report.write("\n\n")

    # Traffic
    report.write("TRAFFIC LEVELS\n")
    report.write("-" * 40 + "\n")
    report.write(df["Traffic_Level"].value_counts().to_string())

print("✅ Data Assessment Report created successfully!")