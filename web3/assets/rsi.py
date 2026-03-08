import pandas as pd
import numpy as np
from datetime import datetime
from typing import Optional, Dict, Any, List
import sys
from pathlib import Path

script_dir = Path(__file__).parent
web3_dir = script_dir.parent
sys.path.insert(0, str(web3_dir))

from assets.i18n import t
from assets.data_fetcher import fetch_yahoo_finance_data

def calculate_rsi(
    symbol: str,
    period: int = 14,
    time_period: str = "1y",
    interval: str = "1d"
) -> Dict[str, Any]:
    """
    Calculate Relative Strength Index (RSI) for a given symbol.
    
    Args:
        symbol: Stock or crypto symbol
        period: RSI calculation period (default: 14)
        time_period: Time period for data ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
        interval: Data interval ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')
    
    Returns:
        Dictionary containing RSI data and analysis
    """
    try:
        data = fetch_yahoo_finance_data(symbol, time_period, interval)
        
        if data.empty or len(data) < period + 1:
            return {
                'success': False,
                'error': t('rsi.insufficient_data'),
                'symbol': symbol
            }
        
        close_prices = data['Close']
        
        delta = close_prices.diff()
        
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        current_rsi = float(rsi.iloc[-1])
        
        signal = interpret_rsi(current_rsi)
        
        rsi_values = []
        for idx, rsi_val in rsi.items():
            if not pd.isna(rsi_val):
                rsi_values.append({
                    'date': idx.strftime('%Y-%m-%d %H:%M:%S'),
                    'rsi': float(rsi_val)
                })
        
        overbought_count = sum(1 for item in rsi_values if item['rsi'] > 70)
        oversold_count = sum(1 for item in rsi_values if item['rsi'] < 30)
        
        return {
            'success': True,
            'symbol': symbol,
            'period': period,
            'time_period': time_period,
            'interval': interval,
            'current_rsi': current_rsi,
            'signal': signal,
            'analysis': {
                'overbought_periods': overbought_count,
                'oversold_periods': oversold_count,
                'rsi_range': {
                    'max': float(rsi.max()),
                    'min': float(rsi.min()),
                    'avg': float(rsi.mean())
                }
            },
            'interpretation': get_rsi_interpretation(current_rsi),
            'rsi_values': rsi_values[-50:]
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'symbol': symbol
        }

def interpret_rsi(rsi: float) -> str:
    """
    Interpret RSI value and provide trading signal.
    
    Args:
        rsi: RSI value
    
    Returns:
        Trading signal string
    """
    if rsi >= 80:
        return 'strong_sell'
    elif rsi >= 70:
        return 'sell'
    elif rsi >= 60:
        return 'weak_sell'
    elif rsi <= 20:
        return 'strong_buy'
    elif rsi <= 30:
        return 'buy'
    elif rsi <= 40:
        return 'weak_buy'
    else:
        return 'neutral'

def get_rsi_interpretation(rsi: float) -> Dict[str, str]:
    """
    Get detailed interpretation of RSI value.
    
    Args:
        rsi: RSI value
    
    Returns:
        Dictionary containing interpretation details
    """
    if rsi >= 80:
        return {
            'level': 'extremely_overbought',
            'description': t('rsi.extremely_overbought'),
            'recommendation': t('rsi.strong_sell_recommendation'),
            'risk': 'very_high'
        }
    elif rsi >= 70:
        return {
            'level': 'overbought',
            'description': t('rsi.overbought'),
            'recommendation': t('rsi.sell_recommendation'),
            'risk': 'high'
        }
    elif rsi >= 60:
        return {
            'level': 'slightly_overbought',
            'description': t('rsi.slightly_overbought'),
            'recommendation': t('rsi.weak_sell_recommendation'),
            'risk': 'medium'
        }
    elif rsi <= 20:
        return {
            'level': 'extremely_oversold',
            'description': t('rsi.extremely_oversold'),
            'recommendation': t('rsi.strong_buy_recommendation'),
            'risk': 'very_high'
        }
    elif rsi <= 30:
        return {
            'level': 'oversold',
            'description': t('rsi.oversold'),
            'recommendation': t('rsi.buy_recommendation'),
            'risk': 'high'
        }
    elif rsi <= 40:
        return {
            'level': 'slightly_oversold',
            'description': t('rsi.slightly_oversold'),
            'recommendation': t('rsi.weak_buy_recommendation'),
            'risk': 'medium'
        }
    else:
        return {
            'level': 'neutral',
            'description': t('rsi.neutral'),
            'recommendation': t('rsi.hold_recommendation'),
            'risk': 'low'
        }

