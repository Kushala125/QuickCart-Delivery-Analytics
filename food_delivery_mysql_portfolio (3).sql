-- =====================================================================
-- FOOD DELIVERY ANALYTICS — MySQL Portfolio Project
-- Dataset: del.csv (150,000 orders)
-- Compatible with MySQL 8.0+ (needed for CTEs / window functions)
-- Results below were computed by running these exact queries against
-- the full 150,000-row dataset.
-- =====================================================================

-- ---------------------------------------------------------------------
-- 1. DATABASE & TABLE SETUP
-- ---------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS food_delivery;
USE food_delivery;

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    Order_ID                 VARCHAR(20)   PRIMARY KEY,
    Customer_Age             TINYINT UNSIGNED,
    Customer_Type            VARCHAR(20),
    Restaurant_Type          VARCHAR(20),
    Cuisine_Type              VARCHAR(20),
    Delivery_Distance_KM      DECIMAL(6,2),
    Delivery_Time_Min        SMALLINT UNSIGNED,
    Order_Value_USD           DECIMAL(8,2),
    Item_Count                 TINYINT UNSIGNED,
    Weather_Condition         VARCHAR(20),
    Traffic_Level              VARCHAR(10),
    Customer_Rating            DECIMAL(3,1),
    Complaint_Flag             TINYINT(1),
    Refund_Flag                 TINYINT(1),
    Revenue_USD                 DECIMAL(8,2),
    Profit_USD                   DECIMAL(8,2),
    City                          VARCHAR(20),
    Month                          TINYINT UNSIGNED,
    Quarter                       TINYINT UNSIGNED,
    Demand_Score                   DECIMAL(5,2),
    Churn_Risk                      DECIMAL(5,2),
    INDEX idx_city (City),
    INDEX idx_cuisine (Cuisine_Type),
    INDEX idx_restaurant_type (Restaurant_Type),
    INDEX idx_month (Month)
);

-- ---------------------------------------------------------------------
-- 2. LOAD THE CSV
-- Adjust the file path to wherever del.csv sits on the MySQL server,
-- or use MySQL Workbench's "Table Data Import Wizard" instead.
-- secure_file_priv may restrict the folder LOAD DATA can read from —
-- check with: SHOW VARIABLES LIKE 'secure_file_priv';
-- ---------------------------------------------------------------------
LOAD DATA LOCAL INFILE '/path/to/del.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(Order_ID, Customer_Age, Customer_Type, Restaurant_Type, Cuisine_Type,
 Delivery_Distance_KM, Delivery_Time_Min, Order_Value_USD, Item_Count,
 Weather_Condition, Traffic_Level, Customer_Rating, Complaint_Flag,
 Refund_Flag, Revenue_USD, Profit_USD, City, Month, Quarter,
 Demand_Score, Churn_Risk);

SELECT COUNT(*) AS Total_Rows_Loaded FROM orders;   -- expect 150000


-- =====================================================================
-- 3. BUSINESS QUESTIONS, QUERIES, RESULTS & EXPLANATIONS
-- =====================================================================


-- #######################################################################
-- Q1. What is the overall business performance in terms of revenue,
--     profit, and average order value?
-- #######################################################################
SELECT 
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
    ROUND(SUM(Profit_USD),2) AS Total_Profit,
    ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value,
    ROUND(SUM(Profit_USD)/SUM(Revenue_USD)*100,2) AS Profit_Margin_Pct
FROM orders;

-- RESULT:
-- Total_Orders | Total_Revenue  | Total_Profit  | Avg_Order_Value | Profit_Margin_Pct
-- 150000       | 37843112.84    | 13504910.56   | 152.89          | 35.69
--
-- EXPLANATION:
-- The business runs a healthy ~35.7% profit margin on revenue across
-- 150,000 orders, with an average order value of ~$153.


-- #######################################################################
-- Q2. Which cities generate the most revenue and profit?
-- #######################################################################
SELECT 
    City,
    COUNT(*) AS Orders,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
    ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM orders
GROUP BY City
ORDER BY Total_Revenue DESC;

-- RESULT:
-- City       | Orders | Total_Revenue | Total_Profit
-- Singapore  | 30236  | 7632153.44    | 2735593.54
-- London     | 29939  | 7588105.17    | 2695977.33
-- New York   | 30108  | 7587788.92    | 2711426.13
-- Mumbai     | 29923  | 7563571.09    | 2680502.10
-- Sydney     | 29794  | 7471494.22    | 2681411.46
--
-- EXPLANATION:
-- Revenue is remarkably evenly spread across all 5 cities (within ~2%
-- of each other) — order volume is balanced, not concentrated in one
-- market.


