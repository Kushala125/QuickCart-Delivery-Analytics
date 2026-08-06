<div align="center">

# 🛒 QuickCart Delivery Analytics

### End-to-End Data Pipeline & Business Intelligence for a Multi-City Food Delivery Platform

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=flat-square&logo=pandas&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20RDS-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Data%20Warehouse-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-Dashboards-E97627?style=flat-square&logo=tableau&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

*A complete data analytics case study built on 150,000 delivery orders across 5 global cities — covering ETL, exploratory data analysis, statistical correlation, and executive reporting.*

</div>

---

## 📑 Table of Contents

1. [Project Overview](#-project-overview)
2. [Tech Stack](#-tech-stack)
3. [Repository Structure](#-repository-structure)
4. [Dataset](#-dataset)
5. [AWS Infrastructure](#-aws-infrastructure)
6. [ETL Pipeline](#-etl-pipeline)
7. [ETL Logger](#-etl-logger)
8. [SQL Analysis](#-sql-analysis)
9. [Executive KPI Summary](#-executive-kpi-summary)
10. [Visual Analytics](#-visual-analytics)
    - [Revenue Analysis](#-revenue-analysis)
    - [Delivery Performance](#-delivery-performance)
    - [Customer Behaviour](#-customer-behaviour)
    - [Risk & Correlation Analysis](#-risk--correlation-analysis)
11. [Key Insights](#-key-insights)
12. [Getting Started](#-getting-started)
13. [License](#-license)

---

## 🧭 Project Overview

**QuickCart Delivery Analytics** simulates a real-world data analyst workflow for an online food delivery marketplace operating across **Singapore, London, New York, Mumbai, and Sydney**. The project ingests raw order-level data, moves it through a Python-based ETL pipeline into a MySQL data warehouse hosted on AWS RDS, and produces a full suite of exploratory visualizations and an executive-ready KPI report.

The goal is to answer the kinds of questions a delivery platform's operations and growth teams actually ask:

- Which cities and restaurant categories drive the most revenue?
- How do traffic and weather conditions affect delivery time?
- What does the relationship between delivery distance and delivery time look like?
- Which customers are most likely to churn, and why?
- Is there a link between order value, ratings, and complaints?

---

## 🛠 Tech Stack

| Layer | Tools |
|---|---|
| **Ingestion** | AWS S3 (raw data lake), `boto3` |
| **Transformation** | Python, Pandas, NumPy |
| **Warehouse** | MySQL on AWS RDS, `SQLAlchemy` |
| **Analysis** | Pandas, NumPy, statistical correlation |
| **Visualization** | Matplotlib, Seaborn |
| **BI / Dashboards** | Tableau |
| **Logging** | Python `logging` module |
| **Environment** | `venv`, `.env` config |

---

## 🗂 Repository Structure

```
QuickCart-Delivery-Analytics/
│
├── data/
│   ├── raw/                    # Original extracted data (150,000 rows)
│   └── processed/              # Cleaned & transformed data
│
├── python/
│   ├── etl/
│   │   ├── extract.py          # Pulls raw data from S3
│   │   ├── transform.py        # Cleans & reshapes the dataset
│   │   ├── load.py             # Loads data into MySQL RDS
│   │   ├── pipeline.py         # Orchestrates the ETL run
│   │   └── logger.py           # Centralized logging config
│   │
│   ├── eda.py                  # Core exploratory data analysis
│   ├── data.py                 # Data assessment / profiling
│   ├── vis.py                  # Shared visualization helpers
│   ├── monthly_revenue.py
│   ├── customer_revenue.py
│   ├── restaurant_ratings.py
│   ├── traffic_delivery.py
│   ├── weather_delivery.py
│   ├── distance_vs_delivery.py
│   ├── customer_age_order_value.py
│   ├── order_value_vs_rating.py
│   ├── complaint_rate_city.py
│   ├── demand_score_distribution.py
│   └── correlation_heatmap.py
│
├── sql/                        # Warehouse queries
├── aws/                        # AWS configuration & IaC notes
├── tableau/                    # Tableau workbooks
├── reports/                    # Generated CSV & Markdown reports
├── screenshots/                # Chart exports referenced in this README
├── docs/                       # Additional documentation
├── etl.log                     # Latest pipeline run log
└── README.md
```

---

## 📊 Dataset

The pipeline processes **150,000 order records** across **21 columns**, with **zero missing values** and **zero duplicate rows** — a clean, analysis-ready dataset.

| Field | Description |
|---|---|
| `Order_ID` | Unique identifier per order |
| `Customer_Age`, `Customer_Type` | Demographics (New / Returning / Premium) |
| `Restaurant_Type`, `Cuisine_Type` | Merchant category |
| `Delivery_Distance_KM`, `Delivery_Time_Min` | Logistics metrics |
| `Order_Value_USD`, `Item_Count` | Transaction size |
| `Weather_Condition`, `Traffic_Level` | External delivery conditions |
| `Customer_Rating`, `Complaint_Flag`, `Refund_Flag` | Satisfaction signals |
| `Revenue_USD`, `Profit_USD` | Financial outcome |
| `City`, `Month`, `Quarter` | Dimensions for slicing |
| `Demand_Score`, `Churn_Risk` | Derived business scores |

**Distribution highlights:**

| Dimension | Breakdown |
|---|---|
| **Customer Type** | New: 50,185 · Returning: 49,912 · Premium: 49,903 |
| **Restaurant Type** | Cafe: 37,743 · Fast Food: 37,528 · Cloud Kitchen: 37,387 · Restaurant: 37,342 |
| **City** | Singapore: 30,236 · New York: 30,108 · London: 29,939 · Mumbai: 29,923 · Sydney: 29,794 |
| **Weather** | Sunny: 37,610 · Cloudy: 37,497 · Stormy: 37,447 · Rainy: 37,446 |
| **Traffic** | Low: 50,105 · Medium: 49,997 · High: 49,898 |

---

## ☁️ AWS Infrastructure

The pipeline runs on two managed AWS services in the **`ap-south-1` (Mumbai)** region: an S3 bucket as the raw data lake, and an RDS MySQL instance as the analytical warehouse.

<table>
<tr>
<td width="50%">

**Amazon S3 — Raw Data Lake**
Incoming order data lands in the `quickcart-food-delivery-kush1250` bucket as a flat CSV (`del.csv`, ~16.3 MB). This is the single source of truth that `extract.py` reads from at the start of every pipeline run.

![S3 Bucket](screenshots/aws_s3_console.png)

</td>
<td width="50%">

**Amazon RDS — MySQL Warehouse**
The transformed data is loaded into `quickcart-db2`, a MySQL instance running on a `db.t4g.micro` node. This is the `delivery_data` table that `load.py` writes into, and the same instance the executive reports and Tableau dashboards query from.

![RDS Database](screenshots/aws_rds_console.png)

</td>
</tr>
</table>

**Why this setup:**
- **S3** decouples ingestion from processing — new data can be dropped into the bucket at any time without touching the pipeline code.
- **RDS (MySQL)** gives the analytics scripts and Tableau a stable, queryable warehouse instead of re-reading a flat file on every run.
- **`db.t4g.micro`** keeps this a low-cost setup appropriate for a portfolio-scale dataset (150K rows); a production version would size up and add a read replica.

---

## 🔄 ETL Pipeline

The `python/etl/` package runs a fully logged, three-stage pipeline: **Extract → Transform → Load**, orchestrated by `pipeline.py`.

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  1. EXTRACT  │ ──▶ │ 2. TRANSFORM │ ──▶ │  3. LOAD    │
│ extract.py   │     │ transform.py │     │  load.py    │
└─────────────┘     └──────────────┘     └─────────────┘
      │                     │                    │
      ▼                     ▼                    ▼
  Pull the CSV        Clean, type-cast,     Write the final
  from the S3          and reshape with      table into
  bucket via            Pandas               MySQL on RDS
  boto3                                       via SQLAlchemy
```

**What each stage does:**

| Stage | File | Responsibility |
|---|---|---|
| **Extract** | `extract.py` | Connects to S3 with `boto3`, locates the source CSV, and reads it into memory. |
| **Transform** | `transform.py` | Validates row counts, fixes data types, and reshapes columns into the warehouse schema. |
| **Load** | `load.py` | Opens a `SQLAlchemy` engine against the RDS MySQL endpoint and bulk-writes the cleaned data into the `delivery_data` table. |
| **Orchestration** | `pipeline.py` | Runs the three stages in sequence, timing the run and stopping on the first failure. |

> ⏱ **Full pipeline runtime: ~24.6 seconds** for 150,000 rows, extract to load.

> 🔐 **Security note:** credentials are read from a local AWS credentials file / `.env` and are **never committed to source control**. If you fork this project, populate your own `python/e.env` and AWS credentials locally — don't reuse or share the ones from this repo's history.

---

## 🪵 ETL Logger

Every pipeline run is logged end-to-end by `logger.py`, which configures a single shared Python `logging` instance used by `extract.py`, `transform.py`, and `load.py`. Each stage logs its own start, result, and row counts, so a full run is traceable from one log file without needing to add print statements.

**Actual run log** (`etl.log`, redacted of host/IP for this README):

```
2026-08-05 18:36:17,246 | INFO | ========== ETL Pipeline Started ==========
2026-08-05 18:36:17,246 | INFO | Starting data extraction from S3
2026-08-05 18:36:17,255 | INFO | Found credentials in shared credentials file: ~/.aws/credentials
2026-08-05 18:36:18,695 | INFO | Successfully extracted 150000 rows from S3
2026-08-05 18:36:18,696 | INFO | Starting data transformation
2026-08-05 18:36:18,754 | INFO | Transformation completed. Rows before: 150000, Rows after: 150000
2026-08-05 18:36:18,754 | INFO | Connecting to MySQL RDS
2026-08-05 18:36:41,845 | INFO | Successfully loaded 150000 rows into delivery_data
2026-08-05 18:36:41,846 | INFO | ETL Pipeline completed successfully
2026-08-05 18:36:41,846 | INFO | Pipeline execution time: 24.6 seconds
2026-08-05 18:36:41,846 | INFO | ========== ETL Pipeline Finished ==========
```

**Reading the log, stage by stage:**

1. **Pipeline start** — a clear `====` banner marks the beginning of the run, making individual runs easy to spot when scrolling through history.
2. **Extraction** — confirms AWS credentials were found locally, then confirms the exact row count pulled from S3 (150,000 rows), so a silent partial read would be immediately visible.
3. **Transformation** — logs row counts **before and after** cleaning (150,000 → 150,000 here), which is the quickest way to catch accidental row drops during transformation.
4. **Load** — logs the RDS connection step, then confirms the exact number of rows written into `delivery_data`.
5. **Completion** — logs total pipeline execution time (24.6 seconds) and a closing banner, giving a simple performance benchmark for every run.

> 🔐 The real `etl.log` includes the RDS host address on the "Connecting to MySQL RDS" line — that's been removed here since a database endpoint is infrastructure detail that shouldn't be published in a public README.

---

## 🗄 SQL Analysis

Once the data lands in `delivery_data` on MySQL RDS, `sql/QuickCart_SQL_Analysis.sql` runs **25 business questions** directly against the warehouse — everything from top-line revenue to churn-risk quartiles — using progressively more advanced SQL: aggregates, `CASE` bucketing, CTEs, and window functions (`RANK`, `ROW_NUMBER`, `LAG`, `NTILE`).

### Table Schema

```sql
CREATE TABLE delivery_data (
    Order_ID              VARCHAR(20)   PRIMARY KEY,
    Customer_Age          TINYINT UNSIGNED,
    Customer_Type         VARCHAR(20),
    Restaurant_Type       VARCHAR(20),
    Cuisine_Type          VARCHAR(20),
    Delivery_Distance_KM  DECIMAL(6,2),
    Delivery_Time_Min     SMALLINT UNSIGNED,
    Order_Value_USD       DECIMAL(8,2),
    Item_Count             TINYINT UNSIGNED,
    Weather_Condition     VARCHAR(20),
    Traffic_Level          VARCHAR(10),
    Customer_Rating        DECIMAL(3,1),
    Complaint_Flag         TINYINT(1),
    Refund_Flag             TINYINT(1),
    Revenue_USD             DECIMAL(8,2),
    Profit_USD               DECIMAL(8,2),
    City                      VARCHAR(20),
    Month                      TINYINT UNSIGNED,
    Quarter                   TINYINT UNSIGNED,
    Demand_Score               DECIMAL(5,2),
    Churn_Risk                  DECIMAL(5,2),
    INDEX idx_city (City),
    INDEX idx_cuisine (Cuisine_Type),
    INDEX idx_restaurant_type (Restaurant_Type),
    INDEX idx_month (Month)
);
```

Loaded with `LOAD DATA LOCAL INFILE` from the same `del.csv` extracted by the ETL pipeline — confirmed with `SELECT COUNT(*)` returning exactly **150,000** rows.

### The 25 Business Questions

Every query below was run against the full dataset; results and a one-line explanation are included with each. Click a question to expand it.

<details>
<summary><b>Q1. What is the overall business performance in terms of revenue, profit, and average order value?</b></summary>

```sql
SELECT
    COUNT(*) AS Total_Delivery_Data,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
    ROUND(SUM(Profit_USD),2) AS Total_Profit,
    ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value,
    ROUND(SUM(Profit_USD)/SUM(Revenue_USD)*100,2) AS Profit_Margin_Pct
FROM delivery_data;
```

| Total Orders | Total Revenue | Total Profit | Avg Order Value | Profit Margin % |
|---:|---:|---:|---:|---:|
| 150,000 | $37,843,112.84 | $13,504,910.56 | $152.89 | 35.69% |

**Explanation:** The business runs a healthy ~35.7% profit margin on revenue across 150,000 orders, with an average order value of ~$153.
</details>

<details>
<summary><b>Q2. Which cities generate the most revenue and profit?</b></summary>

```sql
SELECT City, COUNT(*) AS Delivery_Data,
       ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
       ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM delivery_data
GROUP BY City
ORDER BY Total_Revenue DESC;
```

| City | Orders | Total Revenue | Total Profit |
|---|---:|---:|---:|
| Singapore | 30,236 | $7,632,153.44 | $2,735,593.54 |
| London | 29,939 | $7,588,105.17 | $2,695,977.33 |
| New York | 30,108 | $7,587,788.92 | $2,711,426.13 |
| Mumbai | 29,923 | $7,563,571.09 | $2,680,502.10 |
| Sydney | 29,794 | $7,471,494.22 | $2,681,411.46 |

**Explanation:** Revenue is remarkably evenly spread across all 5 cities (within ~2% of each other) — order volume is balanced, not concentrated in one market.
</details>

<details>
<summary><b>Q3. Which cuisine types drive the highest average order value and revenue?</b></summary>

```sql
SELECT Cuisine_Type, COUNT(*) AS Delivery_Data,
       ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value,
       ROUND(SUM(Revenue_USD),2) AS Total_Revenue
FROM delivery_data
GROUP BY Cuisine_Type
ORDER BY Total_Revenue DESC;
```

| Cuisine | Orders | Avg Order Value | Total Revenue |
|---|---:|---:|---:|
| Indian | 37,635 | $152.95 | $9,512,377.10 |
| Mexican | 37,420 | $152.81 | $9,444,313.95 |
| Chinese | 37,403 | $153.05 | $9,443,342.57 |
| Italian | 37,542 | $152.75 | $9,443,079.22 |

**Explanation:** Cuisine mix is essentially uniform — no single cuisine dominates the platform.
</details>

<details>
<summary><b>Q4. Which restaurant type is most profitable?</b></summary>

```sql
SELECT Restaurant_Type, COUNT(*) AS Delivery_Data,
       ROUND(SUM(Profit_USD),2) AS Total_Profit,
       ROUND(AVG(Profit_USD),2) AS Avg_Profit_Per_Order
FROM delivery_data
GROUP BY Restaurant_Type
ORDER BY Total_Profit DESC;
```

| Restaurant Type | Orders | Total Profit | Avg Profit/Order |
|---|---:|---:|---:|
| Cafe | 37,743 | $3,393,147.78 | $89.90 |
| Fast Food | 37,528 | $3,387,006.02 | $90.25 |
| Restaurant | 37,342 | $3,362,672.10 | $90.05 |
| Cloud Kitchen | 37,387 | $3,362,084.66 | $89.93 |

**Explanation:** All four restaurant formats perform almost identically on profit per order — format alone isn't a profit lever in this data.
</details>

<details>
<summary><b>Q5. How does revenue trend across the 12 months?</b></summary>

```sql
SELECT Month, COUNT(*) AS Delivery_Data, ROUND(SUM(Revenue_USD),2) AS Total_Revenue
FROM delivery_data
GROUP BY Month
ORDER BY Month;
```

| Month | Orders | Revenue |
|---:|---:|---:|
| 1 | 12,695 | $3,185,693.65 |
| 2 | 11,617 | $2,940,248.09 |
| 3 | 12,827 | $3,227,482.16 |
| 4 | 12,295 | $3,105,546.55 |
| 5 | 12,872 | $3,237,190.26 |
| 6 | 12,365 | $3,117,157.08 |
| 7 | 12,761 | $3,215,965.77 |
| 8 | 12,798 | $3,235,179.82 |
| 9 | 12,368 | $3,122,749.79 |
| 10 | 12,527 | $3,143,781.09 |
| 11 | 12,369 | $3,139,674.95 |
| 12 | 12,506 | $3,172,443.63 |

**Explanation:** Revenue is stable year-round (~$2.9M–$3.2M/month); February is the low point, likely because it has fewer days.
</details>

<details>
<summary><b>Q6. How do quarters compare in orders, revenue, and average customer rating?</b></summary>

```sql
SELECT Quarter, COUNT(*) AS Delivery_Data,
       ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
       ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM delivery_data
GROUP BY Quarter
ORDER BY Quarter;
```

| Quarter | Orders | Revenue | Avg Rating |
|---:|---:|---:|---:|
| 1 | 37,139 | $9,353,423.90 | 3.00 |
| 2 | 37,532 | $9,459,893.89 | 3.00 |
| 3 | 37,927 | $9,573,895.38 | 2.99 |
| 4 | 37,402 | $9,455,899.67 | 3.00 |

**Explanation:** Customer satisfaction (avg rating ~3.0/5) is flat across quarters — no seasonal service quality swings.
</details>

<details>
<summary><b>Q7. How do New, Returning, and Premium customers differ in spend and churn risk?</b></summary>

```sql
SELECT Customer_Type, COUNT(*) AS Delivery_Data,
       ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value,
       ROUND(AVG(Churn_Risk),2) AS Avg_Churn_Risk,
       ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM delivery_data
GROUP BY Customer_Type
ORDER BY Avg_Order_Value DESC;
```

| Customer Type | Orders | Avg Order Value | Avg Churn Risk | Avg Rating |
|---|---:|---:|---:|---:|
| Premium | 49,903 | $153.22 | 49.82 | 3.00 |
| Returning | 49,912 | $153.08 | 50.00 | 3.01 |
| New | 50,185 | $152.37 | 49.95 | 3.00 |

**Explanation:** Premium customers spend only marginally more than New/Returning — the "Premium" tier isn't translating into materially higher basket size.
</details>

<details>
<summary><b>Q8. Does traffic congestion correlate with higher complaint rates?</b></summary>

```sql
SELECT Traffic_Level, COUNT(*) AS Delivery_Data,
       SUM(Complaint_Flag) AS Complaints,
       ROUND(SUM(Complaint_Flag)*100.0/COUNT(*),2) AS Complaint_Rate_Pct,
       ROUND(AVG(Delivery_Time_Min),2) AS Avg_Delivery_Time
FROM delivery_data
GROUP BY Traffic_Level
ORDER BY Complaint_Rate_Pct DESC;
```

| Traffic Level | Orders | Complaints | Complaint Rate % | Avg Delivery Time |
|---|---:|---:|---:|---:|
| Low | 50,105 | 5,079 | 10.14% | 64.54 min |
| High | 49,898 | 5,047 | 10.11% | 64.55 min |
| Medium | 49,997 | 4,978 | 9.96% | 64.49 min |

**Explanation:** Contrary to intuition, traffic level shows no meaningful effect on complaint rate or delivery time — congestion isn't the driver of service issues in this dataset.
</details>

<details>
<summary><b>Q9. How does weather condition impact average delivery time and demand?</b></summary>

```sql
SELECT Weather_Condition, COUNT(*) AS Delivery_Data,
       ROUND(AVG(Delivery_Time_Min),2) AS Avg_Delivery_Time,
       ROUND(AVG(Demand_Score),2) AS Avg_Demand_Score
FROM delivery_data
GROUP BY Weather_Condition
ORDER BY Avg_Delivery_Time DESC;
```

| Weather | Orders | Avg Delivery Time | Avg Demand Score |
|---|---:|---:|---:|
| Stormy | 37,447 | 64.60 min | 50.03 |
| Rainy | 37,446 | 64.54 min | 50.17 |
| Cloudy | 37,497 | 64.52 min | 49.98 |
| Sunny | 37,610 | 64.45 min | 50.06 |

**Explanation:** Weather has negligible impact on delivery time in this data — delivery time is likely generated independently of weather.
</details>

<details>
<summary><b>Q10. Which cities have the most customers at high risk of churn (Churn_Risk &gt; 80)?</b></summary>

```sql
SELECT City, COUNT(*) AS High_Risk_Customers,
       ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM delivery_data
WHERE Churn_Risk > 80
GROUP BY City
ORDER BY High_Risk_Customers DESC;
```

| City | High-Risk Customers | Avg Rating |
|---|---:|---:|
| Mumbai | 6,085 | 3.00 |
| Singapore | 6,074 | 3.02 |
| New York | 6,069 | 2.98 |
| London | 6,034 | 3.00 |
| Sydney | 5,909 | 2.99 |

**Explanation:** About 20% of orders in every city carry high churn risk (>80) — this is a uniform retention challenge, not a city-specific one.
</details>

<details>
<summary><b>Q11. Do refunded orders tend to also have complaints, and what's the profit impact?</b></summary>

```sql
SELECT Refund_Flag, COUNT(*) AS Delivery_Data,
       SUM(Complaint_Flag) AS Complaints_In_Group,
       ROUND(AVG(Profit_USD),2) AS Avg_Profit,
       ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM delivery_data
GROUP BY Refund_Flag;
```

| Refunded? | Orders | Complaints in Group | Avg Profit | Total Profit |
|---|---:|---:|---:|---:|
| No | 142,692 | 14,405 | $90.05 | $12,848,971.89 |
| Yes | 7,308 | 699 | $89.76 | $655,938.67 |

**Explanation:** ~4.9% of orders are refunded; refunded orders still generate near-identical average profit, suggesting refunds are handled as partial/goodwill credits rather than a full profit loss.
</details>

<details>
<summary><b>Q12. What are the single highest-value orders in the dataset?</b></summary>

```sql
SELECT Order_ID, City, Cuisine_Type, Order_Value_USD, Revenue_USD, Profit_USD
FROM delivery_data
ORDER BY Revenue_USD DESC
LIMIT 10;
```

| Order ID | City | Cuisine | Order Value | Revenue | Profit |
|---|---|---|---:|---:|---:|
| ORD0063686 | Mumbai | Mexican | $109.41 | $500.00 | $170.86 |
| ORD0094686 | Singapore | Chinese | $52.66 | $500.00 | $178.72 |
| ORD0006516 | New York | Mexican | $245.45 | $499.99 | $105.22 |
| ORD0060038 | Singapore | Indian | $110.09 | $499.99 | $154.13 |
| ORD0112804 | London | Indian | $43.65 | $499.99 | $7.02 |

**Explanation:** Revenue appears capped near $500 — worth flagging as a possible data-generation ceiling rather than a real-world cap.
</details>

<details>
<summary><b>Q13. Rank cities by total profit with a window function, showing each city's share of total profit</b></summary>

```sql
WITH city_profit AS (
    SELECT City, ROUND(SUM(Profit_USD),2) AS Total_Profit
    FROM delivery_data
    GROUP BY City
)
SELECT City, Total_Profit,
       RANK() OVER (ORDER BY Total_Profit DESC) AS Profit_Rank,
       ROUND(100.0 * Total_Profit / SUM(Total_Profit) OVER (), 2) AS Pct_Of_Total_Profit
FROM city_profit
ORDER BY Profit_Rank;
```

| City | Total Profit | Rank | % of Total Profit |
|---|---:|---:|---:|
| Singapore | $2,735,593.54 | 1 | 20.26% |
| New York | $2,711,426.13 | 2 | 20.08% |
| London | $2,695,977.33 | 3 | 19.96% |
| Sydney | $2,681,411.46 | 4 | 19.86% |
| Mumbai | $2,680,502.10 | 5 | 19.85% |

**Explanation:** Singapore edges out as the #1 city by profit, but the spread across all 5 is under half a percentage point.
</details>

<details>
<summary><b>Q14. How many orders per cuisine exceed that cuisine's own average order value?</b></summary>

```sql
WITH cuisine_avg AS (
    SELECT Cuisine_Type, AVG(Order_Value_USD) AS Avg_Value
    FROM delivery_data
    GROUP BY Cuisine_Type
)
SELECT o.Cuisine_Type, COUNT(*) AS Delivery_Data_Above_Avg
FROM delivery_data o
JOIN cuisine_avg c ON o.Cuisine_Type = c.Cuisine_Type
WHERE o.Order_Value_USD > c.Avg_Value
GROUP BY o.Cuisine_Type
ORDER BY Delivery_Data_Above_Avg DESC;
```

| Cuisine | Orders Above Cuisine Average |
|---|---:|
| Indian | 18,876 |
| Chinese | 18,770 |
| Italian | 18,763 |
| Mexican | 18,705 |

**Explanation:** Roughly half of every cuisine's orders sit above its own average — consistent with a fairly symmetric order-value distribution. Written as a CTE joined once per group rather than a correlated subquery re-executed per row — the standard optimization for this pattern at 150K-row scale.
</details>

<details>
<summary><b>Q15. How are orders distributed across low/medium/high value buckets, and what's each bucket's profit contribution?</b></summary>

```sql
SELECT
    CASE
        WHEN Order_Value_USD < 100 THEN 'Low (<$100)'
        WHEN Order_Value_USD BETWEEN 100 AND 300 THEN 'Medium ($100-$300)'
        ELSE 'High (>$300)'
    END AS Value_Bucket,
    COUNT(*) AS Delivery_Data,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
    ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM delivery_data
GROUP BY Value_Bucket
ORDER BY Total_Revenue DESC;
```

| Value Bucket | Orders | Total Revenue | Total Profit |
|---|---:|---:|---:|
| Medium ($100–$300) | 101,953 | $25,720,244.46 | $9,170,193.04 |
| Low (<$100) | 48,047 | $12,122,868.38 | $4,334,717.52 |

**Explanation:** No orders fall in the "High (>$300)" bucket — the mid-tier ($100–$300) basket is the core of the business, driving ~68% of revenue.
</details>

<details>
<summary><b>Q16. For each city, which cuisine type generates the most revenue?</b></summary>

```sql
WITH ranked AS (
    SELECT City, Cuisine_Type, SUM(Revenue_USD) AS Cuisine_Revenue,
           ROW_NUMBER() OVER (PARTITION BY City ORDER BY SUM(Revenue_USD) DESC) AS rn
    FROM delivery_data
    GROUP BY City, Cuisine_Type
)
SELECT City, Cuisine_Type, ROUND(Cuisine_Revenue,2) AS Cuisine_Revenue
FROM ranked
WHERE rn = 1
ORDER BY Cuisine_Revenue DESC;
```

| City | Top Cuisine | Revenue |
|---|---|---:|
| Singapore | Indian | $1,938,917.85 |
| Mumbai | Indian | $1,928,308.05 |
| London | Italian | $1,925,235.27 |
| New York | Chinese | $1,909,726.04 |
| Sydney | Chinese | $1,887,207.59 |

**Explanation:** Cuisine preference does vary meaningfully by city — Indian food leads in Singapore/Mumbai, Italian in London, Chinese in New York/Sydney. Useful for city-specific menu and marketing decisions.
</details>

<details>
<summary><b>Q17. How does customer rating change as delivery time increases?</b></summary>

```sql
SELECT
    CASE
        WHEN Delivery_Time_Min <= 30 THEN '0-30 min'
        WHEN Delivery_Time_Min <= 60 THEN '31-60 min'
        WHEN Delivery_Time_Min <= 90 THEN '61-90 min'
        ELSE '90+ min'
    END AS Delivery_Time_Bucket,
    COUNT(*) AS Delivery_Data,
    ROUND(AVG(Customer_Rating),2) AS Avg_Rating,
    ROUND(SUM(Complaint_Flag)*100.0/COUNT(*),2) AS Complaint_Rate_Pct
FROM delivery_data
GROUP BY Delivery_Time_Bucket
ORDER BY MIN(Delivery_Time_Min);
```

| Delivery Time | Orders | Avg Rating | Complaint Rate % |
|---|---:|---:|---:|
| 0–30 min | 28,590 | 3.01 | 10.25% |
| 31–60 min | 40,849 | 3.00 | 9.84% |
| 61–90 min | 41,119 | 3.00 | 10.21% |
| 90+ min | 39,442 | 3.00 | 10.03% |

**Explanation:** Ratings and complaint rates barely move with delivery time — customer satisfaction here isn't primarily driven by speed.
</details>

<details>
<summary><b>Q18. What is the month-over-month revenue growth rate?</b></summary>

```sql
WITH monthly AS (
    SELECT Month, SUM(Revenue_USD) AS Revenue
    FROM delivery_data
    GROUP BY Month
)
SELECT Month, ROUND(Revenue,2) AS Revenue,
       ROUND(Revenue - LAG(Revenue) OVER (ORDER BY Month),2) AS Change_vs_Prev_Month,
       ROUND((Revenue - LAG(Revenue) OVER (ORDER BY Month)) * 100.0
             / LAG(Revenue) OVER (ORDER BY Month),2) AS Growth_Pct
FROM monthly
ORDER BY Month;
```

| Month | Revenue | Change vs Prev | Growth % |
|---:|---:|---:|---:|
| 1 | $3,185,693.65 | — | — |
| 2 | $2,940,248.09 | -$245,445.56 | -7.70% |
| 3 | $3,227,482.16 | +$287,234.07 | +9.77% |
| 4 | $3,105,546.55 | -$121,935.61 | -3.78% |
| 5 | $3,237,190.26 | +$131,643.71 | +4.24% |
| 6 | $3,117,157.08 | -$120,033.18 | -3.71% |
| 7 | $3,215,965.77 | +$98,808.69 | +3.17% |
| 8 | $3,235,179.82 | +$19,214.05 | +0.60% |
| 9 | $3,122,749.79 | -$112,430.03 | -3.48% |
| 10 | $3,143,781.09 | +$21,031.30 | +0.67% |
| 11 | $3,139,674.95 | -$4,106.14 | -0.13% |
| 12 | $3,172,443.63 | +$32,768.68 | +1.04% |

**Explanation:** Revenue oscillates in a tight ±10% band month to month with no sustained growth or decline trend — a mature, stable-demand business.
</details>

<details>
<summary><b>Q19. Which cities have an average order value higher than the platform-wide average?</b></summary>

```sql
SELECT City, ROUND(AVG(Order_Value_USD),2) AS City_Avg_Order_Value
FROM delivery_data
GROUP BY City
HAVING AVG(Order_Value_USD) > (SELECT AVG(Order_Value_USD) FROM delivery_data)
ORDER BY City_Avg_Order_Value DESC;
```

| City | Avg Order Value |
|---|---:|
| Mumbai | $153.40 |
| Singapore | $153.33 |
| New York | $152.99 |

**Explanation:** Only 3 of the 5 cities beat the global average order value — London and Sydney sit just below it, though the gap is small (~$1–2).
</details>

<details>
<summary><b>Q20. Which restaurant type has the highest complaint rate?</b></summary>

```sql
SELECT Restaurant_Type, COUNT(*) AS Delivery_Data,
       SUM(Complaint_Flag) AS Complaints,
       ROUND(SUM(Complaint_Flag)*100.0/COUNT(*),2) AS Complaint_Rate_Pct
FROM delivery_data
GROUP BY Restaurant_Type
ORDER BY Complaint_Rate_Pct DESC;
```

| Restaurant Type | Orders | Complaints | Complaint Rate % |
|---|---:|---:|---:|
| Restaurant | 37,342 | 3,816 | 10.22% |
| Cafe | 37,743 | 3,784 | 10.03% |
| Fast Food | 37,528 | 3,761 | 10.02% |
| Cloud Kitchen | 37,387 | 3,743 | 10.01% |

**Explanation:** Complaint rates are essentially flat (~10%) across all restaurant formats — no format stands out as a quality problem area.
</details>

<details>
<summary><b>Q21. How do delivery distance and delivery time compare across cities?</b></summary>

```sql
SELECT City, ROUND(AVG(Delivery_Distance_KM),2) AS Avg_Distance_KM,
       ROUND(AVG(Delivery_Time_Min),2) AS Avg_Delivery_Time_Min
FROM delivery_data
GROUP BY City
ORDER BY Avg_Distance_KM DESC;
```

| City | Avg Distance (km) | Avg Delivery Time (min) |
|---|---:|---:|
| Mumbai | 12.81 | 64.70 |
| New York | 12.76 | 64.48 |
| London | 12.75 | 64.58 |
| Singapore | 12.75 | 64.26 |
| Sydney | 12.73 | 64.63 |

**Explanation:** Delivery distance and time are nearly identical across all 5 cities (~12.7–12.8 km, ~64–65 min) — logistics performance is consistent globally, not a differentiator between markets.
</details>

<details>
<summary><b>Q22. Does ordering more items increase the average order value?</b></summary>

```sql
SELECT
    CASE
        WHEN Item_Count <= 5 THEN '1-5 items'
        WHEN Item_Count <= 10 THEN '6-10 items'
        ELSE '11-14 items'
    END AS Item_Count_Bucket,
    COUNT(*) AS Delivery_Data,
    ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value
FROM delivery_data
GROUP BY Item_Count_Bucket
ORDER BY MIN(Item_Count);
```

| Item Count | Orders | Avg Order Value |
|---|---:|---:|
| 1–5 items | 53,487 | $152.68 |
| 6–10 items | 53,639 | $153.25 |
| 11–14 items | 42,874 | $152.69 |

**Explanation:** No relationship between item count and order value — orders with 1–5 items cost about the same on average as orders with 11–14 items, meaning per-item price effectively scales down as basket size grows.
</details>

<details>
<summary><b>Q23. How does customer rating differ across churn-risk quartiles?</b></summary>

```sql
WITH quartiles AS (
    SELECT Customer_Rating, Churn_Risk,
           NTILE(4) OVER (ORDER BY Churn_Risk) AS Churn_Quartile
    FROM delivery_data
)
SELECT Churn_Quartile, COUNT(*) AS Delivery_Data,
       ROUND(MIN(Churn_Risk),2) AS Min_Churn_Risk,
       ROUND(MAX(Churn_Risk),2) AS Max_Churn_Risk,
       ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM quartiles
GROUP BY Churn_Quartile
ORDER BY Churn_Quartile;
```

| Quartile | Orders | Min Churn Risk | Max Churn Risk | Avg Rating |
|---|---:|---:|---:|---:|
| 1 (lowest risk) | 37,500 | 0.00 | 24.88 | 3.00 |
| 2 | 37,500 | 24.88 | 49.83 | 3.00 |
| 3 | 37,500 | 49.83 | 75.00 | 2.99 |
| 4 (highest risk) | 37,500 | 75.00 | 100.00 | 3.00 |

**Explanation:** Customer rating is flat across churn-risk quartiles — high-risk customers aren't rating their experience any lower than low-risk ones, suggesting churn risk here is driven by factors other than satisfaction (e.g. price sensitivity, competition).
</details>

<details>
<summary><b>Q24. Which cuisine types have the most loss-making orders (negative profit)?</b></summary>

```sql
SELECT Cuisine_Type, COUNT(*) AS Loss_Making_Delivery_Data
FROM delivery_data
WHERE Profit_USD < 0
GROUP BY Cuisine_Type
ORDER BY Loss_Making_Delivery_Data DESC;
```

| Cuisine | Loss-Making Orders |
|---|---:|
| Italian | 3,440 |
| Indian | 3,393 |
| Chinese | 3,357 |
| Mexican | 3,356 |

**Explanation:** ~9% of all orders (13,546 of 150,000) are loss-making, spread almost evenly across cuisines — this isn't a cuisine-specific cost problem, it's a platform-wide pattern worth investigating (e.g. discounting, delivery cost outliers).
</details>

<details>
<summary><b>Q25. Which cities have a profit margin higher than the company-wide average?</b></summary>

```sql
SELECT City, ROUND(SUM(Profit_USD)*100.0/SUM(Revenue_USD),2) AS City_Profit_Margin_Pct
FROM delivery_data
GROUP BY City
HAVING SUM(Profit_USD)*100.0/SUM(Revenue_USD) > (
    SELECT SUM(Profit_USD)*100.0/SUM(Revenue_USD) FROM delivery_data
)
ORDER BY City_Profit_Margin_Pct DESC;
```

| City | Profit Margin % |
|---|---:|
| Sydney | 35.89% |
| Singapore | 35.84% |
| New York | 35.73% |

**Explanation:** Sydney, Singapore, and New York run above the company-wide 35.69% margin, while London and Mumbai sit slightly below — a useful lens for margin-improvement initiatives even though the differences are small.
</details>

### SQL Techniques Showcased

`Aggregates (SUM/AVG/COUNT/ROUND)` · `GROUP BY / ORDER BY` · `HAVING with scalar subqueries` · `CASE WHEN bucketing` · `CTEs (WITH)` · `Window functions (RANK, ROW_NUMBER + PARTITION BY, LAG, NTILE, SUM OVER)` · `correlated-subquery → JOIN optimization` · `percent-of-total & period-over-period growth calcs` · `quartile segmentation` · `conditional filtering on derived business logic`

> 📄 The full annotated file — all 25 queries with inline results and explanations exactly as run — lives at [`sql/QuickCart_SQL_Analysis.sql`](sql/QuickCart_SQL_Analysis.sql).

---

## 📈 Executive KPI Summary

| KPI | Value |
|---|---:|
| **Total Orders** | 150,000 |
| **Total Revenue** | $37,843,112.84 |
| **Total Profit** | $13,504,910.56 |
| **Average Order Value** | $152.89 |
| **Average Delivery Time** | 64.53 minutes |
| **Average Customer Rating** | 3.00 / 5 |
| **Complaint Rate** | 10.07% |
| **Refund Rate** | 4.87% |

---

## 🖼 Visual Analytics

All charts below are generated directly by the scripts in `/python` and exported to `/screenshots`.

### 💰 Revenue Analysis

<table>
<tr>
<td width="50%">

**Revenue by City**
Singapore leads narrowly at **$7.63M**, with London, New York, and Mumbai clustered tightly behind ($7.56–7.59M) and Sydney slightly lower at $7.47M — revenue is remarkably evenly distributed across all five markets.

![Revenue by City](screenshots/revenue_by_city.png)

</td>
<td width="50%">

**Revenue by Restaurant Type**
Fast Food ($9.51M), Cafe ($9.48M), Restaurant ($9.47M), and Cloud Kitchen ($9.38M) all contribute almost identically to total revenue — no single category dominates the platform.

![Revenue by Restaurant Type](screenshots/revenue_by_restaurant_type.png)

</td>
</tr>
<tr>
<td width="50%">

**Revenue by Customer Type**
New customers ($12.70M) edge out Premium ($12.58M) and Returning ($12.57M) — acquisition is currently outperforming retention in raw revenue terms.

![Revenue by Customer Type](screenshots/revenue_by_customer_type.png)

</td>
<td width="50%">

**Monthly Revenue Trend**
Revenue holds a stable band of **$2.94M–$3.24M** every month, with no strong seasonality — May and August are the strongest months.

![Monthly Revenue](screenshots/monthly_revenue_lollipop.png)

</td>
</tr>
</table>

---

### 🚚 Delivery Performance

<table>
<tr>
<td width="50%">

**Delivery Time by Traffic Level**
Average delivery time barely shifts with traffic — Medium (64.49 min), Low (64.54 min), and High (64.55 min) are nearly identical, suggesting traffic level isn't a major driver of delay in this dataset.

![Delivery Time by Traffic](screenshots/delivery_time_by_traffic.png)

</td>
<td width="50%">

**Delivery Time by Weather**
Weather shows the same flat pattern — Sunny (64.45 min) through Stormy (64.60 min) — less than a minute of spread across all conditions.

![Delivery Time by Weather](screenshots/delivery_time_by_weather.png)

</td>
</tr>
<tr>
<td width="50%">

**Distance vs. Delivery Time**
Delivery distance ranges from 0.5 km to 25 km with a mean of 12.76 km, but correlates almost not at all with delivery time (**r ≈ 0.00**) — time is being driven by other operational factors, not raw distance.

![Distance vs Delivery](screenshots/distance_vs_delivery.png)

</td>
<td width="50%">

**Delivery Distance Distribution (Hexbin)**
A density view of distance vs. time confirms orders are spread evenly across the full range, with no visible clustering pattern.

![Delivery Distance Hexbin](screenshots/delivery_distance_hexbin.png)

</td>
</tr>
</table>

---

### 🙋 Customer Behaviour

<table>
<tr>
<td width="50%">

**Customer Age vs. Order Value**
Order value shows no meaningful trend across the 18–74 customer age range — spending is consistent regardless of age.

![Customer Age vs Order Value](screenshots/customer_age_order_value.png)

</td>
<td width="50%">

**Restaurant Ratings Distribution**
Ratings are near-uniformly distributed between 1 and 5 (average **3.00**), which suggests either a very balanced merchant pool or synthetic/rounded rating behaviour worth validating.

![Restaurant Ratings Boxplot](screenshots/restaurant_ratings_boxplot.png)

</td>
</tr>
<tr>
<td width="50%">

**Order Value vs. Customer Rating**
No strong relationship between how much a customer spends and the rating they leave — high-value orders aren't systematically rated higher or lower.

![Order Value vs Rating](screenshots/order_value_vs_rating.png)

</td>
<td width="50%">

**Demand Score Distribution**
Demand scores are evenly spread from 0–100 (mean ≈ 50), indicating balanced demand intensity across the order base.

![Demand Score Distribution](screenshots/demand_score_distribution.png)

</td>
</tr>
</table>

---

### ⚠️ Risk & Correlation Analysis

<table>
<tr>
<td width="50%">

**Complaint Rate by City**
Complaint rates hover close to the platform-wide **10.07%** average across all five cities, with no single market standing out as a service quality outlier.

![Complaint Rate by City](screenshots/complaint_rate_city.png)

</td>
<td width="50%">

**Churn Risk by Customer Type**
Churn risk scores are broadly similar across New, Returning, and Premium segments — loyalty status alone doesn't strongly predict churn risk in this dataset.

![Churn Risk by Customer Type](screenshots/churn_risk_customer_type.png)

</td>
</tr>
<tr>
<td colspan="2" align="center">

**Correlation Heatmap — All Numeric Features**
Across Customer_Age, Delivery_Distance_KM, Delivery_Time_Min, Order_Value_USD, Item_Count, Revenue_USD, Profit_USD, and Demand_Score, correlations are consistently near **0** — the dataset's numeric fields behave largely independently of one another.

<img src="screenshots/correlation_heatmap.png" width="60%">

</td>
</tr>
</table>

---

## 💡 Key Insights

- 📍 **Geography is not a differentiator** — revenue is spread almost evenly across all five cities (within a ~2% band), so growth strategy shouldn't lean on any single market.
- 🍔 **Category mix is balanced** — Fast Food, Cafe, Restaurant, and Cloud Kitchen each contribute roughly a quarter of total revenue.
- 🚦 **Traffic and weather have negligible impact on delivery time** in this dataset — average delivery time stays within a ~0.15-minute band regardless of conditions, and distance vs. time correlation is effectively zero. This is worth validating against real operational data, since it runs counter to typical delivery-platform assumptions.
- 💳 **New customers currently out-earn Returning and Premium segments** — a signal that retention and loyalty programs may have room to grow their share of revenue.
- 📉 **Complaint rate (10.07%) is meaningfully higher than refund rate (4.87%)** — over half of complaints don't result in a refund, which could indicate either resolution without refunds or an area for support-process review.
- 🎯 **Demand and churn-risk scores are evenly distributed** rather than concentrated, suggesting these derived scores could be used as-is for targeted operational and marketing rules.

---

## 🚀 Getting Started

### Step 1 — Set up the AWS resources

Before running any code, provision the two AWS services the pipeline depends on:

**Create the S3 bucket:**
1. In the AWS Console, go to **S3 → Create bucket**.
2. Name it something unique, e.g. `quickcart-food-delivery-<yourname>`, and pick your region (this project uses `ap-south-1` / Mumbai).
3. Leave default settings (Block Public Access **on**) and click **Create bucket**.
4. Upload your raw order CSV into the bucket root — `extract.py` reads it from here.

**Create the RDS MySQL instance:**
1. Go to **RDS → Databases → Create database**.
2. Choose **MySQL**, then the **Free tier** or a small template like `db.t4g.micro` (what this project uses).
3. Set a DB identifier (e.g. `quickcart-db`), a master username, and a master password.
4. Under connectivity, make sure the instance is reachable from where your pipeline runs (public access + a security group inbound rule for MySQL port `3306` if running locally; keep it private if running from within the same VPC).
5. Once status shows **Available**, copy the endpoint — that's your `RDS_HOST`.

**Grant your pipeline access:**
- Create an IAM user (or use an existing one) with programmatic access and `AmazonS3ReadOnlyAccess` (or scoped to just this bucket).
- Run `aws configure` locally to store that IAM user's access key/secret in `~/.aws/credentials` — this is what `extract.py`'s `boto3` client picks up automatically (you'll see `Found credentials in shared credentials file` in `etl.log` when it works).

### Step 2 — Run the pipeline

```bash
# 1. Clone the repository
git clone <repo-url>
cd QuickCart-Delivery-Analytics

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn boto3 sqlalchemy pymysql python-dotenv

# 4. Configure environment variables
#    Create python/e.env with your own AWS + MySQL credentials — never commit real secrets:
#    AWS_ACCESS_KEY_ID=...
#    AWS_SECRET_ACCESS_KEY=...
#    RDS_HOST=...          # the endpoint you copied above
#    RDS_USER=...
#    RDS_PASSWORD=...
#    RDS_DB=...

# 5. Run the ETL pipeline (extract from S3 → transform → load into RDS)
python python/etl/pipeline.py

# 6. Generate the analytics & charts
python python/eda.py
```

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

<div align="center">

---

*Built with 🐼 Pandas, 📊 Seaborn, and ☁️ AWS — by the QuickCart Analytics Team*

</div>
