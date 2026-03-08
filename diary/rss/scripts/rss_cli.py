#!/usr/bin/env python3
import sys
import os
import argparse
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from diary.rss.assets.rss_client import RSSClient


def main():
    parser = argparse.ArgumentParser(description='RSS Feed Reader Tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Fetch feed command
    fetch_parser = subparsers.add_parser('fetch', help='Fetch RSS feed')
    fetch_parser.add_argument('url', help='RSS feed URL')
    fetch_parser.add_argument('--limit', type=int, help='Limit number of entries')
    fetch_parser.add_argument('--output', help='Output file path (JSON)')
    fetch_parser.add_argument('--format', choices=['json', 'text'], default='text', help='Output format')

    # Fetch multiple feeds command
    multi_parser = subparsers.add_parser('fetch-multiple', help='Fetch multiple RSS feeds')
    multi_parser.add_argument('urls', nargs='+', help='RSS feed URLs')
    multi_parser.add_argument('--limit', type=int, help='Limit number of entries per feed')
    multi_parser.add_argument('--output', help='Output file path (JSON)')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search entries in RSS feed')
    search_parser.add_argument('url', help='RSS feed URL')
    search_parser.add_argument('keyword', help='Search keyword')
    search_parser.add_argument('--limit', type=int, help='Limit number of results')

    # Latest entries command
    latest_parser = subparsers.add_parser('latest', help='Get latest entries from RSS feed')
    latest_parser.add_argument('url', help='RSS feed URL')
    latest_parser.add_argument('--count', type=int, default=5, help='Number of latest entries (default: 5)')

    # Feed info command
    info_parser = subparsers.add_parser('info', help='Get RSS feed information')
    info_parser.add_argument('url', help='RSS feed URL')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        client = RSSClient()

        if args.command == 'fetch':
            result = client.fetch_feed(args.url, args.limit)
            
            if result.get('success'):
                if args.format == 'json':
                    print(json.dumps(result['data'], indent=2, ensure_ascii=False))
                else:
                    print(f"Feed: {result['data']['feed']['title']}")
                    print(f"Description: {result['data']['feed']['description']}")
                    print(f"Total entries: {result['data']['total_entries']}")
                    print()
                    print(client.format_entries_as_text(result['data']['entries']))
                
                if args.output:
                    save_result = client.save_to_json(result['data'], args.output)
                    if save_result.get('success'):
                        print(f"\nSaved to: {args.output}")
                    else:
                        print(f"\nError saving file: {save_result.get('error')}")
            else:
                print(f"Error: {result.get('error')}")

        elif args.command == 'fetch-multiple':
            result = client.fetch_multiple_feeds(args.urls, args.limit)
            
            if result.get('success'):
                for feed_data in result['data']['feeds']:
                    if 'error' in feed_data:
                        print(f"Error fetching {feed_data['url']}: {feed_data['error']}")
                        continue
                    
                    print(f"\n{'='*60}")
                    print(f"Feed: {feed_data['feed']['title']}")
                    print(f"URL: {feed_data['url']}")
                    print(f"{'='*60}")
                    print(client.format_entries_as_text(feed_data['entries']))
                
                if args.output:
                    save_result = client.save_to_json(result['data'], args.output)
                    if save_result.get('success'):
                        print(f"\nSaved to: {args.output}")
            else:
                print(f"Error: {result.get('error')}")

        elif args.command == 'search':
            result = client.search_entries(args.url, args.keyword, args.limit)
            
            if result.get('success'):
                print(f"Search results for '{result['data']['keyword']}':")
                print(f"Total matches: {result['data']['total_matches']}")
                print()
                print(client.format_entries_as_text(result['data']['matched_entries']))
            else:
                print(f"Error: {result.get('error')}")

        elif args.command == 'latest':
            result = client.get_latest_entries(args.url, args.count)
            
            if result.get('success'):
                print(f"Latest {len(result['data']['entries'])} entries from {result['data']['feed']['title']}:")
                print()
                print(client.format_entries_as_text(result['data']['entries']))
            else:
                print(f"Error: {result.get('error')}")

        elif args.command == 'info':
            result = client.get_feed_info(args.url)
            
            if result.get('success'):
                info = result['data']
                print(f"Feed Information:")
                print(f"  Title: {info['title']}")
                print(f"  Link: {info['link']}")
                print(f"  Description: {info['description']}")
                print(f"  Language: {info['language']}")
                print(f"  Updated: {info['updated']}")
                print(f"  Total Entries: {info['total_entries']}")
                if info['categories']:
                    print(f"  Categories: {', '.join(info['categories'])}")
            else:
                print(f"Error: {result.get('error')}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    main()
