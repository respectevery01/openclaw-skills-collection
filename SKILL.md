---
name: openclaw-skills-collection
description: A comprehensive collection of AI-powered skills for weather queries, map services, travel planning, social media integration, and Web3 interactions
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# OpenClaw Skills Collection

## Overview

OpenClaw Skills Collection is a modular system of AI-powered tools designed to work together or independently. Each skill follows a standardized structure for easy integration and maintenance.

## Design Philosophy

### Token Efficiency Strategy

All skills include comprehensive internationalization (i18n) support to optimize token usage and improve user experience:

**Why i18n?**
- **Direct Language Output**: Skills automatically output results in the user's preferred language
- **Copy-Paste Ready**: AI agents can directly copy and paste results without translation
- **Token Savings**: Eliminates the need for AI to translate outputs, saving tokens
- **Accuracy**: Avoids translation errors by using original, professionally translated content
- **Faster Response**: No additional translation steps required
- **Consistency**: Maintains consistent language across all interactions

**How It Works:**
1. User sets language preference via `LANG` environment variable (default: zh_cn)
2. Skills detect language preference automatically
3. Skills output results in the detected language
4. AI agent copies and pastes results directly to user
5. No translation needed → significant token savings

**Supported Languages:**
- `zh_cn` - Simplified Chinese
- `en_us` - English
- `zh_tw` - Traditional Chinese
- `jp` - Japanese

**Default Languages by Skill:**
- **QWeather**: English (`en_us`)
- **Amap**: Simplified Chinese (`zh_cn`)
- **Web3**: English (`en_us`)
- **Travel**: Inherits from system language
- **Mastodon**: English (`en_us`)
- **Bluesky**: English (`en_us`)

**How to Change Language:**
Set the `LANG` environment variable:
```bash
export LANG=zh_cn    # Simplified Chinese
export LANG=en_us     # English
export LANG=zh_tw     # Traditional Chinese
export LANG=jp        # Japanese
```

**AI Agent Best Practices:**
- **Always copy output directly** - Never translate skill outputs
- **Use original language** - Respect the skill's default language or user's language preference
- **Preserve formatting** - Maintain original output structure
- **No rephrasing needed** - The output is already user-friendly
- **Check default language** - Each skill may have different default language

This design ensures maximum efficiency and minimum token usage while providing the best user experience.

## Available Skills

### 1. Diary Skills (`diary/`)

A collection of tools for daily life assistance including weather, maps, travel planning, and social media integration.

#### QWeather (`diary/qweather/`)
Query weather information including current conditions, forecasts, and air quality.

**When to Use**:
- User asks about weather conditions
- Need weather forecasts for planning
- Query air quality index
- Search cities worldwide

**Usage**:
```bash
python diary.py weather [city] [options]
```

**Key Features**:
- Current weather conditions
- 3-day and 7-day forecasts
- Air quality index
- Global city search
- Multi-language support (zh_cn, en_us, zh_tw, jp)

**Integration**:
- Use for travel planning weather data
- Combine with amap for route planning
- Fetch forecasts for multiple locations

#### Amap (`diary/amap/`)
Query map information including geocoding, POI search, and route planning.

**When to Use**:
- User needs location information
- Calculate routes between cities
- Search for points of interest
- Get coordinates for addresses

**Usage**:
```bash
python diary.py amap [options]
```

**Key Features**:
- Address geocoding
- POI search by keywords
- Route planning (driving, walking, transit, cycling)
- Weather queries
- Multi-language support

**Integration**:
- Use for travel planning routes
- Find attractions for destinations
- Calculate travel times and distances

#### Travel (`diary/travel/`)
Web interface for displaying modular travel plan JSON files.

**When to Use**:
- Display travel plans in web interface
- Visualize travel data
- Show routes, weather, and attractions
- Provide user-friendly travel plan view

**Usage**:
```bash
python diary.py travel [command]
```

**Key Features**:
- Web-based travel plan visualization
- Modular JSON structure
- Route and weather display
- Attraction recommendations
- Daily itinerary view

