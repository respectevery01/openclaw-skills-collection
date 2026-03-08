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

def calculate_macd(
    symbol: str,
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9,
    time_period: str = "1y",
    interval: str = "1d"
) -> Dict[str, Any]:
    """
    Calculate MACD (Moving Average Convergence Divergence) for a given symbol.
    
    Args:
        symbol: Stock or crypto symbol
        fast_period: Fast EMA period (default: 12)
        slow_period: Slow EMA period (default: 26)
        signal_period: Signal line EMA period (default: 9)
        time_period: Time period for data ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
        interval: Data interval ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')
    
    Returns:
        Dictionary containing MACD data and analysis
    """
    try:
        data = fetch_yahoo_finance_data(symbol, time_period, interval)
        
        if data.empty or len(data) < slow_period + signal_period:
            return {
                'success': False,
                'error': t('macd.insufficient_data'),
                'symbol': symbol
            }
        
        close_prices = data['Close']
        
        ema_fast = close_prices.ewm(span=fast_period, adjust=False).mean()
        ema_slow = close_prices.ewm(span=slow_period, adjust=False).mean()
        
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
        histogram = macd_line - signal_line
        
        current_macd = float(macd_line.iloc[-1])
        current_signal = float(signal_line.iloc[-1])
        current_histogram = float(histogram.iloc[-1])
        
        signal = interpret_macd(current_macd, current_signal, current_histogram)
        
        macd_values = []
        for idx in range(len(macd_line)):
            if not pd.isna(macd_line.iloc[idx]) and not pd.isna(signal_line.iloc[idx]):
                macd_values.append({
                    'date': macd_line.index[idx].strftime('%Y-%m-%d %H:%M:%S'),
                    'macd': float(macd_line.iloc[idx]),
                    'signal': float(signal_line.iloc[idx]),
                    'histogram': float(histogram.iloc[idx])
                })
        
        crossover = detect_macd_crossover(macd_line, signal_line)
        
        return {
            'success': True,
            'symbol': symbol,
            'parameters': {
                'fast_period': fast_period,
                'slow_period': slow_period,
                'signal_period': signal_period
            },
            'time_period': time_period,
            'interval': interval,
            'current_values': {
                'macd': current_macd,
                'signal': current_signal,
                'histogram': current_histogram
            },
            'signal': signal,
            'analysis': {
                'trend': determine_trend(macd_line),
                'momentum': determine_momentum(histogram),
                'crossover': crossover
            },
            'interpretation': get_macd_interpretation(signal, crossover),
            'macd_values': macd_values[-50:]
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'symbol': symbol
        }

def interpret_macd(
    macd: float,
    signal: float,
    histogram: float
) -> str:
    """
    Interpret MACD values and provide trading signal.
    
    Args:
        macd: Current MACD value
        signal: Current signal line value
        histogram: Current histogram value
    
    Returns:
        Trading signal string
    """
    if macd > signal and histogram > 0:
        if histogram > 0.5:
            return 'strong_buy'
        else:
            return 'buy'
    elif macd < signal and histogram < 0:
        if histogram < -0.5:
            return 'strong_sell'
        else:
            return 'sell'
    elif macd > signal and histogram < 0:
        return 'weak_buy'
    elif macd < signal and histogram > 0:
        return 'weak_sell'
    else:
        return 'neutral'

def detect_macd_crossover(
    macd_line: pd.Series,
    signal_line: pd.Series,
    lookback: int = 5
) -> Dict[str, Any]:
    """
    Detect MACD crossovers.
    
    Args:
        macd_line: MACD line values
        signal_line: Signal line values
        lookback: Number of periods to look back
    
    Returns:
        Dictionary containing crossover information
    """
    recent_macd = macd_line.tail(lookback)
    recent_signal = signal_line.tail(lookback)
    
    bullish_crossover = False
    bearish_crossover = False
    
    for i in range(1, len(recent_macd)):
        if (recent_macd.iloc[i-1] <= recent_signal.iloc[i-1] and 
            recent_macd.iloc[i] > recent_signal.iloc[i]):
            bullish_crossover = True
            break
        
        if (recent_macd.iloc[i-1] >= recent_signal.iloc[i-1] and 
            recent_macd.iloc[i] < recent_signal.iloc[i]):
            bearish_crossover = True
            break
    
    return {
        'bullish_crossover': bullish_crossover,
        'bearish_crossover': bearish_crossover,
        'last_bullish_date': None,
        'last_bearish_date': None
    }

