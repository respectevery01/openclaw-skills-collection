import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict, Any, List, Optional
from okx.api._client import Client

sys.path.insert(0, str(Path(__file__).parent.parent))
from assets.i18n import t, get_chain_name

load_dotenv()

OKX_WEB3_API_BASE = "https://web3.okx.com"

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

def scan_meme_tokens(
    chain: str = 'sol',
    stage: str = 'NEW',
    min_volume: Optional[float] = None,
    min_market_cap: Optional[float] = None,
    min_holders: Optional[int] = None,
    min_token_age: Optional[int] = None,
    has_social_links: Optional[bool] = None,
    limit: int = 50
) -> Dict[str, Any]:
    """
    Scan for meme tokens using OKX Web3 API.
    
    Args:
        chain: Blockchain ('sol', 'bsc')
        stage: Token stage ('NEW', 'MIGRATING', 'MIGRATED')
        min_volume: Minimum 24h volume in USD
        min_market_cap: Minimum market cap in USD
        min_holders: Minimum number of holders
        min_token_age: Minimum token age in minutes
        has_social_links: Filter tokens with social links
        limit: Maximum number of tokens to return
    
    Returns:
        Dictionary containing scan results
    """
    try:
        chain_ids = {
            'sol': '501',
            'bsc': '56'
        }
        
        chain_id = chain_ids.get(chain, '501')
        
        request_path = "/api/v6/dex/market/memepump/tokenList"
        params = {
            "chainIndex": chain_id,
            "protocolId": "1",
            "stage": stage,
            "sort": "createdTimestamp",
            "order": "desc",
            "limit": str(limit)
        }
        
        if min_volume:
            params["minVolumeUsd"] = str(min_volume)
        
        if min_market_cap:
            params["minMarketCapUsd"] = str(min_market_cap)
        
        if min_holders:
            params["minHolders"] = str(min_holders)
        
        if min_token_age:
            params["minTokenAge"] = str(min_token_age)
        
        if has_social_links:
            params["hasAtLeastOneSocialLink"] = "true"
        
        result = client.send_request(request_path, "GET", proxy_host=None, **params)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'tokens': []
            }
        
        tokens = result.get('data', [])
        
        return {
            'success': True,
            'tokens': tokens,
            'total_found': len(tokens),
            'criteria': {
                'chain': chain,
                'stage': stage,
                'min_volume': min_volume,
                'min_market_cap': min_market_cap,
                'min_holders': min_holders,
                'min_token_age': min_token_age,
                'has_social_links': has_social_links
            }
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'tokens': []
        }

