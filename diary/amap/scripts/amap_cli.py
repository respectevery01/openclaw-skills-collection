#!/usr/bin/env python3
"""Amap CLI tool for querying map information"""

import argparse
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from i18n import i18n, _

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets'))
from amap_client import AmapClient

def print_json(data: dict):
    """Print JSON data with indentation"""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def check_result(result: dict, raw: bool = False):
    """Check API result status and print accordingly"""
    if raw:
        print_json(result)
        return result['status'] == '1'
    
    if result['status'] != '1':
        print(f"{_('common.error')}: {result['info']}")
        return False
    
    return True

def check_empty_result(result: dict, data_key: str):
    """Check if result has empty data"""
    if not result.get(data_key) or len(result[data_key]) == 0:
        print("No results found")
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description=_('amap.cli_tool'))
    parser.add_argument('--geocode', help=_('amap.address_to_query'))
    parser.add_argument('--regeocode', help=_('amap.regeocode_coords_to_address'))
    parser.add_argument('--poi', help=_('amap.search_poi_by_keywords'))
    parser.add_argument('--city', help=_('amap.city_for_weather'))
    parser.add_argument('--weather', help=_('amap.get_weather_info'))
    parser.add_argument('--direction', nargs=2, help=_('amap.travel_mode'))
    parser.add_argument('--raw', action='store_true', help=_('amap.show_raw_json'))
    parser.add_argument('--lang', choices=['zh_cn', 'en_us', 'zh_tw', 'jp'], default='zh_cn', help=_('common.language_selection_default_zh_cn'))
    
    args = parser.parse_args()
    
    i18n.set_language(args.lang)
    
    try:
        client = AmapClient()
        
        if args.geocode:
            result = client.geocode(args.geocode)
            if check_result(result, args.raw) and not args.raw:
                for geocode in result['geocodes']:
                    print(f"{_('amap.address')}: {geocode['formatted_address']}")
                    print(f"{_('amap.coordinates')}: {geocode['location']}")
                    print(f"{_('amap.province')}: {geocode['province']}")
                    print(f"{_('amap.city')}: {geocode['city']}")
                    print(f"{_('amap.district')}: {geocode['district']}")
        
        elif args.regeocode:
            result = client.regeocode(args.regeocode)
            if check_result(result, args.raw) and not args.raw:
                regeocode = result['regeocode']
                print(f"{_('amap.address')}: {regeocode['formatted_address']}")
                print(f"{_('amap.province')}: {regeocode['addressComponent']['province']}")
                print(f"{_('amap.city')}: {regeocode['addressComponent']['city']}")
                print(f"{_('amap.district')}: {regeocode['addressComponent']['district']}")
                print(f"{_('amap.township')}: {regeocode['addressComponent']['township']}")
        
        elif args.poi:
            result = client.search_poi(args.poi, args.city)
            if check_result(result, args.raw) and not args.raw:
                print(f"{_('amap.found_pois')}: {result['count']}")
                for poi in result['pois']:
                    print(f"{poi['name']} - {poi['address']} - {poi['location']}")
        
        elif args.weather:
            result = client.get_weather(args.weather)
            if check_result(result, args.raw) and not args.raw:
                if check_empty_result(result, 'lives'):
                    for weather in result['lives']:
                        print(f"{_('amap.city')}: {weather['city']}")
                        print(f"{_('amap.amap_weather')}: {weather['weather']}")
                        print(f"{_('amap.temperature')}: {weather['temperature']}°C")
                        print(f"{_('amap.wind_direction')}: {weather['winddirection']}")
                        print(f"{_('amap.wind_power')}: {weather['windpower']}")
                        print(f"{_('amap.humidity')}: {weather['humidity']}%")
                        print(f"{_('amap.report_time')}: {weather['reporttime']}")
        
        elif args.direction:
            origin, destination = args.direction
            result = client.get_direction(origin, destination)
            if check_result(result, args.raw) and not args.raw:
                route = result['route']
                if 'paths' in route and len(route['paths']) > 0:
                    path = route['paths'][0]
                    distance_m = int(path['distance'])
                    duration_s = int(path['duration'])
                    
                    print(f"{_('amap.distance')}: {distance_m / 1000:.1f} km ({distance_m} meters)")
                    print(f"{_('amap.duration')}: {duration_s // 3600}h {duration_s % 3600 // 60}m ({duration_s} seconds)")
                    print(f"\n{_('amap.detailed_instructions')}:")
                    
                    for i, step in enumerate(path['steps'], 1):
                        step_distance = int(step['distance'])
                        step_duration = int(step['duration'])
                        print(f"{i}. {step['instruction']}")
                        print(f"   {step_distance}m, {step_duration}s")
                else:
                    print("No route found")
        
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"{_('common.error')}: {str(e)}")

if __name__ == "__main__":
    main()