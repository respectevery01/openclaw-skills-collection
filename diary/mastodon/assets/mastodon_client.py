import os
import requests
from typing import Optional, Dict, List, Any
from dotenv import load_dotenv

class MastodonClient:
    """Mastodon API client for interacting with Mastodon instances"""
    
    def __init__(self):
        """Initialize Mastodon client with credentials from environment variables"""
        # Load .env file from project root
        script_dir = os.path.dirname(os.path.abspath(__file__))
        env_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)), '.env')
        if not os.path.exists(env_path):
            env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))), '.env')
        load_dotenv(env_path)
        
        self.api_url = os.getenv('MASTODON_API_URL')
        self.access_token = os.getenv('MASTODON_ACCESS_TOKEN')
        self.client_id = os.getenv('MASTODON_CLIENT_ID')
        self.client_secret = os.getenv('MASTODON_CLIENT_SECRET')
        
        if not self.api_url:
            raise ValueError("MASTODON_API_URL not found in environment variables")
        if not self.access_token:
            raise ValueError("MASTODON_ACCESS_TOKEN not found in environment variables")
        
        # Remove trailing slash from API URL
        self.api_url = self.api_url.rstrip('/')
        
        # Set up headers with authorization
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None, 
                     params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make an API request to Mastodon"""
        url = f"{self.api_url}/api/v1{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers, params=params)
            elif method == 'POST':
                response = requests.post(url, headers=self.headers, json=data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=self.headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            
            # Handle empty response
            if not response.text:
                return {}
                
            return response.json()
            
        except requests.exceptions.RequestException as e:
            if hasattr(e.response, 'json'):
                error_data = e.response.json()
                raise Exception(f"API Error: {error_data.get('error', str(e))}")
            raise Exception(f"Request failed: {str(e)}")
    
    def post_status(self, status_text: str, in_reply_to_id: Optional[str] = None,
                   media_ids: Optional[List[str]] = None, sensitive: bool = False,
                   spoiler_text: Optional[str] = None, visibility: str = 'public') -> Dict[str, Any]:
        """Post a new status (toot)"""
        data = {
            'status': status_text,
            'visibility': visibility,
            'sensitive': sensitive
        }
        
        if in_reply_to_id:
            data['in_reply_to_id'] = in_reply_to_id
        if media_ids:
            data['media_ids'] = media_ids
        if spoiler_text:
            data['spoiler_text'] = spoiler_text
        
        return self._make_request('POST', '/statuses', data=data)
    
    def get_home_timeline(self, limit: int = 20, max_id: Optional[str] = None,
                         since_id: Optional[str] = None, min_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get the home timeline (statuses from followed accounts)"""
        params = {'limit': min(limit, 40)}
        if max_id:
            params['max_id'] = max_id
        if since_id:
            params['since_id'] = since_id
        if min_id:
            params['min_id'] = min_id
        
        return self._make_request('GET', '/timelines/home', params=params)
    
    def get_public_timeline(self, limit: int = 20, local: bool = False,
                           max_id: Optional[str] = None, since_id: Optional[str] = None,
                           min_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get the public timeline"""
        params = {'limit': min(limit, 40), 'local': local}
        if max_id:
            params['max_id'] = max_id
        if since_id:
            params['since_id'] = since_id
        if min_id:
            params['min_id'] = min_id
        
        return self._make_request('GET', '/timelines/public', params=params)
    
    def get_account_info(self) -> Dict[str, Any]:
        """Get the authenticated user's account information"""
        return self._make_request('GET', '/accounts/verify_credentials')
    
    def get_status(self, status_id: str) -> Dict[str, Any]:
        """Get a specific status by ID"""
        return self._make_request('GET', f'/statuses/{status_id}')
    
    def delete_status(self, status_id: str) -> Dict[str, Any]:
        """Delete a status by ID"""
        return self._make_request('DELETE', f'/statuses/{status_id}')
    
    def reply_to_status(self, status_id: str, reply_text: str, visibility: str = 'public') -> Dict[str, Any]:
        """Reply to a status"""
        return self.post_status(reply_text, in_reply_to_id=status_id, visibility=visibility)
    
    def boost_status(self, status_id: str) -> Dict[str, Any]:
        """Boost (reblog) a status"""
        return self._make_request('POST', f'/statuses/{status_id}/reblog')
    
    def unboost_status(self, status_id: str) -> Dict[str, Any]:
        """Unboost (unreblog) a status"""
        return self._make_request('POST', f'/statuses/{status_id}/unreblog')
    
    def favorite_status(self, status_id: str) -> Dict[str, Any]:
        """Favorite a status"""
        return self._make_request('POST', f'/statuses/{status_id}/favourite')
    
    def unfavorite_status(self, status_id: str) -> Dict[str, Any]:
        """Unfavorite a status"""
        return self._make_request('POST', f'/statuses/{status_id}/unfavourite')
    
    def search(self, query: str, search_type: str = 'statuses', limit: int = 20,
               resolve: bool = False) -> Dict[str, Any]:
        """Search for content on Mastodon"""
        params = {
            'q': query,
            'type': search_type,
            'limit': min(limit, 40),
            'resolve': resolve
        }
        
        # Try v2 API first, fall back to v1
        try:
            url = f"{self.api_url}/api/v2/search"
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            if response.text:
                return response.json()
        except:
            pass
        
        # Fall back to v1 API
        return self._make_request('GET', '/search', params=params)
    
    def search_v2(self, query: str, search_type: str = 'statuses', limit: int = 20,
                  resolve: bool = False) -> Dict[str, Any]:
        """Search for content on Mastodon using v2 API"""
        params = {
            'q': query,
            'type': search_type,
            'limit': min(limit, 40),
            'resolve': resolve
        }
        
        return self._make_request('GET', '/search', params=params)
    
    def get_account_statuses(self, account_id: str, limit: int = 20,
                            max_id: Optional[str] = None, since_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get statuses from a specific account"""
        params = {'limit': min(limit, 40)}
        if max_id:
            params['max_id'] = max_id
        if since_id:
            params['since_id'] = since_id
        
        return self._make_request('GET', f'/accounts/{account_id}/statuses', params=params)
