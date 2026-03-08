import os
import sys
from pathlib import Path

script_dir = Path(__file__).parent
web3_dir = script_dir.parent
sys.path.insert(0, str(web3_dir))

from assets.i18n import t, get_chain_name, SUPPORTED_LANGS

def main():
    lang = os.getenv('LANG', 'en_us')
    
    print(f'=== {t("app_name")} ===')
    print()
    print(f'{t("token_query.title")}: Query token information')
    print(f'{t("wallet_balance.title")}: Query wallet balance')
    print(f'{t("market_data.title")}: Fetch stock/crypto market data')
    print(f'{t("rsi.title")}: Calculate RSI technical indicator')
    print(f'{t("macd.title")}: Calculate MACD technical indicator')
    print('K-line: Analyze candlestick patterns and K-line data')
    print('Chain Scanner: Scan for meme tokens on blockchain')
    print('CoinMarketCap: Get cryptocurrency market data')
    print('Token Details: Get detailed token information')
    print('Similar Tokens: Get similar tokens for a specific token')
    print('Aped Wallets: Get aped wallets for a specific token')
    print('Token Bundle Info: Get token bundle transaction data')
    print('Token Dev Info: Get token developer information')
    print('Signal Chains: Get supported chains for signal tracking')
    print('Signal List: Get recent signal list')
    print()
    
    if len(sys.argv) < 2:
        print('Usage:')
        print('  python web3.py token-query <chain> <contract_address>')
        print('  python web3.py wallet-balance <wallet_address>')
        print('  python web3.py market-data <symbol> [options]')
        print('  python web3.py rsi <symbol> [options]')
        print('  python web3.py macd <symbol> [options]')
        print('  python web3.py kline <symbol> [options]')
        print('  python web3.py chain-scanner [options]')
        print('  python web3.py coinmarketcap <command> [options]')
        print('  python web3.py supported-chains')
        print('  python web3.py token-details <chain> <token_address> [wallet_address]')
        print('  python web3.py similar-tokens <chain> <token_address>')
        print('  python web3.py aped-wallets <chain> <token_address> [wallet_address]')
        print('  python web3.py token-bundle-info <chain> <token_address>')
        print('  python web3.py token-dev-info <chain> <token_address>')
        print('  python web3.py signal-chains')
        print('  python web3.py signal-list <chain> [options]')
        print()
        print('Examples:')
        print('  python web3.py token-query ethereum 0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683')
        print('  python web3.py wallet-balance 0x53A0Fc074E31068CFdBD73B756458546274fEa97')
        print('  python web3.py market-data AAPL')
        print('  python web3.py market-data BTC-USD --period 1mo')
        print('  python web3.py rsi AAPL')
        print('  python web3.py macd AAPL --combined')
        print('  python web3.py coinmarketcap listings --limit 10')
        print('  python web3.py coinmarketcap info BTC')
        print('  python web3.py coinmarketcap global')
        print('  python web3.py coinmarketcap fear-greed')
        print('  python web3.py coinmarketcap cmc20')
        print('  python web3.py coinmarketcap cmc100')
        print('  python web3.py kline AAPL')
        print('  python web3.py kline BTC-USD --interval 1h --period 1mo')
        print('  python web3.py kline ETH-USD --patterns --lookback 30')
        print('  python web3.py chain-scanner --chain sol --stage NEW --min-volume 10000')
        print('  python web3.py chain-scanner --social --limit 20')
        print('  python web3.py supported-chains')
        print('  python web3.py token-details sol 7Gf9...pump')
        print('  python web3.py similar-tokens sol 7Gf9...pump')
        print('  python web3.py aped-wallets sol 7Gf9...pump')
        print('  python web3.py token-bundle-info sol 7Gf9...pump')
        print('  python web3.py token-dev-info sol 7Gf9...pump')
        print('  python web3.py signal-chains')
        print('  python web3.py signal-list sol --wallet-type 1 --min-amount 1000')
        print()
        print('Supported languages:', ', '.join(SUPPORTED_LANGS))
        print('Set language: export LANG=zh_cn')
        print()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'token-query':
        from assets.token_query import token_query
        
        if len(sys.argv) < 4:
            print(t('token_query.usage'))
            print(t('token_query.supported_chains'))
            return
        
        chain = sys.argv[2]
        contract = sys.argv[3]
        
        result = token_query(chain, contract)
        print(t('token_query.result'))
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'wallet-balance':
        from assets.wallet_balance import wallet_balance
        
        if len(sys.argv) < 3:
            print(t('wallet_balance.usage'))
            return
        
        wallet = sys.argv[2]
        
        result = wallet_balance(wallet, show_zero=False)
        print(t('wallet_balance.result'))
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'market-data':
        from assets.market_data import main as market_data_main
        sys.argv = ['market_data.py'] + sys.argv[2:]
        market_data_main()
    
    elif command == 'rsi':
        from assets.rsi import main as rsi_main
        sys.argv = ['rsi.py'] + sys.argv[2:]
        rsi_main()
    
    elif command == 'macd':
        from assets.macd import main as macd_main
        sys.argv = ['macd.py'] + sys.argv[2:]
        macd_main()
    
    elif command == 'coinmarketcap':
        from assets.coinmarketcap import main as coinmarketcap_main
        sys.argv = ['coinmarketcap.py'] + sys.argv[2:]
        coinmarketcap_main()
    
    elif command == 'kline':
        from assets.kline import main as kline_main
        sys.argv = ['kline.py'] + sys.argv[2:]
        kline_main()
    
    elif command == 'chain-scanner':
        from assets.chain_scanner import main as chain_scanner_main
        sys.argv = ['chain_scanner.py'] + sys.argv[2:]
        chain_scanner_main()
    
    elif command == 'supported-chains':
        from assets.chain_scanner import get_supported_chains_and_protocols
        
        result = get_supported_chains_and_protocols()
        print('Supported Chains and Protocols:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'token-details':
        from assets.chain_scanner import get_token_details
        
        if len(sys.argv) < 4:
            print('Usage: python web3.py token-details <chain> <token_address> [wallet_address]')
            print('Example: python web3.py token-details sol 7Gf9...pump')
            return
        
        chain = sys.argv[2]
        token_address = sys.argv[3]
        wallet_address = sys.argv[4] if len(sys.argv) > 4 else None
        
        result = get_token_details(chain, token_address, wallet_address)
        print('Token Details:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'similar-tokens':
        from assets.chain_scanner import get_similar_tokens
        
        if len(sys.argv) < 4:
            print('Usage: python web3.py similar-tokens <chain> <token_address>')
            print('Example: python web3.py similar-tokens sol 7Gf9...pump')
            return
        
        chain = sys.argv[2]
        token_address = sys.argv[3]
        
        result = get_similar_tokens(chain, token_address)
        print('Similar Tokens:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'aped-wallets':
        from assets.chain_scanner import get_token_aped_wallets
        
        if len(sys.argv) < 4:
            print('Usage: python web3.py aped-wallets <chain> <token_address> [wallet_address]')
            print('Example: python web3.py aped-wallets sol 7Gf9...pump')
            return
        
        chain = sys.argv[2]
        token_address = sys.argv[3]
        wallet_address = sys.argv[4] if len(sys.argv) > 4 else None
        
        result = get_token_aped_wallets(chain, token_address, wallet_address)
        print('Aped Wallets:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'token-bundle-info':
        from assets.chain_scanner import get_token_bundle_info
        
        if len(sys.argv) < 4:
            print('Usage: python web3.py token-bundle-info <chain> <token_address>')
            print('Example: python web3.py token-bundle-info sol 7Gf9...pump')
            return
        
        chain = sys.argv[2]
        token_address = sys.argv[3]
        
        result = get_token_bundle_info(chain, token_address)
        print('Token Bundle Info:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'token-dev-info':
        from assets.chain_scanner import get_token_dev_info
        
        if len(sys.argv) < 4:
            print('Usage: python web3.py token-dev-info <chain> <token_address>')
            print('Example: python web3.py token-dev-info sol 7Gf9...pump')
            return
        
        chain = sys.argv[2]
        token_address = sys.argv[3]
        
        result = get_token_dev_info(chain, token_address)
        print('Token Developer Info:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'signal-chains':
        from assets.chain_scanner import get_signal_supported_chains
        
        result = get_signal_supported_chains()
        print('Signal Supported Chains:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif command == 'signal-list':
        from assets.chain_scanner import get_signal_list
        
        if len(sys.argv) < 3:
            print('Usage: python web3.py signal-list <chain> [options]')
            print('Options:')
            print('  --wallet-type <type>    Wallet type (1=Smart Money, 2=KOL/Influencer, 3=Whales)')
            print('  --min-amount <usd>       Minimum transaction amount in USD')
            print('  --max-amount <usd>       Maximum transaction amount in USD')
            print('  --min-address-count <n>  Minimum number of addresses')
            print('  --max-address-count <n>  Maximum number of addresses')
            print('  --token-address <addr>   Token contract address')
            print('  --min-market-cap <usd>   Minimum market cap in USD')
            print('  --max-market-cap <usd>   Maximum market cap in USD')
            print('  --min-liquidity <usd>    Minimum liquidity in USD')
            print('  --max-liquidity <usd>    Maximum liquidity in USD')
            print('Example: python web3.py signal-list sol --wallet-type 1 --min-amount 1000')
            return
        
        chain = sys.argv[2]
        
        wallet_type = None
        min_amount_usd = None
        max_amount_usd = None
        min_address_count = None
        max_address_count = None
        token_address = None
        min_market_cap_usd = None
        max_market_cap_usd = None
        min_liquidity_usd = None
        max_liquidity_usd = None
        
        args = sys.argv[3:]
        i = 0
        while i < len(args):
            if args[i] == '--wallet-type' and i + 1 < len(args):
                wallet_type = args[i + 1]
                i += 2
            elif args[i] == '--min-amount' and i + 1 < len(args):
                min_amount_usd = float(args[i + 1])
                i += 2
            elif args[i] == '--max-amount' and i + 1 < len(args):
                max_amount_usd = float(args[i + 1])
                i += 2
            elif args[i] == '--min-address-count' and i + 1 < len(args):
                min_address_count = int(args[i + 1])
                i += 2
            elif args[i] == '--max-address-count' and i + 1 < len(args):
                max_address_count = int(args[i + 1])
                i += 2
            elif args[i] == '--token-address' and i + 1 < len(args):
                token_address = args[i + 1]
                i += 2
            elif args[i] == '--min-market-cap' and i + 1 < len(args):
                min_market_cap_usd = float(args[i + 1])
                i += 2
            elif args[i] == '--max-market-cap' and i + 1 < len(args):
                max_market_cap_usd = float(args[i + 1])
                i += 2
            elif args[i] == '--min-liquidity' and i + 1 < len(args):
                min_liquidity_usd = float(args[i + 1])
                i += 2
            elif args[i] == '--max-liquidity' and i + 1 < len(args):
                max_liquidity_usd = float(args[i + 1])
                i += 2
            else:
                i += 1
        
        result = get_signal_list(
            chain=chain,
            wallet_type=wallet_type,
            min_amount_usd=min_amount_usd,
            max_amount_usd=max_amount_usd,
            min_address_count=min_address_count,
            max_address_count=max_address_count,
            token_address=token_address,
            min_market_cap_usd=min_market_cap_usd,
            max_market_cap_usd=max_market_cap_usd,
            min_liquidity_usd=min_liquidity_usd,
            max_liquidity_usd=max_liquidity_usd
        )
        print('Signal List:')
        print()
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    else:
        print(f'Unknown command: {command}')
        print()
        print('Available commands:')
        print('  token-query       - Query token information')
        print('  wallet-balance    - Query wallet balance')
        print('  market-data      - Fetch stock/crypto market data')
        print('  rsi              - Calculate RSI technical indicator')
        print('  macd             - Calculate MACD technical indicator')
        print('  kline            - Analyze K-line candlestick patterns')
        print('  chain-scanner    - Scan for meme tokens on blockchain')
        print('  coinmarketcap     - Get cryptocurrency market data')
        print('  supported-chains  - Get supported chains and protocols')
        print('  token-details     - Get detailed token information')
        print('  similar-tokens   - Get similar tokens for a specific token')
        print('  aped-wallets     - Get aped wallets for a specific token')
        print('  token-bundle-info - Get token bundle transaction data')
        print('  token-dev-info    - Get token developer information')
        print('  signal-chains    - Get supported chains for signal tracking')
        print('  signal-list      - Get recent signal list')

if __name__ == '__main__':
    main()
