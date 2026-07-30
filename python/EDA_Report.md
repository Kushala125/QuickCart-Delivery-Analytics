TOTAL REVENUE BY CITY
==================================================
City
Singapore    7632153.44
London       7588105.17
New York     7587788.92
Mumbai       7563571.09
Sydney       7471494.22
Name: Revenue_USD, dtype: float64

✅ Revenue by City report saved successfully!

==================================================
TOTAL REVENUE BY RESTAURANT TYPE
==================================================
Restaurant_Type
Fast Food        9511880.09
Cafe             9476002.56
Restaurant       9472063.19
Cloud Kitchen    9383167.00
Name: Revenue_USD, dtype: float64

✅ Revenue by Restaurant Type report saved successfully!

==================================================
TOTAL REVENUE BY CUSTOMER TYPE
==================================================
Customer_Type
New          12697418.28
Premium      12577799.83
Returning    12567894.73
Name: Revenue_USD, dtype: float64

✅ Revenue by Customer Type report saved successfully!

==================================================
DELIVERY TIME ANALYSIS
==================================================
Average Delivery Time : 64.53 minutes
Median Delivery Time  : 65.00 minutes
Minimum Delivery Time : 10 minutes
Maximum Delivery Time : 119 minutes
Most Common Time      : 112 minutes

==================================================
AVERAGE DELIVERY TIME BY TRAFFIC LEVEL
==================================================
Traffic_Level
Medium    64.49
Low       64.54
High      64.55
Name: Delivery_Time_Min, dtype: float64

✅ Delivery Time by Traffic report saved successfully!

==================================================
AVERAGE DELIVERY TIME BY WEATHER
==================================================
Weather_Condition
Sunny     64.45
Cloudy    64.52
Rainy     64.54
Stormy    64.60
Name: Delivery_Time_Min, dtype: float64

✅ Delivery Time by Weather report saved successfully!

==================================================
DELIVERY DISTANCE VS DELIVERY TIME CORRELATION
==================================================
Correlation:  0.00
Weak or no relationship.

Summary Statistics
       Delivery_Distance_KM  Delivery_Time_Min
count         150000.000000      150000.000000
mean              12.761809          64.528240
std                7.082171          31.742264
min                0.500000          10.000000
25%                6.630000          37.000000
50%               12.760000          65.000000
75%               18.910000          92.000000
max               25.000000         119.000000

✅ Distance vs Delivery report saved successfully!

==================================================
COMPLAINT VS REFUND
==================================================
Refund_Flag          0     1     All
Complaint_Flag                      
0               128287  6609  134896
1                14405   699   15104
All             142692  7308  150000

 Complaint vs Refund report saved successfully!

==================================================
MONTHLY REVENUE
==================================================
Month
1     3185693.65
2     2940248.09
3     3227482.16
4     3105546.55
5     3237190.26
6     3117157.08
7     3215965.77
8     3235179.82
9     3122749.79
10    3143781.09
11    3139674.95
12    3172443.63
Name: Revenue_USD, dtype: float64

✅ Monthly Revenue report saved successfully!

==================================================
CUSTOMER RATING ANALYSIS
==================================================
Average Rating : 3.00
Median Rating  : 3.00
Highest Rating : 5.0
Lowest Rating  : 1.0

Rating Distribution
Customer_Rating
1.0    1843
1.1    3841
1.2    3759
1.3    3732
1.4    3820
1.5    3689
1.6    3684
1.7    3905
1.8    3776
1.9    3709
2.0    3793
2.1    3695
2.2    3763
2.3    3677
2.4    3824
2.5    3760
2.6    3723
2.7    3804
2.8    3708
2.9    3686
3.0    3648
3.1    3739
3.2    3685
3.3    3736
3.4    3745
3.5    3737
3.6    3747
3.7    3796
3.8    3780
3.9    3825
4.0    3683
4.1    3810
4.2    3714
4.3    3701
4.4    3782
4.5    3749
4.6    3771
4.7    3808
4.8    3705
4.9    3782
5.0    1866
Name: count, dtype: int64

✅ Customer Rating report saved successfully!

==================================================
CORRELATION MATRIX
==================================================
                      Customer_Age  ...  Demand_Score
Customer_Age                   1.0  ...          -0.0
Delivery_Distance_KM           0.0  ...          -0.0
Delivery_Time_Min              0.0  ...           0.0
Order_Value_USD                0.0  ...           0.0
Item_Count                    -0.0  ...           0.0
Revenue_USD                    0.0  ...           0.0
Profit_USD                     0.0  ...           0.0
Demand_Score                  -0.0  ...           1.0

[8 rows x 8 columns]

Correlation Matrix report saved successfully!

==================================================
EXECUTIVE KPI SUMMARY
==================================================
Total Orders            : 150,000
Total Revenue (USD)     : $37,843,112.84
Total Profit (USD)      : $13,504,910.56
Average Order Value     : $152.89
Average Delivery Time   : 64.53 minutes
Average Customer Rating : 3.00
Complaint Rate          : 0.00%
Refund Rate             : 0.00%