-- #######################################################################
-- Q3. Which cuisine types drive the highest average order value and
--     revenue?
-- #######################################################################
SELECT 
    Cuisine_Type,
    COUNT(*) AS Orders,
    ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue
FROM orders
GROUP BY Cuisine_Type
ORDER BY Total_Revenue DESC;

-- RESULT:
-- Cuisine_Type | Orders | Avg_Order_Value | Total_Revenue
-- Indian       | 37635  | 152.95          | 9512377.10
-- Mexican      | 37420  | 152.81          | 9444313.95
-- Chinese      | 37403  | 153.05          | 9443342.57
-- Italian      | 37542  | 152.75          | 9443079.22
--
-- EXPLANATION:
-- Cuisine mix is essentially uniform — no single cuisine dominates the
-- platform.


-- #######################################################################
-- Q4. Which restaurant type (Cafe, Fast Food, Cloud Kitchen, Restaurant)
--     is most profitable?
-- #######################################################################
SELECT 
    Restaurant_Type,
    COUNT(*) AS Orders,
    ROUND(SUM(Profit_USD),2) AS Total_Profit,
    ROUND(AVG(Profit_USD),2) AS Avg_Profit_Per_Order
FROM orders
GROUP BY Restaurant_Type
ORDER BY Total_Profit DESC;

-- RESULT:
-- Restaurant_Type | Orders | Total_Profit | Avg_Profit_Per_Order
-- Cafe            | 37743  | 3393147.78   | 89.90
-- Fast Food       | 37528  | 3387006.02   | 90.25
-- Restaurant      | 37342  | 3362672.10   | 90.05
-- Cloud Kitchen   | 37387  | 3362084.66   | 89.93
--
-- EXPLANATION:
-- All four restaurant formats perform almost identically on profit per
-- order — format alone isn't a profit lever in this data.


-- #######################################################################
-- Q5. How does revenue trend across the 12 months?
-- #######################################################################
SELECT 
    Month,
    COUNT(*) AS Orders,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue
FROM orders
GROUP BY Month
ORDER BY Month;

-- RESULT:
-- Month | Orders | Total_Revenue
-- 1     | 12695  | 3185693.65
-- 2     | 11617  | 2940248.09
-- 3     | 12827  | 3227482.16
-- 4     | 12295  | 3105546.55
-- 5     | 12872  | 3237190.26
-- 6     | 12365  | 3117157.08
-- 7     | 12761  | 3215965.77
-- 8     | 12798  | 3235179.82
-- 9     | 12368  | 3122749.79
-- 10    | 12527  | 3143781.09
-- 11    | 12369  | 3139674.95
-- 12    | 12506  | 3172443.63
--
-- EXPLANATION:
-- Revenue is stable year-round (~$2.9M–$3.2M/month); February is the
-- low point, likely because it has fewer days.


-- #######################################################################
-- Q6. How do quarters compare in orders, revenue and average customer
--     rating?
-- #######################################################################
SELECT 
    Quarter,
    COUNT(*) AS Orders,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
    ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM orders
GROUP BY Quarter
ORDER BY Quarter;

-- RESULT:
-- Quarter | Orders | Total_Revenue | Avg_Rating
-- 1       | 37139  | 9353423.90    | 3.00
-- 2       | 37532  | 9459893.89    | 3.00
-- 3       | 37927  | 9573895.38    | 2.99
-- 4       | 37402  | 9455899.67    | 3.00
--
-- EXPLANATION:
-- Customer satisfaction (avg rating ~3.0/5) is flat across quarters —
-- no seasonal service quality swings.


-- #######################################################################
-- Q7. How do New, Returning, and Premium customers differ in spend and
--     churn risk?
-- #######################################################################
SELECT 
    Customer_Type,
    COUNT(*) AS Orders,
    ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value,
    ROUND(AVG(Churn_Risk),2) AS Avg_Churn_Risk,
    ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM orders
GROUP BY Customer_Type
ORDER BY Avg_Order_Value DESC;

