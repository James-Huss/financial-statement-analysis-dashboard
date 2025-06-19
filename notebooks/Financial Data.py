import requests
import pandas as pd
import time
import os

# Your Alpha Vantage API key
API_KEY = 'YOUR_API_KEY_HERE'

# Base URL for Alpha Vantage
BASE_URL = 'https://www.alphavantage.co/query'

# Directory to save financial data
os.makedirs('financial_data_csv', exist_ok=True)

def fetch_financials(ticker, function):
    """
    Fetch financial statements from Alpha Vantage API for given ticker and function.
    function can be: INCOME_STATEMENT, BALANCE_SHEET, or CASH_FLOW
    """
    params = {
        'function': function,
        'symbol': ticker,
        'apikey': API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "Error Message" in data:
            print(f"Error for ticker {ticker} and function {function}: {data['Error Message']}")
            return None
        return data
    except Exception as e:
        print(f"Exception for ticker {ticker} and function {function}: {e}")
        return None

def save_data_as_csv(ticker, function, data):
    """
    Save the financial data to a CSV file.
    Parses the JSON to flatten the statement data.
    """
    key = 'annualReports'  # Consistent key for all 3 statement types

    if key not in data:
        print(f"No '{key}' key found in data for {ticker} {function}")
        return

    reports = data[key]
    if not reports:
        print(f"No reports found for {ticker} {function}")
        return

    df = pd.DataFrame(reports)
    df['Ticker'] = ticker
    df['Statement'] = function

    filename = f'financial_data_csv/{ticker}_{function}.csv'
    df.to_csv(filename, index=False)
    print(f"Saved {function} CSV data for {ticker} to {filename}")

def main():
    ticker = 'AAPL'  # Set your desired ticker here

    for function in ['INCOME_STATEMENT', 'BALANCE_SHEET', 'CASH_FLOW']:
        filename = f'financial_data_csv/{ticker}_{function}.csv'
        if os.path.isfile(filename):
            print(f"Skipping {ticker} {function} - data already exists.")
            continue

        print(f"Fetching {function} for {ticker}...")
        data = fetch_financials(ticker, function)
        if data:
            save_data_as_csv(ticker, function, data)

        # Respect Alpha Vantage free API limit: 5 calls per minute
        time.sleep(12)

if __name__ == '__main__':
    main()
