# Retail Stores End to end Data Warehouse Project

## 📌 Project Overview
This project demonstrates the end‑to‑end process of building a **Retail Data Warehouse** using **Snowflake** as the cloud data platform, **Python (Pandas)** for ETL and data cleaning, and **Power BI** for interactive dashboards.  

The goal is to transform raw retail data into meaningful insights such as **monthly sales trends, customer activity, and KPIs**, enabling better business decision‑making.
Here’s a snapshot of the interactive dashboard built in Power BI:

![Retail Store Analysis Dashboard](Power%20BI/Screenshot%202026-01-06%20000617.png)
---

## 🛠 Tools & Technologies Used
- **Python (Pandas)** → Data cleaning and transformation of raw Excel/CSV files  
- **Snowflake** → Cloud data warehouse for storing fact and dimension tables  
- **SQL** → Schema design, data loading, and analytics queries  
- **Power BI** → Visualization and dashboard creation  
- **Excel/CSV** → Raw datasets used as input  

---

## ⚙️ Workflow
1. **Data Preparation (Python + Pandas)**  
   - Cleaned raw Excel/CSV files  
   - Handled missing values, standardized column names, exported cleaned datasets  

2. **Data Warehouse (Snowflake)**  
   - Created database, schema, fact and dimension tables  
   - Loaded cleaned datasets into Snowflake using `COPY INTO`  
   - Designed a **star schema** for efficient analytics  

3. **Analytics (SQL)**  
   - Wrote queries for monthly sales, customer activity, and KPIs  
   - Created views for reporting  

4. **Visualization (Power BI)**  
   - Connected Power BI to Snowflake  
   - Built dashboards showing sales trends, top customers, and overall KPIs  
   - Exported screenshots and `.pbix` file for sharing  

---

## 📊 Results
- **Amount by store type** → Showing pie chart based on store types, program tiers, region wise amount
- **Customer Activity** → Top customers by age
- **Retail KPIs** → Total sales, average order value,Discount value 

Future Improvements
Automate ETL pipeline using Airflow or Matillion




