# OpenClaw Skills Collection

A comprehensive collection of AI-powered tools for daily life assistance, including weather queries, map services, travel planning, social media integration, and Web3 interactions.

## 📋 Overview

OpenClaw Skills Collection provides modular, AI-friendly tools designed to work together or independently. Each skill follows a standardized structure for easy integration and maintenance.

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Quick Start

1. **Clone or download the repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

4. **Edit `.env` file** with your API credentials:
   - OKX API keys (for Web3 features)
   - QWeather API key (for weather queries)
   - Amap API key (for map services)
   - AI API keys (optional, for AI Aggregator)

### Optional Dependencies

For AI Aggregator functionality, uncomment the relevant lines in `requirements.txt`:

```bash
# For specific AI services
pip install openai>=1.0.0  # OpenAI API
pip install anthropic>=0.18.0  # Claude API
pip install google-generativeai>=0.3.0  # Gemini API
pip install dashscope>=1.14.0  # Qwen API
pip install zhipuai>=2.0.0  # GLM API
```

## 🚀 Available Skills

### Diary Skills (`diary/`)

A collection of tools for daily life assistance.

#### 🌤️ QWeather
Query weather information including current conditions, forecasts, and air quality.

**Features**:
- Current weather conditions
- 3-day and 7-day forecasts
- Air quality index
- Global city search
- Multi-language support (Chinese, English, Japanese)

**Documentation**: [diary/qweather/README.md](diary/qweather/README.md)

#### 🗺️ Amap
Query map information including geocoding, POI search, and route planning.

**Features**:
- Address geocoding
- POI search by keywords
- Route planning (driving, walking, transit, cycling)
- Weather queries
- Multi-language support

**Documentation**: [diary/amap/README.md](diary/amap/README.md)

#### ✈️ Travel
Web interface for displaying modular travel plan JSON files.

**Features**:
- Web-based travel plan visualization
- Modular JSON structure
- Route and weather display
- Attraction recommendations
- Daily itinerary view

**Documentation**: [diary/travel/README.md](diary/travel/README.md)

#### 🐘 Mastodon
Mastodon social media integration for posting statuses, retrieving timelines, and managing notifications.

**Features**:
- Post statuses to Mastodon
- Retrieve home timeline
- Get notifications
- Upload media
- Verify credentials
- Multi-language support

**Documentation**: [diary/mastodon/README.md](diary/mastodon/README.md)

#### 📱 Telegram
Telegram Bot integration for sending messages, managing channels, and notifications.

**Features**:
- Send text messages with formatting (Markdown/HTML)
- Send photos and documents
- Send locations and contacts
- Message management (delete, pin, unpin)
- Bot and chat information
- Real-time updates
- Custom keyboards and buttons
- Text-to-Speech (TTS) - Send voice messages from text
- Speech-to-Text (STT) - Transcribe voice messages to text
- File download and automatic organization by type

**Documentation**: [diary/telegram/references/README.md](diary/telegram/references/README.md)

#### 🔵 Bluesky
Bluesky social media integration for posting text, images, reading timelines, and searching content.

**Features**:
- Post text and images to Bluesky
- Retrieve home timeline
- Get profile information
- Search posts and users
- Reply controls (threadgate)
- Multi-language support for posts
- Automatic image processing and optimization

**Documentation**: [diary/bluesky/README.md](diary/bluesky/README.md)

#### 🤖 AI Aggregator
Intelligent API routing for cost optimization and performance.

**Features**:
- Automatic API selection based on task requirements
- Cost optimization (prioritizes cost-effective APIs)
- Multi-language support (Chinese and English optimized)
- Task analysis and recommendation
- Support for 7 AI services (DeepSeek, OpenAI, Gemini, Minimax, GLM, Qwen, Claude)

**Documentation**: [diary/ai_aggregator/README.md](diary/ai_aggregator/README.md)

#### 📰 RSS Feed Reader
RSS feed reader for fetching, searching, and managing RSS feeds from various sources.

**Features**:
- Fetch RSS feeds with full details
- Search entries by keywords
- Get latest entries from feeds
- Get feed information and metadata
- Fetch and combine multiple feeds
- Flexible output formats (JSON/Text)
- Save feed data to files