def calculate_rsi_divergence(
    symbol: str,
    period: int = 14,
    lookback: int = 20
) -> Dict[str, Any]:
    """
    Calculate RSI divergence patterns.
    
    Args:
        symbol: Stock or crypto symbol
        period: RSI calculation period
        lookback: Number of periods to look back for divergence
    
    Returns:
        Dictionary containing divergence analysis
    """
    try:
        data = fetch_yahoo_finance_data(symbol, "6mo", "1d")
        
        if data.empty or len(data) < period + lookback:
            return {
                'success': False,
                'error': t('rsi.insufficient_data'),
                'symbol': symbol
            }
        
        close_prices = data['Close']
        delta = close_prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        recent_data = data.tail(lookback)
        recent_rsi = rsi.tail(lookback)
        
        price_highs = recent_data['High'].nlargest(3)
        price_lows = recent_data['Low'].nsmallest(3)
        rsi_highs = recent_rsi.nlargest(3)
        rsi_lows = recent_rsi.nsmallest(3)
        
        bearish_divergence = False
        bullish_divergence = False
        
        if len(price_highs) >= 2 and len(rsi_highs) >= 2:
            if price_highs.iloc[-1] > price_highs.iloc[-2] and rsi_highs.iloc[-1] < rsi_highs.iloc[-2]:
                bearish_divergence = True
        
        if len(price_lows) >= 2 and len(rsi_lows) >= 2:
            if price_lows.iloc[-1] < price_lows.iloc[-2] and rsi_lows.iloc[-1] > rsi_lows.iloc[-2]:
                bullish_divergence = True
        
        return {
            'success': True,
            'symbol': symbol,
            'divergence': {
                'bearish_divergence': bearish_divergence,
                'bullish_divergence': bullish_divergence
            },
            'interpretation': {
                'bearish': t('rsi.bearish_divergence') if bearish_divergence else t('rsi.no_bearish_divergence'),
                'bullish': t('rsi.bullish_divergence') if bullish_divergence else t('rsi.no_bullish_divergence')
            }
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'symbol': symbol
        }

def main():
    import json
    
    if len(sys.argv) < 2:
        print(t('rsi.usage'))
        print()
        print('Examples:')
        print('  python rsi.py AAPL')
        print('  python rsi.py BTC-USD --period 7')
        print('  python rsi.py AAPL --divergence')
        print()
        return
    
    symbol = sys.argv[1]
    options = {
        'period': 14,
        'time_period': '1y',
        'interval': '1d',
        'check_divergence': False
    }
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--period' and i + 1 < len(sys.argv):
            options['period'] = int(sys.argv[i + 1])
            i += 1
        elif arg == '--time-period' and i + 1 < len(sys.argv):
            options['time_period'] = sys.argv[i + 1]
            i += 1
        elif arg == '--interval' and i + 1 < len(sys.argv):
            options['interval'] = sys.argv[i + 1]
            i += 1
        elif arg == '--divergence':
            options['check_divergence'] = True
        
        i += 1
    
    if options['check_divergence']:
        result = calculate_rsi_divergence(symbol, options['period'])
    else:
        result = calculate_rsi(
            symbol,
            options['period'],
            options['time_period'],
            options['interval']
        )
    
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