**Integration**:
- Render travel plans created by AI
- Display data from qweather and amap
- Provide URL for user viewing

#### Mastodon (`diary/mastodon/`)
Mastodon social media integration for posting statuses, retrieving timelines, and managing notifications.

**When to Use**:
- User wants to post to Mastodon
- Need to retrieve timeline or notifications
- Upload media to Mastodon
- Verify Mastodon credentials
- Share travel plans or weather updates

**Usage**:
```bash
python diary.py mastodon [command] [options]
```

**Key Features**:
- Post statuses to Mastodon
- Retrieve home timeline
- Get notifications
- Upload media
- Verify credentials
- Multi-language support (en_us, zh_cn, zh_tw, jp)

**Integration**:
- Post weather updates from qweather
- Share travel plans from travel
- Combine with other tools for social media sharing

#### Bluesky (`diary/bluesky/`)
Bluesky social media integration for posting text, images, reading timelines, and searching content.

**When to Use**:
- User wants to post to Bluesky
- Need to retrieve timeline or profile
- Upload images to Bluesky
- Verify Bluesky credentials
- Share travel plans or weather updates

**Usage**:
```bash
python diary.py bluesky [options]
```

**Key Features**:
- Post text and images to Bluesky
- Retrieve home timeline
- Get profile information
- Search posts and users
- Reply controls (threadgate)
- Multi-language support for posts
- Automatic image processing and optimization

**Integration**:
- Post weather updates from qweather
- Share travel plans from travel
- Combine with other tools for social media sharing

#### Telegram (`diary/telegram/`)
Telegram Bot integration for sending messages, managing channels, text-to-speech, speech-to-text, and file management.

**When to Use**:
- User wants to send notifications to Telegram
- Need to send text, photos, or documents
- Convert text to voice messages (TTS)
- Transcribe voice messages to text (STT)
- Download and organize received files
- Manage Telegram channels or groups
- Send automated alerts or reports

**Usage**:
```bash
python diary.py telegram [options]
```

**Key Features**:
- Send text messages with formatting (Markdown/HTML)
- Send photos and documents
- Send locations and contacts
- Text-to-Speech (TTS) - Send voice messages from text
- Speech-to-Text (STT) - Transcribe voice messages to text
- Message management (delete, pin, unpin)
- Bot and chat information
- Real-time updates
- Custom keyboards and buttons
- File download and automatic organization by type
- Multi-language support for TTS and STT

**Integration**:
- Send weather alerts from qweather
- Share travel plans from travel
- Send system notifications
- Create automated voice response systems
- Combine with AI aggregator for intelligent responses

#### AI Aggregator (`diary/ai_aggregator/`)
Intelligent API routing for cost optimization and performance.

**When to Use**:
- User needs AI-powered text processing
- Want to optimize API costs
- Need multi-language support
- Require task analysis and recommendation

**Usage**:
```bash
python diary.py ai_aggregator [options]
```

**Key Features**:
- Automatic API selection based on task requirements
- Cost optimization (prioritizes cost-effective APIs)
- Multi-language support (Chinese and English optimized)
- Task analysis and recommendation
- Support for 7 AI services (DeepSeek, OpenAI, Gemini, Minimax, GLM, Qwen, Claude)

**Integration**:
- Use with Telegram for intelligent voice responses
- Combine with other skills for enhanced functionality
- Process and analyze text from various sources

#### RSS Feed Reader (`diary/rss/`)
RSS feed reader for fetching, searching, and managing RSS feeds from various sources.

**When to Use**:
- User wants to read news or blog posts
- Need to fetch RSS feed content
- Search for specific topics in feeds
- Monitor multiple RSS sources
- Get latest entries from feeds

**Usage**:
```bash
python diary.py rss [command] [options]
```

**Key Features**:
- Fetch RSS feeds with full details
- Search entries by keywords
- Get latest entries from feeds
- Get feed information and metadata
- Fetch and combine multiple feeds
- Flexible output formats (JSON/Text)
- Save feed data to files

**Integration**:
- Send news updates via Telegram
- Combine with AI Aggregator for content analysis
- Monitor multiple sources for automated alerts