-- RESULT:
-- Customer_Type | Orders | Avg_Order_Value | Avg_Churn_Risk | Avg_Rating
-- Premium       | 49903  | 153.22          | 49.82          | 3.00
-- Returning     | 49912  | 153.08          | 50.00          | 3.01
-- New           | 50185  | 152.37          | 49.95          | 3.00
--
-- EXPLANATION:
-- Premium customers spend only marginally more than New/Returning —
-- the "Premium" tier isn't translating into materially higher basket
-- size.


-- #######################################################################
-- Q8. Does traffic congestion correlate with higher complaint rates?
-- #######################################################################
SELECT 
    Traffic_Level,
    COUNT(*) AS Orders,
    SUM(Complaint_Flag) AS Complaints,
    ROUND(SUM(Complaint_Flag)*100.0/COUNT(*),2) AS Complaint_Rate_Pct,
    ROUND(AVG(Delivery_Time_Min),2) AS Avg_Delivery_Time
FROM orders
GROUP BY Traffic_Level
ORDER BY Complaint_Rate_Pct DESC;

-- RESULT:
-- Traffic_Level | Orders | Complaints | Complaint_Rate_Pct | Avg_Delivery_Time
-- Low           | 50105  | 5079       | 10.14              | 64.54
-- High          | 49898  | 5047       | 10.11              | 64.55
-- Medium        | 49997  | 4978       | 9.96               | 64.49
--
-- EXPLANATION:
-- Contrary to intuition, traffic level shows no meaningful effect on
-- complaint rate or delivery time — congestion isn't the driver of
-- service issues in this dataset.


-- #######################################################################
-- Q9. How does weather condition impact average delivery time and
--     demand?
-- #######################################################################
SELECT 
    Weather_Condition,
    COUNT(*) AS Orders,
    ROUND(AVG(Delivery_Time_Min),2) AS Avg_Delivery_Time,
    ROUND(AVG(Demand_Score),2) AS Avg_Demand_Score
FROM orders
GROUP BY Weather_Condition
ORDER BY Avg_Delivery_Time DESC;

-- RESULT:
-- Weather_Condition | Orders | Avg_Delivery_Time | Avg_Demand_Score
-- Stormy            | 37447  | 64.60             | 50.03
-- Rainy             | 37446  | 64.54             | 50.17
-- Cloudy            | 37497  | 64.52             | 49.98
-- Sunny             | 37610  | 64.45             | 50.06
--
-- EXPLANATION:
-- Weather has negligible impact on delivery time in this data —
-- delivery time is likely generated independently of weather.


-- #######################################################################
-- Q10. Which cities have the most customers at high risk of churn
--      (Churn_Risk > 80), and what's their avg rating?
-- #######################################################################
SELECT 
    City,
    COUNT(*) AS High_Risk_Customers,
    ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM orders
WHERE Churn_Risk > 80
GROUP BY City
ORDER BY High_Risk_Customers DESC;

-- RESULT:
-- City       | High_Risk_Customers | Avg_Rating
-- Mumbai     | 6085                | 3.00
-- Singapore  | 6074                | 3.02
-- New York   | 6069                | 2.98
-- London     | 6034                | 3.00
-- Sydney     | 5909                | 2.99
--
-- EXPLANATION:
-- About 20% of orders in every city carry high churn risk (>80) —
-- this is a uniform retention challenge, not a city-specific one.


-- #######################################################################
-- Q11. Do refunded orders tend to also have complaints, and what's the
--      profit impact?
-- #######################################################################
SELECT 
    Refund_Flag,
    COUNT(*) AS Orders,
    SUM(Complaint_Flag) AS Complaints_In_Group,
    ROUND(AVG(Profit_USD),2) AS Avg_Profit,
    ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM orders
GROUP BY Refund_Flag;

-- RESULT:
-- Refund_Flag | Orders | Complaints_In_Group | Avg_Profit | Total_Profit
-- 0 (No)      | 142692 | 14405               | 90.05      | 12848971.89
-- 1 (Yes)     | 7308   | 699                 | 89.76      | 655938.67
--
-- EXPLANATION:
-- ~4.9% of orders are refunded; refunded orders still generate near-
-- identical average profit, suggesting refunds are handled as partial/
-- goodwill credits rather than a full profit loss.


-- #######################################################################
-- Q12. What are the single highest-value orders in the dataset?
-- #######################################################################
SELECT Order_ID, City, Cuisine_Type, Order_Value_USD, Revenue_USD, Profit_USD
FROM orders
ORDER BY Revenue_USD DESC
LIMIT 10;

