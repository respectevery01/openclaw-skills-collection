"""
Telegram Bot Client
"""
import os
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class TelegramClient:
    """Telegram Bot API Client"""
    
    def __init__(self, bot_token: str = None):
        """
        Initialize Telegram client
        
        Args:
            bot_token: Telegram bot token (defaults to TELEGRAM_BOT_TOKEN env var)
        """
        self.bot_token = bot_token or os.getenv('TELEGRAM_BOT_TOKEN')
        if not self.bot_token:
            raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables")
        
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
    
    def _make_request(self, method: str, data: Dict[str, Any] = None, files: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make API request to Telegram
        
        Args:
            method: API method name
            data: Request data
            files: Files to upload
        
        Returns:
            API response
        """
        url = f"{self.base_url}/{method}"
        
        try:
            if files:
                response = requests.post(url, data=data, files=files, timeout=30)
            else:
                response = requests.post(url, json=data, timeout=30)
            
            response.raise_for_status()
            result = response.json()
            
            if not result.get('ok'):
                return {
                    'success': False,
                    'error': result.get('description', 'Unknown error'),
                    'error_code': result.get('error_code')
                }
            
            return {
                'success': True,
                'data': result.get('result')
            }
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def send_message(
        self,
        chat_id: str,
        text: str,
        parse_mode: str = None,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        reply_to_message_id: int = None,
        reply_markup: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Send text message
        
        Args:
            chat_id: Chat ID or username
            text: Message text
            parse_mode: Parse mode (Markdown/HTML)
            disable_web_page_preview: Disable link previews
            disable_notification: Send silently
            reply_to_message_id: Reply to message ID
            reply_markup: Inline keyboard or reply markup
        
        Returns:
            API response
        """
        data = {
            'chat_id': chat_id,
            'text': text
        }
        
        if parse_mode:
            data['parse_mode'] = parse_mode
        
        if disable_web_page_preview:
            data['disable_web_page_preview'] = True
        
        if disable_notification:
            data['disable_notification'] = True
        
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        
        if reply_markup:
            data['reply_markup'] = reply_markup
        
        return self._make_request('sendMessage', data=data)
    
    def send_photo(
        self,
        chat_id: str,
        photo: str,
        caption: str = None,
        parse_mode: str = None,
        disable_notification: bool = False,
        reply_to_message_id: int = None
    ) -> Dict[str, Any]:
        """
        Send photo
        
        Args:
            chat_id: Chat ID or username
            photo: Photo file path or URL
            caption: Photo caption
            parse_mode: Parse mode for caption
            disable_notification: Send silently
            reply_to_message_id: Reply to message ID
        
        Returns:
            API response
        """
        import os as os_module
        
        data = {
            'chat_id': chat_id
        }
        
        if caption:
            data['caption'] = caption
        
        if parse_mode:
            data['parse_mode'] = parse_mode
        
        if disable_notification:
            data['disable_notification'] = True
        
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        
        files = None
        
        if os_module.path.exists(photo):
            with open(photo, 'rb') as f:
                files = {'photo': f}
                return self._make_request('sendPhoto', data=data, files=files)
        else:
            data['photo'] = photo
            return self._make_request('sendPhoto', data=data)
    
    def send_document(
        self,
        chat_id: str,
        document: str,
        caption: str = None,
        parse_mode: str = None,
        disable_notification: bool = False,
        reply_to_message_id: int = None
    ) -> Dict[str, Any]:
        """
        Send document
        
        Args:
            chat_id: Chat ID or username
            document: Document file path or URL
            caption: Document caption
            parse_mode: Parse mode for caption
            disable_notification: Send silently
            reply_to_message_id: Reply to message ID
        
        Returns:
            API response
        """
        import os as os_module
        
        data = {
            'chat_id': chat_id
        }
        
        if caption:
            data['caption'] = caption
        
        if parse_mode:
            data['parse_mode'] = parse_mode
        
        if disable_notification:
            data['disable_notification'] = True
        
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        
        files = None
        
        if os_module.path.exists(document):
            with open(document, 'rb') as f:
                files = {'document': f}
                return self._make_request('sendDocument', data=data, files=files)
        else:
            data['document'] = document
            return self._make_request('sendDocument', data=data)
    
    def send_location(
        self,
        chat_id: str,
        latitude: float,
        longitude: float,
        disable_notification: bool = False,
        reply_to_message_id: int = None
    ) -> Dict[str, Any]:
        """
        Send location
        
        Args:
            chat_id: Chat ID or username
            latitude: Latitude
            longitude: Longitude
            disable_notification: Send silently
            reply_to_message_id: Reply to message ID
        
        Returns:
            API response
        """
        data = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }
        
        if disable_notification:
            data['disable_notification'] = True
        
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        
        return self._make_request('sendLocation', data=data)
    
    def send_contact(
        self,
        chat_id: str,
        phone_number: str,
        first_name: str,
        last_name: str = None,
        disable_notification: bool = False,
        reply_to_message_id: int = None
    ) -> Dict[str, Any]:
        """
        Send contact
        
        Args:
            chat_id: Chat ID or username
            phone_number: Phone number
            first_name: First name
            last_name: Last name
            disable_notification: Send silently
            reply_to_message_id: Reply to message ID
        
        Returns:
            API response
        """
        data = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name
        }
        
        if last_name:
            data['last_name'] = last_name
        
        if disable_notification:
            data['disable_notification'] = True
        
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        
        return self._make_request('sendContact', data=data)
    
    def delete_message(
        self,
        chat_id: str,
        message_id: int
    ) -> Dict[str, Any]:
        """
        Delete message
        
        Args:
            chat_id: Chat ID or username
            message_id: Message ID to delete
        
        Returns:
            API response
        """
        data = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        
        return self._make_request('deleteMessage', data=data)
    
    def pin_chat_message(
        self,
        chat_id: str,
        message_id: int,
        disable_notification: bool = False
    ) -> Dict[str, Any]:
        """
        Pin message in chat
        
        Args:
            chat_id: Chat ID or username
            message_id: Message ID to pin
            disable_notification: Pin silently
        
        Returns:
            API response
        """
        data = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        
        if disable_notification:
            data['disable_notification'] = True
        
        return self._make_request('pinChatMessage', data=data)
    
    def unpin_chat_message(
        self,
        chat_id: str,
        message_id: int = None
    ) -> Dict[str, Any]:
        """
        Unpin message in chat
        
        Args:
            chat_id: Chat ID or username
            message_id: Message ID to unpin (None = unpin all)
        
        Returns:
            API response
        """
        data = {
            'chat_id': chat_id
        }
        
        if message_id:
            data['message_id'] = message_id
        
        return self._make_request('unpinChatMessage', data=data)
    
    def get_me(self) -> Dict[str, Any]:
        """
        Get bot information
        
        Returns:
            API response with bot info
        """
        return self._make_request('getMe')
    
    def get_chat(self, chat_id: str) -> Dict[str, Any]:
        """
        Get chat information
        
        Args:
            chat_id: Chat ID or username
        
        Returns:
            API response with chat info
        """
        data = {
            'chat_id': chat_id
        }
        
        return self._make_request('getChat', data=data)
    
    def get_updates(
        self,
        offset: int = None,
        limit: int = None,
        timeout: int = None
    ) -> Dict[str, Any]:
        """
        Get updates (messages sent to bot)
        
        Args:
            offset: Identifier of the first update to be returned
            limit: Limits the number of updates to be retrieved
            timeout: Timeout for long polling
        
        Returns:
            API response with updates
        """
        data = {}
        
        if offset:
            data['offset'] = offset
        
        if limit:
            data['limit'] = limit
        
        if timeout:
            data['timeout'] = timeout
        
        return self._make_request('getUpdates', data=data)
    
    def download_file(
        self,
        file_id: str,
        save_path: str = None
    ) -> Dict[str, Any]:
        """
        Download file from Telegram
        
        Args:
            file_id: File ID from message
            save_path: Path to save file (default: current directory)
        
        Returns:
            API response with file path
        """
        import os as os_module
        
        file_info = self._make_request('getFile', data={'file_id': file_id})
        
        if not file_info.get('success'):
            return file_info
        
        file_path = file_info['data']['file_path']
        
        download_url = f"https://api.telegram.org/file/bot{self.bot_token}/{file_path}"
        
        try:
            response = requests.get(download_url, timeout=30)
            response.raise_for_status()
            
            if not save_path:
                save_path = os_module.path.basename(file_path)
            
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            return {
                'success': True,
                'file_path': save_path,
                'file_size': len(response.content)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def process_updates(
        self,
        download_dir: str = None,
        offset: int = None
    ) -> Dict[str, Any]:
        """
        Process updates and download received files
        
        Args:
            download_dir: Directory to save downloaded files (default: assets/telegram_downloads)
            offset: Update offset to start from
        
        Returns:
            Summary of processed updates
        """
        import os as os_module
        from datetime import datetime
        
        if not download_dir:
            download_dir = os_module.path.join(
                os_module.path.dirname(os_module.path.abspath(__file__)),
                'telegram_downloads'
            )
        
        if not os_module.path.exists(download_dir):
            os_module.makedirs(download_dir)
        
        updates = self.get_updates(offset=offset)
        
        if not updates.get('success'):
            return updates
        
        results = []
        last_update_id = None
        
        for update in updates['data']:
            last_update_id = update['update_id']
            message = update.get('message', {})
            
            if 'photo' in message:
                photos = message['photo']
                largest_photo = photos[-1]
                file_id = largest_photo['file_id']
                
                photo_dir = os_module.path.join(download_dir, 'photos')
                if not os_module.path.exists(photo_dir):
                    os_module.makedirs(photo_dir)
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                save_path = os_module.path.join(photo_dir, f"photo_{timestamp}.jpg")
                
                result = self.download_file(file_id, save_path)
                results.append({
                    'type': 'photo',
                    'file_id': file_id,
                    'result': result
                })
            
            elif 'document' in message:
                document = message['document']
                file_id = document['file_id']
                file_name = document.get('file_name', 'document')
                mime_type = document.get('mime_type', 'application/octet-stream')
                
                if mime_type.startswith('image/'):
                    file_type = 'images'
                elif mime_type.startswith('video/'):
                    file_type = 'videos'
                elif mime_type.startswith('audio/'):
                    file_type = 'audio'
                elif 'zip' in file_name or 'rar' in file_name or '7z' in file_name:
                    file_type = 'archives'
                elif 'pdf' in file_name:
                    file_type = 'documents'
                elif file_name.endswith(('.doc', '.docx', '.txt', '.xls', '.xlsx')):
                    file_type = 'documents'
                else:
                    file_type = 'other'
                
                file_dir = os_module.path.join(download_dir, file_type)
                if not os_module.path.exists(file_dir):
                    os_module.makedirs(file_dir)
                
                save_path = os_module.path.join(file_dir, file_name)
                
                result = self.download_file(file_id, save_path)
                results.append({
                    'type': 'document',
                    'file_type': file_type,
                    'file_id': file_id,
                    'file_name': file_name,
                    'result': result
                })
            
            elif 'voice' in message:
                voice = message['voice']
                file_id = voice['file_id']
                
                voice_dir = os_module.path.join(download_dir, 'audio')
                if not os_module.path.exists(voice_dir):
                    os_module.makedirs(voice_dir)
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                save_path = os_module.path.join(voice_dir, f"voice_{timestamp}.ogg")
                
                result = self.download_file(file_id, save_path)
                results.append({
                    'type': 'voice',
                    'file_id': file_id,
                    'result': result
                })
            
            elif 'video' in message:
                video = message['video']
                file_id = video['file_id']
                
                video_dir = os_module.path.join(download_dir, 'videos')
                if not os_module.path.exists(video_dir):
                    os_module.makedirs(video_dir)
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                save_path = os_module.path.join(video_dir, f"video_{timestamp}.mp4")
                
                result = self.download_file(file_id, save_path)
                results.append({
                    'type': 'video',
                    'file_id': file_id,
                    'result': result
                })
        
        return {
            'success': True,
            'processed': len(results),
            'last_update_id': last_update_id,
            'results': results
        }
    
    async def text_to_speech(
        self,
        text: str,
        voice: str = 'zh-CN-XiaoxiaoNeural',
        rate: str = '+0%',
        pitch: str = '+0Hz',
        output_path: str = None
    ) -> str:
        """
        Convert text to speech using edge-tts
        
        Args:
            text: Text to convert to speech
            voice: Voice name (default: zh-CN-XiaoxiaoNeural)
            rate: Speech rate (default: +0%)
            pitch: Speech pitch (default: +0Hz)
            output_path: Path to save audio file (default: temp file)
        
        Returns:
            Path to the generated audio file
        """
        import edge_tts
        import tempfile
        import os as os_module
        
        if not output_path:
            temp_dir = tempfile.gettempdir()
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_path = os_module.path.join(temp_dir, f"tts_{timestamp}.mp3")
        
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_path)
        
        return output_path
    
    def send_voice_message(
        self,
        chat_id: str,
        text: str,
        voice: str = 'zh-CN-XiaoxiaoNeural',
        rate: str = '+0%',
        pitch: str = '+0Hz',
        disable_notification: bool = False,
        reply_to_message_id: int = None
    ) -> Dict[str, Any]:
        """
        Send voice message (text-to-speech)
        
        Args:
            chat_id: Chat ID or username
            text: Text to convert to speech
            voice: Voice name (default: zh-CN-XiaoxiaoNeural)
            rate: Speech rate (default: +0%)
            pitch: Speech pitch (default: +0Hz)
            disable_notification: Send silently
            reply_to_message_id: Reply to message ID
        
        Returns:
            API response
        """
        import asyncio
        import os as os_module
        
        async def send_voice():
            audio_path = await self.text_to_speech(text, voice, rate, pitch)
            
            data = {
                'chat_id': chat_id
            }
            
            if disable_notification:
                data['disable_notification'] = True
            
            if reply_to_message_id:
                data['reply_to_message_id'] = reply_to_message_id
            
            files = None
            
            if os_module.path.exists(audio_path):
                with open(audio_path, 'rb') as f:
                    files = {'voice': f}
                    result = self._make_request('sendVoice', data=data, files=files)
                
                os_module.remove(audio_path)
                return result
            else:
                data['voice'] = audio_path
                return self._make_request('sendVoice', data=data)
        
        return asyncio.run(send_voice())
    
    def list_voices(self) -> Dict[str, Any]:
        """
        List available TTS voices
        
        Returns:
            List of available voices
        """
        import edge_tts
        import asyncio
        
        try:
            async def get_voices():
                voices = await edge_tts.list_voices()
                return voices
            
            voices = asyncio.run(get_voices())
            return {
                'success': True,
                'data': voices
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def transcribe_voice(
        self,
        file_id: str,
        api_key: str = None,
        language: str = None
    ) -> Dict[str, Any]:
        """
        Transcribe voice message to text using Whisper
        
        Args:
            file_id: Voice file ID from Telegram
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            language: Language code (e.g., 'zh', 'en', 'ja')
        
        Returns:
            Transcription result
        """
        import os as os_module
        import tempfile
        from openai import OpenAI
        
        if not api_key:
            api_key = os_module.getenv('OPENAI_API_KEY')
            if not api_key:
                return {
                    'success': False,
                    'error': 'OPENAI_API_KEY not found in environment variables'
                }
        
        try:
            download_result = self.download_file(file_id)
            
            if not download_result.get('success'):
                return download_result
            
            audio_path = download_result['file_path']
            
            client = OpenAI(api_key=api_key)
            
            with open(audio_path, 'rb') as audio_file:
                transcription_params = {
                    'model': 'whisper-1',
                    'file': audio_file
                }
                
                if language:
                    transcription_params['language'] = language
                
                response = client.audio.transcriptions.create(**transcription_params)
            
            os_module.remove(audio_path)
            
            return {
                'success': True,
                'data': {
                    'text': response.text,
                    'language': response.language if hasattr(response, 'language') else language
                }
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def process_voice_updates(
        self,
        download_dir: str = None,
        offset: int = None,
        transcribe: bool = False,
        api_key: str = None,
        language: str = None
    ) -> Dict[str, Any]:
        """
        Process updates and optionally transcribe voice messages
        
        Args:
            download_dir: Directory to save downloaded files
            offset: Update offset to start from
            transcribe: Whether to transcribe voice messages
            api_key: OpenAI API key for transcription
            language: Language code for transcription
        
        Returns:
            Summary of processed updates
        """
        import os as os_module
        
        if not download_dir:
            download_dir = os_module.path.join(
                os_module.path.dirname(os_module.path.abspath(__file__)),
                'telegram_downloads'
            )
        
        if not os_module.path.exists(download_dir):
            os_module.makedirs(download_dir)
        
        updates = self.get_updates(offset=offset)
        
        if not updates.get('success'):
            return updates
        
        results = []
        last_update_id = None
        
        for update in updates['data']:
            last_update_id = update['update_id']
            message = update.get('message', {})
            
            if 'voice' in message:
                voice = message['voice']
                file_id = voice['file_id']
                
                voice_dir = os_module.path.join(download_dir, 'audio')
                if not os_module.path.exists(voice_dir):
                    os_module.makedirs(voice_dir)
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                save_path = os_module.path.join(voice_dir, f"voice_{timestamp}.ogg")
                
                download_result = self.download_file(file_id, save_path)
                
                result = {
                    'type': 'voice',
                    'file_id': file_id,
                    'download_result': download_result
                }
                
                if transcribe and download_result.get('success'):
                    transcription_result = self.transcribe_voice(file_id, api_key, language)
                    result['transcription'] = transcription_result
                
                results.append(result)
            
            elif 'photo' in message:
                photos = message['photo']
                largest_photo = photos[-1]
                file_id = largest_photo['file_id']
                
                photo_dir = os_module.path.join(download_dir, 'photos')
                if not os_module.path.exists(photo_dir):
                    os_module.makedirs(photo_dir)
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                save_path = os_module.path.join(photo_dir, f"photo_{timestamp}.jpg")
                
                result = self.download_file(file_id, save_path)
                results.append({
                    'type': 'photo',
                    'file_id': file_id,
                    'result': result
                })
            
            elif 'document' in message:
                document = message['document']
                file_id = document['file_id']
                file_name = document.get('file_name', 'document')
                mime_type = document.get('mime_type', 'application/octet-stream')
                
                if mime_type.startswith('image/'):
                    file_type = 'images'
                elif mime_type.startswith('video/'):
                    file_type = 'videos'
                elif mime_type.startswith('audio/'):
                    file_type = 'audio'
                elif 'zip' in file_name or 'rar' in file_name or '7z' in file_name:
                    file_type = 'archives'
                elif 'pdf' in file_name:
                    file_type = 'documents'
                elif file_name.endswith(('.doc', '.docx', '.txt', '.xls', '.xlsx')):
                    file_type = 'documents'
                else:
                    file_type = 'other'
                
                file_dir = os_module.path.join(download_dir, file_type)
                if not os_module.path.exists(file_dir):
                    os_module.makedirs(file_dir)
                
                save_path = os_module.path.join(file_dir, file_name)
                
                result = self.download_file(file_id, save_path)
                results.append({
                    'type': 'document',
                    'file_type': file_type,
                    'file_id': file_id,
                    'file_name': file_name,
                    'result': result
                })
        
        return {
            'success': True,
            'processed': len(results),
            'last_update_id': last_update_id,
            'results': results
        }