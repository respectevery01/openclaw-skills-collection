#!/usr/bin/env python3
import os
import sys
import requests
import json
from datetime import datetime
from typing import Dict, Optional

try:
    from dotenv import load_dotenv
    # Find .env file by going up from scripts directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)), '.env')
    if not os.path.exists(env_path):
        # Try loading from parent directory (when running from project root)
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))), '.env')
    load_dotenv(env_path)
except ImportError:
    pass

# AQI levels mapping
AQI_LEVELS = {
    '1': 'Excellent', '2': 'Good', '3': 'Lightly Polluted',
    '4': 'Moderately Polluted', '5': 'Heavily Polluted', '6': 'Severely Polluted'
}

# Add i18n support
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from i18n import i18n, _

class QWeatherClient:
    def __init__(self):
        self.api_key = os.getenv('QWEATHER_API_KEY')
        self.api_url = os.getenv('QWEATHER_API_URL')
        self.project_id = os.getenv('QWEATHER_PROJECT_ID')
        self.lang = 'en'  # Default to English
        
        if not all([self.api_key, self.api_url]):
            raise ValueError("Missing required QWeather configuration. Please check QWEATHER_API_KEY and QWEATHER_API_URL in .env file")
    
    def set_language(self, lang):
        """Set language for API responses"""
        # Supported languages according to QWeather API documentation
        supported_langs = ['zh', 'en', 'ja', 'zh-hant']
        if lang in supported_langs:
            self.lang = lang
            return True
        return False
    
    def _make_request(self, endpoint: str, params: Dict = None) -> Dict:
        """Send API request"""
        url = f"{self.api_url}{endpoint}"
        
        headers = {
            'X-QW-Api-Key': self.api_key
        }
        
        if not params:
            params = {}
        # Only add language parameter if not already set
        if 'lang' not in params:
            params['lang'] = self.lang  # Add language parameter
        
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Check response content
            if not response.content:
                print("API returned empty response. Please check if API URL is correct")
                return {}
                
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return {}
    
    def get_current_weather(self, location: str, lang: str = 'en') -> Dict:
        """Get current weather"""
        endpoint = "/v7/weather/now"
        params = {
            'location': location,
            'lang': lang
        }
        
        result = self._make_request(endpoint, params)
        return result
    
    def get_3day_forecast(self, location: str, lang: str = 'en') -> Dict:
        """Get 3-day weather forecast"""
        endpoint = "/v7/weather/3d"
        params = {
            'location': location,
            'lang': lang
        }
        
        result = self._make_request(endpoint, params)
        return result
    
    def get_7day_forecast(self, location: str, lang: str = 'en') -> Dict:
        """Get 7-day weather forecast"""
        endpoint = "/v7/weather/7d"
        params = {
            'location': location,
            'lang': lang
        }
        
        result = self._make_request(endpoint, params)
        return result
    
    def get_air_quality(self, location: str, lang: str = 'en') -> Dict:
        """Get air quality information"""
        endpoint = "/v7/air/now"
        params = {
            'location': location,
            'lang': lang
        }
        
        result = self._make_request(endpoint, params)
        return result
    
    def get_weather_indices(self, location: str, type: str = '0', lang: str = 'en') -> Dict:
        """Get weather life indices"""
        endpoint = "/v7/indices/1d"
        params = {
            'location': location,
            'type': type
        }
        
        # Use English as fallback for Japanese (API limitation)
        if lang == 'ja':
            params['lang'] = 'en'
        else:
            params['lang'] = lang
        
        result = self._make_request(endpoint, params)
        return result
    
    def search_location(self, keyword: str, adm: str = '', range: str = 'cn', number: int = 10) -> Dict:
        """Search for cities/regions"""
        endpoint = "/geo/v2/city/lookup"
        params = {
            'location': keyword,
            'adm': adm,
            'range': range,
            'number': number
        }
        
        result = self._make_request(endpoint, params)
        return result
    
    def search_global(self, keyword: str, number: int = 10) -> Dict:
        """Search global cities"""
        return self.search_location(keyword, range='', number=number)


