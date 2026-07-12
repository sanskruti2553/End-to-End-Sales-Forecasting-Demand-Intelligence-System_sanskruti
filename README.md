# 📊 End-to-End Sales Forecasting & Demand Intelligence System

## 📌 Project Overview

This project develops an end-to-end Sales Forecasting and Demand Intelligence System using machine learning and time series forecasting techniques. The objective is to help businesses forecast future sales, detect unusual sales patterns, segment products based on demand, and support inventory planning through an interactive Streamlit dashboard.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA)
- Analyze time series trends and seasonality
- Build and compare multiple forecasting models
- Forecast product category and regional sales
- Detect sales anomalies
- Segment products using K-Means clustering
- Develop an interactive Streamlit dashboard
- Generate executive business insights

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit

---

## 📂 Project Structure

```
SalesForecasting/

│── analysis.ipynb
│── app.py
│── train.csv
│── vgsales.csv
│── requirements.txt
│── README.md
│── summary.pdf
│── charts/
```

---

## 📈 Project Workflow

### Task 1 – Data Loading & Exploratory Data Analysis

- Data Cleaning
- Missing Value Analysis
- Sales Trend Analysis
- Category-wise Analysis
- Regional Analysis
- Monthly Sales Visualization

---

### Task 2 – Time Series Analysis

- Monthly Sales Aggregation
- Trend Analysis
- Seasonal Decomposition
- Stationarity Analysis

---

### Task 3 – Sales Forecasting

Three forecasting models were developed and compared.

| Model | MAE | RMSE | MAPE |
|-------|------:|------:|------:|
| SARIMA | 18031.40 | 19009.18 | 18.97% |
| Prophet | 20250.79 | 22318.41 | 21.86% |
| **XGBoost** | **14763.81** | **18337.41** | **14.48%** |

**Best Model:** XGBoost

---

### Task 4 – Category & Region Forecasting

Forecasts generated for:

- Furniture
- Technology
- Office Supplies
- West Region
- East Region

---

### Task 5 – Anomaly Detection

Dataset Used:

- Video Game Sales Dataset

Methods:

- Isolation Forest
- Z-Score Analysis

Detected anomaly years:

- 2007
- 2008
- 2009
- 2010

---

### Task 6 – Product Demand Segmentation

K-Means Clustering grouped products into four demand segments:

- High Value Premium Products
- Stable Demand Products
- High Volume Best Sellers
- Emerging Growth Product

---

### Task 7 – Streamlit Dashboard

Interactive dashboard containing:

- 📊 Sales Overview
- 📉 Forecast Explorer
- 🚨 Anomaly Detection
- 📦 Product Demand Segmentation

---

### Task 8 – Executive Business Report

A business report summarizing:

- Key insights
- Forecasting results
- Anomaly detection
- Demand segmentation
- Business recommendations

---

## 📊 Key Findings

- XGBoost achieved the highest forecasting accuracy.
- Furniture showed the highest forecasted sales among product categories.
- Isolation Forest successfully identified anomalous sales years.
- High-volume best-selling products should receive inventory priority.
- Product segmentation supports effective inventory management.

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/SalesForecasting.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📷 Dashboard

The Streamlit dashboard provides:

- Sales trends
- Forecasting results
- Product demand segments
- Anomaly detection insights

---

## 👩‍💻 Author

**Sanskruti Pawar**

- MSc Bioinformatics Student
- Data Analytics Enthusiast

### Skills

- Python
- SQL
- Advanced Excel
- Power BI
- Tableau
- Machine Learning
- Time Series Forecasting
- Streamlit

---

## ⭐ Future Improvements

- Deploy dashboard on Streamlit Community Cloud
- Integrate real-time sales data
- Add advanced forecasting models (LSTM, ARIMA variants)
- Include external business factors such as promotions and holidays
- Automate report generation

---

## 📄 License

This project is created for educational and internship purposes.
