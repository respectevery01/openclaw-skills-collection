# Travel Planning Skill

A comprehensive travel planning tool that integrates weather forecasts, route planning, and attraction recommendations.

## Features

- **Route Planning**: Calculate driving routes with distance, duration, and toll information
- **Weather Forecasts**: Get multi-day weather predictions for all destinations
- **Attraction Recommendations**: Discover popular scenic spots and POIs
- **Multi-stop Trips**: Support for waypoints and complex itineraries
- **Modern Web Interface**: Beautiful, responsive design with real-time updates

## Quick Start

1. Install dependencies:
```bash
cd diary/travel
npm install
```

2. Start the server:
```bash
npm start
```

Or use the launch script from the diary directory:
```bash
python travel.py
```

3. Open your browser:
```
http://localhost:3001
```

## Usage

### Web Interface

1. Enter your starting point (出发地)
2. Add optional waypoints (途经地)
3. Enter your destination (目的地)
4. Select trip duration (旅行天数)
5. Choose language preference (语言)
6. Click "生成旅行计划" to generate your travel plan

### API Endpoint

```bash
GET /api/travel-plan?start={origin}&end={destination}&waypoints={waypoints}&days={days}&lang={language}
```

## Requirements

- Node.js 14+
- npm
- QWeather API key
- Amap API key

## Configuration

Set the following environment variables in your `.env` file:

```
QWEATHER_API_KEY=your_qweather_api_key
QWEATHER_API_URL=https://devapi.qweather.com/v7
AMAP_API_KEY=your_amap_api_key
TRAVEL_PORT=3001
```

## Project Structure

```
travel/
├── SKILL.md              # Skill documentation
├── package.json           # Node.js dependencies
├── scripts/              # Backend code
│   └── server.js        # Express server
├── public/              # Frontend files
│   ├── index.html       # Main HTML page
│   ├── styles.css       # Styling
│   └── app.js          # Frontend logic
└── references/          # Documentation
    └── README.md       # This file
```

## API Integration

### QWeather API
- Weather forecasts (3-day and 7-day)
- Temperature, conditions, and wind data
- Multi-location support

### Amap API
- Geocoding (address to coordinates)
- Route planning with waypoints
- POI search for attractions
- Distance and time calculations

## Example

Plan a trip from Beijing to Shanghai via Wuhan:

1. Start: 北京
2. Waypoints: 武汉
3. End: 上海
4. Days: 7

The tool will provide:
- Complete driving route with distance and time
- 7-day weather forecasts for all three cities
- Recommended attractions in each location

## Troubleshooting

### Server won't start
- Ensure Node.js is installed: `node --version`
- Check that dependencies are installed: `npm install`
- Verify port 3001 is not in use

### API errors
- Check that API keys are set in `.env` file
- Verify API keys are valid and active
- Check internet connection

### Weather not loading
- Verify QWEATHER_API_KEY is correct
- Check QWeather API service status

### Route not found
- Ensure city names are in Chinese
- Verify locations are valid and accessible
- Check Amap API service status

## License

This project is licensed under the MIT License - see the [LICENSE](../../../../LICENSE) file for details.
