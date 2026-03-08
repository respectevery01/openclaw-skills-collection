import pandas as pd
import json
from typing import Dict, Any, Optional
from datetime import datetime
import sys
from pathlib import Path

script_dir = Path(__file__).parent
web3_dir = script_dir.parent
sys.path.insert(0, str(web3_dir))

from assets.data_fetcher import fetch_yahoo_finance_data
from assets.i18n import t

def calculate_kline_indicators(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate K-line (candlestick) indicators.
    
    Args:
        df: DataFrame with OHLCV data
    
    Returns:
        Dictionary with K-line indicators
    """
    if df.empty:
        return {}
    
    close = df['Close']
    high = df['High']
    low = df['Low']
    open_price = df['Open']
    volume = df['Volume']
    
    latest = df.iloc[-1]
    
    indicators = {
        'latest': {
            'timestamp': latest.name.strftime('%Y-%m-%d %H:%M:%S') if hasattr(latest.name, 'strftime') else str(latest.name),
            'open': float(latest['Open']),
            'high': float(latest['High']),
            'low': float(latest['Low']),
            'close': float(latest['Close']),
            'volume': float(latest['Volume'])
        },
        'price_change': {
            'absolute': float(latest['Close'] - df.iloc[-2]['Close']) if len(df) > 1 else 0,
            'percentage': ((latest['Close'] - df.iloc[-2]['Close']) / df.iloc[-2]['Close'] * 100) if len(df) > 1 else 0
        },
        'period_stats': {
            'period_high': float(high.max()),
            'period_low': float(low.min()),
            'period_open': float(open_price.iloc[0]),
            'period_close': float(close.iloc[-1]),
            'avg_volume': float(volume.mean()),
            'total_volume': float(volume.sum())
        },
        'candlestick_type': analyze_candlestick(latest)
    }
    
    return indicators

def analyze_candlestick(candle: pd.Series) -> Dict[str, Any]:
    """
    Analyze candlestick pattern.
    
    Args:
        candle: Single candle data
    
    Returns:
        Dictionary with candlestick analysis
    """
    open_price = float(candle['Open'])
    high = float(candle['High'])
    low = float(candle['Low'])
    close = float(candle['Close'])
    
    body_size = abs(close - open_price)
    upper_shadow = high - max(open_price, close)
    lower_shadow = min(open_price, close) - low
    
    candle_type = 'neutral'
    if close > open_price:
        candle_type = 'bullish'
    elif close < open_price:
        candle_type = 'bearish'
    
    strength = 'weak'
    if body_size > 0:
        total_range = high - low
        if total_range > 0:
            body_ratio = body_size / total_range
            if body_ratio > 0.7:
                strength = 'strong'
            elif body_ratio > 0.4:
                strength = 'moderate'
    
    return {
        'type': candle_type,
        'strength': strength,
        'body_size': body_size,
        'upper_shadow': upper_shadow,
        'lower_shadow': lower_shadow,
        'description': get_candlestick_description(candle_type, strength, upper_shadow, lower_shadow)
    }

def get_candlestick_description(candle_type: str, strength: str, upper_shadow: float, lower_shadow: float) -> str:
    """
    Get human-readable candlestick description.
    
    Args:
        candle_type: bullish/bearish/neutral
        strength: strong/moderate/weak
        upper_shadow: Upper shadow size
        lower_shadow: Lower shadow size
    
    Returns:
        Description string
    """
    descriptions = {
        'bullish': {
            'strong': 'Strong bullish candle - strong upward momentum',
            'moderate': 'Bullish candle - upward movement',
            'weak': 'Weak bullish candle - slight upward movement'
        },
        'bearish': {
            'strong': 'Strong bearish candle - strong downward momentum',
            'moderate': 'Bearish candle - downward movement',
            'weak': 'Weak bearish candle - slight downward movement'
        },
        'neutral': {
            'strong': 'Strong neutral candle - indecision in market',
            'moderate': 'Neutral candle - market consolidation',
            'weak': 'Weak neutral candle - low volatility'
        }
    }
    
    desc = descriptions.get(candle_type, {}).get(strength, 'Unknown pattern')
    
    if upper_shadow > 0 and lower_shadow > 0:
        desc += ' with both upper and lower shadows'
    elif upper_shadow > 0:
        desc += ' with upper shadow'
    elif lower_shadow > 0:
        desc += ' with lower shadow'
    
    return desc

def detect_patterns(df: pd.DataFrame, lookback: int = 20) -> Dict[str, Any]:
    """
    Detect common candlestick patterns.
    
    Args:
        df: DataFrame with OHLCV data
        lookback: Number of candles to look back
    
    Returns:
        Dictionary with detected patterns
    """
    if len(df) < lookback:
        return {'patterns': [], 'message': 'Insufficient data for pattern detection'}
    
    patterns = []
    recent = df.tail(lookback)
    
    for i in range(2, len(recent)):
        candle = recent.iloc[i]
        prev1 = recent.iloc[i-1]
        prev2 = recent.iloc[i-2]
        
        pattern = detect_single_pattern(candle, prev1, prev2)
        if pattern:
            patterns.append({
                'timestamp': candle.name.strftime('%Y-%m-%d %H:%M:%S') if hasattr(candle.name, 'strftime') else str(candle.name),
                'pattern': pattern
            })
    
    return {
        'patterns': patterns[-5:] if len(patterns) > 5 else patterns,
        'total_detected': len(patterns)
    }

def detect_single_pattern(candle: pd.Series, prev1: pd.Series, prev2: pd.Series) -> Optional[str]:
    """
    Detect single candlestick pattern.
    
    Args:
        candle: Current candle
        prev1: Previous candle
        prev2: Two candles back
    
    Returns:
        Pattern name or None
    """
    open_price = float(candle['Open'])
    close = float(candle['Close'])
    high = float(candle['High'])
    low = float(candle['Low'])
    
    prev1_close = float(prev1['Close'])
    prev1_open = float(prev1['Open'])
    prev1_high = float(prev1['High'])
    prev1_low = float(prev1['Low'])
    
    prev2_close = float(prev2['Close'])
    
    body_size = abs(close - open_price)
    prev1_body = abs(prev1_close - prev1_open)
    
    if body_size == 0:
        return None
    
    patterns = []
    
    if close > open_price:
        if prev1_close < prev1_open:
            if close > prev1_high:
                patterns.append('Bullish Engulfing')
        if close < prev1_high and close > prev1_close:
            patterns.append('Hammer')
    
    if close < open_price:
        if prev1_close > prev1_open:
            if close < prev1_low:
                patterns.append('Bearish Engulfing')
        if close > prev1_low and close < prev1_close:
            patterns.append('Shooting Star')
    
    if abs(close - open_price) < 0.1 * (high - low):
        patterns.append('Doji')
    
    if abs(close - prev1_close) < 0.05 * prev1_close:
        patterns.append('Spinning Top')
    
    return patterns[0] if patterns else None

def main():
    if len(sys.argv) < 2:
        print('Usage:')
        print('  python kline.py <symbol> [options]')
        print()
        print('Options:')
        print('  --period <period>    Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max)')
        print('  --interval <interval>  Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 1wk, 1mo)')
        print('  --patterns             Detect candlestick patterns')
        print('  --lookback <n>        Number of candles to look back for patterns (default: 20)')
        print()
        print('Examples:')
        print('  python kline.py AAPL')
        print('  python kline.py BTC-USD --interval 1h --period 1mo')
        print('  python kline.py ETH-USD --patterns --lookback 30')
        print()
        return
    
    symbol = sys.argv[1]
    
    options = {
        'period': '1y',
        'interval': '1d',
        'patterns': False,
        'lookback': 20
    }
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--period' and i + 1 < len(sys.argv):
            options['period'] = sys.argv[i + 1]
            i += 1
        elif arg == '--interval' and i + 1 < len(sys.argv):
            options['interval'] = sys.argv[i + 1]
            i += 1
        elif arg == '--patterns':
            options['patterns'] = True
        elif arg == '--lookback' and i + 1 < len(sys.argv):
            options['lookback'] = int(sys.argv[i + 1])
            i += 1
        
        i += 1
    
    try:
        print(f'Fetching K-line data for {symbol}...')
        df = fetch_yahoo_finance_data(symbol, options['period'], options['interval'])
        
        if df.empty:
            print('No data found for symbol')
            return
        
        print(f'\nData fetched: {len(df)} candles')
        print(f'Period: {options["period"]}, Interval: {options["interval"]}')
        print()
        
        indicators = calculate_kline_indicators(df)
        
        print('=== Latest K-line ===')
        latest = indicators['latest']
        print(f"Time: {latest['timestamp']}")
        print(f"Open: {latest['open']:.4f}")
        print(f"High: {latest['high']:.4f}")
        print(f"Low: {latest['low']:.4f}")
        print(f"Close: {latest['close']:.4f}")
        print(f"Volume: {latest['volume']:,.0f}")
        print()
        
        print('=== Price Change ===')
        change = indicators['price_change']
        print(f"Change: {change['absolute']:+.4f} ({change['percentage']:+.2f}%)")
        print()
        
        print('=== Period Statistics ===')
        stats = indicators['period_stats']
        print(f"Period High: {stats['period_high']:.4f}")
        print(f"Period Low: {stats['period_low']:.4f}")
        print(f"Period Open: {stats['period_open']:.4f}")
        print(f"Period Close: {stats['period_close']:.4f}")
        print(f"Average Volume: {stats['avg_volume']:,.0f}")
        print(f"Total Volume: {stats['total_volume']:,.0f}")
        print()
        
        print('=== Candlestick Analysis ===')
        candlestick = indicators['candlestick_type']
        print(f"Type: {candlestick['type']}")
        print(f"Strength: {candlestick['strength']}")
        print(f"Body Size: {candlestick['body_size']:.4f}")
        print(f"Upper Shadow: {candlestick['upper_shadow']:.4f}")
        print(f"Lower Shadow: {candlestick['lower_shadow']:.4f}")
        print(f"Description: {candlestick['description']}")
        print()
        
        if options['patterns']:
            print('=== Pattern Detection ===')
            pattern_results = detect_patterns(df, options['lookback'])
            print(f"Lookback period: {options['lookback']} candles")
            print(f"Total patterns detected: {pattern_results['total_detected']}")
            print()
            
            if pattern_results['patterns']:
                print('Recent patterns:')
                for pattern in pattern_results['patterns'][-5:]:
                    print(f"  {pattern['timestamp']}: {pattern['pattern']}")
            else:
                print('No significant patterns detected')
        
        print('\n=== Full Data ===')
        print(df.tail(10).to_string())
        
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