def format_weather_data(weather_data: Dict, lang: str = 'en_us') -> str:
    """Format weather data"""
    if not weather_data or weather_data.get('code') != '200':
        return "Failed to get weather data"
    
    i18n.set_language(lang)
    
    now_data = weather_data.get('now', {})
    result = []
    
    result.append(f"{_('weather.title')}")
    result.append(f"{_('weather.temp')}: {now_data.get('temp', 'N/A')}°C")
    result.append(f"{_('weather.feels_like')}: {now_data.get('feelsLike', 'N/A')}°C")
    result.append(f"{_('weather.text')}: {now_data.get('text', 'N/A')}")
    result.append(f"{_('weather.wind_dir')}: {now_data.get('windDir', 'N/A')}")
    result.append(f"{_('weather.wind_scale')}: {now_data.get('windScale', 'N/A')}")
    result.append(f"{_('weather.humidity')}: {now_data.get('humidity', 'N/A')}%")
    
    visibility = now_data.get('vis', 'N/A')
    if lang in ['zh_cn', 'zh_tw']:
        result.append(f"{_('weather.visibility')}: {visibility}公里")
    else:
        result.append(f"{_('weather.visibility')}: {visibility} km")
    
    return '\n'.join(result)


def format_forecast_data(forecast_data: Dict, days: int = 3) -> str:
    """Format forecast data"""
    if not forecast_data or forecast_data.get('code') != '200':
        return "Failed to get forecast data"
    
    daily_data = forecast_data.get('daily', [])[:days]
    
    result = []
    result.append(f"{_('forecast.title').format(days=days)}")
    
    for day in daily_data:
        date = datetime.strptime(day['fxDate'], '%Y-%m-%d').strftime('%m/%d')
        result.append(f"\n{date}:")
        result.append(f"  {_('forecast.daytime').format(textDay=day['textDay'], tempMin=day['tempMin'], tempMax=day['tempMax'])}")
        result.append(f"  {_('forecast.night').format(textNight=day['textNight'])}")
        result.append(f"  {_('forecast.wind').format(windDirDay=day['windDirDay'], windScaleDay=day['windScaleDay'])}")
    
    return '\n'.join(result)


def format_air_quality_data(air_data: Dict) -> str:
    """Format air quality data"""
    if not air_data or air_data.get('code') != '200':
        return "Failed to get air quality data"
    
    now_data = air_data.get('now', {})
    
    result = []
    result.append(f"{_('air.title')}")
    result.append(f"{_('air.aqi')}: {now_data.get('aqi', 'N/A')}")
    result.append(f"{_('air.level')}: {AQI_LEVELS.get(str(now_data.get('category', '')), 'N/A')}")
    result.append(f"{_('air.primary')}: {now_data.get('primary', 'N/A')}")
    result.append(f"{_('air.pm2p5')}: {now_data.get('pm2p5', 'N/A')} μg/m³")
    result.append(f"{_('air.pm10')}: {now_data.get('pm10', 'N/A')} μg/m³")
    
    return '\n'.join(result)


def main():
    """Main function - Demo script usage"""
    try:
        client = QWeatherClient()
        
        print("QWeather Query Tool")
        print("=" * 50)
        
        # Search for Beijing
        search_result = client.search_location("Beijing")
        if search_result.get('code') == '200' and search_result.get('location'):
            location_id = search_result['location'][0]['id']
            location_name = search_result['location'][0]['name']
            
            print(f"Query Location: {location_name} (ID: {location_id})")
            print()
            
            # Get current weather
            current_weather = client.get_current_weather(location_id)
            print(format_weather_data(current_weather))
            print()
            
            # Get 3-day forecast
            forecast_3d = client.get_3day_forecast(location_id)
            print(format_forecast_data(forecast_3d, 3))
            print()
            
            # Get air quality
            air_quality = client.get_air_quality(location_id)
            print(format_air_quality_data(air_quality))
            print()
            
            # Get weather indices (use English as fallback for Japanese)
            indices = client.get_weather_indices(location_id, lang='en')
            if indices.get('code') == '200' and indices.get('daily'):
                print(f"{_('indices.title')}")
                for index in indices['daily'][:5]:  # Show first 5 indices
                    print(f"  {index['name']}: {index['category']} - {index['text']}")
            else:
                print(f"{_('common.no_results')}")
                
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()