**Documentation**: [diary/rss/references/README.md](diary/rss/references/README.md)

### Web3 Skills (`web3/`)

Comprehensive tools for blockchain interactions, financial market analysis, technical indicators, and complete OKX Web3 API support for meme token scanning.

#### 💰 Market Data
Fetch comprehensive market data for stocks and cryptocurrencies.

**Features**:
- Stock and cryptocurrency data
- Multiple time periods (1d to max)
- Multiple intervals (1m to 3mo)
- OHLCV data
- Price change statistics
- 52-week high/low
- Historical data export

**Documentation**: [web3/README.md](web3/README.md)

#### 📈 RSI Technical Indicator
Calculate Relative Strength Index for technical analysis.

**Features**:
- RSI calculation with customizable period
- Overbought/oversold signal detection
- RSI divergence analysis
- Trading recommendations
- Risk assessment

**Documentation**: [web3/README.md](web3/README.md)

#### 📉 MACD Technical Indicator
Calculate Moving Average Convergence Divergence for trend analysis.

**Features**:
- MACD line calculation
- Signal line calculation
- Histogram analysis
- Golden cross/death cross detection
- Trend strength analysis

**Documentation**: [web3/README.md](web3/README.md)

#### 💎 CoinMarketCap API
Access professional cryptocurrency market data.

**Features**:
- Top cryptocurrency listings
- Individual token information
- Global market metrics
- Real-time price data
- Market dominance tracking

**Documentation**: [web3/README.md](web3/README.md)

#### 💰 Token Query
Query token information including price, market cap, and volume.

**Features**:
- Token price information
- Market cap and volume
- Support for multiple chains (Ethereum, BSC, Solana)
- Multi-language support

**Documentation**: [web3/README.md](web3/README.md)

#### 💳 Wallet Balance
Query wallet balances across multiple blockchain networks.

**Features**:
- Multi-chain balance queries
- Support for Ethereum, BSC, Solana
- Zero-balance filtering
- Multi-language support

**Documentation**: [web3/README.md](web3/README.md)

#### 🎯 Meme Token Scanner (OKX Web3 API)
Complete OKX Web3 API support for meme token scanning and analysis.

**Features**:
- Scan for meme tokens across multiple blockchains (Solana, BSC, X Layer, TRON, Ethereum)
- Get supported chains and protocols (pumpfun, bonk, moonshot, raydium, pancakeswap, etc.)
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

**Documentation**: [web3/README.md](web3/README.md)

## 📁 Project Structure

```
openclaw/
├── SKILL.md              # AI skill documentation (this file)
├── README.md             # User documentation (this file)
├── .env                  # Environment variables
├── .env.example          # Environment variables template
├── diary/               # Diary skills
│   ├── SKILL.md         # Diary skills AI documentation
│   ├── README.md         # Diary skills user documentation
│   ├── qweather/        # Weather tool
│   ├── amap/           # Map tool
│   ├── travel/          # Travel planning tool
│   ├── mastodon/        # Mastodon integration
│   ├── bluesky/         # Bluesky integration
│   └── i18n/           # Internationalization
└── web3/                # Web3 skills
    ├── SKILL.md         # Web3 skills AI documentation
    ├── README.md         # Web3 skills user documentation
    ├── scripts/         # Launch scripts
    ├── assets/          # Core modules
    └── references/      # Documentation
```

## 🔧 Installation

### Prerequisites

- Python 3.8+
- Node.js 14+ (for travel tool)
- Valid API keys for respective services

### Setup

1. Clone or navigate to the openclaw directory
2. Install Python dependencies:
   ```bash
   pip install python-dotenv requests flask okx pandas numpy
   ```
3. Install Node.js dependencies (for travel tool):
   ```bash
   cd diary/travel
   npm install
   ```
4. Set up environment variables in `.env` file:
   ```env
   QWEATHER_API_KEY=your_qweather_api_key
   AMAP_API_KEY=your_amap_api_key
   ```

## 🚀 Quick Start

### Weather Queries
```bash
# Current weather
python diary.py weather 北京

# 7-day forecast
python diary.py weather 上海 --forecast 7

# Search city
python diary.py weather --search "San Francisco" --global-search
```

