# Web3 Tools

Web3 tools provide comprehensive blockchain data querying, financial market analysis, and complete OKX Web3 API support for meme token scanning across multiple blockchain networks.

## Quick Start

```bash
# Query token information
python scripts/web3.py token-query ethereum 0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683

# Query wallet balance
python scripts/web3.py wallet-balance 0x53A0Fc074E31068CFdBD73B756458546274fEa97

# Get market data
python scripts/web3.py market-data AAPL

# Calculate RSI indicator
python scripts/web3.py rsi BTC-USD

# Calculate MACD indicator
python scripts/web3.py macd ETH-USD

# Scan for meme tokens
python scripts/web3.py chain-scanner --chain sol --stage NEW --limit 10

# Get token details
python scripts/web3.py token-details sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get cryptocurrency data
python scripts/web3.py coinmarketcap listings --limit 10
```

## Supported Languages

- English (en_us) - Default
- Chinese (zh_cn)
- Japanese (jp)
- Traditional Chinese (zh_tw)

Set language:
```bash
export LANG=zh_cn
```

## Features

### Token Query
- Real-time price data
- Token name and symbol
- Market capitalization
- 24-hour trading volume
- Total and maximum supply
- Logo and official website
- Social media links

### Wallet Balance
- Multi-chain support (EVM, Bitcoin, Solana)
- Native token balances
- USD value calculation
- Automatic address type detection
- ERC20 token balance queries

### Market Data
- Stock and cryptocurrency data
- Multiple time periods and intervals
- OHLCV data
- Price change statistics
- 52-week high/low
- Historical data export

### Technical Indicators
- **RSI (Relative Strength Index)**: Overbought/oversold signals, divergence analysis
- **MACD (Moving Average Convergence Divergence)**: Trend analysis, crossover detection
- Trading recommendations
- Risk assessment

### CoinMarketCap Integration
- Top cryptocurrency listings
- Individual token information
- Global market metrics
- Real-time price data
- Market dominance tracking

### Meme Token Scanner (OKX Web3 API)
- **Supported Chains**: Solana, BSC, X Layer, TRON, Ethereum
- **Supported Protocols**: pumpfun, bonk, moonshot, raydium, pancakeswap, xswap, sunswap, uniswap
- Scan for meme tokens across multiple blockchains
- Get supported chains and protocols
- Query detailed token information
- Find similar tokens
- Track aped wallets (co-ride wallets)
- Get token bundle transaction data
- Get token developer information
- Track signal-supported chains
- Get recent signal lists
- Real-time risk analysis and recommendations
- Smart money signal tracking
- Developer reputation analysis

## Environment Variables

Required for token query:
```
OKX_API_KEY=your_api_key
OKX_API_SECRET=your_api_secret
OKX_API_PASSPHRASE=your_passphrase
```

Required for CoinMarketCap:
```
COINMARKETCAP_API_KEY=your_api_key
```

Optional:
```
ETHERSCAN_API_KEY=your_etherscan_api_key
```

## Directory Structure

```
web3/
├── SKILL.md           # AI skill documentation
├── README.md          # This file
├── scripts/           # Python scripts
│   ├── web3.py       # Main launcher
│   ├── token_query.py
│   ├── wallet_balance.py
│   ├── market_data.py
│   ├── rsi.py
│   ├── macd.py
│   └── coinmarketcap.py
├── assets/            # Asset modules
│   ├── i18n/         # Translation files
│   │   ├── en_us.json
│   │   ├── zh_cn.json
│   │   ├── jp.json
│   │   └── zh_tw.json
│   ├── data_fetcher.py
│   └── __pycache__/
└── references/         # User documentation
    └── README.md
```

## Documentation

For detailed documentation, see:
- [SKILL.md](SKILL.md) - AI skill documentation
- [references/README.md](references/README.md) - User documentation

## Available Commands

### Token Query
```bash
python scripts/web3.py token-query <chain> <contract_address>
```

### Wallet Balance
```bash
python scripts/web3.py wallet-balance <wallet_address>
```

### Market Data
```bash
python scripts/web3.py market-data <symbol> [options]
```

Options:
- `--period`: Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
- `--interval`: Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)

### RSI Indicator
```bash
python scripts/web3.py rsi <symbol> [options]
```

Options:
- `--period`: RSI calculation period (default: 14)
- `--time-period`: Time period for data (default: 1y)
- `--interval`: Data interval (default: 1d)

### MACD Indicator
```bash
python scripts/web3.py macd <symbol> [options]
```

Options:
- `--fast`: Fast EMA period (default: 12)
- `--slow`: Slow EMA period (default: 26)
- `--signal`: Signal line EMA period (default: 9)
- `--time-period`: Time period for data (default: 1y)
- `--interval`: Data interval (default: 1d)

### CoinMarketCap
```bash
python scripts/web3.py coinmarketcap <command> [options]
```

Commands:
- `listings`: Get cryptocurrency listings
- `info`: Get specific cryptocurrency information
- `global`: Get global market metrics (Pro plan required)
- `fear-greed`: Get Fear and Greed Index
- `cmc20`: Get CMC20 Index
- `cmc100`: Get CMC100 Index

