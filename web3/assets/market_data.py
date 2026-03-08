import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
import sys
from pathlib import Path

script_dir = Path(__file__).parent
web3_dir = script_dir.parent
sys.path.insert(0, str(web3_dir))

from assets.i18n import t

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

def fetch_market_data(
    symbol: str,
    period: str = "1y",
    interval: str = "1d",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Fetch market data for stocks or cryptocurrencies.
    
    Args:
        symbol: Stock symbol (e.g., 'AAPL', 'MSFT') or crypto symbol (e.g., 'BTC-USD', 'ETH-USD')
        period: Time period ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
        interval: Data interval ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')
        start_date: Start date in 'YYYY-MM-DD' format (overrides period)
        end_date: End date in 'YYYY-MM-DD' format (overrides period)
    
    Returns:
        Dictionary containing market data and metadata
    """
    try:
        data = fetch_yahoo_finance_data(symbol, period, interval)
        
        if data.empty:
            return {
                'success': False,
                'error': t('market_data.no_data'),
                'symbol': symbol
            }
        
        result = {
            'success': True,
            'symbol': symbol,
            'period': period,
            'interval': interval,
            'data_points': len(data),
            'start_date': data.index[0].strftime('%Y-%m-%d %H:%M:%S'),
            'end_date': data.index[-1].strftime('%Y-%m-%d %H:%M:%S'),
            'current_price': {
                'open': float(data['Open'].iloc[-1]),
                'high': float(data['High'].iloc[-1]),
                'low': float(data['Low'].iloc[-1]),
                'close': float(data['Close'].iloc[-1]),
                'volume': int(data['Volume'].iloc[-1])
            },
            'price_change': {
                'absolute': float(data['Close'].iloc[-1] - data['Close'].iloc[0]),
                'percent': float((data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0] * 100)
            },
            'statistics': {
                'high_52w': float(data['High'].max()),
                'low_52w': float(data['Low'].min()),
                'avg_volume': int(data['Volume'].mean()),
                'market_cap': 'N/A',
                'pe_ratio': 'N/A',
                'dividend_yield': 'N/A'
            },
            'historical_data': []
        }
        
        for idx, row in data.iterrows():
            result['historical_data'].append({
                'date': idx.strftime('%Y-%m-%d %H:%M:%S'),
                'open': float(row['Open']),
                'high': float(row['High']),
                'low': float(row['Low']),
                'close': float(row['Close']),
                'volume': int(row['Volume'])
            })
        
        return result
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'symbol': symbol
        }

def get_company_info(symbol: str) -> Dict[str, Any]:
    """
    Get detailed company information for a stock symbol.
    
    Args:
        symbol: Stock symbol
    
    Returns:
        Dictionary containing company information
    """
    return {
        'success': False,
        'error': 'Company info not available in this mode',
        'symbol': symbol
    }

def main():
    import json
    
    if len(sys.argv) < 2:
        print(t('market_data.usage'))
        print()
        print('Examples:')
        print('  python market_data.py AAPL')
        print('  python market_data.py BTC-USD --period 1mo')
        print('  python market_data.py AAPL MSFT GOOG --period 3mo')
        print('  python market_data.py AAPL --info')
        print()
        return
    
    symbols = []
    options = {
        'period': '1y',
        'interval': '1d',
        'start_date': None,
        'end_date': None,
        'show_info': False
    }
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg.startswith('--'):
            if arg == '--period' and i + 1 < len(sys.argv):
                options['period'] = sys.argv[i + 1]
                i += 1
            elif arg == '--interval' and i + 1 < len(sys.argv):
                options['interval'] = sys.argv[i + 1]
                i += 1
            elif arg == '--start' and i + 1 < len(sys.argv):
                options['start_date'] = sys.argv[i + 1]
                i += 1
            elif arg == '--end' and i + 1 < len(sys.argv):
                options['end_date'] = sys.argv[i + 1]
                i += 1
            elif arg == '--info':
                options['show_info'] = True
        else:
            symbols.append(arg)
        
        i += 1
    
    if not symbols:
        print(t('market_data.no_symbol'))
        return
    
    if options['show_info']:
        if len(symbols) > 1:
            print(t('market_data.info_single_only'))
            return
        
        result = get_company_info(symbols[0])
    elif len(symbols) == 1:
        result = fetch_market_data(
            symbols[0],
            options['period'],
            options['interval'],
            options['start_date'],
            options['end_date']
        )
    else:
        result = {
            'success': True,
            'symbols_count': len(symbols),
            'data': {}
        }
        for symbol in symbols:
            result['data'][symbol] = fetch_market_data(
                symbol,
                options['period'],
                options['interval']
            )
    
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
