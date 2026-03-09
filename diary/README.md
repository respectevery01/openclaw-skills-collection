# Diary Tools

A collection of AI-powered tools for weather queries, map services, and travel planning.

## 📋 Overview

Diary provides three main tools:
- **QWeather** - Weather information queries
- **Amap** - Map services and route planning
- **Travel** - Travel planning web interface

## 🚀 Quick Start

### Installation

1. Clone or navigate to the diary directory
2. Install required dependencies:
   ```bash
   pip install python-dotenv requests
   ```
3. Set up environment variables in `.env` file:
   ```
   QWEATHER_API_KEY=your_qweather_api_key
   AMAP_API_KEY=your_amap_api_key
   ```

### Basic Usage

```bash
# Show all available tools
python diary.py

# Query weather
python diary.py weather 北京

# Query map information
python diary.py amap route 北京 上海

# Travel planning
python diary.py travel          # Show usage guide
python diary.py travel start      # Start web server
```

## 🌤️ QWeather Tool

Query weather information including current conditions, forecasts, and air quality.

### Features
- Current weather conditions
- 3-day and 7-day forecasts
- Air quality index
- Global city search
- Multi-language support (Chinese, English, Japanese, Traditional Chinese)

### Examples
```bash
# Current weather
python diary.py weather 北京

# 7-day forecast
python diary.py weather 上海 --forecast 7

# Search city
python diary.py weather --search "San Francisco" --global-search

# Change language
python diary.py weather Tokyo --lang en_us
```

### Help
```bash
python diary.py weather --help
```

## 🗺️ Amap Tool

Query map information including geocoding, POI search, and route planning.

### Features
- Address geocoding (address to coordinates)
- Reverse geocoding (coordinates to address)
- POI search by keywords
- Route planning (driving, walking, transit, cycling)
- Weather queries
- Multi-language support

### Examples
```bash
# Route planning
python diary.py amap route 北京 上海 武汉

# Geocoding
python diary.py amap --geocode "天安门"

# POI search
python diary.py amap --poi 景点 --city 北京

# Reverse geocoding
python diary.py amap --regeocode "116.397428,39.90923"
```

### Help
```bash
python diary.py amap --help
```

## ✈️ Travel Tool

Web interface for displaying modular travel plan JSON files.

### Features
- Web-based travel plan visualization
- Modular JSON structure
- Route and weather display
- Attraction recommendations
- Daily itinerary view

### Usage
```bash
# Show usage guide
python diary.py travel

# Start web server
python diary.py travel start
```

Then open your browser to:
```
http://localhost:3001
```

### How It Works

The travel tool doesn't generate data itself. Instead, it displays travel plans created by AI agents using qweather and amap tools:

1. AI agent uses qweather to fetch weather forecasts
2. AI agent uses amap to calculate routes and find attractions
3. AI agent creates modular JSON files in `travel/assets/modules/`
4. You view the plan in the web interface

### Help
```bash
python diary.py travel
```

## 📁 Directory Structure

```
diary/
├── diary.py              # Main launcher
├── SKILL.md             # AI skill documentation
├── README.md            # This file
├── qweather/           # Weather tool
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── weather.py
│   │   └── weather_cli.py
│   ├── assets/
│   │   ├── qweather_client.py
│   │   └── city_mapping.py
│   └── references/
│       └── README.md
├── amap/              # Map tool
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── amap.py
│   │   └── amap_cli.py
│   ├── assets/
│   │   └── amap_client.py
│   └── references/
│       └── README.md
├── travel/            # Travel tool
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── travel.py
│   │   └── server.js
│   ├── assets/
│   │   └── modules/
│   │       └── example/
│   ├── public/
│   └── references/
│       └── README.md
└── i18n/              # Internationalization
    ├── __init__.py
    ├── common/
    ├── qweather/
    └── amap/
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the diary directory:

```env
QWEATHER_API_KEY=your_qweather_api_key
AMAP_API_KEY=your_amap_api_key
```

### API Keys

- **QWeather API Key**: Get from https://dev.qweather.com/
- **Amap API Key**: Get from https://lbs.amap.com/

## 🌍 Multi-language Support

All tools support multiple languages:
- `zh_cn` - Simplified Chinese (default)
- `en_us` - English
- `zh_tw` - Traditional Chinese
- `jp` - Japanese

Example:
```bash
python diary.py weather London --lang en_us
python diary.py amap --poi attraction --city Tokyo --lang jp
```

## 🤖 AI Agent Integration

These tools are designed to work with AI agents. For detailed integration instructions, see the SKILL.md files in each tool directory.

### Example Workflow

When an AI agent receives a travel planning request:

1. Use qweather to fetch weather forecasts
2. Use amap to calculate routes and find attractions
3. Generate daily itinerary
4. Create modular JSON files
5. Provide URL to user

## 📚 Documentation

- **SKILL.md** - AI agent documentation
- **references/README.md** - User documentation for each tool
- **i18n/** - Translation files

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

## 📝 License

This project is licensed under the GNU General Public License v3 - see the [LICENSE](../LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows existing style conventions
- All tools support multi-language
- Documentation is updated

## 📧 Support

For issues or questions:
1. Check tool-specific help commands
2. Review SKILL.md files
3. Check API documentation for respective services

## 👨‍💻 Author

**Jask**

- **Website**: https://jask.dev
- **GitHub**: https://github.com/respectevery01
- **Twitter**: [@jaskdon](https://twitter.com/jaskdon)