Options:
- `--limit`: Number of results (default: 100)
- `--convert`: Currency for price conversion (default: USD)
- `--sort`: Sort field (market_cap, price, volume, etc.)

**Note:** The `global` command requires CoinMarketCap Pro plan or higher. Other features (listings, info, fear-greed, cmc20, cmc100) are available on the Basic plan.

### Meme Token Scanner

```bash
# Scan for meme tokens
python scripts/web3.py chain-scanner [options]

# Get supported chains and protocols
python scripts/web3.py supported-chains

# Get token details
python scripts/web3.py token-details <chain> <token_address> [wallet_address]

# Get similar tokens
python scripts/web3.py similar-tokens <chain> <token_address>

# Get aped wallets
python scripts/web3.py aped-wallets <chain> <token_address> [wallet_address]

# Get token bundle info
python scripts/web3.py token-bundle-info <chain> <token_address>

# Get token developer info
python scripts/web3.py token-dev-info <chain> <token_address>

# Get signal-supported chains
python scripts/web3.py signal-chains

# Get signal list
python scripts/web3.py signal-list <chain> [options]
```

**Options for chain-scanner:**
- `--chain`: Blockchain (sol, bsc, xlayer, tron, eth) - default: sol
- `--stage`: Token stage (NEW, MIGRATING, MIGRATED) - default: NEW
- `--min-volume`: Minimum 24h volume
- `--min-mcap`: Minimum market cap
- `--min-holders`: Minimum holders
- `--min-age`: Minimum token age (minutes)
- `--social`: Only tokens with social links
- `--limit`: Number of results - default: 10

**Options for signal-list:**
- `--chain`: Blockchain (sol, bsc, xlayer, tron, eth) - default: sol
- `--wallet-type`: Wallet type (1=Smart Money, 2=KOL/Influencer, 3=Whales)
- `--min-amount`: Minimum amount
- `--max-amount`: Maximum amount
- `--min-address-count`: Minimum address count
- `--max-address-count`: Maximum address count
- `--min-market-cap`: Minimum market cap
- `--max-market-cap`: Maximum market cap
- `--min-liquidity`: Minimum liquidity
- `--max-liquidity`: Maximum liquidity

## Examples

### Stock Analysis
```bash
# Get Apple stock data
python scripts/web3.py market-data AAPL

# Calculate RSI for Tesla
python scripts/web3.py rsi TSLA

# Calculate MACD for Microsoft
python scripts/web3.py macd MSFT
```

### Cryptocurrency Analysis
```bash
# Get Bitcoin data
python scripts/web3.py market-data BTC-USD

# Calculate RSI for Ethereum
python scripts/web3.py rsi ETH-USD

# Get top 10 cryptocurrencies
python scripts/web3.py coinmarketcap listings --limit 10

# Get Bitcoin info
python scripts/web3.py coinmarketcap info BTC
```

### Combined Analysis
```bash
# Get market data and RSI
python scripts/web3.py market-data AAPL --period 1mo
python scripts/web3.py rsi AAPL --period 1mo

# Get market data and MACD
python scripts/web3.py market-data BTC-USD --interval 1h
python scripts/web3.py macd BTC-USD --interval 1h
```

### Meme Token Analysis
```bash
# Scan for new meme tokens on Solana
python scripts/web3.py chain-scanner --chain sol --stage NEW --limit 10

# Scan for meme tokens with social links
python scripts/web3.py chain-scanner --chain sol --social --limit 20

# Get detailed token information
python scripts/web3.py token-details sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Find similar tokens
python scripts/web3.py similar-tokens sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Track aped wallets
python scripts/web3.py aped-wallets sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get bundle transaction data
python scripts/web3.py token-bundle-info sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get developer information
python scripts/web3.py token-dev-info sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Track smart money signals
python scripts/web3.py signal-list sol --wallet-type 1 --min-amount 1000

# Get supported chains
python scripts/web3.py supported-chains
```

## Dependencies

Install required packages:
```bash
pip install python-dotenv requests okx pandas numpy
```

## Troubleshooting

### Common Issues

**API Key Errors:**
- Verify API keys are set in `.env` file
- Check API key format and validity
- Ensure API key has required permissions

**Data Not Available:**
- Some stocks/crypto may not be available on Yahoo Finance
- Check symbol format (e.g., BTC-USD for Bitcoin)
- Verify network connectivity

**Rate Limiting:**
- CoinMarketCap API has rate limits
- Reduce frequency of requests
- Consider caching results

**Technical Indicator Errors:**
- Ensure sufficient historical data is available
- Check time period and interval settings
- Verify symbol is valid

## Support

For detailed documentation and examples, see [SKILL.md](SKILL.md).

## 👨‍💻 Author

**Jask**

- **Website**: https://jask.dev
- **GitHub**: https://github.com/respectevery01
- **Twitter**: [@jaskdon](https://twitter.com/jaskdon)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