def determine_trend(macd_line: pd.Series) -> str:
    """
    Determine trend based on MACD line.
    
    Args:
        macd_line: MACD line values
    
    Returns:
        Trend string
    """
    recent_macd = macd_line.tail(20)
    
    if recent_macd.iloc[-1] > recent_macd.iloc[0]:
        if recent_macd.diff().mean() > 0:
            return 'strong_uptrend'
        else:
            return 'uptrend'
    else:
        if recent_macd.diff().mean() < 0:
            return 'strong_downtrend'
        else:
            return 'downtrend'

def determine_momentum(histogram: pd.Series) -> str:
    """
    Determine momentum based on histogram.
    
    Args:
        histogram: Histogram values
    
    Returns:
        Momentum string
    """
    recent_hist = histogram.tail(10)
    current_hist = recent_hist.iloc[-1]
    
    if current_hist > 0.5:
        return 'strong_bullish'
    elif current_hist > 0:
        return 'bullish'
    elif current_hist < -0.5:
        return 'strong_bearish'
    elif current_hist < 0:
        return 'bearish'
    else:
        return 'neutral'

def get_macd_interpretation(
    signal: str,
    crossover: Dict[str, Any]
) -> Dict[str, str]:
    """
    Get detailed interpretation of MACD signal.
    
    Args:
        signal: MACD signal
        crossover: Crossover information
    
    Returns:
        Dictionary containing interpretation details
    """
    interpretation = {
        'signal': signal,
        'description': '',
        'recommendation': '',
        'risk': 'medium'
    }
    
    if signal == 'strong_buy':
        interpretation['description'] = t('macd.strong_bullish')
        interpretation['recommendation'] = t('macd.strong_buy_recommendation')
        interpretation['risk'] = 'high'
    elif signal == 'buy':
        interpretation['description'] = t('macd.bullish')
        interpretation['recommendation'] = t('macd.buy_recommendation')
        interpretation['risk'] = 'medium'
    elif signal == 'weak_buy':
        interpretation['description'] = t('macd.weak_bullish')
        interpretation['recommendation'] = t('macd.weak_buy_recommendation')
        interpretation['risk'] = 'low'
    elif signal == 'strong_sell':
        interpretation['description'] = t('macd.strong_bearish')
        interpretation['recommendation'] = t('macd.strong_sell_recommendation')
        interpretation['risk'] = 'high'
    elif signal == 'sell':
        interpretation['description'] = t('macd.bearish')
        interpretation['recommendation'] = t('macd.sell_recommendation')
        interpretation['risk'] = 'medium'
    elif signal == 'weak_sell':
        interpretation['description'] = t('macd.weak_bearish')
        interpretation['recommendation'] = t('macd.weak_sell_recommendation')
        interpretation['risk'] = 'low'
    else:
        interpretation['description'] = t('macd.neutral')
        interpretation['recommendation'] = t('macd.hold_recommendation')
        interpretation['risk'] = 'low'
    
    if crossover['bullish_crossover']:
        interpretation['crossover_signal'] = t('macd.bullish_crossover')
    elif crossover['bearish_crossover']:
        interpretation['crossover_signal'] = t('macd.bearish_crossover')
    else:
        interpretation['crossover_signal'] = t('macd.no_crossover')
    
    return interpretation

