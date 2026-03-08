#!/usr/bin/env python3
"""
Amap API client module
"""

import os
import requests
from dotenv import load_dotenv

class AmapClient:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv('AMAP_API_KEY')
        self.api_url = 'https://restapi.amap.com/v3'
        
        if not self.api_key:
            raise ValueError("Missing AMAP_API_KEY in .env file")
    
    def geocode(self, address: str) -> dict:
        """Geocode address to coordinates"""
        url = f"{self.api_url}/geocode/geo"
        params = {
            'address': address,
            'key': self.api_key,
            'output': 'json'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def regeocode(self, location: str) -> dict:
        """Regeocode coordinates to address"""
        url = f"{self.api_url}/geocode/regeo"
        params = {
            'location': location,
            'key': self.api_key,
            'output': 'json'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def search_poi(self, keywords: str, city: str = None) -> dict:
        """Search POI by keywords"""
        url = f"{self.api_url}/place/text"
        params = {
            'keywords': keywords,
            'key': self.api_key,
            'output': 'json'
        }
        
        if city:
            params['city'] = city
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_weather(self, city: str) -> dict:
        """Get weather information"""
        url = f"{self.api_url}/weather/weatherInfo"
        params = {
            'city': city,
            'key': self.api_key,
            'output': 'json'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_direction(self, origin: str, destination: str) -> dict:
        """Get driving direction"""
        url = f"{self.api_url}/direction/driving"
        params = {
            'origin': origin,
            'destination': destination,
            'key': self.api_key,
            'output': 'json'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()