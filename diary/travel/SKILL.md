---
name: travel
description: Render travel plan JSON files with a modular web interface for displaying comprehensive travel information including routes, weather, and attractions
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# Travel Planning Skill

## Quick Start

This skill provides a web interface for rendering and displaying modular travel plan JSON files. The skill itself does not generate travel data - it only renders pre-generated JSON modules created by AI agents using the qweather and amap skills.

## Basic Usage

### Start Travel Planning Server
```bash
python diary.py travel start
```
This starts a web server on port 3001 (configurable via TRAVEL_PORT environment variable).

### Access Web Interface
Open your browser and navigate to:
```
http://localhost:3001
```

### View Existing Travel Plans
To view a specific travel plan:
```
http://localhost:3001?plan=modules/example
```

To view the latest travel plan:
```
http://localhost:3001
```

## API Endpoints

### 1. Read Travel Plan
```
GET /api/travel-plan/:filename
```

**Parameters**:
- `filename` (required): Travel plan filename without .json extension (e.g., "modules/example")

**Response**: Complete travel plan JSON data.

### 2. List Available Travel Plans
```
GET /api/travel-plans
```

**Response**: Array of available travel plans with metadata.

**Response Example**:
```json
[
  {
    "filename": "modules/example",
    "title": "北京-武汉-南京-上海 7天旅游规划",
    "created_date": "2026-03-08",
    "origin": "北京",
    "destination": "上海",
    "days": 7
  }
]
```

### 3. Read Modular Travel Plan
```
GET /api/travel-plan/modules/:plan_name
```

**Parameters**:
- `plan_name` (required): Travel plan name (e.g., "example")

**Response**: Complete travel plan JSON data by merging all module files.

## AI Usage Guidelines

### When to Use This Skill

Use this skill when:
- You need to display a travel plan in a web interface
- You have generated modular travel plan JSON files using qweather and amap skills
- You want to provide a user-friendly visualization of travel data

### OpenClaw Integration Workflow

This skill is designed to work with openclaw's skill system. The workflow is:

#### Step 1: Generate Travel Data Using Other Skills

When openclaw receives a travel planning request, it should:

1. **Use the qweather skill** to fetch weather forecasts:
   ```bash
   python diary.py weather 北京 --forecast 7
   python diary.py weather 武汉 --forecast 7
   python diary.py weather 上海 --forecast 7
   ```

2. **Use the amap skill** to calculate routes and search attractions:
   ```bash
   python diary.py amap route 北京 上海 武汉
   python diary.py amap --poi 景点 --city 北京
   python diary.py amap --poi 景点 --city 武汉
   python diary.py amap --poi 景点 --city 上海
   ```

3. **Generate daily itinerary** using AI reasoning:
   - Create realistic daily schedules with time slots
   - Match activities with weather conditions
   - Include travel time between locations
   - Balance activities across all days

#### Step 2: Create Modular Travel Plan JSON Files

OpenClaw should create modular JSON files in `diary/travel/assets/modules/{plan_name}/`:

**Directory Structure**:
```
diary/travel/assets/modules/
├── example/
│   ├── metadata.json
│   ├── trip-info.json
│   ├── route.json
│   ├── weather.json
│   ├── attractions.json
│   ├── itinerary.json
│   └── summary.json
```

**Module File Examples**:

**metadata.json**:
```json
{
  "created_date": "2026-03-08",
  "title": "北京-武汉-上海 7天旅游规划",
  "description": "从北京到上海，途径武汉的7天旅游计划"
}
```

**trip-info.json**:
```json
{
  "origin": "北京",
  "destination": "上海",
  "waypoints": ["武汉"],
  "total_days": 7,
  "travel_mode": "driving"
}
```