### Map Queries
```bash
# Route planning
python diary.py amap route 北京 上海 武汉

# Geocoding
python diary.py amap --geocode "天安门"

# POI search
python diary.py amap --poi 景点 --city 北京
```

### Travel Planning
```bash
# Show usage guide
python diary.py travel

# Start web server
python diary.py travel start
```

### Mastodon Integration
```bash
# Verify credentials
python diary.py mastodon verify-credentials

# Post a status
python diary.py mastodon post-status "Hello from OpenClaw!"

# Get timeline
python diary.py mastodon get-timeline

# Get notifications
python diary.py mastodon get-notifications

# Upload media
python diary.py mastodon upload-media /path/to/image.jpg --description "My photo"
```

### Bluesky Integration
```bash
# Post text
python diary.py bluesky --post "Hello Bluesky!"

# Post image
python diary.py bluesky --post "Beautiful photo!" --image "photo.jpg" --alt "Sunset"

# Get profile
python diary.py bluesky --profile

# Get timeline
python diary.py bluesky --timeline --limit 20

# Search content
python diary.py bluesky --search "python" --type posts --limit 10
```

### Web3 Queries
```bash
# Token query
python web3.py token-query ethereum 0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683

# Wallet balance
python web3.py wallet-balance 0x53A0Fc074E31068CFdBD73B756458546274fEa97

# Market data
python web3.py market-data AAPL
python web3.py market-data BTC-USD --period 1mo

# Technical indicators
python web3.py rsi AAPL
python web3.py macd BTC-USD --interval 1h

# CoinMarketCap
python web3.py coinmarketcap listings --limit 10
python web3.py coinmarketcap info BTC
python web3.py coinmarketcap global

# Meme token scanning
python web3.py chain-scanner --chain sol --stage NEW --limit 10
python web3.py supported-chains
python web3.py token-details sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump
python web3.py similar-tokens sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump
python web3.py aped-wallets sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump
python web3.py token-bundle-info sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump
python web3.py token-dev-info sol FGSpAGvkR1zRjjBpY2utb5JDyPnYSB7y3KDGpP53pump
python web3.py signal-list sol --wallet-type 1 --min-amount 1000
```

## 🌍 Multi-language Support

All skills support multiple languages:
- `zh_cn` - Simplified Chinese (default)
- `en_us` - English
- `zh_tw` - Traditional Chinese
- `jp` - Japanese

Set language via environment variable:
```bash
export LANG=en_us
```

## 📚 Documentation

### AI Agent Documentation
- **[SKILL.md](SKILL.md)** - Main AI skill documentation
- **[diary/SKILL.md](diary/SKILL.md)** - Diary skills AI documentation
- **[diary/qweather/SKILL.md](diary/qweather/SKILL.md)** - QWeather skill documentation
- **[diary/amap/SKILL.md](diary/amap/SKILL.md)** - Amap skill documentation
- **[diary/travel/SKILL.md](diary/travel/SKILL.md)** - Travel skill documentation
- **[diary/mastodon/SKILL.md](diary/mastodon/SKILL.md)** - Mastodon skill documentation
- **[web3/SKILL.md](web3/SKILL.md)** - Web3 skill documentation

### User Documentation
- **[diary/README.md](diary/README.md)** - Diary skills user guide
- **[diary/qweather/README.md](diary/qweather/README.md)** - QWeather user guide
- **[diary/amap/README.md](diary/amap/README.md)** - Amap user guide
- **[diary/travel/README.md](diary/travel/README.md)** - Travel user guide
- **[diary/mastodon/README.md](diary/mastodon/README.md)** - Mastodon user guide
- **[diary/bluesky/README.md](diary/bluesky/README.md)** - Bluesky user guide
- **[web3/README.md](web3/README.md)** - Web3 user guide

## 🔑 API Keys

### Required API Keys

1. **QWeather API Key**
   - Get from: https://dev.qweather.com/
   - Required for: Weather queries, travel planning
   - Set as: `QWEATHER_API_KEY`

2. **Amap API Key**
   - Get from: https://lbs.amap.com/
   - Required for: Map queries, route planning, travel planning
   - Set as: `AMAP_API_KEY`

