import json
import os
import sys
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))
from assets.i18n import t, get_chain_name

load_dotenv()

EVM_CHAINS = {
    'ethereum': {
        'chain_id': '1',
        'rpc_url': 'https://eth-mainnet.public.blastapi.io',
        'explorer': 'https://api.etherscan.io/api',
        'native_token': 'ETH'
    },
    'bsc': {
        'chain_id': '56',
        'rpc_url': 'https://bsc-dataseed.binance.org',
        'explorer': 'https://api.bscscan.com/api',
        'native_token': 'BNB'
    },
    'polygon': {
        'chain_id': '137',
        'rpc_url': 'https://polygon-rpc.com',
        'explorer': 'https://api.polygonscan.com/api',
        'native_token': 'POL'
    },
    'arbitrum': {
        'chain_id': '42161',
        'rpc_url': 'https://arb1.arbitrum.io/rpc',
        'explorer': 'https://api.arbiscan.io/api',
        'native_token': 'ETH'
    },
    'optimism': {
        'chain_id': '10',
        'rpc_url': 'https://mainnet.optimism.io',
        'explorer': 'https://api-optimistic.etherscan.io/api',
        'native_token': 'ETH'
    },
    'avalanche': {
        'chain_id': '43114',
        'rpc_url': 'https://api.avax.network/ext/bc/C/rpc',
        'explorer': 'https://api.snowtrace.io/api',
        'native_token': 'AVAX'
    },
    'base': {
        'chain_id': '8453',
        'rpc_url': 'https://mainnet.base.org',
        'explorer': 'https://api.basescan.org/api',
        'native_token': 'ETH'
    },
    'linea': {
        'chain_id': '59144',
        'rpc_url': 'https://rpc.linea.build',
        'explorer': 'https://api.lineascan.build/api',
        'native_token': 'ETH'
    },
    'fantom': {
        'chain_id': '250',
        'rpc_url': 'https://rpc.ftm.tools',
        'explorer': 'https://api.ftmscan.com/api',
        'native_token': 'FTM'
    },
    'cronos': {
        'chain_id': '25',
        'rpc_url': 'https://evm.cronos.org',
        'explorer': 'https://api.cronoscan.com/api',
        'native_token': 'CRO'
    }
}

NON_EVM_CHAINS = {
    'bitcoin': {
        'chain_id': 'btc',
        'api_url': 'https://blockstream.info/api',
        'native_token': 'BTC'
    },
    'solana': {
        'chain_id': 'sol',
        'rpc_url': 'https://api.mainnet-beta.solana.com',
        'native_token': 'SOL'
    }
}

ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY', '')

def get_native_balance(chain_name, wallet_address):
    """Query native token balance (via RPC)"""
    try:
        chain = EVM_CHAINS[chain_name]
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [wallet_address, "latest"],
            "id": 1
        }
        
        response = requests.post(chain['rpc_url'], json=payload, timeout=10)
        result = response.json()
        
        if 'result' in result:
            balance_wei = int(result['result'], 16)
            balance_eth = balance_wei / 1e18
            
            return {
                "balance": str(balance_eth),
                "balance_raw": str(balance_wei),
                "decimals": "18",
                "unit": chain['native_token']
            }
        else:
            return {"error": t('wallet_balance.error_get_balance')}
    except Exception as e:
        return {"error": str(e)}

def get_btc_balance(wallet_address):
    """Query Bitcoin balance (via Blockstream API)"""
    try:
        chain = NON_EVM_CHAINS['bitcoin']
        
        addr_url = f"{chain['api_url']}/address/{wallet_address}"
        addr_response = requests.get(addr_url, timeout=10)
        
        if addr_response.status_code == 400:
            return {"error": t('wallet_balance.error_invalid_btc_address')}
        elif addr_response.status_code != 200:
            return {"error": f"{t('wallet_balance.error_query_address')} {addr_response.status_code}"}
        
        utxo_url = f"{chain['api_url']}/address/{wallet_address}/utxo"
        response = requests.get(utxo_url, timeout=10)
        
        if response.status_code == 200:
            utxos = response.json()
            if not utxos:
                return {
                    "balance": "0",
                    "balance_raw": "0",
                    "decimals": "8",
                    "unit": "BTC"
                }
            
            total_satoshis = sum(utxo['value'] for utxo in utxos)
            total_btc = total_satoshis / 1e8
            
            return {
                "balance": str(total_btc),
                "balance_raw": str(total_satoshis),
                "decimals": "8",
                "unit": "BTC"
            }
        else:
            return {"error": f"{t('wallet_balance.error_query_utxo')} {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def get_sol_balance(wallet_address):
    """Query SOL balance (via Solana RPC)"""
    try:
        chain = NON_EVM_CHAINS['solana']
        
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [wallet_address]
        }
        
        response = requests.post(chain['rpc_url'], json=payload, timeout=10)
        result = response.json()
        
        if 'result' in result:
            balance_lamports = result['result']['value']
            balance_sol = balance_lamports / 1e9
            
            return {
                "balance": str(balance_sol),
                "balance_raw": str(balance_lamports),
                "decimals": "9",
                "unit": "SOL"
            }
        else:
            return {"error": t('wallet_balance.error_get_balance')}
    except Exception as e:
        return {"error": str(e)}