**route.json**:
```json
{
  "total_distance": "1142.5",
  "total_distance_unit": "km",
  "total_time": 40097,
  "total_time_formatted": "11h 8m",
  "segments": [
    {
      "from": "北京",
      "to": "武汉",
      "distance": "1152.3",
      "distance_unit": "km",
      "time": 20048,
      "time_formatted": "5h 34m"
    },
    {
      "from": "武汉",
      "to": "上海",
      "distance": "823.6",
      "distance_unit": "km",
      "time": 31107,
      "time_formatted": "8h 37m"
    }
  ]
}
```

**weather.json**:
```json
{
  "北京": {
    "city_id": "101010100",
    "city_name": "北京",
    "forecast": [
      {
        "date": "2026-03-08",
        "temp_min": 7,
        "temp_max": 16,
        "condition": "Sunny",
        "wind_direction": "N",
        "wind_scale": "1-3"
      }
    ],
    "average_temp": 12.0,
    "weather_conditions": ["Sunny", "Cloudy"]
  },
  "武汉": {
    "city_id": "101200101",
    "city_name": "武汉",
    "forecast": [...],
    "average_temp": 11.5,
    "weather_conditions": ["Sunny", "Cloudy"]
  },
  "上海": {
    "city_id": "101020100",
    "city_name": "上海",
    "forecast": [...],
    "average_temp": 10.5,
    "weather_conditions": ["Sunny", "Cloudy"]
  }
}
```

**attractions.json**:
```json
{
  "北京": [
    {
      "name": "故宫博物院",
      "address": "景山前街4号",
      "coordinates": "116.397026,39.918058",
      "category": "景点",
      "description": "景点",
      "recommended_visit_time": "1-2小时"
    }
  ],
  "武汉": [...],
  "上海": [...]
}
```

**itinerary.json**:
```json
[
  {
    "day": 1,
    "date": "2026-03-08",
    "location": "北京",
    "activities": [
      {
        "time": "上午",
        "activity": "故宫博物院",
        "type": "景点游览",
        "weather": "Sunny 7°C ~ 16°C"
      },
      {
        "time": "下午",
        "activity": "天坛公园",
        "type": "景点游览",
        "weather": "Sunny 7°C ~ 16°C"
      },
      {
        "time": "晚上",
        "activity": "王府井大街",
        "type": "美食",
        "weather": "Sunny 7°C ~ 16°C"
      }
    ],
    "weather_summary": "晴天，7-16°C，北风1-3级"
  }
]
```

**summary.json**:
```json
{
  "total_locations": 3,
  "total_attractions": 12,
  "average_temperature": 11.3,
  "weather_conditions": ["Sunny", "Cloudy"],
  "total_distance": 1142.5,
  "total_time": "11h 8m",
  "recommendations": [
    "建议在晴天进行户外景点游览",
    "准备轻薄外套，早晚温差较大",
    "每个城市建议停留2-3天",
    "提前预订酒店和门票"
  ]
}
```

#### Step 3: Provide URL to User

After generating the modular JSON files, openclaw should provide the user with a URL to view the travel plan:

```
Your travel plan has been generated and saved as `modules/example`.

You can view it at: http://localhost:3001?plan=modules/example
```

### Example OpenClaw Workflow

**User Request**: "Plan a trip from Beijing to Shanghai via Wuhan for 7 days"

**OpenClaw Response**:
```
I'll help you plan a 7-day trip from Beijing to Shanghai via Wuhan. Let me gather the necessary information using the available skills.

Step 1: Fetching weather forecasts for all locations...
[Call qweather skill for Beijing, Wuhan, and Shanghai]

Step 2: Calculating optimal route...
[Call amap skill for route planning]

Step 3: Finding attractions at each destination...
[Call amap skill for POI search]

Step 4: Generating daily itinerary...
[Use AI reasoning to create detailed schedule]

Step 5: Creating modular travel plan JSON files...
[Save to diary/travel/assets/modules/example/]

✅ Your travel plan is ready!

📍 **Route Overview**:
- Total Distance: ~1,142 km
- Estimated Time: ~11 hours
- Stops: Beijing → Wuhan → Shanghai

🌤️ **Weather Forecast**:
[Display weather summary]

🎯 **Recommended Attractions**:
[Display attraction summary]

📅 **Daily Itinerary**:
[Display itinerary summary]

You can view the complete travel plan with all details at:
http://localhost:3001?plan=modules/example

The plan includes:
- Detailed route information with segments
- 7-day weather forecasts for all locations
- Recommended attractions with addresses
- Day-by-day itinerary with activities
- Travel tips and recommendations
```