### 2. Web3 Skills (`web3/`)

Comprehensive tools for blockchain interactions, financial market analysis, and technical indicators.

#### Token Query (`web3/`)
Query token information including price, market cap, and volume.

**When to Use**:
- User asks about token information
- Need token price or market data
- Query token details by contract address

**Usage**:
```bash
python web3.py token-query <chain> <contract_address>
```

**Key Features**:
- Token price information
- Market cap and volume
- Support for multiple chains (Ethereum, BSC, Solana)
- Multi-language support

**Integration**:
- Use for financial queries
- Provide token market data
- Support blockchain-related requests

#### Wallet Balance (`web3/`)
Query wallet balances across multiple blockchain networks.

**When to Use**:
- User asks about wallet balance
- Check account holdings
- Query multiple chain balances

**Usage**:
```bash
python web3.py wallet-balance <wallet_address>
```

**Key Features**:
- Multi-chain balance queries
- Support for Ethereum, BSC, Solana
- Zero-balance filtering
- Multi-language support

**Integration**:
- Use for financial queries
- Check user wallet status
- Support blockchain interactions

#### Market Data (`web3/`)
Fetch comprehensive market data for stocks and cryptocurrencies.

**When to Use**:
- User asks about stock or crypto prices
- Need historical price data
- Analyze market trends
- Get OHLCV data

**Usage**:
```bash
python web3.py market-data <symbol> [options]
```

**Key Features**:
- Stock and cryptocurrency data
- Multiple time periods (1d to max)
- Multiple intervals (1m to 3mo)
- OHLCV data
- Price change statistics
- 52-week high/low
- Historical data export

**Integration**:
- Use for market analysis
- Provide price data for technical indicators
- Support financial research

#### RSI Technical Indicator (`web3/`)
Calculate Relative Strength Index for technical analysis.

**When to Use**:
- User asks about RSI indicator
- Need overbought/oversold signals
- Analyze momentum
- Identify potential reversals

**Usage**:
```bash
python web3.py rsi <symbol> [options]
```

**Key Features**:
- RSI calculation with customizable period
- Overbought/oversold signal detection
- RSI divergence analysis
- Trading recommendations
- Risk assessment
- Historical RSI values

**Integration**:
- Use for technical analysis
- Combine with MACD for signals
- Support trading decisions

#### MACD Technical Indicator (`web3/`)
Calculate Moving Average Convergence Divergence for trend analysis.

**When to Use**:
- User asks about MACD indicator
- Need trend analysis
- Identify crossovers
- Analyze momentum

**Usage**:
```bash
python web3.py macd <symbol> [options]
```

**Key Features**:
- MACD line calculation
- Signal line calculation
- Histogram analysis
- Golden cross/death cross detection
- Trend strength analysis
- Trading recommendations

**Integration**:
- Use for trend analysis
- Combine with RSI for confirmation
- Support trading decisions

#### CoinMarketCap API (`web3/`)
Access professional cryptocurrency market data.

**When to Use**:
- User asks about cryptocurrency rankings
- Need global market metrics
- Get top cryptocurrencies by market cap
- Query specific cryptocurrency information

**Usage**:
```bash
python web3.py coinmarketcap <command> [options]
```

**Key Features**:
- Top cryptocurrency listings
- Individual token information
- Global market metrics
- Real-time price data
- Market dominance tracking
- Multiple currency conversions

**Integration**:
- Use for crypto market overview
- Get comprehensive crypto data
- Support market research

## AI Agent Workflow

### Step 1: Analyze User Request

Determine which skills are needed based on the user's request:
- Weather queries → Use diary/qweather
- Location/route queries → Use diary/amap
- Travel planning → Use combination of diary/qweather + diary/amap + diary/travel
- Token queries → Use web3
- Wallet queries → Use web3

### Step 2: Execute Skills Sequentially

**For Travel Planning**:
1. Use qweather to fetch weather forecasts for all locations
2. Use amap to calculate routes and find attractions
3. Generate daily itinerary using AI reasoning
4. Create modular JSON files in travel/assets/modules/
5. Provide URL to user for viewing

