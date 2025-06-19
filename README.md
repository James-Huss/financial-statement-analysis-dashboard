# Financial Statement Analysis Dashboard

## Overview
This project gathers, cleans, and visualizes financial statement data from three major Fortune 500 companies to create a multi-page interactive **Power BI dashboard**. The dashboard includes analysis of income statements, balance sheets, cash flows, and key financial ratios. Historical stock prices and a Fortune 500 company list are also incorporated.

This project demonstrates:
- API-driven data acquisition using Python
- Data cleaning and transformation
- Financial statement analysis
- Data visualization using Power BI

---

## Tools & Technologies
- Python (Pandas, NumPy, Requests)
- Alpha Vantage API
- Power BI
- Scripts
- Git/GitHub

---

## Dashboard Pages
The Power BI dashboard includes four interactive pages:
1. **Overview** – KPIs, company filters, high-level financial summaries  
2. **Income Statement** – Revenue, net income, gross profit, and trends  
3. **Balance Sheet & Ratios** – Total assets, liabilities, and equity with calculated financial ratios  
4. **Cash Flow** – Operating, investing, and financing cash flow over time  

---

## Project Structure
financial-statement-analysis-dashboard/
├── README.md
├── requirements.txt
├── data/ # Clean csv financial statements, fortune 500 companies list, and stock prices
├── notebooks/ # Python scripts for cleaning and data gathering
├── dashboards/ # Power BI workbook (.pbix)
└── images/ # Dashboard screenshots

---

## How to Run

### 1. Get Your API Key
Sign up for a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

Update the key in 'Financial Data.py':

'''python
API_KEY = 'YOUR_API_KEY_HERE'

### 2. Fetch Financial Data
Run the script to download financial statements for a given ticker (e.g., AAPL):
notebooks/Financial Data.py

### 3. Clean thee Data
Run the cleanup script to convert raw files into analysis-ready format:
notebooks/Clean Up.py

### 4. Open Power BI Dashboard
Launch Financial_Statement_Dashboard.pbix in Power BI Desktop to explore the dashboard. 
If prompted, point data sources to your local cleaned CSVs.

---

## Key Features
- API integration (Income Statement, Balance Sheet, Cash Flow)
- Company-level filtering
- Automatic currency and time standardization
- Ratio calculations and trend visualizations

---

## Credits
- Financial data sourced via Alpha Vantage API (this project respects Alpha Vantage's free tier limits)
- Fortune 500 list from public domain sources