def get_token_balance(chain_name, wallet_address, token_address):
    """Query ERC20 token balance"""
    try:
        chain = EVM_CHAINS[chain_name]
        
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [{
                "to": token_address,
                "data": "0x70a08231" + wallet_address[2:].zfill(64)
            }, "latest"],
            "id": 1
        }
        
        response = requests.post(chain['rpc_url'], json=payload, timeout=10)
        result = response.json()
        
        if 'result' in result:
            balance_raw = int(result['result'], 16)
            return str(balance_raw)
        else:
            return "0"
    except Exception as e:
        return "0"

def query_wallet_balance(chain_name, wallet_address):
    """Query wallet balance for a single chain"""
    if chain_name == 'bitcoin':
        try:
            balance_info = get_btc_balance(wallet_address)
            
            if "error" in balance_info:
                return {
                    "error": balance_info["error"],
                    "chain": chain_name,
                    "chain_id": NON_EVM_CHAINS['bitcoin']['chain_id']
                }
            
            price_usd = "0"
            value_usd = "0"
            try:
                price_response = requests.get(
                    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
                    timeout=5
                )
                price_data = price_response.json()
                if 'bitcoin' in price_data:
                    price_usd = str(price_data['bitcoin']['usd'])
                    value_usd = str(float(balance_info['balance']) * float(price_usd))
            except:
                pass
            
            return {
                "chain": chain_name,
                "chain_id": NON_EVM_CHAINS['bitcoin']['chain_id'],
                "wallet_address": wallet_address,
                "balance": balance_info['balance'],
                "balance_raw": balance_info.get('balance_raw', '0'),
                "decimals": balance_info.get('decimals', '8'),
                "unit": balance_info.get('unit', 'BTC'),
                "price_usd": price_usd,
                "value_usd": value_usd
            }
        except Exception as e:
            return {
                "error": f"{t('wallet_balance.error_api_failed')} {str(e)}",
                "chain": chain_name,
                "chain_id": NON_EVM_CHAINS['bitcoin']['chain_id']
            }
    
    elif chain_name == 'solana':
        try:
            balance_info = get_sol_balance(wallet_address)
            
            if "error" in balance_info:
                return {
                    "error": balance_info["error"],
                    "chain": chain_name,
                    "chain_id": NON_EVM_CHAINS['solana']['chain_id']
                }
            
            price_usd = "0"
            value_usd = "0"
            try:
                price_response = requests.get(
                    "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd",
                    timeout=5
                )
                price_data = price_response.json()
                if 'solana' in price_data:
                    price_usd = str(price_data['solana']['usd'])
                    value_usd = str(float(balance_info['balance']) * float(price_usd))
            except:
                pass
            
            return {
                "chain": chain_name,
                "chain_id": NON_EVM_CHAINS['solana']['chain_id'],
                "wallet_address": wallet_address,
                "balance": balance_info['balance'],
                "balance_raw": balance_info.get('balance_raw', '0'),
                "decimals": balance_info.get('decimals', '9'),
                "unit": balance_info.get('unit', 'SOL'),
                "price_usd": price_usd,
                "value_usd": value_usd
            }
        except Exception as e:
            return {
                "error": f"{t('wallet_balance.error_api_failed')} {str(e)}",
                "chain": chain_name,
                "chain_id": NON_EVM_CHAINS['solana']['chain_id']
            }
    
    else:
        if chain_name not in EVM_CHAINS:
            return {"error": f"{t('wallet_balance.error_unsupported_chain')} {chain_name}"}
        
        chain = EVM_CHAINS[chain_name]
        
        try:
            balance_info = get_native_balance(chain_name, wallet_address)
            
            if "error" in balance_info:
                return {
                    "error": balance_info["error"],
                    "chain": chain_name,
                    "chain_id": chain['chain_id']
                }
            
            price_usd = "0"
            value_usd = "0"
            
            try:
                price_map = {
                    'ETH': 'ethereum',
                    'BNB': 'binancecoin',
                    'POL': 'matic-network',
                    'AVAX': 'avalanche-2',
                    'FTM': 'fantom',
                    'CRO': 'crypto-com-chain'
                }
                
                coin_id = price_map.get(chain['native_token'])
                if coin_id:
                    price_response = requests.get(
                        f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd",
                        timeout=5
                    )
                    price_data = price_response.json()
                    if coin_id in price_data:
                        price_usd = str(price_data[coin_id]['usd'])
                        value_usd = str(float(balance_info['balance']) * float(price_usd))
            except:
                pass
            
            return {
                "chain": chain_name,
                "chain_id": chain['chain_id'],
                "wallet_address": wallet_address,
                "balance": balance_info['balance'],
                "balance_raw": balance_info.get('balance_raw', '0'),
                "decimals": balance_info.get('decimals', '18'),
                "unit": chain['native_token'],
                "price_usd": price_usd,
                "value_usd": value_usd
            }
        except Exception as e:
            return {
                "error": f"{t('wallet_balance.error_api_failed')} {str(e)}",
                "chain": chain_name,
                "chain_id": chain['chain_id']
            }

