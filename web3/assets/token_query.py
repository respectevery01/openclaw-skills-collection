import json
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
from okx.api._client import Client

sys.path.insert(0, str(Path(__file__).parent.parent))
from assets.i18n import t, get_chain_name

load_dotenv()

OKX_WEB3_API_BASE = "https://web3.okx.com"

CHAIN_IDS = {
    'ethereum': '1',
    'bsc': '56',
    'sol': '501'
}

OKX_API_KEY = os.getenv('OKX_API_KEY')
OKX_API_SECRET = os.getenv('OKX_API_SECRET')
OKX_API_PASSPHRASE = os.getenv('OKX_API_PASSPHRASE')

client = Client(
    key=OKX_API_KEY,
    secret=OKX_API_SECRET,
    passphrase=OKX_API_PASSPHRASE,
    flag='0',
    proxy_host=OKX_WEB3_API_BASE
)

def token_query(chain, token_address):
    """
    Query token information (price, market cap, liquidity, etc.)
    Args:
        chain: Chain name ('ethereum', 'bsc', 'sol')
        token_address: Token contract address
    Returns:
        Dictionary containing detailed token information
    """
    if chain not in CHAIN_IDS:
        return {"error": t('token_query.error_unsupported_chain')}
    
    try:
        price_result = _get_token_price(chain, token_address)
        if price_result.get('error'):
            return price_result
        
        detail_result = _get_token_details(chain, token_address)
        
        result = {
            'chain': chain,
            'token_address': token_address,
            'price_usd': price_result.get('price', '0'),
            'timestamp': price_result.get('timestamp', str(int(time.time() * 1000)))
        }
        
        if not detail_result.get('error'):
            result.update({
                'name': detail_result.get('name', ''),
                'symbol': detail_result.get('symbol', ''),
                'market_cap': detail_result.get('marketCap', ''),
                'volume_24h': detail_result.get('volume24h', ''),
                'total_supply': detail_result.get('totalSupply', ''),
                'max_supply': detail_result.get('maxSupply', ''),
                'decimals': detail_result.get('decimals', ''),
                'logo_url': detail_result.get('logoUrl', ''),
                'official_website': detail_result.get('officialWebsite', ''),
                'social_urls': detail_result.get('socialUrls', {})
            })
        
        return result
    except Exception as e:
        return {'error': f"{t('token_query.error_api_failed')} {str(e)}"}

def _get_token_price(chain, token_address):
    """Query token real-time price"""
    request_path = "/api/v5/wallet/token/real-time-price"
    payload = [{
        "chainIndex": CHAIN_IDS[chain],
        "tokenAddress": token_address
    }]
    
    try:
        result = client.send_request(request_path, "POST", payload, proxy_host=None)
        if result.get('code') == '0' and result.get('data'):
            token_data = result['data'][0]
            return {
                'price': token_data.get('price', '0'),
                'timestamp': token_data.get('time', str(int(time.time() * 1000)))
            }
        else:
            return {'error': f"{t('token_query.error_query_price')} {result.get('msg', 'Unknown error')}"}
    except Exception as e:
        return {'error': f"{t('token_query.error_price_failed')} {str(e)}"}

def _get_token_details(chain, token_address):
    """Query token detailed information"""
    request_path = "/api/v5/wallet/token/token-detail"
    params = {
        "chainIndex": CHAIN_IDS[chain],
        "tokenAddress": token_address
    }
    
    try:
        result = client.send_request(request_path, "GET", proxy_host=None, **params)
        if result.get('code') == '0' and result.get('data'):
            data = result['data']
            if isinstance(data, list) and len(data) > 0:
                return data[0]
            elif isinstance(data, dict):
                return data
            else:
                return {'error': t('wallet_balance.error_no_data_found')}
        else:
            return {'error': f"{t('token_query.error_query_details')} {result.get('msg', 'Unknown error')}"}
    except Exception as e:
        return {'error': f"{t('token_query.error_details_failed')} {str(e)}"}

if __name__ == '__main__':
    lang = os.getenv('LANG', 'en_us')
    
    print(f'=== {t("app_name")} - {t("token_query.title")} ===')
    print()
    
    if len(sys.argv) > 2:
        chain = sys.argv[1]
        contract = sys.argv[2]
    else:
        print(t('token_query.usage'))
        print(t('token_query.supported_chains'))
        print()
        print(t('token_query.examples'))
        print(f'  python token_query.py ethereum 0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683')
        print(f'  python token_query.py bsc 0x...')
        print(f'  python token_query.py sol So11111111111111111111111111111111111111112')
        print()
        print(t('token_query.interactive_mode'))
        print()
        
        chain = input(f'{t("token_query.enter_chain")} ').strip().lower()
        contract = input(f'{t("token_query.enter_contract")} ').strip()
    
    if not chain or not contract:
        print(t('token_query.error_chain_required'))
        sys.exit(1)
    
    print()
    print(f'{t("token_query.querying")} {contract} on {get_chain_name(chain, lang)}')
    print()
    
    result = token_query(chain, contract)
    print(t('token_query.result'))
    print(json.dumps(result, indent=2, ensure_ascii=False))
