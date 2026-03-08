import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

def fetch_yahoo_finance_data(
    symbol: str,
    period: str = "1y",
    interval: str = "1d"
) -> pd.DataFrame:
    """
    Fetch data from Yahoo Finance using requests.
    
    Args:
        symbol: Stock or crypto symbol
        period: Time period
        interval: Data interval
    
    Returns:
        DataFrame with OHLCV data
    """
    try:
        base_url = "https://query1.finance.yahoo.com/v8/finance/chart/"
        
        period_map = {
            '1d': '1d',
            '5d': '5d',
            '1mo': '1mo',
            '3mo': '3mo',
            '6mo': '6mo',
            '1y': '1y',
            '2y': '2y',
            '5y': '5y',
            '10y': '10y',
            'ytd': 'ytd',
            'max': 'max'
        }
        
        interval_map = {
            '1m': '1m',
            '2m': '2m',
            '5m': '5m',
            '15m': '15m',
            '30m': '30m',
            '60m': '1h',
            '90m': '90m',
            '1h': '1h',
            '1d': '1d',
            '5d': '5d',
            '1wk': '1wk',
            '1mo': '1mo',
            '3mo': '3mo'
        }
        
        url = f"{base_url}{symbol}"
        params = {
            'interval': interval_map.get(interval, '1d'),
            'range': period_map.get(period, '1y'),
            'includePrePost': 'true',
            'events': 'div%7Csplit'
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        if 'chart' not in data or 'result' not in data['chart'] or not data['chart']['result']:
            return pd.DataFrame()
        
        result = data['chart']['result'][0]
        timestamp = result['timestamp']
        indicators = result['indicators']
        
        ohlcv = indicators['quote'][0]
        
        df_data = []
        for i in range(len(timestamp)):
            df_data.append({
                'Date': pd.to_datetime(timestamp[i], unit='s'),
                'Open': ohlcv['open'][i],
                'High': ohlcv['high'][i],
                'Low': ohlcv['low'][i],
                'Close': ohlcv['close'][i],
                'Volume': ohlcv['volume'][i]
            })
        
        df = pd.DataFrame(df_data)
        df.set_index('Date', inplace=True)
        
        return df
    
    except Exception as e:
        raise Exception(f"Failed to fetch data: {str(e)}")
