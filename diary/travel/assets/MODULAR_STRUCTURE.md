# Modular Travel Plan Structure

## Overview

The travel planning system now supports a modular JSON structure, allowing you to create and manage travel plans using separate, focused JSON files for each component.

## Directory Structure

```
travel/assets/
├── modules/              # Modular JSON files
│   ├── metadata.json      # Plan metadata
│   ├── trip-info.json    # Trip information
│   ├── route.json        # Route details
│   ├── weather.json      # Weather forecasts
│   ├── attractions.json  # Attraction recommendations
│   ├── itinerary.json    # Daily itinerary
│   └── summary.json      # Trip summary
├── example.json         # Complete example plan (legacy)
└── travel-{date}.json  # Generated complete plans
```

## Module Files

### 1. metadata.json
Contains basic information about the travel plan.

```json
{
  "created_date": "2026-03-08",
  "title": "武汉-南京-上海 七天旅游规划",
  "description": "从武汉到上海，途径南京的七天旅游计划"
}
```

### 2. trip-info.json
Contains core trip details.

```json
{
  "origin": "武汉",
  "destination": "上海",
  "waypoints": ["南京"],
  "total_days": 7,
  "travel_mode": "driving"
}
```

### 3. route.json
Contains route information with segments.

```json
{
  "total_distance": 823.6,
  "total_distance_unit": "km",
  "total_time": 31107,
  "total_time_formatted": "8h 37m",
  "segments": [
    {
      "from": "武汉",
      "to": "南京",
      "distance": 523.0,
      "distance_unit": "km",
      "time": 19475,
      "time_formatted": "5h 24m"
    }
  ]
}
```

### 4. weather.json
Contains weather forecasts for all cities.

```json
{
  "武汉": {
    "city_id": "101200101",
    "city_name": "武汉",
    "forecast": [
      {
        "date": "2026-03-08",
        "temp_min": 7,
        "temp_max": 16,
        "condition": "Overcast",
        "wind_direction": "N",
        "wind_scale": "1-3"
      }
    ],
    "average_temp": 12.0,
    "weather_conditions": ["Overcast", "Sunny", "Cloudy"]
  }
}
```

### 5. attractions.json
Contains attraction recommendations for each city.

```json
{
  "武汉": [
    {
      "name": "黄鹤楼",
      "address": "蛇山西山坡特1号",
      "coordinates": "114.302467,30.544649",
      "category": "景点",
      "description": "千古名楼，武汉地标",
      "recommended_visit_time": "2-3小时"
    }
  ]
}
```

### 6. itinerary.json
Contains daily itinerary with activities.

```json
[
  {
    "day": 1,
    "date": "2026-03-08",
    "location": "武汉",
    "activities": [
      {
        "time": "上午",
        "activity": "黄鹤楼",
        "type": "景点游览",
        "weather": "Overcast 7°C ~ 16°C"
      }
    ],
    "weather_summary": "阴天，7-16°C，北风1-3级"
  }
]
```

### 7. summary.json
Contains trip summary statistics and recommendations.

```json
{
  "total_locations": 3,
  "total_attractions": 9,
  "average_temperature": 10.3,
  "weather_conditions": ["Overcast", "Sunny", "Cloudy"],
  "total_distance": 823.6,
  "total_time": "8h 37m",
  "recommendations": [
    "建议在晴天进行户外景点游览",
    "准备轻薄外套，早晚温差较大",
    "每个城市建议停留2-3天",
    "提前预订酒店和门票"
  ]
}
```

## API Endpoints

### Get Modular Travel Plan
```
GET /api/travel-plan/modules/:planName
```

Merges all module files from `assets/modules/` directory and returns a complete travel plan.

**Example**: `http://localhost:3001/api/travel-plan/modules/example`

### Get Complete Travel Plan
```
GET /api/travel-plan/:filename
```

Returns a complete travel plan from a single JSON file.

**Example**: `http://localhost:3001/api/travel-plan/travel-2026-03-08`

### List All Travel Plans
```
GET /api/travel-plans
```

Lists all available travel plans (excludes modules directory and example.json).

## Usage

### For OpenClaw Integration

When generating a travel plan, openclaw should:

1. **Create individual module files** in `assets/modules/`:
   - Use qweather skill to generate weather data → `weather.json`
   - Use amap skill to generate route data → `route.json`
   - Use amap skill to generate attraction data → `attractions.json`
   - Use AI to generate itinerary → `itinerary.json`
   - Create metadata and summary files

2. **Access the merged plan** via:
   ```
   GET /api/travel-plan/modules/example
   ```

3. **Optionally save complete plan** as `travel-{date}.json` for future reference.

### For Direct Access

Users can access the modular plan directly:
```
http://localhost:3001?plan=modules/example
```

## Benefits of Modular Structure

1. **Easier Maintenance**: Each component is in a separate file
2. **Better Organization**: Clear separation of concerns
3. **Flexible Updates**: Update individual modules without affecting others
4. **AI-Friendly**: Easier for AI to generate specific components
5. **Reusability**: Share common modules across different plans
6. **Version Control**: Better tracking of changes to specific components

## Example Workflow

1. User requests: "Plan a trip from Beijing to Shanghai for 5 days"

2. OpenClaw generates modules:
   ```
   assets/modules/
   ├── metadata.json      (AI generated)
   ├── trip-info.json    (User input)
   ├── route.json        (Amap skill)
   ├── weather.json      (QWeather skill)
   ├── attractions.json  (Amap skill)
   ├── itinerary.json    (AI generated)
   └── summary.json      (AI generated)
   ```

3. User accesses: `http://localhost:3001?plan=modules/example`

4. Server merges modules and displays complete travel plan

5. Optionally save as: `travel-2026-03-08.json`

## Validation

All module files are validated when merged. If any module is missing or invalid, the server returns an error.

## Notes

- The `modules/` directory is excluded from the travel plans list
- `example.json` is kept as a reference for the complete structure
- All module files must be valid JSON
- The merge function ensures all required fields are present
