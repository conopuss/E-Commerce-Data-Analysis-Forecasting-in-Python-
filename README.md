🧩 Overview

This project builds a comprehensive data processing and forecasting pipeline using Python.
It focuses on cleaning, analyzing, visualizing, and predicting e-commerce sales data.
The goal is to strengthen data engineering and analytical skills while automating repetitive workflows.

🚀 Features
🧹 Data Cleaning & Preparation

Filled missing price values in sales.csv using data from products.csv.

Corrected invalid or inconsistent date formats.

Cleaned incomplete records in feedback.csv (customer feedback data).

📊 Data Analysis & Manipulation

Aggregated sales data by year, month, and day.

Added a new column total_spent to represent customer spending.

Merged datasets to analyze sales distribution by product categories.

📈 Visualization

Line chart → Yearly sales trends.

Bar chart → Monthly sales summaries.

Pie chart → Category-wise sales distribution.

🔮 Forecasting & Recommendations

Predicted the next six months of sales using a linear regression model.

Identified top 5 best-selling products and provided recommendations to improve sales performance.

💱 Currency Conversion

Integrated an API to fetch the daily USD/TRY exchange rate.

Converted total sales values from TRY to USD for additional insights.

⚙️ Automation

Developed a Python script that:

Automatically reads all .csv files in the directory.

Cleans, analyzes, and generates reports.

Saves all results to an Excel file with multiple sheets.

📦 Deliverables
File	Description
case_analiz.py	Performs data cleaning, analysis, and visualization.
case_otomasyon.py	Automates the entire data pipeline from input to output.
sales_summary.xlsx	Consolidated Excel report with multiple analysis sheets and charts.
future_predictions.csv	Forecasted sales for the next six months.
top_products.csv	Top 5 best-selling products with recommendations.
🛠️ Tools & Technologies

Python – Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Excel Automation – via Pandas ExcelWriter

API Integration – Currency exchange (USD/TRY)

Version Control – Git

🧠 Scenario Summary

An e-commerce company wants to understand customer behavior, identify top-performing products, and forecast future sales.
You are responsible for building a complete data pipeline that:

Cleans and processes raw data from multiple sources.

Performs statistical and predictive analysis.

Automates reporting and visualization tasks.

The final result is a fully functional AI-powered data analysis pipeline that supports better business decision-making.