**For Token/Blockchain Queries**:
1. Use web3 token-query for token information
2. Use web3 wallet-balance for wallet balances
3. Present results in user-friendly format

**For Weather/Map Queries**:
1. Use qweather for weather information
2. Use amap for location and route data
3. Combine results if needed

### Step 3: Present Results

- Provide clear, formatted output
- Include relevant details and context
- Offer follow-up suggestions
- Handle errors gracefully

### Step 4: Iterate and Refine

If user requests changes:
1. Update specific data as needed
2. Re-run specific skills if required
3. Refresh or regenerate outputs
4. Provide updated results

## Skill Integration Patterns

### Pattern 1: Weather + Route (Travel Planning)
```bash
# Get weather for route planning
python diary.py weather 北京
python diary.py weather 上海
python diary.py amap route 北京 上海
```

### Pattern 2: POI + Weather (Attraction Planning)
```bash
# Find attractions with weather context
python diary.py weather 杭州 --forecast 3
python diary.py amap --poi 景点 --city 杭州
```

### Pattern 3: Full Travel Planning
```bash
# Complete travel planning workflow
# 1. Weather for all locations
# 2. Route calculation
# 3. Attraction search
# 4. Itinerary generation
# 5. JSON module creation
# 6. Web interface display
```

### Pattern 4: Blockchain Queries
```bash
# Token and wallet queries
python web3.py token-query ethereum 0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683
python web3.py wallet-balance 0x53A0Fc074E31068CFdBD73B756458546274fEa97
```

### Pattern 5: Financial Market Analysis
```bash
# Market data and technical indicators
python web3.py market-data AAPL --period 1mo
python web3.py rsi AAPL --period 1mo
python web3.py macd AAPL --period 1mo

# Cryptocurrency analysis
python web3.py market-data BTC-USD --interval 1h
python web3.py rsi BTC-USD --interval 1h
python web3.py coinmarketcap listings --limit 10
```

### Pattern 6: Combined Analysis
```bash
# Get market data and calculate indicators
python web3.py market-data ETH-USD --period 3mo
python web3.py rsi ETH-USD --period 3mo
python web3.py macd ETH-USD --period 3mo

# Get crypto rankings and analyze top tokens
python web3.py coinmarketcap listings --limit 5
python web3.py market-data BTC-USD
python web3.py market-data ETH-USD
python web3.py rsi BTC-USD
python web3.py rsi ETH-USD
```

## Standardized Skill Structure

Each skill follows this structure:

```
skill_name/
├── SKILL.md              # AI skill documentation
├── README.md             # User documentation
├── scripts/              # Launch scripts and CLI tools
│   └── skill_name.py    # Main launch script
├── assets/              # Core modules and resources
│   ├── skill_client.py   # API clients
│   └── ...            # Other modules
├── references/          # User documentation
│   └── README.md
└── evals/             # Test cases (optional)
```

### Internationalization (i18n) Structure

**Diary Skills** - i18n files are located in the diary root directory:
```
diary/
├── i18n/
│   ├── __init__.py     # i18n manager
│   ├── common/         # Common translations
│   │   ├── en_us.json
│   │   ├── zh_cn.json
│   │   ├── zh_tw.json
│   │   └── jp.json
│   ├── qweather/       # QWeather-specific translations
│   │   ├── en_us.json
│   │   ├── zh_cn.json
│   │   ├── zh_tw.json
│   │   └── jp.json
│   ├── amap/          # Amap-specific translations
│   │   ├── en_us.json
│   │   ├── zh_cn.json
│   │   ├── zh_tw.json
│   │   └── jp.json
│   └── mastodon/      # Mastodon-specific translations
│       ├── en_us.json
│       ├── zh_cn.json
│       ├── zh_tw.json
│       └── jp.json
└── qweather/
    └── scripts/
        └── weather.py  # Uses diary/i18n
```