def detect_address_type(wallet_address):
    """Detect address type and return chains to query"""
    if wallet_address.startswith('1') or wallet_address.startswith('3') or wallet_address.startswith('bc1'):
        return ['bitcoin']
    
    if 32 <= len(wallet_address) <= 44 and all(c in '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' for c in wallet_address):
        return ['solana']
    
    if wallet_address.startswith('0x') and len(wallet_address) == 42:
        return list(EVM_CHAINS.keys())
    
    return list(EVM_CHAINS.keys()) + list(NON_EVM_CHAINS.keys())

def wallet_balance(wallet_address, chains=None, show_zero=False):
    """
    Query wallet balance across multiple chains
    Args:
        wallet_address: Wallet address
        chains: Optional list of chains to query, if None auto-detect
        show_zero: Whether to show chains with zero balance
    Returns:
        Dictionary containing balance information for all chains
    """
    balances = []
    total_value_usd = 0.0
    
    if chains:
        chains_to_query = chains
    else:
        chains_to_query = detect_address_type(wallet_address)
    
    for chain in chains_to_query:
        balance = query_wallet_balance(chain, wallet_address)
        
        if not show_zero and not balance.get('error'):
            try:
                if float(balance.get('balance', '0')) == 0:
                    continue
            except:
                pass
        
        balances.append(balance)
        
        if not balance.get('error') and balance.get('value_usd'):
            try:
                total_value_usd += float(balance['value_usd'])
            except:
                pass
    
    return {
        "wallet_address": wallet_address,
        "balances": balances,
        "total_value_usd": str(total_value_usd),
        "chain_count": len(balances),
        "timestamp": str(int(time.time() * 1000))
    }

def wallet_balance_with_tokens(wallet_address, chain, token_addresses=None):
    """
    Query wallet native and ERC20 token balances for a specific chain
    Args:
        wallet_address: Wallet address
        chain: Chain name
        token_addresses: List of ERC20 token contract addresses
    Returns:
        Dictionary containing all token balance information
    """
    if chain not in EVM_CHAINS:
        return {"error": f"{t('wallet_balance.error_unsupported_chain')} {chain}"}
    
    chain_info = EVM_CHAINS[chain]
    balances = []
    
    try:
        native_balance = get_native_balance(chain, wallet_address)
        if "error" not in native_balance:
            balances.append({
                "token_name": f"{chain} Native Token",
                "token_symbol": chain_info['native_token'],
                "token_address": "native",
                "balance": native_balance['balance'],
                "balance_raw": native_balance.get('balance_raw', '0'),
                "decimals": native_balance.get('decimals', '18')
            })
        
        if token_addresses:
            for token_addr in token_addresses:
                balance_raw = get_token_balance(chain, wallet_address, token_addr)
                balances.append({
                    "token_name": "Unknown Token",
                    "token_symbol": "UNKNOWN",
                    "token_address": token_addr,
                    "balance": balance_raw,
                    "balance_raw": balance_raw,
                    "decimals": "18"
                })
        
        return {
            "chain": chain,
            "chain_id": chain_info['chain_id'],
            "wallet_address": wallet_address,
            "balances": balances,
            "timestamp": str(int(time.time() * 1000))
        }
    except Exception as e:
        return {
            "error": f"{t('wallet_balance.error_api_failed')} {str(e)}",
            "chain": chain
        }

if __name__ == "__main__":
    lang = os.getenv('LANG', 'en_us')
    
    print(f'=== {t("app_name")} - {t("wallet_balance.title")} ===')
    print()
    
    if len(sys.argv) > 1:
        wallet = sys.argv[1]
    else:
        print(t('wallet_balance.usage'))
        print()
        print(t('wallet_balance.examples'))
        print(f'  {t("wallet_balance.evm_example")}')
        print(f'  {t("wallet_balance.btc_example")}')
        print(f'  {t("wallet_balance.sol_example")}')
        print()
        print(t('token_query.interactive_mode'))
        print()
        
        wallet = input(f'{t("wallet_balance.enter_wallet")} ').strip()
    
    if not wallet:
        print(t('wallet_balance.error_wallet_required'))
        sys.exit(1)
    
    print()
    print(f'{t("wallet_balance.querying_balance")} {wallet}')
    print()
    
    result = wallet_balance(wallet, show_zero=False)
    print(t('wallet_balance.result'))
    print(json.dumps(result, indent=2, ensure_ascii=False))
