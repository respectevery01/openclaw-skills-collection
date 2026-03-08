#!/usr/bin/env python3
import os
import sys
import argparse

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

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from i18n import i18n, _

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets'))
from city_mapping import get_city_id, search_city
from qweather_client import QWeatherClient, format_weather_data, format_forecast_data, format_air_quality_data

def get_api_lang(lang: str) -> str:
    """Convert i18n language to API language"""
    lang_map = {
        'zh_cn': 'zh',
        'en_us': 'en',
        'zh_tw': 'zh-hant',
        'jp': 'ja'
    }
    return lang_map.get(lang, 'en')


def search_city_api(client: QWeatherClient, keyword: str):
    """Search for a city by keyword"""
    result = client.search_location(keyword)
    if result.get('code') == '200' and result.get('location'):
        print(_('common.search_results'))
        for i, loc in enumerate(result['location'][:5], 1):
            print(f"{i}. {loc['name']} ({loc['adm2']}, {loc['adm1']}) - ID: {loc['id']}")
        return result['location'][0]['id'] if result['location'] else None
    else:
        print(_('common.no_results'))
        return None


def get_weather_info(client: QWeatherClient, location_id: str, show_all: bool = False, lang: str = 'en_us'):
    """Get weather information"""
    api_lang = get_api_lang(lang)
    
    if show_all:
        # Show all information
        current_weather = client.get_current_weather(location_id)
        print(format_weather_data(current_weather, lang))
        print()
        
        forecast_3d = client.get_3day_forecast(location_id)
        print(format_forecast_data(forecast_3d, 3))
        print()
        
        air_quality = client.get_air_quality(location_id)
        print(format_air_quality_data(air_quality))
        print()
        
        indices = client.get_weather_indices(location_id, lang=api_lang)
        if indices.get('code') == '200' and indices.get('daily'):
            print(f"{_('indices.title')}")
            for index in indices['daily'][:5]:  # Show first 5 indices
                print(f"  {index['name']}: {index['category']} - {index['text']}")
    else:
        # Show only real-time weather
        current_weather = client.get_current_weather(location_id)
        print(format_weather_data(current_weather, lang))


def main():
    parser = argparse.ArgumentParser(description=_('qweather.cli_tool'))
    parser.add_argument('city', nargs='?', help=_('qweather.city_name_example'))
    parser.add_argument('--location-id', help=_('qweather.use_city_id_example'))
    parser.add_argument('--simple', action='store_true', help=_('qweather.display_simple_weather'))
    parser.add_argument('--forecast', type=int, choices=[3, 7], help=_('qweather.show_forecast_3_7_days'))
    parser.add_argument('--air', action='store_true', help=_('qweather.show_air_quality'))
    parser.add_argument('--search', help=_('qweather.search_cities'))
    parser.add_argument('--api-search', action='store_true', help=_('qweather.force_api_search'))
    parser.add_argument('--global-search', action='store_true', help=_('qweather.search_global_cities'))
    parser.add_argument('--range', help=_('qweather.search_range_example'))
    parser.add_argument('--lang', choices=['zh_cn', 'en_us', 'zh_tw', 'jp'], default='en_us', help=_('qweather.language_selection_default_en'))
    
    args = parser.parse_args()
    
    i18n.set_language(args.lang)
    
    try:
        client = QWeatherClient()
        client.set_language(get_api_lang(args.lang))
        
        if args.search:
            # Search mode
            if args.global_search:
                # Global search
                result = client.search_global(args.search)
                if result.get('code') == '200' and result.get('location'):
                    print(f"{_('common.search_results')}")
                    for i, loc in enumerate(result['location'][:10], 1):
                        country = loc.get('country', _('common.unknown_country'))
                        adm1 = loc.get('adm1', _('common.unknown_province'))
                        adm2 = loc.get('adm2', _('common.unknown_city'))
                        print(f"{i}. {loc['name']} ({adm2}, {adm1}, {country}) - ID: {loc['id']}")
                else:
                    print(f"{_('common.no_results').format(keyword=args.search)}")
            elif args.range:
                # Search with specified range
                result = client.search_location(args.search, range=args.range)
                if result.get('code') == '200' and result.get('location'):
                    print(f"{_('common.search_results')}")
                    for i, loc in enumerate(result['location'][:10], 1):
                        adm2 = loc.get('adm2', _('common.unknown_city'))
                        adm1 = loc.get('adm1', _('common.unknown_province'))
                        print(f"{i}. {loc['name']} ({adm2}, {adm1}) - ID: {loc['id']}")
                else:
                    print(f"{_('common.no_results').format(keyword=args.search)}")
            elif args.api_search:
                # Use API search (default China range)
                result = client.search_location(args.search)
                if result.get('code') == '200' and result.get('location'):
                    print(f"{_('common.search_results')}")
                    for i, loc in enumerate(result['location'][:10], 1):
                        print(f"{i}. {loc['name']} ({loc['adm2']}, {loc['adm1']}) - ID: {loc['id']}")
                else:
                    print(f"{_('common.no_results').format(keyword=args.search)}")
            else:
                # Local search
                results = search_city(args.search)
                if results:
                    print(f"{_('common.found_matching_cities').format(count=len(results))}")
                    for name, city_id in results:
                        print(f"  {name}: {city_id}")
                else:
                    print(f"{_('common.no_results').format(keyword=args.search)}")
                    print(f"{_('common.try_api_search')}")
            return
        
        location_id = args.location_id
            
        if not location_id and args.city:
                # First try local mapping
                location_id = get_city_id(args.city)
                
                if location_id:
                    print(i18n.get('common.query_location', name=args.city, id=location_id))
                else:
                    # Try API search
                    print(f"{_('common.city_not_found_locally').format(city=args.city)}")
                    print(f"{_('common.trying_search_api').format(city=args.city)}")
                    result = client.search_location(args.city)
                    if result.get('code') == '200' and result.get('location'):
                        # Show multiple results for selection
                        if len(result['location']) > 1:
                            print(f"{_('common.found_matching_cities').format(count=len(result['location']))}")
                            for i, loc in enumerate(result['location'][:5], 1):
                                print(f"{i}. {loc['name']} ({loc['adm2']}, {loc['adm1']}) - ID: {loc['id']}")
                            print(f"{_('common.use_location_id')}")
                            return
                        else:
                            location_id = result['location'][0]['id']
                            location_name = result['location'][0]['name']
                            print(i18n.get('common.query_location', name=location_name, id=location_id))
                    else:
                        print(f"{_('common.city_not_found').format(city=args.city)}")
                        print(f"{_('common.suggest_city_id')}")
                        print(f"{_('common.common_city_id_examples')}")
                        print("  Beijing: 101010100")
                        print("  Shanghai: 101020100")
                        print("  Guangzhou: 101280101")
                        print("  Shenzhen: 101280601")
                        print("  Chengdu: 101270101")
                        return
            
        if not location_id:
            print(f"{_('common.please_provide_city')}")
            parser.print_help()
            return
        
        # Display corresponding information based on parameters
        if args.forecast:
            forecast_data = client.get_3day_forecast(location_id) if args.forecast == 3 else client.get_7day_forecast(location_id)
            print(format_forecast_data(forecast_data, args.forecast))
        elif args.air:
            air_data = client.get_air_quality(location_id)
            print(format_air_quality_data(air_data))
        elif args.simple:
            # Show only real-time weather
            get_weather_info(client, location_id, show_all=False, lang=args.lang)
        else:
            # Show complete weather information by default
            get_weather_info(client, location_id, show_all=True, lang=args.lang)
            
    except Exception as e:
        print(f"{_('common.error')}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()