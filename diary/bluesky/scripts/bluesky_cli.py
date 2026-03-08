#!/usr/bin/env python3
import os
import sys
import argparse
import json

try:
    from dotenv import load_dotenv
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)), '.env')
    if not os.path.exists(env_path):
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))), '.env')
    load_dotenv(env_path)
except ImportError:
    pass

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets'))
from bluesky_client import BlueskyClient


def print_json(data: dict):
    """Print JSON data with indentation"""
    print(json.dumps(data, indent=2, ensure_ascii=False))


def print_post(post: dict):
    """Print post information"""
    author = post.get('author', {})
    record = post.get('record', {})
    
    print(f"@{author.get('handle', 'unknown')} ({author.get('displayName', 'N/A')})")
    print(f"Content: {record.get('text', 'N/A')}")
    print(f"Created: {record.get('createdAt', 'N/A')}")
    print(f"URI: {post.get('uri', 'N/A')}")
    print()


def print_profile(profile: dict):
    """Print profile information"""
    print(f"Handle: @{profile.get('handle', 'unknown')}")
    print(f"Display Name: {profile.get('displayName', 'N/A')}")
    print(f"Bio: {profile.get('description', 'N/A')}")
    print(f"Followers: {profile.get('followersCount', 0)}")
    print(f"Following: {profile.get('followsCount', 0)}")
    print(f"Posts: {profile.get('postsCount', 0)}")
    print()


def main():
    parser = argparse.ArgumentParser(description='Bluesky CLI tool')
    parser.add_argument('--post', help='Post text to Bluesky')
    parser.add_argument('--image', help='Post single image with path')
    parser.add_argument('--images', help='Post multiple images (comma-separated paths)')
    parser.add_argument('--alt', help='Alt text for single image', default='')
    parser.add_argument('--alts', help='Alt texts for multiple images (comma-separated)')
    parser.add_argument('--langs', help='Languages for post (comma-separated, e.g., "en,zh")')
    parser.add_argument('--reply-to', help='Reply controls (nobody/mentions/following/followers or comma-separated)')
    parser.add_argument('--profile', action='store_true', help='Get profile information')
    parser.add_argument('--profile-handle', help='Get profile for specific handle')
    parser.add_argument('--timeline', action='store_true', help='Get timeline')
    parser.add_argument('--limit', type=int, default=20, help='Limit number of results')
    parser.add_argument('--search', help='Search query')
    parser.add_argument('--type', choices=['posts', 'actors'], default='posts', help='Search type')
    parser.add_argument('--api-call', help='Make custom API call (endpoint)')
    parser.add_argument('--method', choices=['GET', 'POST'], default='GET', help='API call method')
    parser.add_argument('--params', help='API call params (JSON string)')
    parser.add_argument('--json-data', help='API call JSON data (JSON string)')
    parser.add_argument('--raw', action='store_true', help='Show raw JSON output')
    
    args = parser.parse_args()
    
    try:
        client = BlueskyClient()
        
        if args.post:
            # Parse languages
            langs = None
            if args.langs:
                langs = [lang.strip() for lang in args.langs.split(',')]
            
            # Parse reply_to
            reply_to = None
            if args.reply_to:
                reply_to = args.reply_to
            
            if args.image:
                # Post single image
                result = client.post_image(args.post, args.image, args.alt, langs, reply_to)
                if args.raw:
                    print_json(result)
                else:
                    print("Post successful!")
                    print(f"URI: {result.get('uri', 'N/A')}")
            
            elif args.images:
                # Post multiple images
                image_paths = [path.strip() for path in args.images.split(',')]
                alt_texts = [alt.strip() for alt in args.alts.split(',')] if args.alts else [''] * len(image_paths)
                
                result = client.post_images(args.post, image_paths, alt_texts, langs, reply_to)
                if args.raw:
                    print_json(result)
                else:
                    print("Post successful!")
                    print(f"URI: {result.get('uri', 'N/A')}")
            
            else:
                # Post text only
                result = client.post_text(args.post, langs, reply_to)
                if args.raw:
                    print_json(result)
                else:
                    print("Post successful!")
                    print(f"URI: {result.get('uri', 'N/A')}")
        
        elif args.profile:
            handle = args.profile_handle if args.profile_handle else None
            result = client.get_profile(handle)
            
            if args.raw:
                print_json(result)
            else:
                print("Profile Information:")
                print()
                print_profile(result)
        
        elif args.timeline:
            result = client.get_timeline(limit=args.limit)
            
            if args.raw:
                print_json(result)
            else:
                feed = result.get('feed', [])
                print(f"Timeline ({len(feed)} posts):")
                print()
                for item in feed:
                    post = item.get('post', {})
                    print_post(post)
        
        elif args.search:
            result = client.search(args.search, search_type=args.type, limit=args.limit)
            
            if args.raw:
                print_json(result)
            else:
                if args.type == 'posts':
                    posts = result.get('posts', [])
                    print(f"Found {len(posts)} posts:")
                    print()
                    for post in posts:
                        print_post(post)
                else:
                    actors = result.get('actors', [])
                    print(f"Found {len(actors)} actors:")
                    print()
                    for actor in actors:
                        print_profile(actor)
        
        elif args.api_call:
            # Parse params
            params = None
            if args.params:
                params = json.loads(args.params)
            
            # Parse JSON data
            json_data = None
            if args.json_data:
                json_data = json.loads(args.json_data)
            
            result = client.api_call(args.api_call, method=args.method, json=json_data, params=params)
            
            if args.raw:
                print_json(result)
            else:
                print("API Call Result:")
                print()
                print_json(result)
        
        else:
            parser.print_help()
            
    except ValueError as e:
        if 'BLUESKY_HANDLE_ID' in str(e) or 'BLUESKY_HANDLE' in str(e) or 'BLUESKY_CLIENT_PASSWORD_SECRET' in str(e) or 'BLUESKY_APP_PASSWORD' in str(e):
            print(f"Error: Missing Bluesky credentials in .env file")
            print("Please set BLUESKY_HANDLE_ID and BLUESKY_CLIENT_PASSWORD_SECRET in your .env file")
        else:
            print(f"Error: {str(e)}")
        sys.exit(1)
    except ImportError as e:
        print(f"Error: {str(e)}")
        print("Please install bsky-bridge: pip install bsky-bridge")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