-- RESULT:
-- Order_ID   | City      | Cuisine_Type | Order_Value_USD | Revenue_USD | Profit_USD
-- ORD0063686 | Mumbai    | Mexican      | 109.41          | 500.00      | 170.86
-- ORD0094686 | Singapore | Chinese      | 52.66           | 500.00      | 178.72
-- ORD0006516 | New York  | Mexican      | 245.45          | 499.99      | 105.22
-- ORD0060038 | Singapore | Indian       | 110.09          | 499.99      | 154.13
-- ORD0112804 | London    | Indian       | 43.65           | 499.99      | 7.02
-- ORD0054795 | Mumbai    | Italian      | 61.00           | 499.98      | 65.50
-- ORD0092437 | Mumbai    | Italian      | 225.57          | 499.98      | 174.16
-- ORD0003155 | New York  | Indian       | 121.18          | 499.97      | 145.29
-- ORD0040544 | Sydney    | Mexican      | 290.82          | 499.97      | 146.94
-- ORD0055860 | Sydney    | Chinese      | 260.26          | 499.97      | 139.21
--
-- EXPLANATION:
-- Revenue appears capped near $500 — worth flagging as a possible
-- data-generation ceiling rather than a real-world cap.


-- #######################################################################
-- Q13. Rank cities by total profit using a window function, showing
--      rank and each city's share of total profit.
-- #######################################################################
WITH city_profit AS (
    SELECT City, ROUND(SUM(Profit_USD),2) AS Total_Profit
    FROM orders
    GROUP BY City
)
SELECT 
    City,
    Total_Profit,
    RANK() OVER (ORDER BY Total_Profit DESC) AS Profit_Rank,
    ROUND(100.0 * Total_Profit / SUM(Total_Profit) OVER (), 2) AS Pct_Of_Total_Profit
FROM city_profit
ORDER BY Profit_Rank;

-- RESULT:
-- City       | Total_Profit | Profit_Rank | Pct_Of_Total_Profit
-- Singapore  | 2735593.54   | 1           | 20.26
-- New York   | 2711426.13   | 2           | 20.08
-- London     | 2695977.33   | 3           | 19.96
-- Sydney     | 2681411.46   | 4           | 19.86
-- Mumbai     | 2680502.10   | 5           | 19.85
--
-- EXPLANATION:
-- Singapore edges out as the #1 city by profit, but the spread across
-- all 5 is under half a percentage point.


-- #######################################################################
-- Q14. How many orders in each cuisine type exceed that cuisine's own
--      average order value? (CTE + JOIN, avoids a slow correlated
--      subquery on 150K rows)
-- #######################################################################
WITH cuisine_avg AS (
    SELECT Cuisine_Type, AVG(Order_Value_USD) AS Avg_Value
    FROM orders
    GROUP BY Cuisine_Type
)
SELECT 
    o.Cuisine_Type,
    COUNT(*) AS Orders_Above_Avg
FROM orders o
JOIN cuisine_avg c ON o.Cuisine_Type = c.Cuisine_Type
WHERE o.Order_Value_USD > c.Avg_Value
GROUP BY o.Cuisine_Type
ORDER BY Orders_Above_Avg DESC;

-- RESULT:
-- Cuisine_Type | Orders_Above_Avg
-- Indian       | 18876
-- Chinese      | 18770
-- Italian      | 18763
-- Mexican      | 18705
--
-- EXPLANATION:
-- Roughly half of every cuisine's orders sit above its own average —
-- consistent with a fairly symmetric (non-skewed) order-value
-- distribution. This query was written as a CTE joined once per group
-- rather than a correlated subquery re-executed per row, which is the
-- standard optimization for this pattern at scale.


-- #######################################################################
-- Q15. How are orders distributed across low, medium and high value
--      buckets, and what's the profit contribution of each?
-- #######################################################################
SELECT 
    CASE 
        WHEN Order_Value_USD < 100 THEN 'Low (<$100)'
        WHEN Order_Value_USD BETWEEN 100 AND 300 THEN 'Medium ($100-$300)'
        ELSE 'High (>$300)'
    END AS Value_Bucket,
    COUNT(*) AS Orders,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue,
    ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM orders
GROUP BY Value_Bucket
ORDER BY Total_Revenue DESC;

