---
name: diary
description: A collection of AI-powered tools for weather queries, map services, travel planning, and social media integration with modular architecture
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# Diary Tools

## Overview

Diary is a modular tool collection providing weather information, map services, travel planning, and social media integration. Each tool is designed to work independently or in combination with others.

## Available Tools

### 1. QWeather (weather)
Query weather information including current conditions, forecasts, and air quality.

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

**Common Commands**:
```bash
python diary.py weather 北京
python diary.py weather London --forecast 7 --lang en_us
python diary.py weather --search "San Francisco" --global-search
```

### 2. Amap (amap)
Query map information including geocoding, POI search, and route planning.

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

**Common Commands**:
```bash
python diary.py amap route 北京 上海 武汉
python diary.py amap --geocode "天安门"
python diary.py amap --poi 景点 --city 北京
```

### 3. Travel (travel)
Web interface for displaying modular travel plan JSON files.

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

**Common Commands**:
```bash
python diary.py travel          # Show usage guide
python diary.py travel start      # Start web server
```

### 4. Mastodon (mastodon)
Mastodon social media integration for posting statuses, retrieving timelines, and managing notifications.

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

**Common Commands**:
```bash
python diary.py mastodon verify-credentials
python diary.py mastodon post-status "Hello from OpenClaw!"
python diary.py mastodon get-timeline
python diary.py mastodon get-notifications
python diary.py mastodon upload-media /path/to/image.jpg --description "My photo"
```

### 5. Bluesky (bluesky)
Bluesky social media integration for posting text, images, reading timelines, and searching content.

**Usage**:
```bash
python diary.py bluesky [command] [options]
```

**Key Features**:
- Post text and images to Bluesky
- Retrieve home timeline
- Get profile information
- Search posts and users
- Reply controls (threadgate)
- Multi-language support for posts
- Automatic image processing and optimization

**Common Commands**:
```bash
python diary.py bluesky verify-credentials
python diary.py bluesky post "Hello from OpenClaw!"
python diary.py bluesky get-timeline
python diary.py bluesky get-profile
python diary.py bluesky post --image /path/to/image.jpg --alt "My photo"
```

### 6. Telegram (telegram)
Telegram Bot integration for sending messages, managing channels, text-to-speech, speech-to-text, and file management.

**Usage**:
```bash
python diary.py telegram [command] [options]
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

**Common Commands**:
```bash
python diary.py telegram send <chat_id> <message>
python diary.py telegram send-photo <chat_id> <image_path>
python diary.py telegram send-voice <chat_id> <text> --voice zh-CN-XiaoxiaoNeural
python diary.py telegram transcribe-voice <file_id> --language zh
python diary.py telegram process-voice-updates --transcribe
python diary.py telegram get-updates
python diary.py telegram delete-message <chat_id> <message_id>
```

### 7. AI Aggregator (ai_aggregator)
Intelligent API routing for cost optimization and performance.

**Usage**:
```bash
python diary.py ai_aggregator [command] [options]
```

**Key Features**:
- Automatic API selection based on task requirements
- Cost optimization (prioritizes cost-effective APIs)
- Multi-language support (Chinese and English optimized)
- Task analysis and recommendation
- Support for 7 AI services (DeepSeek, OpenAI, Gemini, Minimax, GLM, Qwen, Claude)

**Common Commands**:
```bash
python diary.py ai_aggregator analyze <task_description>
python diary.py ai_aggregator recommend <task_description>
python diary.py ai_aggregator list-apis
```

### 8. RSS Feed Reader (rss)
RSS feed reader for fetching, searching, and managing RSS feeds from various sources.

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

**Common Commands**:
```bash
python diary.py rss fetch <rss_url>
python diary.py rss latest <rss_url> --count 5
python diary.py rss search <rss_url> <keyword>
python diary.py rss info <rss_url>
python diary.py rss fetch-multiple <url1> <url2> --limit 5
```

## AI Agent Workflow

### Step 1: Understand User Request

Analyze user's request to determine which tools are needed:
- Weather queries → Use qweather
- Location/route queries → Use amap
- Travel planning → Use combination of qweather + amap + travel
- Social media posts → Use mastodon
- RSS feed reading → Use rss
- Combined requests → Use multiple tools in sequence

### Step 2: Execute Tools Sequentially

**For Travel Planning**:
1. Use qweather to fetch weather forecasts for all locations
2. Use amap to calculate routes and find attractions
3. Generate daily itinerary using AI reasoning
4. Create modular JSON files in travel/assets/modules/
5. Provide URL to user for viewing

**Example**:
```bash
# Step 1: Get weather
python diary.py weather 北京 --forecast 7
python diary.py weather 武汉 --forecast 7
python diary.py weather 上海 --forecast 7