def analyze_token_risk(token: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze token risk based on various factors.
    
    Args:
        token: Token data from API
    
    Returns:
        Dictionary containing risk analysis
    """
    try:
        market = token.get('market', {})
        tags = token.get('tags', {})
        
        market_cap = float(market.get('marketCapUsd', 0))
        volume_1h = float(market.get('volumeUsd1h', 0))
        holders = int(tags.get('totalHolders', 0))
        dev_holdings_percent = float(tags.get('devHoldingsPercent', 0))
        top10_holdings_percent = float(tags.get('top10HoldingsPercent', 0))
        bundlers_percent = float(tags.get('bundlersPercent', 0))
        snipers_percent = float(tags.get('snipersPercent', 0))
        
        risk_score = 0
        risk_factors = []
        
        if market_cap < 10000:
            risk_score += 3
            risk_factors.append('Very low market cap (<$10K)')
        elif market_cap < 100000:
            risk_score += 2
            risk_factors.append('Low market cap (<$100K)')
        elif market_cap < 1000000:
            risk_score += 1
            risk_factors.append('Medium market cap (<$1M)')
        
        if dev_holdings_percent > 50:
            risk_score += 3
            risk_factors.append(f'High dev holdings ({dev_holdings_percent}%)')
        elif dev_holdings_percent > 20:
            risk_score += 2
            risk_factors.append(f'Moderate dev holdings ({dev_holdings_percent}%)')
        elif dev_holdings_percent > 10:
            risk_score += 1
            risk_factors.append(f'Some dev holdings ({dev_holdings_percent}%)')
        
        if top10_holdings_percent > 80:
            risk_score += 2
            risk_factors.append(f'High concentration ({top10_holdings_percent}% in top 10)')
        elif top10_holdings_percent > 60:
            risk_score += 1
            risk_factors.append(f'Moderate concentration ({top10_holdings_percent}% in top 10)')
        
        if bundlers_percent > 10:
            risk_score += 2
            risk_factors.append(f'High bundler activity ({bundlers_percent}%)')
        elif bundlers_percent > 5:
            risk_score += 1
            risk_factors.append(f'Some bundler activity ({bundlers_percent}%)')
        
        if snipers_percent > 10:
            risk_score += 2
            risk_factors.append(f'High sniper activity ({snipers_percent}%)')
        elif snipers_percent > 5:
            risk_score += 1
            risk_factors.append(f'Some sniper activity ({snipers_percent}%)')
        
        if holders < 50:
            risk_score += 2
            risk_factors.append(f'Low holder count ({holders})')
        elif holders < 100:
            risk_score += 1
            risk_factors.append(f'Moderate holder count ({holders})')
        
        risk_level = 'Low'
        if risk_score >= 8:
            risk_level = 'Very High'
        elif risk_score >= 6:
            risk_level = 'High'
        elif risk_score >= 4:
            risk_level = 'Medium'
        
        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'risk_factors': risk_factors,
            'recommendation': _get_risk_recommendation(risk_score, volume_1h, market_cap)
        }
        
    except Exception as e:
        return {
            'error': str(e),
            'risk_score': 0,
            'risk_level': 'Unknown',
            'risk_factors': [],
            'recommendation': 'Unable to analyze'
        }

def _get_risk_recommendation(risk_score: int, volume_24h: float, market_cap: float) -> str:
    """Get investment recommendation based on risk score."""
    if risk_score >= 8:
        return 'Extremely High Risk - Not Recommended'
    elif risk_score >= 6:
        return 'High Risk - Not Recommended'
    elif risk_score >= 4:
        if volume_24h > market_cap:
            return 'Medium Risk / High Volume - Monitor Closely'
        else:
            return 'Medium Risk - Monitor'
    elif risk_score >= 2:
        return 'Low Risk / Medium Potential - Consider Small Position'
    else:
        return 'Low Risk - Monitor'

def get_supported_chains_and_protocols() -> Dict[str, Any]:
    """
    Get supported chains and protocols for meme pump scanning.
    
    Returns:
        Dictionary containing supported chains and protocols
    """
    try:
        request_path = "/api/v6/dex/market/memepump/supported/chainsProtocol"
        
        result = client.send_request(request_path, "GET", proxy_host=None)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'chains': []
            }
        
        chains = result.get('data', [])
        
        return {
            'success': True,
            'chains': chains,
            'total_chains': len(chains)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'chains': []
        }

def get_token_details(
    chain: str = 'sol',
    token_address: str = None,
    wallet_address: str = None
) -> Dict[str, Any]:
    """
    Get detailed information for a specific token.
    
    Args:
        chain: Blockchain ('sol', 'bsc')
        token_address: Token contract address
        wallet_address: User wallet address (optional)
    
    Returns:
        Dictionary containing token details
    """
    try:
        chain_ids = {
            'sol': '501',
            'bsc': '56'
        }
        
        chain_id = chain_ids.get(chain, '501')
        
        request_path = "/api/v6/dex/market/memepump/tokenDetails"
        params = {
            "chainIndex": chain_id,
            "tokenContractAddress": token_address
        }
        
        if wallet_address:
            params["walletAddress"] = wallet_address
        
        result = client.send_request(request_path, "GET", proxy_host=None, **params)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'token': None
            }
        
        token_data = result.get('data', {})
        
        return {
            'success': True,
            'token': token_data
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'token': None
        }

def get_similar_tokens(
    chain: str = 'sol',
    token_address: str = None
) -> Dict[str, Any]:
    """
    Get similar tokens for a specific token.
    
    Args:
        chain: Blockchain ('sol', 'bsc')
        token_address: Token contract address
    
    Returns:
        Dictionary containing similar tokens
    """
    try:
        chain_ids = {
            'sol': '501',
            'bsc': '56'
        }
        
        chain_id = chain_ids.get(chain, '501')
        
        request_path = "/api/v6/dex/market/memepump/similarToken"
        params = {
            "chainIndex": chain_id,
            "tokenContractAddress": token_address
        }
        
        result = client.send_request(request_path, "GET", proxy_host=None, **params)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'similar_tokens': []
            }
        
        data = result.get('data', {})
        similar_tokens = data if isinstance(data, list) else data.get('similarToken', [])
        
        return {
            'success': True,
            'similar_tokens': similar_tokens,
            'total_found': len(similar_tokens)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'similar_tokens': []
        }

def get_token_aped_wallets(
    chain: str = 'sol',
    token_address: str = None,
    wallet_address: str = None
) -> Dict[str, Any]:
    """
    Get aped wallets for a specific token (up to 50 wallets).
    
    Args:
        chain: Blockchain ('sol', 'bsc')
        token_address: Token contract address
        wallet_address: Wallet address (optional)
    
    Returns:
        Dictionary containing aped wallets
    """
    try:
        chain_ids = {
            'sol': '501',
            'bsc': '56'
        }
        
        chain_id = chain_ids.get(chain, '501')
        
        request_path = "/api/v6/dex/market/memepump/apedWallet"
        params = {
            "chainIndex": chain_id,
            "tokenContractAddress": token_address
        }
        
        if wallet_address:
            params["walletAddress"] = wallet_address
        
        result = client.send_request(request_path, "GET", proxy_host=None, **params)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'aped_wallets': []
            }
        
        data = result.get('data', {})
        aped_wallets = data if isinstance(data, list) else data.get('apedWalletList', [])
        
        return {
            'success': True,
            'aped_wallets': aped_wallets,
            'total_found': len(aped_wallets)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'aped_wallets': []
        }

def get_signal_supported_chains() -> Dict[str, Any]:
    """
    Get supported chains for signal tracking.
    
    Returns:
        Dictionary containing supported chains
    """
    try:
        request_path = "/api/v6/dex/market/signal/supported/chains"
        
        result = client.send_request(request_path, "GET", proxy_host=None)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'chains': []
            }
        
        chains = result.get('data', [])
        
        return {
            'success': True,
            'chains': chains,
            'total_chains': len(chains)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'chains': []
        }

def get_signal_list(
    chain: str = 'sol',
    wallet_type: Optional[str] = None,
    min_amount_usd: Optional[float] = None,
    max_amount_usd: Optional[float] = None,
    min_address_count: Optional[int] = None,
    max_address_count: Optional[int] = None,
    token_address: Optional[str] = None,
    min_market_cap_usd: Optional[float] = None,
    max_market_cap_usd: Optional[float] = None,
    min_liquidity_usd: Optional[float] = None,
    max_liquidity_usd: Optional[float] = None
) -> Dict[str, Any]:
    """
    Get recent signal list for specified chain.
    
    Args:
        chain: Blockchain ('sol', 'eth', etc.)
        wallet_type: Wallet type (1=Smart Money, 2=KOL/Influencer, 3=Whales)
        min_amount_usd: Minimum transaction amount in USD
        max_amount_usd: Maximum transaction amount in USD
        min_address_count: Minimum number of addresses
        max_address_count: Maximum number of addresses
        token_address: Token contract address
        min_market_cap_usd: Minimum market cap in USD
        max_market_cap_usd: Maximum market cap in USD
        min_liquidity_usd: Minimum liquidity in USD
        max_liquidity_usd: Maximum liquidity in USD
    
    Returns:
        Dictionary containing signal list
    """
    try:
        chain_ids = {
            'sol': 501,
            'bsc': 56,
            'eth': 1,
            'tron': 195,
            'xlayer': 196
        }
        
        chain_index = chain_ids.get(chain, 501)
        
        request_path = "/api/v6/dex/market/signal/list"
        
        params = {
            "chainIndex": str(chain_index)
        }
        
        if wallet_type:
            params["walletType"] = wallet_type
        
        if min_amount_usd:
            params["minAmountUsd"] = str(min_amount_usd)
        
        if max_amount_usd:
            params["maxAmountUsd"] = str(max_amount_usd)
        
        if min_address_count:
            params["minAddressCount"] = str(min_address_count)
        
        if max_address_count:
            params["maxAddressCount"] = str(max_address_count)
        
        if token_address:
            params["tokenAddress"] = token_address
        
        if min_market_cap_usd:
            params["minMarketCapUsd"] = str(min_market_cap_usd)
        
        if max_market_cap_usd:
            params["maxMarketCapUsd"] = str(max_market_cap_usd)
        
        if min_liquidity_usd:
            params["minLiquidityUsd"] = str(min_liquidity_usd)
        
        if max_liquidity_usd:
            params["maxLiquidityUsd"] = str(max_liquidity_usd)
        
        result = client.send_request(request_path, "POST", proxy_host=None, **params)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'signals': []
            }
        
        signals = result.get('data', [])
        
        return {
            'success': True,
            'signals': signals,
            'total_found': len(signals)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'signals': []
        }

def get_token_bundle_info(
    chain: str = 'sol',
    token_address: str = None
) -> Dict[str, Any]:
    """
    Get token bundle information.
    
    Args:
        chain: Blockchain ('sol', 'bsc')
        token_address: Token contract address
    
    Returns:
        Dictionary containing token bundle information
    """
    try:
        chain_ids = {
            'sol': '501',
            'bsc': '56'
        }
        
        chain_id = chain_ids.get(chain, '501')
        
        request_path = "/api/v6/dex/market/memepump/tokenBundleInfo"
        params = {
            "chainIndex": chain_id,
            "tokenContractAddress": token_address
        }
        
        result = client.send_request(request_path, "GET", proxy_host=None, **params)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'bundle_info': None
            }
        
        bundle_info = result.get('data', {})
        
        return {
            'success': True,
            'bundle_info': bundle_info
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'bundle_info': None
        }

def get_token_dev_info(
    chain: str = 'sol',
    token_address: str = None
) -> Dict[str, Any]:
    """
    Get token developer information.
    
    Args:
        chain: Blockchain ('sol', 'bsc')
        token_address: Token contract address
    
    Returns:
        Dictionary containing token developer information
    """
    try:
        chain_ids = {
            'sol': '501',
            'bsc': '56'
        }
        
        chain_id = chain_ids.get(chain, '501')
        
        request_path = "/api/v6/dex/market/memepump/tokenDevInfo"
        params = {
            "chainIndex": chain_id,
            "tokenContractAddress": token_address
        }
        
        result = client.send_request(request_path, "GET", proxy_host=None, **params)
        
        if str(result.get('code', '')) != '0':
            return {
                'success': False,
                'error': result.get('msg', 'Unknown error'),
                'error_code': result.get('code'),
                'dev_info': None
            }
        
        dev_info = result.get('data', {})
        
        return {
            'success': True,
            'dev_info': dev_info
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'dev_info': None
        }

def main():
    lang = os.getenv('LANG', 'en_us')
    
    print(f'=== {t("app_name")} - Meme Token Scanner ===')
    print()
    
    if not all([OKX_API_KEY, OKX_API_SECRET, OKX_API_PASSPHRASE]):
        print('Error: OKX API credentials not configured.')
        print('Please set the following environment variables:')
        print('  OKX_API_KEY')
        print('  OKX_API_SECRET')
        print('  OKX_API_PASSPHRASE')
        print()
        return
    
    chain = 'sol'
    stage = 'NEW'
    min_volume = None
    min_market_cap = None
    min_holders = None
    min_token_age = None
    has_social_links = False
    limit = 50
    analyze_risk = True
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--chain' and i + 1 < len(sys.argv):
            chain = sys.argv[i + 1].lower()
            i += 1
        elif arg == '--stage' and i + 1 < len(sys.argv):
            stage = sys.argv[i + 1].upper()
            i += 1
        elif arg == '--min-volume' and i + 1 < len(sys.argv):
            try:
                min_volume = float(sys.argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif arg == '--min-mcap' and i + 1 < len(sys.argv):
            try:
                min_market_cap = float(sys.argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif arg == '--min-holders' and i + 1 < len(sys.argv):
            try:
                min_holders = int(sys.argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif arg == '--min-age' and i + 1 < len(sys.argv):
            try:
                min_token_age = int(sys.argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif arg == '--social':
            has_social_links = True
        elif arg == '--limit' and i + 1 < len(sys.argv):
            try:
                limit = int(sys.argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif arg == '--no-risk':
            analyze_risk = False
        
        i += 1
    
    print('Scan Criteria:')
    print(f'  Chain: {chain.upper()}')
    print(f'  Stage: {stage}')
    if min_volume:
        print(f'  Minimum 1h volume: ${min_volume:,.2f}')
    else:
        print(f'  Minimum 1h volume: No limit')
    if min_market_cap:
        print(f'  Minimum market cap: ${min_market_cap:,.2f}')
    else:
        print(f'  Minimum market cap: No limit')
    if min_holders:
        print(f'  Minimum holders: {min_holders}')
    else:
        print(f'  Minimum holders: No limit')
    if min_token_age:
        print(f'  Minimum token age: {min_token_age} minutes')
    else:
        print(f'  Minimum token age: No limit')
    print(f'  Has social links: {has_social_links}')
    print(f'  Limit: {limit} tokens')
    print(f'  Analyze risk: {analyze_risk}')
    print()
    
    print('Scanning for meme tokens...')
    print()
    
    result = scan_meme_tokens(
        chain=chain,
        stage=stage,
        min_volume=min_volume,
        min_market_cap=min_market_cap,
        min_holders=min_holders,
        min_token_age=min_token_age,
        has_social_links=has_social_links,
        limit=limit
    )
    
    if not result['success']:
        print(f'Error: {result.get("error", "Unknown error")}')
        return
    
    tokens = result['tokens']
    print(f'Found {result["total_found"]} tokens matching criteria')
    print(f'Processing {len(tokens)} tokens...')
    print()
    
    if not tokens:
        print('No tokens found matching criteria.')
        return
    
    print('=' * 140)
    print(f"{'Symbol':<12} {'Name':<25} {'Price':<12} {'Volume 1h':<15} {'Market Cap':<15} {'Holders':<10} {'Risk':<12}")
    print('=' * 140)
    
    for token in tokens:
        symbol = token.get('symbol', 'N/A')
        name = token.get('name', 'N/A')
        market = token.get('market', {})
        tags = token.get('tags', {})
        
        price = 0.0
        volume = float(market.get('volumeUsd1h', 0) or 0)
        market_cap = float(market.get('marketCapUsd', 0) or 0)
        holders = int(tags.get('totalHolders', 0) or 0)
        
        print(f"{symbol:<12} {name[:25]:<25} ${price:<11.6f} ${volume:>13,.0f} ${market_cap:>13,.0f} {holders:>10}", end='')
        
        if analyze_risk:
            risk_analysis = analyze_token_risk(token)
            print(f" {risk_analysis['risk_level']:<12}")
            if risk_analysis['risk_factors']:
                print(f"       Factors: {', '.join(risk_analysis['risk_factors'][:2])}")
            print(f"       Recommendation: {risk_analysis['recommendation']}")
        else:
            print()
        
        print('-' * 140)
    
    print()
    print(f'Scan completed. Found {len(tokens)} tokens.')
    print('Use --json flag to see detailed information.')
    
    if '--json' in sys.argv:
        print()
        print('Detailed Information:')
        print(json.dumps(tokens, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
