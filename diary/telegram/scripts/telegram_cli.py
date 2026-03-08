"""
Telegram Bot CLI
"""
import os
import sys
import argparse
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'assets'))

from telegram_client import TelegramClient


def main():
    parser = argparse.ArgumentParser(description='Telegram Bot CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Send message command
    send_parser = subparsers.add_parser('send', help='Send text message')
    send_parser.add_argument('chat_id', help='Chat ID or username')
    send_parser.add_argument('message', help='Message text')
    send_parser.add_argument('--parse-mode', choices=['Markdown', 'HTML'], help='Parse mode')
    send_parser.add_argument('--disable-web-page-preview', action='store_true', help='Disable link previews')
    send_parser.add_argument('--disable-notification', action='store_true', help='Send silently')
    send_parser.add_argument('--reply-to', type=int, help='Reply to message ID')
    send_parser.add_argument('--keyboard', help='Custom keyboard (JSON)')
    
    # Send photo command
    send_photo_parser = subparsers.add_parser('send-photo', help='Send photo')
    send_photo_parser.add_argument('chat_id', help='Chat ID or username')
    send_photo_parser.add_argument('photo', help='Photo file path or URL')
    send_photo_parser.add_argument('caption', nargs='?', default='', help='Photo caption')
    send_photo_parser.add_argument('--parse-mode', choices=['Markdown', 'HTML'], help='Parse mode')
    send_photo_parser.add_argument('--disable-notification', action='store_true', help='Send silently')
    send_photo_parser.add_argument('--reply-to', type=int, help='Reply to message ID')
    
    # Send document command
    send_document_parser = subparsers.add_parser('send-document', help='Send document')
    send_document_parser.add_argument('chat_id', help='Chat ID or username')
    send_document_parser.add_argument('document', help='Document file path or URL')
    send_document_parser.add_argument('caption', nargs='?', default='', help='Document caption')
    send_document_parser.add_argument('--parse-mode', choices=['Markdown', 'HTML'], help='Parse mode')
    send_document_parser.add_argument('--disable-notification', action='store_true', help='Send silently')
    send_document_parser.add_argument('--reply-to', type=int, help='Reply to message ID')
    
    # Send location command
    send_location_parser = subparsers.add_parser('send-location', help='Send location')
    send_location_parser.add_argument('chat_id', help='Chat ID or username')
    send_location_parser.add_argument('latitude', type=float, help='Latitude')
    send_location_parser.add_argument('longitude', type=float, help='Longitude')
    send_location_parser.add_argument('--disable-notification', action='store_true', help='Send silently')
    send_location_parser.add_argument('--reply-to', type=int, help='Reply to message ID')
    
    # Send contact command
    send_contact_parser = subparsers.add_parser('send-contact', help='Send contact')
    send_contact_parser.add_argument('chat_id', help='Chat ID or username')
    send_contact_parser.add_argument('phone_number', help='Phone number')
    send_contact_parser.add_argument('first_name', help='First name')
    send_contact_parser.add_argument('last_name', nargs='?', default='', help='Last name')
    send_contact_parser.add_argument('--disable-notification', action='store_true', help='Send silently')
    send_contact_parser.add_argument('--reply-to', type=int, help='Reply to message ID')
    
    # Delete message command
    delete_parser = subparsers.add_parser('delete-message', help='Delete message')
    delete_parser.add_argument('chat_id', help='Chat ID or username')
    delete_parser.add_argument('message_id', type=int, help='Message ID to delete')
    
    # Pin message command
    pin_parser = subparsers.add_parser('pin-message', help='Pin message')
    pin_parser.add_argument('chat_id', help='Chat ID or username')
    pin_parser.add_argument('message_id', type=int, help='Message ID to pin')
    pin_parser.add_argument('--disable-notification', action='store_true', help='Pin silently')
    
    # Unpin message command
    unpin_parser = subparsers.add_parser('unpin-message', help='Unpin message')
    unpin_parser.add_argument('chat_id', help='Chat ID or username')
    unpin_parser.add_argument('message_id', nargs='?', type=int, help='Message ID to unpin (optional)')
    
    # Bot info command
    subparsers.add_parser('bot-info', help='Get bot information')
    
    # Chat info command
    chat_info_parser = subparsers.add_parser('chat-info', help='Get chat information')
    chat_info_parser.add_argument('chat_id', help='Chat ID or username')
    
    # Get updates command
    get_updates_parser = subparsers.add_parser('get-updates', help='Get updates')
    get_updates_parser.add_argument('--offset', type=int, help='Offset')
    get_updates_parser.add_argument('--limit', type=int, help='Limit')
    get_updates_parser.add_argument('--timeout', type=int, help='Timeout')
    
    # Download file command
    download_file_parser = subparsers.add_parser('download-file', help='Download file by ID')
    download_file_parser.add_argument('file_id', help='File ID')
    download_file_parser.add_argument('--save-path', help='Save path (default: current directory)')
    
    # Process updates command
    process_updates_parser = subparsers.add_parser('process-updates', help='Process and download received files')
    process_updates_parser.add_argument('--download-dir', help='Download directory (default: assets/telegram_downloads)')
    process_updates_parser.add_argument('--offset', type=int, help='Update offset to start from')
    
    # Send voice message command (TTS)
    send_voice_parser = subparsers.add_parser('send-voice', help='Send voice message (text-to-speech)')
    send_voice_parser.add_argument('chat_id', help='Chat ID or username')
    send_voice_parser.add_argument('text', help='Text to convert to speech')
    send_voice_parser.add_argument('--voice', default='zh-CN-XiaoxiaoNeural', help='Voice name (default: zh-CN-XiaoxiaoNeural)')
    send_voice_parser.add_argument('--rate', default='+0%', help='Speech rate (default: +0%)')
    send_voice_parser.add_argument('--pitch', default='+0Hz', help='Speech pitch (default: +0Hz)')
    send_voice_parser.add_argument('--disable-notification', action='store_true', help='Send silently')
    send_voice_parser.add_argument('--reply-to', type=int, help='Reply to message ID')
    
    # List voices command
    subparsers.add_parser('list-voices', help='List available TTS voices')
    
    # Transcribe voice command
    transcribe_parser = subparsers.add_parser('transcribe-voice', help='Transcribe voice message to text')
    transcribe_parser.add_argument('file_id', help='Voice file ID')
    transcribe_parser.add_argument('--api-key', help='OpenAI API key (default: OPENAI_API_KEY env var)')
    transcribe_parser.add_argument('--language', help='Language code (e.g., zh, en, ja)')
    
    # Process voice updates command
    process_voice_parser = subparsers.add_parser('process-voice-updates', help='Process updates and transcribe voice messages')
    process_voice_parser.add_argument('--download-dir', help='Download directory (default: assets/telegram_downloads)')
    process_voice_parser.add_argument('--offset', type=int, help='Update offset to start from')
    process_voice_parser.add_argument('--transcribe', action='store_true', help='Transcribe voice messages')
    process_voice_parser.add_argument('--api-key', help='OpenAI API key (default: OPENAI_API_KEY env var)')
    process_voice_parser.add_argument('--language', help='Language code for transcription (e.g., zh, en, ja)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        client = TelegramClient()
        
        if args.command == 'send':
            reply_markup = None
            if args.keyboard:
                try:
                    reply_markup = json.loads(args.keyboard)
                except json.JSONDecodeError:
                    print('Error: Invalid JSON format for keyboard')
                    return
            
            result = client.send_message(
                chat_id=args.chat_id,
                text=args.message,
                parse_mode=args.parse_mode,
                disable_web_page_preview=args.disable_web_page_preview,
                disable_notification=args.disable_notification,
                reply_to_message_id=args.reply_to,
                reply_markup=reply_markup
            )
        
        elif args.command == 'send-photo':
            result = client.send_photo(
                chat_id=args.chat_id,
                photo=args.photo,
                caption=args.caption if args.caption else None,
                parse_mode=args.parse_mode,
                disable_notification=args.disable_notification,
                reply_to_message_id=args.reply_to
            )
        
        elif args.command == 'send-document':
            result = client.send_document(
                chat_id=args.chat_id,
                document=args.document,
                caption=args.caption if args.caption else None,
                parse_mode=args.parse_mode,
                disable_notification=args.disable_notification,
                reply_to_message_id=args.reply_to
            )
        
        elif args.command == 'send-location':
            result = client.send_location(
                chat_id=args.chat_id,
                latitude=args.latitude,
                longitude=args.longitude,
                disable_notification=args.disable_notification,
                reply_to_message_id=args.reply_to
            )
        
        elif args.command == 'send-contact':
            result = client.send_contact(
                chat_id=args.chat_id,
                phone_number=args.phone_number,
                first_name=args.first_name,
                last_name=args.last_name if args.last_name else None,
                disable_notification=args.disable_notification,
                reply_to_message_id=args.reply_to
            )
        
        elif args.command == 'delete-message':
            result = client.delete_message(
                chat_id=args.chat_id,
                message_id=args.message_id
            )
        
        elif args.command == 'pin-message':
            result = client.pin_chat_message(
                chat_id=args.chat_id,
                message_id=args.message_id,
                disable_notification=args.disable_notification
            )
        
        elif args.command == 'unpin-message':
            result = client.unpin_chat_message(
                chat_id=args.chat_id,
                message_id=args.message_id
            )
        
        elif args.command == 'bot-info':
            result = client.get_me()
        
        elif args.command == 'chat-info':
            result = client.get_chat(args.chat_id)
        
        elif args.command == 'get-updates':
            result = client.get_updates(
                offset=args.offset,
                limit=args.limit,
                timeout=args.timeout
            )
        
        elif args.command == 'download-file':
            result = client.download_file(
                file_id=args.file_id,
                save_path=args.save_path
            )
        
        elif args.command == 'process-updates':
            result = client.process_updates(
                download_dir=args.download_dir,
                offset=args.offset
            )
        
        elif args.command == 'send-voice':
            result = client.send_voice_message(
                chat_id=args.chat_id,
                text=args.text,
                voice=args.voice,
                rate=args.rate,
                pitch=args.pitch,
                disable_notification=args.disable_notification,
                reply_to_message_id=args.reply_to
            )
        
        elif args.command == 'list-voices':
            result = client.list_voices()
        
        elif args.command == 'transcribe-voice':
            result = client.transcribe_voice(
                file_id=args.file_id,
                api_key=args.api_key,
                language=args.language
            )
        
        elif args.command == 'process-voice-updates':
            result = client.process_voice_updates(
                download_dir=args.download_dir,
                offset=args.offset,
                transcribe=args.transcribe,
                api_key=args.api_key,
                language=args.language
            )
        
        if result.get('success'):
            print('Success!')
            print(json.dumps(result.get('data'), indent=2, ensure_ascii=False))
        else:
            print(f'Error: {result.get("error")}')
            if result.get('error_code'):
                print(f'Error Code: {result.get("error_code")}')
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')


if __name__ == '__main__':
    main()