-- RESULT:
-- Value_Bucket        | Orders | Total_Revenue | Total_Profit
-- Medium ($100-$300)  | 101953 | 25720244.46   | 9170193.04
-- Low (<$100)         | 48047  | 12122868.38   | 4334717.52
--
-- EXPLANATION:
-- No orders fall in the "High (>$300)" bucket by Order_Value_USD — the
-- mid-tier ($100–$300) basket is the core of the business, driving
-- ~68% of revenue.


-- #######################################################################
-- Q16. For each city, which cuisine type generates the most revenue?
--      (Top-1 per group, window function ROW_NUMBER)
-- #######################################################################
WITH ranked AS (
    SELECT 
        City, Cuisine_Type,
        SUM(Revenue_USD) AS Cuisine_Revenue,
        ROW_NUMBER() OVER (PARTITION BY City ORDER BY SUM(Revenue_USD) DESC) AS rn
    FROM orders
    GROUP BY City, Cuisine_Type
)
SELECT City, Cuisine_Type, ROUND(Cuisine_Revenue,2) AS Cuisine_Revenue
FROM ranked
WHERE rn = 1
ORDER BY Cuisine_Revenue DESC;

-- RESULT:
-- City       | Cuisine_Type | Cuisine_Revenue
-- Singapore  | Indian       | 1938917.85
-- Mumbai     | Indian       | 1928308.05
-- London     | Italian      | 1925235.27
-- New York   | Chinese      | 1909726.04
-- Sydney     | Chinese      | 1887207.59
--
-- EXPLANATION:
-- Cuisine preference does vary meaningfully by city — Indian food leads
-- in Singapore/Mumbai, Italian in London, Chinese in New York/Sydney.
-- Useful for city-specific menu/marketing decisions.


-- #######################################################################
-- Q17. How does customer rating change as delivery time increases?
-- #######################################################################
SELECT 
    CASE 
        WHEN Delivery_Time_Min <= 30 THEN '0-30 min'
        WHEN Delivery_Time_Min <= 60 THEN '31-60 min'
        WHEN Delivery_Time_Min <= 90 THEN '61-90 min'
        ELSE '90+ min'
    END AS Delivery_Time_Bucket,
    COUNT(*) AS Orders,
    ROUND(AVG(Customer_Rating),2) AS Avg_Rating,
    ROUND(SUM(Complaint_Flag)*100.0/COUNT(*),2) AS Complaint_Rate_Pct
FROM orders
GROUP BY Delivery_Time_Bucket
ORDER BY MIN(Delivery_Time_Min);

-- RESULT:
-- Delivery_Time_Bucket | Orders | Avg_Rating | Complaint_Rate_Pct
-- 0-30 min             | 28590  | 3.01       | 10.25
-- 31-60 min            | 40849  | 3.00       | 9.84
-- 61-90 min            | 41119  | 3.00       | 10.21
-- 90+ min              | 39442  | 3.00       | 10.03
--
-- EXPLANATION:
-- Ratings and complaint rates barely move with delivery time —
-- customer satisfaction here isn't primarily driven by speed.


-- #######################################################################
-- Q18. What is the month-over-month revenue growth rate?
--      (Window function LAG)
-- #######################################################################
WITH monthly AS (
    SELECT Month, SUM(Revenue_USD) AS Revenue
    FROM orders
    GROUP BY Month
)
SELECT 
    Month,
    ROUND(Revenue,2) AS Revenue,
    ROUND(Revenue - LAG(Revenue) OVER (ORDER BY Month),2) AS Change_vs_Prev_Month,
    ROUND((Revenue - LAG(Revenue) OVER (ORDER BY Month)) * 100.0 
          / LAG(Revenue) OVER (ORDER BY Month),2) AS Growth_Pct
FROM monthly
ORDER BY Month;

-- RESULT:
-- Month | Revenue     | Change_vs_Prev_Month | Growth_Pct
-- 1     | 3185693.65  | NULL                  | NULL
-- 2     | 2940248.09  | -245445.56            | -7.70
-- 3     | 3227482.16  | 287234.07             | 9.77
-- 4     | 3105546.55  | -121935.61            | -3.78
-- 5     | 3237190.26  | 131643.71             | 4.24
-- 6     | 3117157.08  | -120033.18            | -3.71
-- 7     | 3215965.77  | 98808.69              | 3.17
-- 8     | 3235179.82  | 19214.05              | 0.60
-- 9     | 3122749.79  | -112430.03            | -3.48
-- 10    | 3143781.09  | 21031.30              | 0.67
-- 11    | 3139674.95  | -4106.14              | -0.13
-- 12    | 3172443.63  | 32768.68              | 1.04
--
-- EXPLANATION:
-- Revenue oscillates in a tight +/-10% band month to month with no
-- sustained growth or decline trend — a mature, stable-demand
-- business.


