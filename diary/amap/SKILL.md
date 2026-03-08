---
name: amap
description: Access Amap (Gaode Map) API for geocoding, POI search, weather queries, and route planning
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# Amap Skill

## Quick Start

This skill provides location-based services through the Amap (Gaode Map) API. Use it when users need address lookup, business search, weather data, or navigation assistance.

## Basic Usage

### Geocoding (Address to Coordinates)
```bash
python amap.py --geocode "{address}" --lang {language}
```
- `address`: Human-readable address
- `language`: zh_cn, en_us, zh_tw, jp (default: zh_cn)

Returns coordinates, formatted address, and administrative divisions.

### Reverse Geocoding (Coordinates to Address)
```bash
python amap.py --regeocode "{longitude},{latitude}" --lang {language}
```
- `coordinates`: Format "longitude,latitude" (e.g., "116.397463,39.909187")

Returns address components and formatted address.

### POI Search
```bash
python amap.py --poi "{keywords}" --city "{city}" --lang {language}
```
- `keywords`: Search terms (e.g., "咖啡厅", "restaurant", "hospital")
- `city`: Optional - city to limit search scope

Returns list of POIs with names, addresses, and coordinates.

### Weather Query
```bash
python amap.py --weather "{city}" --lang {language}
```
- `city`: City name or adcode

Returns current weather data (temperature, conditions, wind, humidity).

### Route Planning
```bash
python amap.py --direction "{origin_coords}" "{dest_coords}" --lang {language}
```
- `origin`: Starting coordinates "longitude,latitude"
- `destination`: Ending coordinates "longitude,latitude"

Returns distance, duration, and step-by-step directions.

### Raw JSON Output
Add `--raw` flag to any command for complete API response:
```bash
python amap.py --raw --weather "北京"
```

## Language Matching

Match language to user's preference:
- Chinese: `--lang zh_cn`
- English: `--lang en_us`
- Traditional Chinese: `--lang zh_tw`
- Japanese: `--lang jp`

## Error Handling

### Missing API Key
```
Missing AMAP_API_KEY in .env file
```
Inform user they need to configure Amap API credentials.

### No Results Found
- Suggest alternative search terms
- Check spelling
- Try broader search terms
- For POI search, add city parameter

### API Errors
Check error message and provide user-friendly explanation. Common issues:
- Invalid parameters
- Rate limits exceeded
- Service unavailable

## Best Practices

1. **Coordinate format**: Always use "longitude,latitude" (NOT "latitude,longitude")
2. **City names**: Use Chinese for best results (e.g., "北京" not "Beijing")
3. **POI search**: Include city parameter for more accurate results
4. **Rate limiting**: Be mindful of API rate limits
5. **Data validation**: Always check API response status before processing

## Response Format

### Geocoding
```json
{
  "status": "1",
  "geocodes": [{
    "formatted_address": "北京市东城区天安门",
    "location": "116.397463,39.909187",
    "province": "北京市",
    "city": "北京市",
    "district": "东城区"
  }]
}
```

### Weather
```json
{
  "status": "1",
  "lives": [{
    "city": "北京市",
    "weather": "霾",
    "temperature": "6",
    "winddirection": "东南",
    "windpower": "≤3",
    "humidity": "46"
  }]
}
```

### POI Search
```json
{
  "status": "1",
  "count": "406",
  "pois": [{
    "name": "糖房咖啡(什刹海店)",
    "address": "北京城区什刹海街道前海东沿22号3层-4层",
    "location": "116.394115,39.938976"
  }]
}
```

## Common Scenarios

### Location Verification
User wants to verify address and get coordinates.
```bash
python amap.py --geocode "{address}" --lang {user_language}
```
Check if results returned, provide coordinates and formatted address.

### Finding Nearby Services
User needs to find restaurants near a location.
```bash
python amap.py --poi "餐厅" --city "{city}" --lang {user_language}
```
Present top results with addresses and coordinates.

### Travel Planning
User wants weather for trip destination.
```bash
python amap.py --weather "{destination}" --lang {user_language}
```
Provide current conditions and suggest appropriate activities.

### Route Calculation
User needs driving directions between two locations.
```bash
# First get coordinates for both addresses
python amap.py --raw --geocode "{origin_address}"
python amap.py --raw --geocode "{dest_address}"

# Then get route
python amap.py --direction "{origin_coords}" "{dest_coords}" --lang {user_language}
```
Provide distance, duration, and step-by-step directions.

## Limitations

- **Geographic coverage**: Primarily China and surrounding regions
- **International coverage**: Limited
- **Rate limits**: Apply (check Amap documentation)
- **Real-time traffic**: Not included in basic queries
- **Weather data**: Current conditions only (no forecasts in basic query)
- **POI accuracy**: May not be completely up-to-date

## Dependencies

- Python 3.7+
- requests
- python-dotenv
- Amap API key (set in .env file as AMAP_API_KEY)