# Step 2: Get route and attractions
python diary.py amap route 北京 上海 武汉
python diary.py amap --poi 景点 --city 北京
python diary.py amap --poi 景点 --city 武汉
python diary.py amap --poi 景点 --city 上海

# Step 3: Create modular JSON files
# Save to diary/travel/assets/modules/{plan_name}/
# - metadata.json
# - trip-info.json
# - route.json
# - weather.json
# - attractions.json
# - itinerary.json
# - summary.json

# Step 4: Provide URL
# http://localhost:3001?plan=modules/{plan_name}
```

### Step 3: Iterate and Refine

If user requests changes:
1. Update specific JSON modules as needed
2. Re-run specific tools if required
3. Refresh web interface to view changes

## Tool Integration Patterns

### Pattern 1: Weather + Route
```bash
# Get weather for route planning
python diary.py weather 北京
python diary.py weather 上海
python diary.py amap route 北京 上海
```

### Pattern 2: POI + Weather
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

### Pattern 4: Weather + Social Media
```bash
# Post weather update to Mastodon
weather=$(python diary.py weather 北京)
python diary.py mastodon post-status "$weather"
```

### Pattern 5: Travel + Social Media
```bash
# Share travel plan on Mastodon
python diary.py mastodon post-status "Planning a trip to Shanghai! 🚀"
# Then share the travel plan URL
```

### Pattern 6: Weather + Telegram
```bash
# Send weather alert to Telegram
weather=$(python diary.py weather 北京 --lang zh_cn)
python diary.py telegram send <chat_id> "$weather"
```

### Pattern 7: Voice Response System
```bash
# Create an automated voice response system
# 1. Get user's voice message
python diary.py telegram get-updates

# 2. Transcribe the voice message
python diary.py telegram transcribe-voice <voice_file_id> --language zh

# 3. Process the text with AI
response=$(python diary.py ai_aggregator analyze "$user_message")

# 4. Send voice response
python diary.py telegram send-voice <chat_id> "$response" --voice zh-CN-XiaoxiaoNeural
```

### Pattern 8: Social Media + Telegram
```bash
# Post to Mastodon and notify via Telegram
post_result=$(python diary.py mastodon post-status "Hello from OpenClaw!")
python diary.py telegram send <chat_id> "Posted to Mastodon: $post_result"
```

### Pattern 9: AI Analysis + Telegram
```bash
# Analyze task and send results
analysis=$(python diary.py ai_aggregator analyze "Summarize this text")
python diary.py telegram send <chat_id> "$analysis"
```

## Environment Variables

Required environment variables in `.env` file:
```
# Weather and Map Services
QWEATHER_API_KEY=your_qweather_api_key
AMAP_API_KEY=your_amap_api_key

# Social Media
MASTODON_API_URL=https://mastodon.social
MASTODON_ACCESS_TOKEN=your_mastodon_access_token
MASTODON_CLIENT_ID=your_mastodon_client_id
MASTODON_CLIENT_SECRET=your_mastodon_client_secret

BLUESKY_API_URL=https://bsky.social
BLUESKY_CLIENT_PASSWORD_SECRET=your_bluesky_password
BLUESKY_HANDLE_ID=your_bluesky_handle

# Telegram
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# AI Services (Optional)
OPENAI_API_KEY=your_openai_api_key  # For STT and AI Aggregator
DEEPSEEK_API_KEY=your_deepseek_api_key
GEMINI_API_KEY=your_gemini_api_key
MINIMAX_API_KEY=your_minimax_api_key
GLM_API_KEY=your_glm_api_key
QWEN_API_KEY=your_qwen_api_key
CLAUDE_API_KEY=your_claude_api_key
```

**Note**: RSS Feed Reader doesn't require API keys, but needs `feedparser>=6.0.0` dependency installed.

## Error Handling

If a tool fails:
1. Check environment variables are set correctly
2. Verify API keys are valid
3. Check network connectivity
4. Review tool-specific error messages
5. Retry with different parameters if needed

## Best Practices

1. **Sequential Execution**: Execute tools in logical order (weather → route → attractions)
2. **Data Validation**: Verify API responses before proceeding
3. **Modular Storage**: Store data in appropriate JSON modules
4. **User Feedback**: Provide progress updates during execution
5. **Error Recovery**: Handle failures gracefully and provide alternatives

## Limitations

- Tools require valid API keys
- Some features depend on external API availability
- Travel planning requires manual JSON file creation
- No real-time data synchronization between tools

## Getting Help

Each tool provides built-in help:
```bash
python diary.py weather --help
python diary.py amap --help
python diary.py travel
```
