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

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from i18n import i18n, _

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets'))
from mastodon_client import MastodonClient


def print_json(data: dict):
    """Print JSON data with indentation"""
    print(json.dumps(data, indent=2, ensure_ascii=False))


def print_status(status: dict, show_details: bool = False):
    """Print status information"""
    account = status.get('account', {})
    print(f"@{account.get('username', 'unknown')} ({account.get('display_name', 'N/A')})")
    print(f"Content: {status.get('content', '').replace('<p>', '').replace('</p>', '')}")
    print(f"Created: {status.get('created_at', 'N/A')}")
    print(f"URL: {status.get('url', 'N/A')}")
    
    if show_details:
        print(f"Favorites: {status.get('favourites_count', 0)}")
        print(f"Boosts: {status.get('reblogs_count', 0)}")
        print(f"Replies: {status.get('replies_count', 0)}")
    
    print()


def print_account(account: dict):
    """Print account information"""
    print(f"Username: @{account.get('username', 'unknown')}")
    print(f"Display Name: {account.get('display_name', 'N/A')}")
    print(f"Bio: {account.get('note', 'N/A').replace('<p>', '').replace('</p>', '')}")
    print(f"Followers: {account.get('followers_count', 0)}")
    print(f"Following: {account.get('following_count', 0)}")
    print(f"Statuses: {account.get('statuses_count', 0)}")
    print(f"URL: {account.get('url', 'N/A')}")
    print()


def main():
    parser = argparse.ArgumentParser(description=_('mastodon.cli_tool'))
    parser.add_argument('--post', help=_('mastodon.post_status'))
    parser.add_argument('--timeline', choices=['home', 'public'], help=_('mastodon.read_timeline'))
    parser.add_argument('--limit', type=int, default=20, help=_('mastodon.limit_count'))
    parser.add_argument('--account', action='store_true', help=_('mastodon.get_account_info'))
    parser.add_argument('--search', help=_('mastodon.search_query'))
    parser.add_argument('--type', choices=['statuses', 'accounts'], default='statuses', help=_('mastodon.search_type'))
    parser.add_argument('--status', help=_('mastodon.status_id'))
    parser.add_argument('--delete', help=_('mastodon.status_id'))
    parser.add_argument('--reply', help=_('mastodon.status_id'))
    parser.add_argument('--boost', help=_('mastodon.status_id'))
    parser.add_argument('--unboost', help=_('mastodon.status_id'))
    parser.add_argument('--favorite', help=_('mastodon.status_id'))
    parser.add_argument('--unfavorite', help=_('mastodon.status_id'))
    parser.add_argument('--details', action='store_true', help=_('mastodon.get_status_details'))
    parser.add_argument('--raw', action='store_true', help=_('mastodon.show_raw_json'))
    parser.add_argument('--lang', choices=['zh_cn', 'en_us', 'zh_tw', 'jp'], default='en_us', 
                       help=_('common.language_selection_default_en'))
    
    args = parser.parse_args()
    
    i18n.set_language(args.lang)
    
    try:
        client = MastodonClient()
        
        if args.post:
            if args.reply:
                result = client.reply_to_status(args.reply, args.post)
                if args.raw:
                    print_json(result)
                else:
                    print(f"{_('mastodon.success_replied')}")
                    print(f"{_('mastodon.status_url')}: {result.get('url', 'N/A')}")
            else:
                result = client.post_status(args.post)
                if args.raw:
                    print_json(result)
                else:
                    print(f"{_('mastodon.success_posted')}")
                    print(f"{_('mastodon.status_url')}: {result.get('url', 'N/A')}")
        
        elif args.timeline:
            if args.timeline == 'home':
                result = client.get_home_timeline(limit=args.limit)
            else:
                result = client.get_public_timeline(limit=args.limit)
            
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.timeline')} ({args.timeline}):")
                print()
                for status in result:
                    print_status(status, show_details=args.details)
        
        elif args.account:
            result = client.get_account_info()
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.account_info')}:")
                print()
                print_account(result)
        
        elif args.search:
            result = client.search(args.search, search_type=args.type, limit=args.limit)
            
            if args.raw:
                print_json(result)
            else:
                if args.type == 'statuses':
                    statuses = result.get('statuses', [])
                    print(f"{_('mastodon.found_statuses')}: {len(statuses)}")
                    print()
                    for status in statuses:
                        print_status(status, show_details=args.details)
                else:
                    accounts = result.get('accounts', [])
                    print(f"{_('mastodon.found_accounts')}: {len(accounts)}")
                    print()
                    for account in accounts:
                        print_account(account)
        
        elif args.status:
            result = client.get_status(args.status)
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.status_details')}:")
                print()
                print_status(result, show_details=True)
        
        elif args.delete:
            result = client.delete_status(args.delete)
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.success_deleted')}")
        
        elif args.boost:
            result = client.boost_status(args.boost)
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.success_boosted')}")
                print(f"{_('mastodon.status_url')}: {result.get('url', 'N/A')}")
        
        elif args.unboost:
            result = client.unboost_status(args.unboost)
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.success_unboosted')}")
        
        elif args.favorite:
            result = client.favorite_status(args.favorite)
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.success_favorited')}")
                print(f"{_('mastodon.status_url')}: {result.get('url', 'N/A')}")
        
        elif args.unfavorite:
            result = client.unfavorite_status(args.unfavorite)
            if args.raw:
                print_json(result)
            else:
                print(f"{_('mastodon.success_unfavorited')}")
        
        else:
            parser.print_help()
            
    except ValueError as e:
        if 'MASTODON_API_URL' in str(e) or 'MASTODON_ACCESS_TOKEN' in str(e):
            print(f"{_('mastodon.error_missing_credentials')}")
        else:
            print(f"{_('common.error')}: {str(e)}")
        sys.exit(1)
    except Exception as e:
        error_msg = str(e)
        if 'Authentication' in error_msg or '401' in error_msg:
            print(f"{_('mastodon.error_auth_failed')}")
        elif 'rate limit' in error_msg.lower() or '429' in error_msg:
            print(f"{_('mastodon.error_rate_limit')}")
        elif 'not found' in error_msg.lower() or '404' in error_msg:
            print(f"{_('mastodon.error_status_not_found')}")
        elif 'Connection' in error_msg or 'Network' in error_msg:
            print(f"{_('mastodon.error_network')}")
        else:
            print(f"{_('mastodon.error_unknown')}: {error_msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
