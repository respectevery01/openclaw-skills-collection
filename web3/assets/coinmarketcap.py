import os
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from typing import Dict, Any, List, Optional
import sys
from pathlib import Path
from dotenv import load_dotenv

script_dir = Path(__file__).parent
web3_dir = script_dir.parent
sys.path.insert(0, str(web3_dir))

from assets.i18n import t

load_dotenv()

COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')

def get_cryptocurrency_listings(
    start: int = 1,
    limit: int = 100,
    convert: str = 'USD',
    sort: str = 'market_cap',
    sort_dir: str = 'desc',
    cryptocurrency_type: str = 'all'
) -> Dict[str, Any]:
    """
    Get a paginated list of all cryptocurrencies by CoinMarketCap ID.
    
    Args:
        start: Return results from rank [start] and above
        limit: Only return the top [limit] results
        convert: Return price, 24h volume, and market cap in terms of another fiat or cryptocurrency
        sort: Sort by market_cap, name, symbol, date_added, market_cap_strict, price, circulating_supply, total_supply, max_supply, market_cap_by_total_supply_strict, volume_24h, percent_change_1h, percent_change_24h, percent_change_7d, volume_7d, volume_30d
        sort_dir: Direction in which to order cryptocurrencies ('asc' or 'desc')
        cryptocurrency_type: Type of cryptocurrency to include ('all', 'coins', 'tokens')
    
    Returns:
        Dictionary containing cryptocurrency listings data
    """
    try:
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        
        parameters = {
            'start': str(start),
            'limit': str(limit),
            'convert': convert,
            'sort': sort,
            'sort_dir': sort_dir,
            'cryptocurrency_type': cryptocurrency_type
        }
        
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }
        
        session = Session()
        session.headers.update(headers)
        
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        if 'status' in data and str(data['status']['error_code']) != '0':
            return {
                'success': False,
                'error': data['status']['error_message'],
                'error_code': data['status']['error_code']
            }
        
        return {
            'success': True,
            'data': data.get('data', data),
            'status': data.get('status', {})
        }
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return {
            'success': False,
            'error': str(e)
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def get_cryptocurrency_info(
    symbol: str,
    convert: str = 'USD'
) -> Dict[str, Any]:
    """
    Get information for a specific cryptocurrency by symbol.
    
    Args:
        symbol: Cryptocurrency symbol (e.g., 'BTC', 'ETH')
        convert: Return price in terms of another fiat or cryptocurrency
    
    Returns:
        Dictionary containing cryptocurrency information
    """
    try:
        url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
        
        parameters = {
            'symbol': symbol,
            'convert': convert
        }
        
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }
        
        session = Session()
        session.headers.update(headers)
        
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        if 'status' in data and str(data['status']['error_code']) != '0':
            return {
                'success': False,
                'error': data['status']['error_message'],
                'error_code': data['status']['error_code']
            }
        
        return {
            'success': True,
            'data': data.get('data', data),
            'status': data.get('status', {})
        }
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return {
            'success': False,
            'error': str(e)
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def get_global_metrics(convert: str = 'USD') -> Dict[str, Any]:
    """
    Get global market data.
    
    Args:
        convert: Return price in terms of another fiat or cryptocurrency
    
    Returns:
        Dictionary containing global market metrics
    """
    try:
        url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
        
        parameters = {
            'convert': convert
        }
        
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }
        
        session = Session()
        session.headers.update(headers)
        
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        if 'status' in data and str(data['status']['error_code']) != '0':
            return {
                'success': False,
                'error': data['status']['error_message'],
                'error_code': data['status']['error_code']
            }
        
        return {
            'success': True,
            'data': data.get('data', data),
            'status': data.get('status', {})
        }
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return {
            'success': False,
            'error': str(e)
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def get_fear_and_greed_index() -> Dict[str, Any]:
    """
    Get the Fear and Greed Index for cryptocurrency market sentiment.
    
    Returns:
        Dictionary containing fear and greed index data
    """
    response = None
    try:
        url = 'https://pro-api.coinmarketcap.com/v3/fear-and-greed/latest'
        
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }
        
        session = Session()
        session.headers.update(headers)
        
        response = session.get(url)
        data = json.loads(response.text)
        
        if 'status' in data and str(data['status']['error_code']) != '0':
            return {
                'success': False,
                'error': data['status']['error_message'],
                'error_code': data['status']['error_code']
            }
        
        return {
            'success': True,
            'data': data.get('data', data),
            'status': data.get('status', {})
        }
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return {
            'success': False,
            'error': str(e),
            'response': response.text if response else None
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def get_cmc20_index() -> Dict[str, Any]:
    """
    Get the CMC20 Index data.
    
    Returns:
        Dictionary containing CMC20 index data
    """
    response = None
    try:
        url = 'https://pro-api.coinmarketcap.com/v3/cmc20/latest'
        
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }
        
        session = Session()
        session.headers.update(headers)
        
        response = session.get(url)
        data = json.loads(response.text)
        
        if 'status' in data and str(data['status']['error_code']) != '0':
            return {
                'success': False,
                'error': data['status']['error_message'],
                'error_code': data['status']['error_code']
            }
        
        return {
            'success': True,
            'data': data.get('data', data),
            'status': data.get('status', {})
        }
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return {
            'success': False,
            'error': str(e),
            'response': response.text if response else None
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def get_cmc100_index() -> Dict[str, Any]:
    """
    Get the CMC100 Index data.
    
    Returns:
        Dictionary containing CMC100 index data
    """
    response = None
    try:
        url = 'https://pro-api.coinmarketcap.com/v3/cmc100/latest'
        
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }
        
        session = Session()
        session.headers.update(headers)
        
        response = session.get(url)
        data = json.loads(response.text)
        
        if 'status' in data and str(data['status']['error_code']) != '0':
            return {
                'success': False,
                'error': data['status']['error_message'],
                'error_code': data['status']['error_code']
            }
        
        return {
            'success': True,
            'data': data.get('data', data),
            'status': data.get('status', {})
        }
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return {
            'success': False,
            'error': str(e),
            'response': response.text if response else None
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def main():
    if len(sys.argv) < 2:
        print('Usage:')
        print('  python coinmarketcap.py listings [options]')
        print('  python coinmarketcap.py info <symbol> [options]')
        print('  python coinmarketcap.py global [options]')
        print('  python coinmarketcap.py fear-greed')
        print('  python coinmarketcap.py cmc20')
        print('  python coinmarketcap.py cmc100')
        print()
        print('Examples:')
        print('  python coinmarketcap.py listings --limit 10')
        print('  python coinmarketcap.py listings --limit 50 --convert EUR')
        print('  python coinmarketcap.py info BTC')
        print('  python coinmarketcap.py info ETH --convert EUR')
        print('  python coinmarketcap.py global')
        print('  python coinmarketcap.py fear-greed')
        print('  python coinmarketcap.py cmc20')
        print('  python coinmarketcap.py cmc100')
        print()
        return
    
    command = sys.argv[1].lower()
    
    options = {
        'start': 1,
        'limit': 100,
        'convert': 'USD',
        'sort': 'market_cap',
        'sort_dir': 'desc',
        'cryptocurrency_type': 'all'
    }
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg.startswith('--'):
            if arg == '--start' and i + 1 < len(sys.argv):
                options['start'] = int(sys.argv[i + 1])
                i += 1
            elif arg == '--limit' and i + 1 < len(sys.argv):
                options['limit'] = int(sys.argv[i + 1])
                i += 1
            elif arg == '--convert' and i + 1 < len(sys.argv):
                options['convert'] = sys.argv[i + 1]
                i += 1
            elif arg == '--sort' and i + 1 < len(sys.argv):
                options['sort'] = sys.argv[i + 1]
                i += 1
            elif arg == '--sort-dir' and i + 1 < len(sys.argv):
                options['sort_dir'] = sys.argv[i + 1]
                i += 1
            elif arg == '--type' and i + 1 < len(sys.argv):
                options['cryptocurrency_type'] = sys.argv[i + 1]
                i += 1
        
        i += 1
    
    if command == 'listings':
        result = get_cryptocurrency_listings(
            start=options['start'],
            limit=options['limit'],
            convert=options['convert'],
            sort=options['sort'],
            sort_dir=options['sort_dir'],
            cryptocurrency_type=options['cryptocurrency_type']
        )
    elif command == 'info':
        if len(sys.argv) < 3:
            print('Error: Symbol required')
            print('Usage: python coinmarketcap.py info <symbol> [options]')
            return
        
        symbol = sys.argv[2]
        result = get_cryptocurrency_info(symbol, convert=options['convert'])
    elif command == 'global':
        result = get_global_metrics(convert=options['convert'])
    elif command == 'fear-greed':
        result = get_fear_and_greed_index()
    elif command == 'cmc20':
        result = get_cmc20_index()
    elif command == 'cmc100':
        result = get_cmc100_index()
    else:
        print(f'Unknown command: {command}')
        print()
        print('Available commands:')
        print('  listings    - Get cryptocurrency listings')
        print('  info        - Get cryptocurrency info by symbol')
        print('  global      - Get global market metrics')
        print('  fear-greed - Get Fear and Greed Index')
        print('  cmc20       - Get CMC20 Index')
        print('  cmc100      - Get CMC100 Index')
        return
    
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