**Web3 Skills** - i18n files are located in the assets directory:
```
web3/
├── assets/
│   ├── i18n/
│   │   ├── __init__.py
│   │   ├── en_us.json
│   │   ├── zh_cn.json
│   │   ├── zh_tw.json
│   │   └── jp.json
│   ├── token_query.py
│   └── wallet_balance.py
└── scripts/
    └── web3.py        # Uses web3/assets/i18n
```

**Key Differences**:
- **Diary skills**: Centralized i18n in `diary/i18n/` with module-specific subdirectories
- **Web3 skills**: Self-contained i18n in `web3/assets/i18n/`
- Both approaches are valid and follow the modular design philosophy

## Environment Variables

Required environment variables in `.env` file:
```
QWEATHER_API_KEY=your_qweather_api_key
AMAP_API_KEY=your_amap_api_key
MASTODON_ACCESS_TOKEN=your_mastodon_access_token
```

Optional environment variables:
```
LANG=en_us              # Language preference (zh_cn, en_us, zh_tw, jp)
TRAVEL_PORT=3001        # Travel web server port (default: 3001)
```

## Error Handling

If a skill fails:
1. Check environment variables are set correctly
2. Verify API keys are valid
3. Check network connectivity
4. Review skill-specific error messages
5. Retry with different parameters if needed
6. Provide user-friendly error messages

## Best Practices

1. **Sequential Execution**: Execute skills in logical order (weather → route → attractions)
2. **Data Validation**: Verify API responses before proceeding
3. **Modular Storage**: Store data in appropriate JSON modules
4. **User Feedback**: Provide progress updates during execution
5. **Error Recovery**: Handle failures gracefully and provide alternatives
6. **Language Support**: Respect user's language preference
7. **Context Awareness**: Use previous context to improve responses

## Multi-language Support

All skills support multiple languages:
- `zh_cn` - Simplified Chinese (default)
- `en_us` - English
- `zh_tw` - Traditional Chinese
- `jp` - Japanese

Set language via environment variable:
```bash
export LANG=en_us
```

## Getting Help

Each skill provides built-in help:
```bash
python diary.py weather --help
python diary.py amap --help
python diary.py travel
python web3.py
```

For detailed AI integration instructions, see individual SKILL.md files in each skill directory.

## Limitations

- Skills require valid API keys
- Some features depend on external API availability
- Travel planning requires manual JSON file creation
- No real-time data synchronization between skills
- Blockchain queries depend on OKX API availability

## Skill-Specific Documentation

For detailed information about each skill, refer to their individual SKILL.md files:

### Diary Skills
- **[diary/SKILL.md](diary/SKILL.md)** - Diary skills AI documentation (overview of all diary skills)
- **[diary/qweather/SKILL.md](diary/qweather/SKILL.md)** - QWeather skill documentation
- **[diary/amap/SKILL.md](diary/amap/SKILL.md)** - Amap skill documentation
- **[diary/travel/SKILL.md](diary/travel/SKILL.md)** - Travel skill documentation
- **[diary/mastodon/SKILL.md](diary/mastodon/SKILL.md)** - Mastodon skill documentation
- **[diary/bluesky/SKILL.md](diary/bluesky/SKILL.md)** - Bluesky skill documentation
- **[diary/telegram/SKILL.md](diary/telegram/SKILL.md)** - Telegram Bot skill documentation (TTS, STT, messaging)
- **[diary/ai_aggregator/SKILL.md](diary/ai_aggregator/SKILL.md)** - AI Aggregator skill documentation
- **[diary/rss/SKILL.md](diary/rss/SKILL.md)** - RSS Feed Reader skill documentation

### Web3 Skills
- **[web3/SKILL.md](web3/SKILL.md)** - Web3 skills AI documentation (overview of all web3 skills)

### Quick Reference
- **QWeather**: `diary/qweather/SKILL.md`
- **Amap**: `diary/amap/SKILL.md`
- **Travel**: `diary/travel/SKILL.md`
- **Token Query**: `web3/SKILL.md` (see Token Query section)
- **Wallet Balance**: `web3/SKILL.md` (see Wallet Balance section)
