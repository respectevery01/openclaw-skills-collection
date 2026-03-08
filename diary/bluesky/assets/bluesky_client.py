import os
import requests
import json
from typing import Optional, Dict, List, Any
from dotenv import load_dotenv

try:
    from bsky_bridge import BskySession, post_text, post_image, post_images
except ImportError:
    raise ImportError("bsky-bridge package is required. Install it with: pip install bsky-bridge")


class BlueskyClient:
    """Bluesky API client for interacting with Bluesky social network"""
    
    def __init__(self):
        """Initialize Bluesky client with credentials from environment variables"""
        # Load .env file from project root
        script_dir = os.path.dirname(os.path.abspath(__file__))
        env_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)), '.env')
        if not os.path.exists(env_path):
            env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))), '.env')
        load_dotenv(env_path)
        
        self.api_url = os.getenv('BLUESKY_API_URL', 'https://bsky.social')
        self.handle = os.getenv('BLUESKY_HANDLE_ID') or os.getenv('BLUESKY_HANDLE')
        self.app_password = os.getenv('BLUESKY_CLIENT_PASSWORD_SECRET') or os.getenv('BLUESKY_APP_PASSWORD')
        
        if not self.handle:
            raise ValueError("BLUESKY_HANDLE_ID or BLUESKY_HANDLE not found in environment variables")
        if not self.app_password:
            raise ValueError("BLUESKY_CLIENT_PASSWORD_SECRET or BLUESKY_APP_PASSWORD not found in environment variables")
        
        # Check if using standard Bluesky instance
        self.is_standard_instance = 'bsky.social' in self.api_url
        
        if self.is_standard_instance:
            # Use bsky-bridge for standard instance
            try:
                self.session = BskySession(self.handle, self.app_password)
                self.use_bridge = True
            except Exception as e:
                print(f"Warning: Could not create bsky-bridge session: {e}")
                print("Falling back to direct API calls")
                self.use_bridge = False
                self.session = None
                self._authenticate_direct()
        else:
            # Use direct API calls for custom instances
            self.use_bridge = False
            self.session = None
            self._authenticate_direct()
    
    def _authenticate_direct(self):
        """Authenticate using direct API calls for custom instances"""
        # Remove trailing slash from API URL
        api_base = self.api_url.rstrip('/')
        
        # Get DID from handle
        did_url = f"{api_base}/xrpc/com.atproto.identity.resolveHandle"
        response = requests.post(did_url, json={"handle": self.handle}, timeout=10)
        response.raise_for_status()
        self.did = response.json()['did']
        
        # Create session
        session_url = f"{api_base}/xrpc/com.atproto.server.createSession"
        response = requests.post(session_url, json={
            "identifier": self.handle,
            "password": self.app_password
        }, timeout=10)
        response.raise_for_status()
        session_data = response.json()
        
        self.access_jwt = session_data['accessJwt']
        self.refresh_jwt = session_data['refreshJwt']
        self.headers = {
            'Authorization': f'Bearer {self.access_jwt}',
            'Content-Type': 'application/json'
        }
    
    def _api_call(self, endpoint: str, method: str = 'GET', 
                  json_data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make direct API call"""
        api_base = self.api_url.rstrip('/')
        url = f"{api_base}/xrpc/{endpoint}"
        
        response = requests.request(method, url, headers=self.headers, json=json_data, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def post_text(self, text: str, langs: Optional[List[str]] = None, 
                 reply_to: Optional[str] = None) -> Dict[str, Any]:
        """Post text to Bluesky"""
        if self.use_bridge:
            kwargs = {}
            if langs:
                kwargs['langs'] = langs
            if reply_to:
                kwargs['reply_to'] = reply_to
            return post_text(self.session, text, **kwargs)
        else:
            # Direct API call
            record = {
                "$type": "app.bsky.feed.post",
                "text": text,
                "createdAt": self._get_timestamp()
            }
            
            if langs:
                record["langs"] = langs
            
            if reply_to:
                record["reply"] = self._parse_reply_to(reply_to)
            
            return self._api_call(
                "com.atproto.repo.createRecord",
                method="POST",
                json_data={
                    "repo": self.did,
                    "collection": "app.bsky.feed.post",
                    "record": record
                }
            )
    
    def post_image(self, text: str, image_path: str, alt_text: str = "",
                  langs: Optional[List[str]] = None, reply_to: Optional[str] = None) -> Dict[str, Any]:
        """Post a single image to Bluesky"""
        if self.use_bridge:
            kwargs = {}
            if langs:
                kwargs['langs'] = langs
            if reply_to:
                kwargs['reply_to'] = reply_to
            return post_image(self.session, text, image_path, alt_text=alt_text, **kwargs)
        else:
            # Direct API call - simplified version
            print("Note: Image posting with direct API calls requires additional implementation")
            print("For full image support, please use standard bsky.social instance")
            return self.post_text(text, langs, reply_to)
    
    def post_images(self, text: str, image_paths: List[str], alt_texts: List[str],
                   langs: Optional[List[str]] = None, reply_to: Optional[str] = None) -> Dict[str, Any]:
        """Post multiple images to Bluesky"""
        if self.use_bridge:
            if len(image_paths) > 4:
                raise ValueError("Maximum 4 images allowed per post")
            
            if len(image_paths) != len(alt_texts):
                raise ValueError("Number of image paths must match number of alt texts")
            
            images = []
            for path, alt in zip(image_paths, alt_texts):
                images.append({"path": path, "alt": alt})
            
            kwargs = {}
            if langs:
                kwargs['langs'] = langs
            if reply_to:
                kwargs['reply_to'] = reply_to
            
            return post_images(self.session, text, images, **kwargs)
        else:
            # Direct API call - simplified version
            print("Note: Image posting with direct API calls requires additional implementation")
            print("For full image support, please use standard bsky.social instance")
            return self.post_text(text, langs, reply_to)
    
    def get_profile(self, handle: Optional[str] = None) -> Dict[str, Any]:
        """Get profile information"""
        if self.use_bridge:
            if handle:
                return self.session.api_call(
                    "app.bsky.actor.getProfile",
                    method="GET",
                    params={"actor": handle}
                )
            else:
                return self.session.api_call(
                    "app.bsky.actor.getProfile",
                    method="GET",
                    params={"actor": self.handle}
                )
        else:
            # Direct API call
            actor = handle or self.did
            return self._api_call(
                "app.bsky.actor.getProfile",
                method="GET",
                params={"actor": actor}
            )
    
    def get_timeline(self, limit: int = 20, cursor: Optional[str] = None) -> Dict[str, Any]:
        """Get timeline"""
        if self.use_bridge:
            params = {"limit": min(limit, 100)}
            if cursor:
                params["cursor"] = cursor
            return self.session.api_call(
                "app.bsky.feed.getTimeline",
                method="GET",
                params=params
            )
        else:
            # Direct API call
            params = {"limit": min(limit, 100)}
            if cursor:
                params["cursor"] = cursor
            return self._api_call(
                "app.bsky.feed.getTimeline",
                method="GET",
                params=params
            )
    
    def search(self, query: str, search_type: str = "posts", limit: int = 20) -> Dict[str, Any]:
        """Search content on Bluesky"""
        if self.use_bridge:
            params = {"q": query, "limit": min(limit, 100)}
            
            if search_type == "posts":
                return self.session.api_call(
                    "app.bsky.feed.searchPosts",
                    method="GET",
                    params=params
                )
            elif search_type == "actors":
                return self.session.api_call(
                    "app.bsky.actor.searchActors",
                    method="GET",
                    params=params
                )
            else:
                raise ValueError(f"Invalid search type: {search_type}. Use 'posts' or 'actors'")
        else:
            # Direct API call
            params = {"q": query, "limit": min(limit, 100)}
            
            if search_type == "posts":
                return self._api_call(
                    "app.bsky.feed.searchPosts",
                    method="GET",
                    params=params
                )
            elif search_type == "actors":
                return self._api_call(
                    "app.bsky.actor.searchActors",
                    method="GET",
                    params=params
                )
            else:
                raise ValueError(f"Invalid search type: {search_type}. Use 'posts' or 'actors'")
    
    def api_call(self, endpoint: str, method: str = "GET", 
                json_data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make custom API call"""
        if self.use_bridge:
            return self.session.api_call(endpoint, method=method, json=json_data, params=params)
        else:
            return self._api_call(endpoint, method, json_data, params)
    
    def logout(self):
        """Logout and clear session"""
        if self.session:
            self.session.logout()
        else:
            self.access_jwt = None
            self.refresh_jwt = None
    
    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format"""
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    
    def _parse_reply_to(self, reply_to: str) -> Dict[str, Any]:
        """Parse reply_to parameter"""
        # Simplified version - full implementation would handle various reply control types
        if reply_to == "nobody":
            return {"$type": "app.bsky.feed.post#replyRef", "root": {}, "parent": {}}
        elif reply_to == "mentions":
            return {"$type": "app.bsky.feed.post#replyRef", "root": {}, "parent": {}}
        elif reply_to == "following":
            return {"$type": "app.bsky.feed.post#replyRef", "root": {}, "parent": {}}
        elif reply_to == "followers":
            return {"$type": "app.bsky.feed.post#replyRef", "root": {}, "parent": {}}
        else:
            return {"$type": "app.bsky.feed.post#replyRef", "root": {}, "parent": {}}
