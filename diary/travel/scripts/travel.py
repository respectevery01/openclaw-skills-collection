#!/usr/bin/env python3
"""
Travel planning usage guide
"""

import os
import sys
import subprocess
import shutil

def show_usage():
    """Show usage guide"""
    print("=== Travel Planning Tool ===")
    print()
    print("The travel planning tool provides a web interface for creating and viewing travel plans.")
    print()
    print("Usage:")
    print("  python diary.py travel          - Show this usage guide")
    print("  python diary.py travel --help    - Show this usage guide")
    print("  python diary.py travel start      - Start the Node.js server")
    print()
    print("To start the server:")
    print("  1. cd diary/travel")
    print("  2. npm install  # First time only")
    print("  3. npm start")
    print()
    print("Or use:")
    print("  python diary.py travel start")
    print()
    print("Features:")
    print("  - Weather information integration (via QWeather API)")
    print("  - Route planning (via Amap API)")
    print("  - Attraction recommendations")
    print("  - Modular JSON structure for travel plans")
    print("  - AI-powered travel plan generation")
    print()
    print("For AI Agents:")
    print("  1. Generate travel plan data using qweather and amap skills")
    print("  2. Create modular JSON files in travel/assets/modules/:")
    print("     - metadata.json (plan metadata)")
    print("     - trip-info.json (origin, destination, days)")
    print("     - route.json (route segments, distance, time)")
    print("     - weather.json (weather forecasts)")
    print("     - attractions.json (recommended attractions)")
    print("     - itinerary.json (daily activities)")
    print("     - summary.json (statistics and recommendations)")
    print("  3. Access via API: GET /api/travel-plan/modules/example")
    print("  4. View in browser: http://localhost:3001?plan=modules/example")
    print()
    print("Documentation:")
    print("  - SKILL.md: AI skill documentation")
    print("  - references/README.md: User documentation")
    print("  - assets/MODULAR_STRUCTURE.md: JSON structure guide")
    print()
    print("Environment Variables:")
    print("  - QWEATHER_API_KEY: QWeather API key")
    print("  - AMAP_API_KEY: Amap API key")
    print()

def start_server():
    """Start the Node.js server"""
    # Get current directory (scripts directory)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    travel_dir = os.path.dirname(current_dir)
    
    # Check if npm is available
    npm_cmd = 'npm'
    if not shutil.which(npm_cmd):
        # Try to find npm in common locations
        possible_paths = [
            os.path.join(os.environ.get('APPDATA', ''), 'npm', 'npm.cmd'),
            os.path.join(os.environ.get('LOCALAPPDATA', ''), 'npm', 'npm.cmd'),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                npm_cmd = path
                break
        
        if not shutil.which(npm_cmd) and not os.path.exists(npm_cmd):
            print("Error: npm is not installed or not in PATH")
            print("Please install Node.js from https://nodejs.org/")
            sys.exit(1)
    
    # Check if node_modules exists, if not install dependencies
    node_modules_path = os.path.join(travel_dir, 'node_modules')
    if not os.path.exists(node_modules_path):
        print("Installing Node.js dependencies...")
        subprocess.run([npm_cmd, 'install'], cwd=travel_dir, check=True, shell=True)
    
    # Start the Node.js server
    print("Starting travel planning server...")
    print("Open http://localhost:3001 in your browser")
    subprocess.run([npm_cmd, 'start'], cwd=travel_dir, shell=True)

def main():
    if len(sys.argv) < 2:
        show_usage()
        return
    
    command = sys.argv[1].lower()
    
    if command in ['--help', '-h']:
        show_usage()
    elif command == 'start':
        start_server()
    else:
        show_usage()

if __name__ == "__main__":
    main()