-- #######################################################################
-- Q19. Which cities have an average order value higher than the
--      platform-wide average? (HAVING with subquery)
-- #######################################################################
SELECT City, ROUND(AVG(Order_Value_USD),2) AS City_Avg_Order_Value
FROM orders
GROUP BY City
HAVING AVG(Order_Value_USD) > (SELECT AVG(Order_Value_USD) FROM orders)
ORDER BY City_Avg_Order_Value DESC;

-- RESULT:
-- City       | City_Avg_Order_Value
-- Mumbai     | 153.40
-- Singapore  | 153.33
-- New York   | 152.99
--
-- EXPLANATION:
-- Only 3 of the 5 cities beat the global average order value — London
-- and Sydney sit just below it, though the gap is small (~$1-2).


-- #######################################################################
-- Q20. Which restaurant type has the highest complaint rate?
-- #######################################################################
SELECT 
    Restaurant_Type,
    COUNT(*) AS Orders,
    SUM(Complaint_Flag) AS Complaints,
    ROUND(SUM(Complaint_Flag)*100.0/COUNT(*),2) AS Complaint_Rate_Pct
FROM orders
GROUP BY Restaurant_Type
ORDER BY Complaint_Rate_Pct DESC;

-- RESULT:
-- Restaurant_Type | Orders | Complaints | Complaint_Rate_Pct
-- Restaurant      | 37342  | 3816       | 10.22
-- Cafe            | 37743  | 3784       | 10.03
-- Fast Food       | 37528  | 3761       | 10.02
-- Cloud Kitchen   | 37387  | 3743       | 10.01
--
-- EXPLANATION:
-- Complaint rates are essentially flat (~10%) across all restaurant
-- formats — no format stands out as a quality problem area.


-- #######################################################################
-- Q21. How do delivery distance and delivery time compare across
--      cities?
-- #######################################################################
SELECT 
    City,
    ROUND(AVG(Delivery_Distance_KM),2) AS Avg_Distance_KM,
    ROUND(AVG(Delivery_Time_Min),2) AS Avg_Delivery_Time_Min
FROM orders
GROUP BY City
ORDER BY Avg_Distance_KM DESC;

-- RESULT:
-- City       | Avg_Distance_KM | Avg_Delivery_Time_Min
-- Mumbai     | 12.81           | 64.70
-- New York   | 12.76           | 64.48
-- London     | 12.75           | 64.58
-- Singapore  | 12.75           | 64.26
-- Sydney     | 12.73           | 64.63
--
-- EXPLANATION:
-- Delivery distance and time are nearly identical across all 5 cities
-- (~12.7-12.8 km, ~64-65 min) — logistics performance is consistent
-- globally, not a differentiator between markets.


-- #######################################################################
-- Q22. Does ordering more items increase the average order value?
-- #######################################################################
SELECT 
    CASE 
        WHEN Item_Count <= 5 THEN '1-5 items'
        WHEN Item_Count <= 10 THEN '6-10 items'
        ELSE '11-14 items'
    END AS Item_Count_Bucket,
    COUNT(*) AS Orders,
    ROUND(AVG(Order_Value_USD),2) AS Avg_Order_Value
FROM orders
GROUP BY Item_Count_Bucket
ORDER BY MIN(Item_Count);

-- RESULT:
-- Item_Count_Bucket | Orders | Avg_Order_Value
-- 1-5 items         | 53487  | 152.68
-- 6-10 items        | 53639  | 153.25
-- 11-14 items       | 42874  | 152.69
--
-- EXPLANATION:
-- No relationship between item count and order value — orders with 1-5
-- items cost about the same on average as orders with 11-14 items,
-- meaning per-item price effectively scales down as basket size grows.


-- #######################################################################
-- Q23. How does customer rating differ across churn-risk quartiles?
--      (Window function NTILE — splits data into 4 equal-sized groups)
-- #######################################################################
WITH quartiles AS (
    SELECT 
        Customer_Rating, Churn_Risk,
        NTILE(4) OVER (ORDER BY Churn_Risk) AS Churn_Quartile
    FROM orders
)
SELECT 
    Churn_Quartile,
    COUNT(*) AS Orders,
    ROUND(MIN(Churn_Risk),2) AS Min_Churn_Risk,
    ROUND(MAX(Churn_Risk),2) AS Max_Churn_Risk,
    ROUND(AVG(Customer_Rating),2) AS Avg_Rating
