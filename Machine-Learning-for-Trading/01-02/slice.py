"""Utility functions"""

import os
import pandas as pd


def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_symbol = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
                                usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_symbol = df_symbol.rename(columns={'Adj Close': symbol})
        df = df.join(df_symbol, how='inner')

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    select_dates = pd.date_range('2010-01-01', '2010-01-31')
    print df.loc[select_dates, ['SPY', 'IBM']].dropna()


if __name__ == "__main__":
    test_run()
