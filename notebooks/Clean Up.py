import os
import pandas as pd
import numpy as np
from glob import glob

# Directory containing the CSV files
input_dir = "financial_data_csv"

# Define renaming maps for each statement type
rename_maps = {
    'BALANCE_SHEET': {
        'cashAndCashEquivalentsAtCarryingValue': 'cash_equiv',
        'cashAndShortTermInvestments': 'cash_and_short_term_inv',
        'commonStockSharesOutstanding': 'shares_outstanding',
        'totalAssets': 'total_assets',
        'totalCurrentAssets': 'current_assets',
        'totalNonCurrentAssets': 'noncurrent_assets',
        'totalLiabilities': 'total_liabilities',
        'totalCurrentLiabilities': 'current_liabilities',
        'totalNonCurrentLiabilities': 'noncurrent_liabilities',
        'totalShareholderEquity': 'shareholder_equity'
    },
    'INCOME_STATEMENT': {
        'totalRevenue': 'revenue',
        'grossProfit': 'gross_profit',
        'operatingIncome': 'operating_income',
        'netIncome': 'net_income',
        'ebit': 'ebit',
        'ebitda': 'ebitda'
    },
    'CASH_FLOW': {
        'operatingCashflow': 'operating_cf',
        'capitalExpenditures': 'capex',
        'cashflowFromInvestment': 'cf_investing',
        'cashflowFromFinancing': 'cf_financing',
        'changeInCashAndCashEquivalents': 'change_in_cash',
        'netIncome': 'net_income'
    }
}

# Columns that should not be treated as numeric
non_numeric_cols = ['fiscalDateEnding', 'reportedCurrency', 'Ticker', 'Statement']

# Pattern to find all CSVs inside the directory
file_pattern = os.path.join(input_dir, "*_*.csv")

for file_path in glob(file_pattern):
    # Extract TICKER and STATEMENT from the filename
    base_name = os.path.basename(file_path)
    try:
        ticker, statement = base_name.replace(".csv", "").split("_", 1)
    except ValueError:
        print(f"Skipping file with unexpected name format: {file_path}")
        continue

    if statement not in ['BALANCE_SHEET', 'INCOME_STATEMENT', 'CASH_FLOW']:
        print(f"Skipping unknown statement type in file: {file_path}")
        continue

    print(f"Processing: {file_path}")

    # Load and clean
    df = pd.read_csv(file_path)

    # Replace 'None' with np.nan
    df.replace("None", np.nan, inplace=True)

    # Convert date
    df['fiscalDateEnding'] = pd.to_datetime(df['fiscalDateEnding'], errors='coerce')

    # Rename columns
    rename_map = rename_maps.get(statement, {})
    df.rename(columns=rename_map, inplace=True)

    # Convert numeric columns
    numeric_cols = df.columns.difference(non_numeric_cols)
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Drop columns with > 50% missing values
    df.dropna(axis=1, thresh=len(df) * 0.5, inplace=True)

    # Save cleaned version in the same folder
    output_file = os.path.join(input_dir, f"{ticker}_{statement}_CLEANED.csv")
    df.to_csv(output_file, index=False)
    print(f"Saved cleaned file: {output_file}")