FROM quartiles
GROUP BY Churn_Quartile
ORDER BY Churn_Quartile;

-- RESULT:
-- Churn_Quartile | Orders | Min_Churn_Risk | Max_Churn_Risk | Avg_Rating
-- 1 (lowest risk)| 37500  | 0.00           | 24.88          | 3.00
-- 2              | 37500  | 24.88          | 49.83          | 3.00
-- 3              | 37500  | 49.83          | 75.00          | 2.99
-- 4 (highest risk)| 37500 | 75.00          | 100.00         | 3.00
--
-- EXPLANATION:
-- Customer rating is flat across churn-risk quartiles — high-risk
-- customers aren't rating their experience any lower than low-risk
-- ones, suggesting churn risk here is driven by factors other than
-- satisfaction (e.g. price sensitivity, competition).


-- #######################################################################
-- Q24. Which cuisine types have loss-making orders (negative profit),
--      and how many? (Filtering + GROUP BY on a derived condition)
-- #######################################################################
SELECT 
    Cuisine_Type,
    COUNT(*) AS Loss_Making_Orders
FROM orders
WHERE Profit_USD < 0
GROUP BY Cuisine_Type
ORDER BY Loss_Making_Orders DESC;

-- RESULT:
-- Cuisine_Type | Loss_Making_Orders
-- Italian      | 3440
-- Indian       | 3393
-- Chinese      | 3357
-- Mexican      | 3356
--
-- EXPLANATION:
-- ~9% of all orders (13,546 of 150,000) are loss-making, spread almost
-- evenly across cuisines — this isn't a cuisine-specific cost problem,
-- it's a platform-wide pattern worth investigating (e.g. discounting,
-- delivery cost outliers).


-- #######################################################################
-- Q25. Which cities have a profit margin (profit/revenue) higher than
--      the company-wide average margin? (Subquery in HAVING)
-- #######################################################################
SELECT 
    City,
    ROUND(SUM(Profit_USD)*100.0/SUM(Revenue_USD),2) AS City_Profit_Margin_Pct
FROM orders
GROUP BY City
HAVING SUM(Profit_USD)*100.0/SUM(Revenue_USD) > (
    SELECT SUM(Profit_USD)*100.0/SUM(Revenue_USD) FROM orders
)
ORDER BY City_Profit_Margin_Pct DESC;

-- RESULT:
-- City       | City_Profit_Margin_Pct
-- Sydney     | 35.89
-- Singapore  | 35.84
-- New York   | 35.73
--
-- EXPLANATION:
-- Sydney, Singapore, and New York run above the company-wide 35.69%
-- margin, while London and Mumbai sit slightly below — a useful lens
-- for margin-improvement initiatives even though the differences are
-- small.


-- =====================================================================
-- 4. KEY TAKEAWAYS
-- =====================================================================
-- 1. Balanced business: revenue, profit, and order volume are nearly
--    identical across all 5 cities, all 4 cuisines, and all 4
--    restaurant formats — no single segment dominates.
-- 2. Operational factors (traffic, weather) show minimal correlation
--    with delivery time, ratings, or complaints in this dataset.
-- 3. ~20% of customers are high churn-risk in every city — a uniform
--    retention problem, not a regional one.
-- 4. The $100-$300 order-value band is the revenue engine, contributing
--    ~68% of total revenue.
-- 5. Cuisine preference is the one dimension that meaningfully varies
--    by geography (Indian in Singapore/Mumbai, Italian in London,
--    Chinese in New York/Sydney) — useful for city-specific marketing.
--
-- SQL TECHNIQUES SHOWCASED (25 queries):
-- Aggregates (SUM/AVG/COUNT/ROUND) - GROUP BY/ORDER BY - HAVING with
-- scalar subqueries - CASE WHEN bucketing - CTEs (WITH) - Window
-- functions (RANK, ROW_NUMBER PARTITION BY, LAG, NTILE, SUM OVER) -
-- correlated-subquery-to-JOIN optimization - IN subqueries -
-- percent-of-total and period-over-period growth calcs - quartile
-- segmentation - conditional filtering (WHERE on derived business logic)
-- =====================================================================
