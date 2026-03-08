---
name: web3
version: 3.0.0
description: Web3 tools for querying token information, wallet balances, financial market analysis, and complete OKX Web3 API support for meme token scanning across multiple blockchain networks
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
tags: [web3, blockchain, crypto, wallet, token, finance, trading, technical-analysis, meme-tokens, okx-web3]
category: finance
dependencies:
  - python-dotenv
  - requests
  - okx
  - pandas
  - numpy
environment_variables:
  - OKX_API_KEY
  - OKX_API_SECRET
  - OKX_API_PASSPHRASE
  - COINMARKETCAP_API_KEY
---

# Web3 Tools

## Overview

Web3 tools provide comprehensive blockchain data querying and financial analysis capabilities, including token information queries, multi-chain wallet balance tracking, stock/crypto market data fetching, and technical indicator analysis. The tools support multiple blockchain networks including Ethereum, BSC, Solana, Bitcoin, and various EVM-compatible chains.

## Capabilities

### Token Query (`token_query.py`)

Query detailed token information including:
- Real-time price data
- Token name and symbol
- Market capitalization
- 24-hour trading volume
- Total and maximum supply
- Token decimals
- Logo and official website
- Social media links

**Supported Chains:**
- Ethereum
- BSC (Binance Smart Chain)
- Solana

### Wallet Balance (`wallet_balance.py`)

Query wallet balances across multiple blockchain networks:
- Native token balances for each chain
- USD value calculation using real-time prices
- Automatic address type detection
- Support for EVM chains, Bitcoin, and Solana
- ERC20 token balance queries (EVM chains only)

**Supported Chains:**
- EVM Chains: Ethereum, BSC, Polygon, Arbitrum, Optimism, Avalanche, Base, Linea, Fantom, Cronos
- Non-EVM: Bitcoin, Solana

### Market Data (`market_data.py`)

