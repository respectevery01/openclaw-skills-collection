#!/usr/bin/env python3
"""
Diary tools launcher
"""

import os
import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Diary Tools Launcher")
        print()
        print("Usage:")
        print("  python diary.py <tool> [args...]")
        print()
        print("Available tools:")
        print("  weather   - Query weather information")
        print("  amap      - Query map and route information")
        print("  travel    - Travel planning tool")
        print("  mastodon  - Mastodon social media integration")
        print("  bluesky   - Bluesky social media integration")
        print("  telegram  - Telegram bot integration")
        print("  rss       - RSS feed reader")
        print()
        print("Examples:")
        print("  python diary.py weather 北京")
        print("  python diary.py amap route 北京 上海")
        print("  python diary.py travel")
        print("  python diary.py mastodon verify-credentials")
        print("  python diary.py bluesky --profile")
        print("  python diary.py telegram send 123456789 'Hello!'")
        print("  python diary.py rss fetch http://feeds.bbci.co.uk/news/rss.xml")
        print()
        return
    
    tool = sys.argv[1].lower()
    args = sys.argv[2:]
    
    # Get diary directory
    diary_dir = os.path.dirname(os.path.abspath(__file__))
    
    if tool == 'weather':
        script_path = os.path.join(diary_dir, 'qweather', 'scripts', 'weather.py')
        result = subprocess.run([sys.executable, script_path] + args, cwd=diary_dir)
        sys.exit(result.returncode)
    
    elif tool == 'amap':
        script_path = os.path.join(diary_dir, 'amap', 'scripts', 'amap.py')
        result = subprocess.run([sys.executable, script_path] + args, cwd=diary_dir)
        sys.exit(result.returncode)
    
    elif tool == 'travel':
        script_path = os.path.join(diary_dir, 'travel', 'scripts', 'travel.py')
        result = subprocess.run([sys.executable, script_path] + args, cwd=diary_dir)
        sys.exit(result.returncode)
    
    elif tool == 'mastodon':
        script_path = os.path.join(diary_dir, 'mastodon', 'scripts', 'mastodon.py')
        result = subprocess.run([sys.executable, script_path] + args, cwd=diary_dir)
        sys.exit(result.returncode)
    
    elif tool == 'bluesky':
        script_path = os.path.join(diary_dir, 'bluesky', 'scripts', 'bluesky.py')
        result = subprocess.run([sys.executable, script_path] + args, cwd=diary_dir)
        sys.exit(result.returncode)
    
    elif tool == 'telegram':
        script_path = os.path.join(diary_dir, 'telegram', 'scripts', 'telegram.py')
        result = subprocess.run([sys.executable, script_path] + args, cwd=diary_dir)
        sys.exit(result.returncode)
    
    elif tool == 'rss':
        script_path = os.path.join(diary_dir, 'rss', 'scripts', 'rss_cli.py')
        result = subprocess.run([sys.executable, script_path] + args, cwd=diary_dir)
        sys.exit(result.returncode)
    
    else:
        print(f"Unknown tool: {tool}")
        print()
        print("Available tools: weather, amap, travel, mastodon, bluesky, telegram, rss")
        sys.exit(1)

if __name__ == "__main__":
    main()