def calculate_multiple_indicators(
    symbol: str,
    time_period: str = "1y",
    interval: str = "1d"
) -> Dict[str, Any]:
    """
    Calculate multiple technical indicators for comprehensive analysis.
    
    Args:
        symbol: Stock or crypto symbol
        time_period: Time period for data
        interval: Data interval
    
    Returns:
        Dictionary containing multiple indicators
    """
    try:
        from assets.rsi import calculate_rsi
        
        macd_result = calculate_macd(symbol, time_period=time_period, interval=interval)
        rsi_result = calculate_rsi(symbol, time_period=time_period, interval=interval)
        
        if not macd_result.get('success') or not rsi_result.get('success'):
            return {
                'success': False,
                'error': t('macd.calculation_error'),
                'symbol': symbol
            }
        
        combined_signal = combine_signals(
            macd_result['signal'],
            rsi_result['signal']
        )
        
        return {
            'success': True,
            'symbol': symbol,
            'combined_signal': combined_signal,
            'macd': {
                'signal': macd_result['signal'],
                'current_values': macd_result['current_values'],
                'trend': macd_result['analysis']['trend'],
                'momentum': macd_result['analysis']['momentum']
            },
            'rsi': {
                'signal': rsi_result['signal'],
                'current_rsi': rsi_result['current_rsi'],
                'level': rsi_result['interpretation']['level']
            },
            'recommendation': get_combined_recommendation(combined_signal)
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'symbol': symbol
        }

def combine_signals(macd_signal: str, rsi_signal: str) -> str:
    """
    Combine MACD and RSI signals for a more robust trading signal.
    
    Args:
        macd_signal: MACD signal
        rsi_signal: RSI signal
    
    Returns:
        Combined signal string
    """
    buy_signals = ['strong_buy', 'buy', 'weak_buy']
    sell_signals = ['strong_sell', 'sell', 'weak_sell']
    
    if macd_signal in buy_signals and rsi_signal in buy_signals:
        if macd_signal == 'strong_buy' or rsi_signal == 'strong_buy':
            return 'strong_buy'
        else:
            return 'buy'
    elif macd_signal in sell_signals and rsi_signal in sell_signals:
        if macd_signal == 'strong_sell' or rsi_signal == 'strong_sell':
            return 'strong_sell'
        else:
            return 'sell'
    elif macd_signal in buy_signals and rsi_signal not in sell_signals:
        return 'weak_buy'
    elif macd_signal in sell_signals and rsi_signal not in buy_signals:
        return 'weak_sell'
    else:
        return 'neutral'

def get_combined_recommendation(signal: str) -> str:
    """
    Get recommendation based on combined signal.
    
    Args:
        signal: Combined signal
    
    Returns:
        Recommendation string
    """
    recommendations = {
        'strong_buy': t('macd.strong_buy_combined'),
        'buy': t('macd.buy_combined'),
        'weak_buy': t('macd.weak_buy_combined'),
        'strong_sell': t('macd.strong_sell_combined'),
        'sell': t('macd.sell_combined'),
        'weak_sell': t('macd.weak_sell_combined'),
        'neutral': t('macd.hold_combined')
    }
    
    return recommendations.get(signal, t('macd.hold_combined'))

def main():
    import json
    
    if len(sys.argv) < 2:
        print(t('macd.usage'))
        print()
        print('Examples:')
        print('  python macd.py AAPL')
        print('  python macd.py BTC-USD --fast 10 --slow 20')
        print('  python macd.py AAPL --combined')
        print()
        return
    
    symbol = sys.argv[1]
    options = {
        'fast_period': 12,
        'slow_period': 26,
        'signal_period': 9,
        'time_period': '1y',
        'interval': '1d',
        'combined': False
    }
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--fast' and i + 1 < len(sys.argv):
            options['fast_period'] = int(sys.argv[i + 1])
            i += 1
        elif arg == '--slow' and i + 1 < len(sys.argv):
            options['slow_period'] = int(sys.argv[i + 1])
            i += 1
        elif arg == '--signal' and i + 1 < len(sys.argv):
            options['signal_period'] = int(sys.argv[i + 1])
            i += 1
        elif arg == '--time-period' and i + 1 < len(sys.argv):
            options['time_period'] = sys.argv[i + 1]
            i += 1
        elif arg == '--interval' and i + 1 < len(sys.argv):
            options['interval'] = sys.argv[i + 1]
            i += 1
        elif arg == '--combined':
            options['combined'] = True
        
        i += 1
    
    if options['combined']:
        result = calculate_multiple_indicators(
            symbol,
            options['time_period'],
            options['interval']
        )
    else:
        result = calculate_macd(
            symbol,
            options['fast_period'],
            options['slow_period'],
            options['signal_period'],
            options['time_period'],
            options['interval']
        )
    
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