Fetch comprehensive market data for stocks and cryptocurrencies:
- OHLCV (Open, High, Low, Close, Volume) data
- Multiple time periods (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
- Multiple intervals (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
- Price change statistics
- 52-week high/low
- Average volume
- Historical data export

**Supported Assets:**
- Stocks: AAPL, MSFT, GOOGL, TSLA, etc.
- Crypto: BTC-USD, ETH-USD, SOL-USD, etc.

### RSI Technical Indicator (`rsi.py`)

Calculate Relative Strength Index (RSI) for technical analysis:
- RSI calculation with customizable period (default: 14)
- Overbought/oversold signal detection
- RSI divergence analysis
- Historical RSI values
- Trading recommendations
- Risk assessment

**Features:**
- Automatic signal interpretation (overbought >70, oversold <30)
- Divergence pattern detection
- Comprehensive statistics (max, min, average RSI)
- Multiple timeframe support

### MACD Technical Indicator (`macd.py`)

Calculate Moving Average Convergence Divergence (MACD) for trend analysis:
- MACD line calculation (fast EMA - slow EMA)
- Signal line calculation (MACD EMA)
- Histogram calculation (MACD - Signal)
- Golden cross / Death cross detection
- Trend strength analysis
- Trading recommendations

**Features:**
- Customizable periods (fast: 12, slow: 26, signal: 9)
- Crossover signal detection
- Trend analysis
- Multiple timeframe support
- Combined analysis with RSI

### CoinMarketCap API (`coinmarketcap.py`)

Access professional cryptocurrency market data:
- Cryptocurrency listings by market cap
- Individual cryptocurrency information
- Global market metrics
- Real-time price data
- Market dominance tracking
- DeFi, stablecoin, and derivatives data

**Features:**
- Top cryptocurrencies by market cap
- Custom sorting (market_cap, price, volume, etc.)
- Multiple currency conversions
- Global market statistics
- Comprehensive token metadata

### Meme Token Scanner (`chain_scanner.py`)

Complete OKX Web3 API support for meme token analysis:
- Scan for meme tokens across multiple blockchains
- Get supported chains and protocols
- Query detailed token information
- Find similar tokens
- Track aped wallets (co-ride wallets)
- Get token bundle transaction data
- Get token developer information
- Track signal-supported chains
- Get recent signal lists

**Supported Chains:**
- Solana (SOL)
- BSC (Binance Smart Chain)
- X Layer
- TRON
- Ethereum (ETH)

**Supported Protocols:**
- pumpfun (Solana)
- bonk (Solana)
- moonshot (Solana)
- raydium (Solana)
- pancakeswap (BSC)
- xswap (X Layer)
- sunswap (TRON)
- uniswap (Ethereum)

**Features:**
- Real-time meme token scanning
- Risk analysis and recommendations
- Social media link verification
- Token age and liquidity tracking
- Smart money signal tracking
- Developer reputation analysis
- Bundle transaction monitoring

## Usage

### Token Query

```bash
python scripts/web3.py token-query <chain> <contract_address>
```

**Examples:**
```bash
# Ethereum token
python scripts/web3.py token-query ethereum 0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683

# BSC token
python scripts/web3.py token-query bsc 0x...

# Solana token
python scripts/web3.py token-query sol So11111111111111111111111111111111111111112
```

### Wallet Balance

```bash
python scripts/web3.py wallet-balance <wallet_address>
```

**Examples:**
```bash
# EVM wallet address
python scripts/web3.py wallet-balance 0x53A0Fc074E31068CFdBD73B756458546274fEa97

# Bitcoin address
python scripts/web3.py wallet-balance bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh

# Solana address
python scripts/web3.py wallet-balance 9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM
```

### Market Data

```bash
python scripts/web3.py market-data <symbol> [options]
```

**Examples:**
```bash
# Get Apple stock data (default 1 year)
python scripts/web3.py market-data AAPL

# Get Bitcoin data for 1 month
python scripts/web3.py market-data BTC-USD --period 1mo

# Get Ethereum data with 1-hour interval
python scripts/web3.py market-data ETH-USD --interval 1h

# Get multiple stocks
python scripts/web3.py market-data AAPL MSFT GOOG --period 3mo
```

**Options:**
- `--period`: Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
- `--interval`: Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
- `--start`: Start date (YYYY-MM-DD)
- `--end`: End date (YYYY-MM-DD)
- `--info`: Show company information

### RSI Technical Indicator

```bash
python scripts/web3.py rsi <symbol> [options]
```

**Examples:**
```bash
# Calculate RSI for Apple (default 14-period)
python scripts/web3.py rsi AAPL

# Calculate RSI for Bitcoin with custom period
python scripts/web3.py rsi BTC-USD --period 21

# Calculate RSI for Ethereum with 1-hour interval
python scripts/web3.py rsi ETH-USD --interval 1h

# Analyze RSI divergence
python scripts/web3.py rsi AAPL --divergence
```

**Options:**
- `--period`: RSI calculation period (default: 14)
- `--time-period`: Time period for data (default: 1y)
- `--interval`: Data interval (default: 1d)
- `--divergence`: Analyze RSI divergence patterns

### MACD Technical Indicator

```bash
python scripts/web3.py macd <symbol> [options]
```

**Examples:**
```bash
# Calculate MACD for Apple (default periods)
python scripts/web3.py macd AAPL

# Calculate MACD for Bitcoin with custom periods
python scripts/web3.py macd BTC-USD --fast 10 --slow 20 --signal 8

# Calculate MACD for Ethereum with 1-hour interval
python scripts/web3.py macd ETH-USD --interval 1h

# Combined analysis with RSI
python scripts/web3.py macd AAPL --combined
```

**Options:**
- `--fast`: Fast EMA period (default: 12)
- `--slow`: Slow EMA period (default: 26)
- `--signal`: Signal line EMA period (default: 9)
- `--time-period`: Time period for data (default: 1y)
- `--interval`: Data interval (default: 1d)
- `--combined`: Include RSI analysis in results

### CoinMarketCap API

```bash
python scripts/web3.py coinmarketcap <command> [options]
```

**Examples:**
```bash
# Get top 10 cryptocurrencies
python scripts/web3.py coinmarketcap listings --limit 10

# Get Bitcoin information
python scripts/web3.py coinmarketcap info BTC

# Get global market metrics
python scripts/web3.py coinmarketcap global

# Get Fear and Greed Index (Pro plan required)
python scripts/web3.py coinmarketcap fear-greed

# Get CMC20 Index (Pro plan required)
python scripts/web3.py coinmarketcap cmc20

# Get CMC100 Index (Pro plan required)
python scripts/web3.py coinmarketcap cmc100

# Get top 50 cryptocurrencies sorted by price
python scripts/web3.py coinmarketcap listings --limit 50 --sort price

# Get Ethereum info with EUR conversion
python scripts/web3.py coinmarketcap info ETH --convert EUR
```

**Commands:**
- `listings`: Get cryptocurrency listings
- `info`: Get specific cryptocurrency information
- `global`: Get global market metrics (Pro plan required)
- `fear-greed`: Get Fear and Greed Index
- `cmc20`: Get CMC20 Index
- `cmc100`: Get CMC100 Index

**Options:**
- `--limit`: Number of results (default: 100)
- `--start`: Start rank (default: 1)
- `--convert`: Currency for price conversion (default: USD)
- `--sort`: Sort field (market_cap, price, volume, etc.)
- `--sort-dir`: Sort direction (asc, desc)
- `--type`: Cryptocurrency type (all, coins, tokens)

**Note:** The `global` command requires CoinMarketCap Pro plan or higher. Other features (listings, info, fear-greed, cmc20, cmc100) are available on the Basic plan.

### Meme Token Scanner

```bash
python scripts/web3.py chain-scanner [options]
```

**Examples:**
```bash
# Scan for new meme tokens on Solana
python scripts/web3.py chain-scanner --chain sol --stage NEW --limit 10

# Scan for meme tokens with social links
python scripts/web3.py chain-scanner --chain sol --social --limit 20

# Scan with minimum volume and market cap
python scripts/web3.py chain-scanner --chain sol --min-volume 10000 --min-mcap 50000

# Get supported chains and protocols
python scripts/web3.py supported-chains

# Get detailed token information
python scripts/web3.py token-details sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get similar tokens
python scripts/web3.py similar-tokens sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get aped wallets (co-ride wallets)
python scripts/web3.py aped-wallets sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get token bundle transaction data
python scripts/web3.py token-bundle-info sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get token developer information
python scripts/web3.py token-dev-info sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump

# Get signal-supported chains
python scripts/web3.py signal-chains

# Get recent signal list
python scripts/web3.py signal-list sol --wallet-type 1 --min-amount 1000
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

**Wallet Types for signal-list:**
- 1: Smart Money wallets
- 2: KOL/Influencer wallets
- 3: Whales wallets

## Complete Analysis Workflow

### Meme Token Analysis Workflow

This section demonstrates how to use web3 commands step-by-step to perform a comprehensive meme token analysis.

#### Step 1: Scan for New Meme Tokens

Start by scanning for new meme tokens on Solana with specific criteria:

```bash
python scripts/web3.py chain-scanner --chain sol --stage NEW --min-volume 10000 --min-holders 100 --limit 10
```

This returns a list of new meme tokens that meet your criteria. Review the results and select a token for deeper analysis.

#### Step 2: Get Detailed Token Information

Once you've identified a promising token, get its detailed information:

```bash
python scripts/web3.py token-details sol <token_address>
```

This provides comprehensive data including:
- Token price and market cap
- 24h volume
- Holder count
- Token age
- Social media links
- Risk factors

#### Step 3: Analyze Developer Reputation

Check the developer's track record to assess trustworthiness:

```bash
python scripts/web3.py token-dev-info sol <token_address>
```

Look for:
- Developer's previous launches
- Golden gem count (successful projects)
- Migrated count (projects that migrated to Raydium)
- Rug pull count (scams - should be 0)
- Total tokens launched

#### Step 4: Find Similar Tokens

Identify similar tokens to understand the token's category and potential:

```bash
python scripts/web3.py similar-tokens sol <token_address>
```

This helps you:
- Compare with similar tokens
- Understand market positioning
- Identify potential competitors
- Gauge market interest

#### Step 5: Check Bundle Transactions

Analyze bundle transactions to detect potential manipulation:

```bash
python scripts/web3.py token-bundle-info sol <token_address>
```

Key metrics to review:
- Bundled token amount
- Bundled value in native tokens
- Bundler ATH percentage
- Total bundlers count

High bundler activity may indicate coordinated buying or potential manipulation.

#### Step 6: Track Aped Wallets

Identify wallets that have aped into the token:

```bash
python scripts/web3.py aped-wallets sol <token_address>
```

Analyze:
- Wallet types (Smart Money, KOL, Whales)
- Entry amounts
- Current PnL
- Entry timing

This helps you understand who's investing and their track record.

#### Step 7: Monitor Smart Money Signals

Track recent signals from smart money wallets:

```bash
python scripts/web3.py signal-list sol --wallet-type 1 --min-amount 1000 --limit 50
```

This shows:
- Recent smart money transactions
- Token addresses
- Transaction amounts
- Market cap ranges
- Liquidity data

#### Step 8: Get Supported Chains and Protocols

Understand the ecosystem:

```bash
python scripts/web3.py supported-chains
```

This provides:
- All supported blockchains
- Available protocols on each chain
- Chain IDs for API calls

### Example: Complete Analysis Script

Here's a complete example of analyzing a meme token:

```bash
# Step 1: Scan for new meme tokens
echo "Step 1: Scanning for new meme tokens..."
python scripts/web3.py chain-scanner --chain sol --stage NEW --min-volume 10000 --limit 5

# Step 2: Get token details (replace with actual token address)
echo "Step 2: Getting token details..."
TOKEN_ADDRESS="FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump"
python scripts/web3.py token-details sol $TOKEN_ADDRESS

# Step 3: Check developer info
echo "Step 3: Checking developer information..."
python scripts/web3.py token-dev-info sol $TOKEN_ADDRESS

# Step 4: Find similar tokens
echo "Step 4: Finding similar tokens..."
python scripts/web3.py similar-tokens sol $TOKEN_ADDRESS

# Step 5: Check bundle transactions
echo "Step 5: Checking bundle transactions..."
python scripts/web3.py token-bundle-info sol $TOKEN_ADDRESS

# Step 6: Track aped wallets
echo "Step 6: Tracking aped wallets..."
python scripts/web3.py aped-wallets sol $TOKEN_ADDRESS

# Step 7: Monitor smart money signals
echo "Step 7: Monitoring smart money signals..."
python scripts/web3.py signal-list sol --wallet-type 1 --min-amount 1000 --limit 20
```

### Decision Framework

Based on the analysis, use this framework to make decisions:

#### Green Flags (Positive Indicators)
- Developer has multiple successful launches (golden gems)
- Low or zero rug pull count
- High holder count with organic growth
- Smart money wallets are entering
- Strong social media presence
- Reasonable bundle activity
- Similar tokens performing well

#### Red Flags (Negative Indicators)
- Developer has rug pull history
- Very high bundler activity (potential manipulation)
- Low holder count with high volume
- No social media links
- Smart money wallets are exiting
- Extremely high price volatility
- Suspicious transaction patterns

#### Risk Assessment

Combine the data to assess risk:

```bash
# Low Risk: All green flags, no red flags
# Medium Risk: Some green flags, minor red flags
# High Risk: Multiple red flags, developer issues
# Very High Risk: Rug pull history, extreme manipulation signs
```

### Advanced Analysis Tips

1. **Cross-Reference Data**: Compare data from multiple commands to validate findings
2. **Historical Context**: Track signals over time to identify trends
3. **Portfolio Diversification**: Don't invest everything in one token
4. **Set Stop-Losses**: Use technical indicators (RSI, MACD) to set exit points
5. **Monitor Continuously**: Run analysis periodically to catch changes

### Integration with Technical Analysis

Combine meme token analysis with technical indicators:

```bash
# Get market data for a token
python scripts/web3.py market-data <symbol> --period 1mo

# Calculate RSI
python scripts/web3.py rsi <symbol> --period 14

# Calculate MACD
python scripts/web3.py macd <symbol> --fast 12 --slow 26 --signal 9
```

This provides both fundamental (meme token data) and technical (indicators) analysis.

## Technical Analysis Workflow

This section demonstrates how to use web3 commands step-by-step to perform comprehensive technical analysis for stocks and cryptocurrencies.

### Stock Analysis Workflow

#### Step 1: Get Market Data

Start by fetching comprehensive market data for a stock:

```bash
python scripts/web3.py market-data AAPL --period 1y
```

This provides:
- OHLCV data (Open, High, Low, Close, Volume)
- Price change statistics
- 52-week high/low
- Average volume
- Historical data points

#### Step 2: Calculate RSI Indicator

Calculate Relative Strength Index to identify overbought/oversold conditions:

```bash
python scripts/web3.py rsi AAPL --period 14 --time-period 1y
```

Key RSI signals to watch:
- **RSI > 70**: Overbought (potential sell signal)
- **RSI < 30**: Oversold (potential buy signal)
- **RSI = 50**: Neutral
- **Divergence**: Price making new highs/lows but RSI not confirming

#### Step 3: Calculate MACD Indicator

Calculate MACD to identify trend direction and momentum:

```bash
python scripts/web3.py macd AAPL --fast 12 --slow 26 --signal 9 --time-period 1y
```

Key MACD signals:
- **Golden Cross**: MACD line crosses above signal line (bullish)
- **Death Cross**: MACD line crosses below signal line (bearish)
- **Histogram**: Positive = bullish momentum, Negative = bearish momentum
- **Zero Line**: MACD above zero = uptrend, below zero = downtrend

#### Step 4: Combined Analysis with RSI

Use MACD with RSI for confirmation:

```bash
python scripts/web3.py macd AAPL --combined --time-period 1y
```

This provides:
- MACD analysis
- RSI analysis
- Combined trading signals
- Risk assessment

### Cryptocurrency Analysis Workflow

#### Step 1: Get Crypto Market Data

Fetch market data for cryptocurrency:

```bash
python scripts/web3.py market-data BTC-USD --period 6mo --interval 1d
```

For more granular data, use shorter intervals:
```bash
python scripts/web3.py market-data ETH-USD --period 1mo --interval 1h
```

#### Step 2: Calculate RSI for Crypto

```bash
python scripts/web3.py rsi BTC-USD --period 14 --time-period 6mo --interval 1d
```

Crypto-specific RSI considerations:
- Crypto markets are more volatile
- RSI extremes (>80 or <20) are more common
- Use longer periods (21 or 28) for smoother signals
- Watch for rapid RSI reversals

#### Step 3: Calculate MACD for Crypto

```bash
python scripts/web3.py macd BTC-USD --fast 12 --slow 26 --signal 9 --time-period 6mo --interval 1d
```

Crypto-specific MACD considerations:
- Use shorter intervals (1h, 4h) for day trading
- Use longer periods (1d, 1wk) for swing trading
- Crypto trends are stronger and more persistent
- Watch for histogram divergences

#### Step 4: Get Crypto Market Metrics

Use CoinMarketCap for additional context:

```bash
python scripts/web3.py coinmarketcap info BTC
python scripts/web3.py coinmarketcap listings --limit 10 --sort market_cap
```

This provides:
- Market cap ranking
- 24h volume
- Circulating supply
- All-time high/low
- Price change percentages

### Example: Complete Stock Analysis Script

```bash
# Analyze Apple (AAPL) stock
echo "=== Apple Stock Technical Analysis ==="

# Step 1: Get market data
echo "Step 1: Fetching market data..."
python scripts/web3.py market-data AAPL --period 1y

# Step 2: Calculate RSI
echo "Step 2: Calculating RSI..."
python scripts/web3.py rsi AAPL --period 14 --time-period 1y

# Step 3: Calculate MACD
echo "Step 3: Calculating MACD..."
python scripts/web3.py macd AAPL --fast 12 --slow 26 --signal 9 --time-period 1y

# Step 4: Combined analysis
echo "Step 4: Combined technical analysis..."
python scripts/web3.py macd AAPL --combined --time-period 1y
```

### Example: Complete Crypto Analysis Script

```bash
# Analyze Bitcoin (BTC)
echo "=== Bitcoin Technical Analysis ==="

# Step 1: Get market data
echo "Step 1: Fetching market data..."
python scripts/web3.py market-data BTC-USD --period 6mo --interval 1d

# Step 2: Calculate RSI
echo "Step 2: Calculating RSI..."
python scripts/web3.py rsi BTC-USD --period 14 --time-period 6mo --interval 1d

# Step 3: Calculate MACD
echo "Step 3: Calculating MACD..."
python scripts/web3.py macd BTC-USD --fast 12 --slow 26 --signal 9 --time-period 6mo --interval 1d

# Step 4: Get CoinMarketCap info
echo "Step 4: Getting CoinMarketCap data..."
python scripts/web3.py coinmarketcap info BTC

# Step 5: Combined analysis
echo "Step 5: Combined technical analysis..."
python scripts/web3.py macd BTC-USD --combined --time-period 6mo --interval 1d
```

### Example: Multi-Timeframe Analysis

Analyze across multiple timeframes for better signals:

```bash
# Bitcoin multi-timeframe analysis
echo "=== Bitcoin Multi-Timeframe Analysis ==="

# Daily timeframe (long-term)
echo "Daily timeframe..."
python scripts/web3.py rsi BTC-USD --period 14 --time-period 1y --interval 1d
python scripts/web3.py macd BTC-USD --time-period 1y --interval 1d

# 4-hour timeframe (medium-term)
echo "4-hour timeframe..."
python scripts/web3.py rsi BTC-USD --period 14 --time-period 3mo --interval 4h
python scripts/web3.py macd BTC-USD --time-period 3mo --interval 4h

# 1-hour timeframe (short-term)
echo "1-hour timeframe..."
python scripts/web3.py rsi BTC-USD --period 14 --time-period 1mo --interval 1h
python scripts/web3.py macd BTC-USD --time-period 1mo --interval 1h
```

### Technical Analysis Decision Framework

#### Bullish Signals (Buy)
- **RSI**: Oversold (<30) and rising
- **MACD**: Golden cross (MACD above signal)
- **MACD Histogram**: Positive and increasing
- **MACD Zero Line**: Crossing above zero
- **Confirmation**: Multiple timeframes aligned

#### Bearish Signals (Sell)
- **RSI**: Overbought (>70) and falling
- **MACD**: Death cross (MACD below signal)
- **MACD Histogram**: Negative and decreasing
- **MACD Zero Line**: Crossing below zero
- **Confirmation**: Multiple timeframes aligned

#### Neutral Signals (Hold)
- **RSI**: Between 40-60
- **MACD**: Near signal line
- **MACD Histogram**: Near zero
- **Mixed signals**: Different timeframes disagree

### Advanced Technical Analysis Tips

#### 1. Divergence Analysis

Watch for divergences between price and indicators:

```bash
# Check for RSI divergence
python scripts/web3.py rsi AAPL --divergence --time-period 1y
```

- **Bullish Divergence**: Price makes lower low, RSI makes higher low
- **Bearish Divergence**: Price makes higher high, RSI makes lower high

#### 2. Support and Resistance

Use market data to identify key levels:

```bash
python scripts/web3.py market-data AAPL --period 2y
```

Look for:
- **Support**: Price levels where stock bounced multiple times
- **Resistance**: Price levels where stock rejected multiple times
- **Breakouts**: Price breaking above resistance
- **Breakdowns**: Price falling below support

#### 3. Volume Analysis

Monitor volume with price movements:

```bash
python scripts/web3.py market-data AAPL --period 1y
```

- **High Volume + Price Up**: Strong buying pressure
- **High Volume + Price Down**: Strong selling pressure
- **Low Volume + Price Up**: Weak buying (potential reversal)
- **Low Volume + Price Down**: Weak selling (potential reversal)

#### 4. Trend Analysis

Use MACD to determine trend:

```bash
python scripts/web3.py macd AAPL --time-period 1y
```

- **Uptrend**: MACD above zero, histogram positive
- **Downtrend**: MACD below zero, histogram negative
- **Sideways**: MACD near zero, histogram fluctuating

### Risk Management

#### Stop Loss Levels

Use technical levels to set stop losses:

```bash
# Calculate RSI to find exit points
python scripts/web3.py rsi AAPL --period 14

# Use MACD to confirm trend reversal
python scripts/web3.py macd AAPL
```

Stop loss strategies:
- **ATR-based**: Use volatility to set stops
- **Support-based**: Set stops below support levels
- **Indicator-based**: Exit when RSI >70 or MACD death cross

#### Position Sizing

Adjust position size based on risk:

- **High volatility (crypto)**: Smaller positions
- **Low volatility (blue-chip stocks)**: Larger positions
- **Multiple confirmations**: Larger positions
- **Mixed signals**: Smaller positions

### Trading Strategies

#### Strategy 1: RSI Reversal

```bash
# Step 1: Wait for oversold condition
python scripts/web3.py rsi AAPL --period 14

# Step 2: Confirm with MACD
python scripts/web3.py macd AAPL

# Step 3: Enter when RSI <30 and MACD golden cross
# Step 4: Exit when RSI >70 or MACD death cross
```

#### Strategy 2: MACD Crossover

```bash
# Step 1: Monitor MACD
python scripts/web3.py macd AAPL --time-period 1y --interval 1d

# Step 2: Enter on golden cross
# Step 3: Exit on death cross
# Step 4: Use RSI as confirmation
```

#### Strategy 3: Multi-Timeframe Confirmation

```bash
# Step 1: Check daily trend
python scripts/web3.py macd BTC-USD --time-period 1y --interval 1d

# Step 2: Check 4-hour trend
python scripts/web3.py macd BTC-USD --time-period 3mo --interval 4h

# Step 3: Check 1-hour trend
python scripts/web3.py macd BTC-USD --time-period 1mo --interval 1h

# Step 4: Enter only when all timeframes aligned
```

### Backtesting and Validation

To validate strategies, analyze historical data:

```bash
# Get historical data
python scripts/web3.py market-data AAPL --period 5y

# Calculate indicators on historical data
python scripts/web3.py rsi AAPL --period 14 --time-period 5y
python scripts/web3.py macd AAPL --time-period 5y

# Review past signals and outcomes
# Adjust parameters based on results
```

## API Integration

### Token Query API

The token query tool uses the OKX Web3 API:
- Base URL: `https://web3.okx.com`
- Endpoints:
  - `/api/v5/wallet/token/real-time-price` - Real-time token price
  - `/api/v5/wallet/token/token-detail` - Token details

**Required Environment Variables:**
- `OKX_API_KEY` - OKX API key
- `OKX_API_SECRET` - OKX API secret
- `OKX_API_PASSPHRASE` - OKX API passphrase

### Wallet Balance API

The wallet balance tool uses multiple APIs:
- **RPC Nodes**: For querying blockchain data directly
- **CoinGecko API**: For fetching token prices
- **Blockstream API**: For Bitcoin UTXO data
- **Solana RPC**: For Solana balance queries

**Optional Environment Variables:**
- `ETHERSCAN_API_KEY` - For enhanced EVM chain queries

### Market Data API

The market data tool uses Yahoo Finance API:
- **Base URL**: `https://query1.finance.yahoo.com/v8/finance/chart/`
- **Endpoints**:
  - `/chart/{symbol}` - Historical OHLCV data
- **Features**:
  - Real-time and historical data
  - Multiple timeframes and intervals
  - No API key required
  - Supports stocks and cryptocurrencies

### RSI & MACD API

The technical indicator tools use the same Yahoo Finance API as market data:
- Calculations performed locally using pandas and numpy
- Supports all symbols available on Yahoo Finance
- No additional API dependencies

### CoinMarketCap API

The CoinMarketCap tool uses professional API:
- **Base URL**: `https://pro-api.coinmarketcap.com`
- **Endpoints**:
  - `/v1/cryptocurrency/listings/latest` - Cryptocurrency listings
  - `/v2/cryptocurrency/quotes/latest` - Individual cryptocurrency data
  - `/v1/global-metrics/quotes/latest` - Global market metrics

**Required Environment Variables:**
- `COINMARKETCAP_API_KEY` - CoinMarketCap API key

**Features:**
- Professional-grade cryptocurrency data
- Real-time price updates
- Comprehensive market metrics
- Multiple currency conversions
- Rate-limited with credit system

### OKX Web3 Meme Token API

The meme token scanner uses the OKX Web3 API:
- **Base URL**: `https://web3.okx.com`
- **Endpoints**:
  - `/api/v6/dex/market/memepump/supported/chainsProtocol` - Get supported chains and protocols
  - `/api/v6/dex/market/memepump/tokenList` - Scan for meme tokens
  - `/api/v6/dex/market/memepump/tokenDetails` - Get token details
  - `/api/v6/dex/market/memepump/similarToken` - Get similar tokens
  - `/api/v6/dex/market/memepump/apedWallet` - Get aped wallets
  - `/api/v6/dex/market/memepump/tokenBundleInfo` - Get token bundle transaction data
  - `/api/v6/dex/market/memepump/tokenDevInfo` - Get token developer information
  - `/api/v6/dex/market/signal/supported/chain` - Get signal-supported chains
  - `/api/v6/dex/market/signal/list` - Get recent signal list

**Required Environment Variables:**
- `OKX_API_KEY` - OKX API key
- `OKX_API_SECRET` - OKX API secret
- `OKX_API_PASSPHRASE` - OKX API passphrase

**Features:**
- Real-time meme token scanning
- Smart money signal tracking
- Developer reputation analysis
- Bundle transaction monitoring
- Multi-chain support
- Risk analysis

## Data Structures

### Token Query Response

```json
{
  "chain": "ethereum",
  "token_address": "0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683",
  "price_usd": "123.45",
  "name": "Token Name",
  "symbol": "TKN",
  "market_cap": "1000000000",
  "volume_24h": "50000000",
  "total_supply": "1000000000",
  "max_supply": "1000000000",
  "decimals": "18",
  "logo_url": "https://...",
  "official_website": "https://...",
  "social_urls": {},
  "timestamp": "1700000000000"
}
```

### Wallet Balance Response

```json
{
  "wallet_address": "0x53A0Fc074E31068CFdBD73B756458546274fEa97",
  "balances": [
    {
      "chain": "ethereum",
      "chain_id": "1",
      "balance": "1.5",
      "balance_raw": "1500000000000000000",
      "decimals": "18",
      "unit": "ETH",
      "price_usd": "2000.00",
      "value_usd": "3000.00"
    }
  ],
  "total_value_usd": "3000.00",
  "chain_count": 1,
  "timestamp": "1700000000000"
}
```

## Error Handling

The tools implement comprehensive error handling:
- Invalid chain names
- Invalid wallet addresses
- API request failures
- Network timeouts
- Missing environment variables

Error responses include descriptive messages to help identify and resolve issues.

## Address Type Detection

The wallet balance tool automatically detects address types:
- **Bitcoin**: Addresses starting with `1`, `3`, or `bc1`
- **Solana**: Base58 encoded addresses (32-44 characters)
- **EVM**: Addresses starting with `0x` and 42 characters long

## Advanced Features

### Multi-Chain Queries

Query balances across all supported chains simultaneously:
```python
from scripts.wallet_balance import wallet_balance

result = wallet_balance(wallet_address, show_zero=False)
```

### ERC20 Token Balances

Query ERC20 token balances for EVM chains:
```python
from scripts.wallet_balance import wallet_balance_with_tokens

result = wallet_balance_with_tokens(
    wallet_address,
    chain='ethereum',
    token_addresses=['0x...', '0x...']
)
```

### Custom Chain Selection

Specify which chains to query:
```python
from scripts.wallet_balance import wallet_balance

result = wallet_balance(
    wallet_address,
    chains=['ethereum', 'bsc'],
    show_zero=True
)
```

## Internationalization

The tools support multiple languages:
- English (en_us) - Default
- Chinese (zh_cn)
- Japanese (jp)
- Traditional Chinese (zh_tw)

Language can be specified via command-line arguments or environment variables.

## Dependencies

- `python-dotenv` - Environment variable management
- `requests` - HTTP requests
- `okx` - OKX API client

Install dependencies:
```bash
pip install python-dotenv requests okx
```

## Configuration

Environment variables should be set in the `.env` file:
```
OKX_API_KEY=your_api_key
OKX_API_SECRET=your_api_secret
OKX_API_PASSPHRASE=your_passphrase
ETHERSCAN_API_KEY=your_etherscan_api_key
```

## Performance Considerations

- Token queries use OKX API with rate limiting
- Wallet balance queries are optimized with parallel requests
- Price data is cached when possible to reduce API calls
- Timeout settings prevent hanging on unresponsive endpoints

## Security Notes

- API keys are loaded from environment variables only
- No sensitive data is logged or stored
- All API requests use HTTPS
- Wallet addresses are validated before querying

## Limitations

- Token query requires OKX API credentials
- Some chains may have rate limits
- Price data may have slight delays
- Not all tokens have complete metadata
- Bitcoin queries rely on public APIs

## Best Practices

1. **API Key Management**: Keep API keys secure and rotate regularly
2. **Error Handling**: Always check for errors in responses
3. **Rate Limiting**: Respect API rate limits to avoid being blocked
4. **Data Validation**: Validate addresses before querying
5. **Caching**: Cache results when appropriate to reduce API calls
6. **Monitoring**: Monitor API usage and error rates

## Troubleshooting

### Common Issues

**"Unsupported chain" error:**
- Verify chain name is in the supported chains list
- Check chain name spelling (case-sensitive)

**"Invalid wallet address" error:**
- Verify address format matches the expected blockchain
- Check for typos in the address

**API request failures:**
- Verify API keys are correctly configured
- Check network connectivity
- Verify API endpoints are accessible

**Missing price data:**
- Some tokens may not have price data available
- Check CoinGecko API status
- Verify token symbol mapping is correct

## Future Enhancements

Potential improvements:
- Support for additional blockchain networks
- Real-time price alerts
- Historical balance queries
- Transaction history tracking
- Portfolio analytics
- Multi-wallet aggregation
- NFT balance queries
- DeFi protocol integration

## Related Skills

- `qweather` - Weather information for travel planning
- `amap` - Route planning and location services
- `travel` - Travel planning integration

## Support

For issues or questions:
1. Check the error messages in the output
2. Verify environment variables are set correctly
3. Ensure all dependencies are installed
4. Check API status pages for service availability
