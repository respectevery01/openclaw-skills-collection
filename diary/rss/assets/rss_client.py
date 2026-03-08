import os
import feedparser
from datetime import datetime
from typing import Dict, List, Any, Optional
import json


class RSSClient:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        feedparser.USER_AGENT = self.user_agent

    def fetch_feed(self, url: str, limit: int = None) -> Dict[str, Any]:
        try:
            feed = feedparser.parse(url)
            
            if feed.bozo:
                return {
                    'success': False,
                    'error': f'Failed to parse feed: {feed.bozo_exception}'
                }
            
            entries = feed.entries
            if limit:
                entries = entries[:limit]
            
            formatted_entries = []
            for entry in entries:
                formatted_entry = {
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'published_parsed': self._format_date(entry.get('published_parsed')),
                    'summary': self._clean_html(entry.get('summary', '')),
                    'author': entry.get('author', ''),
                    'tags': [tag.get('term', '') for tag in entry.get('tags', [])],
                    'id': entry.get('id', entry.get('link', ''))
                }
                formatted_entries.append(formatted_entry)
            
            return {
                'success': True,
                'data': {
                    'feed': {
                        'title': feed.feed.get('title', ''),
                        'link': feed.feed.get('link', ''),
                        'description': feed.feed.get('description', ''),
                        'language': feed.feed.get('language', ''),
                        'updated': feed.feed.get('updated', ''),
                        'updated_parsed': self._format_date(feed.feed.get('updated_parsed'))
                    },
                    'entries': formatted_entries,
                    'total_entries': len(feed.entries)
                }
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def fetch_multiple_feeds(self, urls: List[str], limit: int = None) -> Dict[str, Any]:
        results = []
        for url in urls:
            result = self.fetch_feed(url, limit)
            if result.get('success'):
                results.append({
                    'url': url,
                    'feed': result['data']['feed'],
                    'entries': result['data']['entries']
                })
            else:
                results.append({
                    'url': url,
                    'error': result.get('error', 'Unknown error')
                })
        
        return {
            'success': True,
            'data': {
                'feeds': results,
                'total_feeds': len(urls)
            }
        }

    def search_entries(self, url: str, keyword: str, limit: int = None) -> Dict[str, Any]:
        result = self.fetch_feed(url)
        
        if not result.get('success'):
            return result
        
        keyword_lower = keyword.lower()
        matched_entries = []
        
        for entry in result['data']['entries']:
            title_lower = entry['title'].lower()
            summary_lower = entry['summary'].lower()
            
            if keyword_lower in title_lower or keyword_lower in summary_lower:
                matched_entries.append(entry)
        
        if limit:
            matched_entries = matched_entries[:limit]
        
        return {
            'success': True,
            'data': {
                'keyword': keyword,
                'matched_entries': matched_entries,
                'total_matches': len(matched_entries)
            }
        }

    def get_latest_entries(self, url: str, count: int = 5) -> Dict[str, Any]:
        return self.fetch_feed(url, limit=count)

    def get_feed_info(self, url: str) -> Dict[str, Any]:
        try:
            feed = feedparser.parse(url)
            
            if feed.bozo:
                return {
                    'success': False,
                    'error': f'Failed to parse feed: {feed.bozo_exception}'
                }
            
            return {
                'success': True,
                'data': {
                    'title': feed.feed.get('title', ''),
                    'link': feed.feed.get('link', ''),
                    'description': feed.feed.get('description', ''),
                    'language': feed.feed.get('language', ''),
                    'updated': feed.feed.get('updated', ''),
                    'updated_parsed': self._format_date(feed.feed.get('updated_parsed')),
                    'total_entries': len(feed.entries),
                    'categories': [tag.get('term', '') for tag in feed.feed.get('tags', [])]
                }
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _format_date(self, date_tuple) -> Optional[str]:
        if not date_tuple:
            return None
        try:
            dt = datetime(*date_tuple[:6])
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return None

    def _clean_html(self, html: str) -> str:
        import re
        html = re.sub(r'<[^>]+>', '', html)
        html = re.sub(r'\s+', ' ', html).strip()
        return html

    def format_entries_as_text(self, entries: List[Dict[str, Any]], show_summary: bool = True) -> str:
        output = []
        for i, entry in enumerate(entries, 1):
            output.append(f"{i}. {entry['title']}")
            output.append(f"   链接: {entry['link']}")
            if entry['published']:
                output.append(f"   发布时间: {entry['published']}")
            if entry['author']:
                output.append(f"   作者: {entry['author']}")
            if show_summary and entry['summary']:
                output.append(f"   摘要: {entry['summary'][:200]}...")
            output.append('')
        return '\n'.join(output)

    def save_to_json(self, data: Dict[str, Any], filepath: str) -> Dict[str, Any]:
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return {
                'success': True,
                'data': {
                    'filepath': filepath
                }
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