## Modular JSON Structure

The travel plan uses a modular structure with separate JSON files for each component:

### metadata.json
- `created_date`: Date when the plan was created (YYYY-MM-DD)
- `title`: Human-readable title for the travel plan
- `description`: Brief description of the trip

### trip-info.json
- `origin`: Starting city name
- `destination`: Final destination city name
- `waypoints`: Array of intermediate cities (optional)
- `total_days`: Number of days for the trip
- `travel_mode`: Mode of transportation (e.g., "driving")

### route.json
- `total_distance`: Total distance in km
- `total_distance_unit`: Distance unit (e.g., "km")
- `total_time`: Total time in seconds
- `total_time_formatted`: Formatted time string (e.g., "11h 8m")
- `segments`: Array of route segments with from, to, distance, time

### weather.json
Object with city names as keys, each containing:
- `city_id`: QWeather city ID
- `city_name`: City name
- `forecast`: Array of daily weather forecasts
- `average_temp`: Average temperature across all days
- `weather_conditions`: Array of unique weather conditions

### attractions.json
Object with city names as keys, each containing an array of attractions:
- `name`: Attraction name
- `address`: Physical address
- `coordinates`: GPS coordinates (longitude,latitude)
- `category`: Type of attraction
- `description`: Brief description
- `recommended_visit_time`: Suggested visit duration

### itinerary.json
Array of daily plans, each containing:
- `day`: Day number (1, 2, 3, ...)
- `date`: Date (YYYY-MM-DD)
- `location`: City name for that day
- `activities`: Array of activities with time, activity name, type, weather
- `weather_summary`: Brief weather summary for the day

### summary.json
- `total_locations`: Number of unique locations
- `total_attractions`: Total number of attractions
- `average_temperature`: Average temperature across all locations
- `weather_conditions`: Array of unique weather conditions
- `total_distance`: Total trip distance
- `total_time`: Formatted total time
- `recommendations`: Array of travel tips

## Dependencies

- Node.js 14+
- npm
- Environment variable: TRAVEL_PORT (optional, defaults to 3001)

## Error Handling

### Directory Not Found
```
Error: Travel plan directory not found
```
The specified travel plan directory does not exist in the assets/modules directory.

### Invalid JSON
```
Error: Failed to read travel plan module
```
One of the JSON module files is corrupted or has invalid syntax.

### Missing Module
```
Error: Missing required module: {module_name}
```
A required module file is missing from the travel plan directory.

## Web Interface Features

- **Responsive Design**: Works on desktop and mobile devices
- **Automatic Loading**: Loads the latest travel plan by default
- **Plan Selection**: View specific plans via URL parameter
- **Visual Display**: Weather cards, route segments, attraction lists
- **Daily Itinerary**: Day-by-day schedule with activities
- **Summary Statistics**: Trip overview with key metrics
- **Modular Rendering**: Dynamically merges module files for display

## Best Practices

1. **Directory Naming**: Use descriptive names for plan directories (e.g., "example", "beijing-shanghai")
2. **Date Format**: Use ISO 8601 format (YYYY-MM-DD) for dates
3. **Language**: Use Chinese for city names and descriptions
4. **Validation**: Ensure all module JSON files are valid and complete
5. **Reference**: Keep the example module as a reference template
6. **Modularity**: Keep each module focused on its specific data type

## Limitations

- **No Data Generation**: This skill only renders pre-generated JSON modules
- **No API Integration**: Does not call external APIs directly
- **Static Display**: Does not support real-time updates
- **File-Based**: Requires JSON module files to be stored in the assets/modules directory
- **AI-Dependent**: Relies on AI agents to generate travel data using other skills
