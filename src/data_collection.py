import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data


if __name__ == "__main__":
    
    ticker = "AAPL"  
    start_date = "2020-01-01"  
    end_date = "2024-01-01"  

    data = fetch_stock_data(ticker, start_date, end_date)
    print(data.head())  