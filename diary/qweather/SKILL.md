---
name: qweather
description: Query weather information, forecasts, air quality, and weather indices using QWeather API
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# QWeather Skill

## Quick Start

This skill provides weather data through the QWeather API. Use it when users need current weather, forecasts, air quality, or weather-related recommendations.

## Basic Usage

### Current Weather
```bash
python weather.py "{city}" --lang {language}
```
- `city`: City name (Chinese recommended) or city ID
- `language`: zh_cn, en_us, zh_tw, jp (default: en_us)

### Weather Forecast
```bash
python weather.py "{city}" --forecast {days} --lang {language}
```
- `days`: 3 or 7 days

### Air Quality
```bash
python weather.py "{city}" --air --lang {language}
```

### Weather Indices
```bash
python weather.py "{city}" --forecast {days} --lang {language}
```
Returns lifestyle recommendations (sports, car wash, dressing, fishing, UV)

### City Search
```bash
python weather.py --search "{city_name}" --global-search --lang {language}
```
Use `--global-search` for international cities

### Simple Weather
```bash
python weather.py "{city}" --simple --lang {language}
```
Basic current weather only

## Language Matching

Match language to user's preference:
- Chinese: `--lang zh_cn`
- English: `--lang en_us`
- Traditional Chinese: `--lang zh_tw`
- Japanese: `--lang jp` (weather indices will be in English - API limitation)

## Error Handling

### Missing API Key
```
Missing QWEATHER_API_KEY in .env file
```
Inform user they need to configure QWeather API credentials.

### City Not Found
- Suggest using `--search` to find correct city ID
- Try alternative spellings
- Use `--global-search` for international cities

### API Errors
Check error message and provide user-friendly explanation. Common issues:
- Invalid parameters
- Rate limits exceeded
- Service unavailable

## Best Practices

1. **Use Chinese city names** for best accuracy (e.g., "北京" not "Beijing")
2. **Use city IDs** when available for better precision
3. **Enable global search** for international locations
4. **Default shows complete info** - use `--simple` for basic data only
5. **Non-Chinese languages** use metric units (km instead of 公里)

## Response Format

### Current Weather
```
Temperature: 6°C
Feels Like: 1°C
Weather Condition: Haze
Wind Direction: S
Wind Scale: 2
Humidity: 46%
Visibility: 10 km
```

### Forecast
```
03/08:
  Daytime: Sunny -1°C ~ 13°C
  Night: Clear
  Wind: N 1-3 levels
```

### Air Quality
```
AQI Index: 88
Air Quality Level: Good
Primary Pollutant: PM2.5
PM2.5: 65 μg/m³
PM10: 87 μg/m³
```

## Common Scenarios

### Daily Weather Check
User wants current weather for their location.
```bash
python weather.py "{user_city}" --lang {user_language}
```
Present temperature, conditions, and activity suggestions.

### Trip Planning
User needs weather forecast for destination.
```bash
python weather.py "{destination}" --forecast 7 --lang {user_language}
```
Provide multi-day forecast and highlight concerning patterns.

### Health & Safety
User wants air quality for outdoor activities.
```bash
python weather.py "{city}" --air --lang {user_language}
```
Explain AQI level, health implications, and recommendations.

### Activity Planning
User wants to know if conditions are good for outdoor activities.
```bash
python weather.py "{city}" --forecast 3 --lang {user_language}
```
Provide sports, fishing, UV, and other lifestyle recommendations.

### International Location
User wants weather for city outside China.
```bash
# First find city ID
python weather.py --search "{city}" --global-search --lang {user_language}

# Then get weather
python weather.py "{city_id}" --lang {user_language}
```

## Limitations

- **Rate limits** apply (check QWeather documentation)
- **Free tier** has request limitations
- **Weather indices** only available in Chinese and English (Japanese uses English fallback)
- **Forecast accuracy** decreases for longer timeframes
- **Geographic coverage** varies by region

## Dependencies

- Python 3.7+
- requests
- python-dotenv
- QWeather API key (set in .env file as QWEATHER_API_KEY)