3. **Mastodon Access Token**
   - Get from: https://mastodon.social/settings/applications
   - Required for: Mastodon social media integration
   - Set as: `MASTODON_ACCESS_TOKEN`

4. **Bluesky Credentials**
   - Get from: https://bsky.social/settings/app-passwords
   - Required for: Bluesky social media integration
   - Set as: `BLUESKY_HANDLE_ID` and `BLUESKY_CLIENT_PASSWORD_SECRET`

5. **OKX API Credentials**
   - Get from: https://www.okx.com/account/my-api
   - Required for: Token query
   - Set as: `OKX_API_KEY`, `OKX_API_SECRET`, and `OKX_API_PASSPHRASE`

6. **CoinMarketCap API Key**
   - Get from: https://pro.coinmarketcap.com/signup
   - Required for: Cryptocurrency market data
   - Set as: `COINMARKETCAP_API_KEY`

### Environment Variables

Create a `.env` file in the root directory:
```env
QWEATHER_API_KEY=your_qweather_api_key
AMAP_API_KEY=your_amap_api_key
MASTODON_ACCESS_TOKEN=your_mastodon_access_token
BLUESKY_HANDLE_ID=your_bluesky_handle
BLUESKY_CLIENT_PASSWORD_SECRET=your_bluesky_app_password
OKX_API_KEY=your_okx_api_key
OKX_API_SECRET=your_okx_api_secret
OKX_API_PASSPHRASE=your_okx_passphrase
COINMARKETCAP_API_KEY=your_coinmarketcap_api_key
```

## 🤖 AI Agent Integration

These tools are designed to work with AI agents. For detailed integration instructions, see [SKILL.md](SKILL.md).

### Example Workflow

When an AI agent receives a travel planning request:

1. Use qweather to fetch weather forecasts
2. Use amap to calculate routes and find attractions
3. Generate daily itinerary
4. Create modular JSON files
5. Provide URL to user

## 🐛 Troubleshooting

### Common Issues

**API Key Errors**
- Verify API keys are correct in `.env` file
- Check API key validity with respective service providers

**Network Errors**
- Check internet connection
- Verify API service status

**Module Not Found**
- Ensure all dependencies are installed
- Check Python virtual environment

**Import Errors**
- Verify Python version compatibility
- Check if all required packages are installed

## 📝 License

This project is provided as-is for educational and personal use.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows existing style conventions
- All tools support multi-language
- Documentation is updated
- Skills follow the standardized structure

## 📧 Support

For issues or questions:
1. Check skill-specific help commands
2. Review SKILL.md files
3. Check API documentation for respective services
4. Refer to user documentation in each skill directory

## 🎯 Use Cases

### Daily Life
- Check weather before going out
- Find routes to destinations
- Search for nearby attractions
- Plan weekend trips

### Travel Planning
- Multi-city trip planning
- Weather-aware itinerary
- Route optimization
- Attraction recommendations

### Blockchain
- Check token prices
- Query wallet balances
- Multi-chain support
- Real-time market data

## 🔮 Future Enhancements

- More weather data sources
- Additional map providers
- Enhanced travel planning features
- More blockchain networks
- Improved AI integration

## 📊 Statistics

- **Total Skills**: 9
- **Supported Languages**: 4
- **API Integrations**: 12 (Weather, Map, Social Media, Web3, AI Services, Telegram)
- **Blockchain Networks**: 5 (Ethereum, BSC, Solana, X Layer, TRON)
- **Web3 Features**: 15 (token query, wallet balance, market data, RSI, MACD, CoinMarketCap, chain scanner, supported chains, token details, similar tokens, aped wallets, token bundle info, token dev info, signal chains, signal list)
- **AI Services**: 7 (DeepSeek, OpenAI, Gemini, Minimax, GLM, Qwen, Claude)
- **Documentation Files**: 18

---

**OpenClaw Skills Collection** - Empowering AI with practical, modular tools for everyday use.

## 👨‍💻 Author

**Jask**

- **Website**: https://jask.dev
- **GitHub**: https://github.com/respectevery01
- **Twitter**: [@jaskdon](https://twitter.com/jaskdon)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ☕ Support Me

If you find this project helpful, consider supporting me:

<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support me on Ko-fi', '#f57394', 'E1E51932I0');kofiwidget2.draw();</script>
