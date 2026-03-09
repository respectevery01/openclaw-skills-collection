---
name: telegram
description: Telegram Bot integration for sending messages, managing channels, text-to-speech, speech-to-text, and interacting with Telegram API
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# Telegram Bot Skill

## Overview

Telegram Bot skill provides comprehensive integration with Telegram Bot API for sending messages, managing channels, text-to-speech (TTS), speech-to-text (STT), and interacting with Telegram services. Use this skill when users need to send notifications, manage Telegram channels, convert text to voice, transcribe voice messages, or integrate Telegram messaging into their workflows.

## Quick Start

### Prerequisites

- Telegram Bot Token (Get from [@BotFather](https://t.me/botfather))
- Python 3.7+
- Required dependencies: `requests`, `python-dotenv`
- Optional for TTS: `edge-tts>=6.1.0`
- Optional for STT: `openai>=1.0.0` and `OPENAI_API_KEY` in environment

### Installation

1. Set up environment variables in `.env` file:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   # Optional for STT:
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. Install dependencies:
   ```bash
   # Basic dependencies
   pip install requests python-dotenv
   
   # For TTS (text-to-speech)
   pip install edge-tts>=6.1.0
   
   # For STT (speech-to-text)
   pip install openai>=1.0.0
   ```

## Basic Usage

### Send Text Message

```bash
python telegram.py send <chat_id> <message>
```

**Example**:
```bash
python telegram.py send 123456789 "Hello from Telegram Bot!"
```

### Send Message with Parse Mode

```bash
python telegram.py send <chat_id> <message> --parse-mode <mode>
```

**Parse modes**:
- `Markdown` - Markdown formatting
- `HTML` - HTML formatting
- `None` - Plain text (default)

**Example**:
```bash
python telegram.py send 123456789 "*Bold text* and _italic text_" --parse-mode Markdown
```

### Send Photo

```bash
python telegram.py send-photo <chat_id> <photo_path> [caption]
```

**Example**:
```bash
python telegram.py send-photo 123456789 "path/to/photo.jpg" "Beautiful sunset!"
```

### Send Document

```bash
python telegram.py send-document <chat_id> <document_path> [caption]
```

**Example**:
```bash
python telegram.py send-document 123456789 "path/to/file.pdf" "Important document"
```

### Get Bot Information

```bash
python telegram.py bot-info
```

### Get Chat Information

```bash
python telegram.py chat-info <chat_id>
```

### Get Updates

```bash
python telegram.py get-updates
```

### Download File

```bash
python telegram.py download-file <file_id> [options]
```

**Options**:
- `--save-path`: Save path (default: current directory)

**Example**:
```bash
python telegram.py download-file "AgACAgUAAxkDAAMMaa08NVZvZLYnYKheatwcO_7oXtcAAvwMaxuxFXBVqo0RpyylgeEBAAMCAANzAAM6BA" --save-path "./downloaded_photo.jpg"
```

### Process Updates and Download Files

```bash
python telegram.py process-updates [options]
```

**Options**:
- `--download-dir`: Download directory (default: assets/telegram_downloads)
- `--offset`: Update offset to start from

**Example**:
```bash
# Process all pending updates and download files
python telegram.py process-updates

# Process updates from specific offset
python telegram.py process-updates --offset 584268297

# Use custom download directory
python telegram.py process-updates --download-dir "./my_downloads"
```

**File Organization**:
Files are automatically organized by type in the download directory:
- `photos/` - Photos sent as messages
- `images/` - Image documents
- `videos/` - Videos
- `audio/` - Audio files and voice messages
- `archives/` - Archive files (zip, rar, 7z)
- `documents/` - Documents (pdf, doc, docx, txt, xls, xlsx)
- `other/` - Other file types

**Example file structure**:
```
assets/telegram_downloads/
├── photos/
│   ├── photo_20260308_170530.jpg
│   └── photo_20260308_171245.jpg
├── images/
│   └── screenshot.png
├── videos/
│   └── video_20260308_171000.mp4
├── audio/
│   ├── voice_20260308_170000.ogg
│   └── music.mp3
├── archives/
│   └── backup.zip
├── documents/
│   ├── report.pdf
│   └── notes.txt
└── other/
    └── unknown_file.bin
```

### Send Voice Message (Text-to-Speech)

```bash
python telegram.py send-voice <chat_id> <text> [options]
```

**Options**:
- `--voice`: Voice name (default: zh-CN-XiaoxiaoNeural)
- `--rate`: Speech rate (default: +0%)
- `--pitch`: Speech pitch (default: +0Hz)
- `--disable-notification`: Send silently
- `--reply-to`: Reply to message ID

**Examples**:
```bash
# Send voice message with default voice
python telegram.py send-voice 123456789 "Hello, this is a voice message!"

# Send voice message with custom voice
python telegram.py send-voice 123456789 "你好，这是语音消息" --voice zh-CN-YunxiNeural

# Send voice message with faster rate
python telegram.py send-voice 123456789 "This is a fast message" --rate "+20%"

# Send voice message with higher pitch
python telegram.py send-voice 123456789 "This is a high pitch message" --pitch "+10Hz"
```

### List Available Voices

```bash
python telegram.py list-voices
```

This command lists all available TTS voices with their names, languages, and genders.

**Popular Chinese Voices**:
- `zh-CN-XiaoxiaoNeural` - Female, standard (default)
- `zh-CN-YunxiNeural` - Male, standard
- `zh-CN-XiaoyiNeural` - Female, child
- `zh-CN-YunjianNeural` - Male, standard

**Popular English Voices**:
- `en-US-JennyNeural` - Female, standard
- `en-US-GuyNeural` - Male, standard
- `en-GB-SoniaNeural` - Female, UK English

### Transcribe Voice Message (Speech-to-Text)

```bash
python telegram.py transcribe-voice <file_id> [options]
```

**Options**:
- `--api-key`: OpenAI API key (default: OPENAI_API_KEY env var)
- `--language`: Language code (e.g., zh, en, ja)

**Examples**:
```bash
# Transcribe voice message
python telegram.py transcribe-voice "AwACAgUAAxkDAAMPaa0-nkc_5jH0lIL1UoZ62yDCj-AAAm8jAAKxFXBVisMQTEPHEbg6BA"

# Transcribe with language specified
python telegram.py transcribe-voice "AwACAgUAAxkDAAMPaa0-nkc_5jH0lIL1UoZ62yDCj-AAAm8jAAKxFXBVisMQTEPHEbg6BA" --language zh

# Transcribe with custom API key
python telegram.py transcribe-voice "AwACAgUAAxkDAAMPaa0-nkc_5jH0lIL1UoZ62yDCj-AAAm8jAAKxFXBVisMQTEPHEbg6BA" --api-key "your-api-key"
```

### Process Voice Updates with Transcription

```bash
python telegram.py process-voice-updates [options]
```

**Options**:
- `--download-dir`: Download directory (default: assets/telegram_downloads)
- `--offset`: Update offset to start from
- `--transcribe`: Transcribe voice messages
- `--api-key`: OpenAI API key (default: OPENAI_API_KEY env var)
- `--language`: Language code for transcription (e.g., zh, en, ja)

**Examples**:
```bash
# Process updates and transcribe voice messages
python telegram.py process-voice-updates --transcribe

# Process with language specified
python telegram.py process-voice-updates --transcribe --language zh

# Process from specific offset
python telegram.py process-voice-updates --transcribe --offset 584268298
```

**Note**: This command processes all pending updates, downloads voice messages, and optionally transcribes them to text using OpenAI's Whisper model.

## Advanced Features

### Send Message with Options

```bash
python telegram.py send <chat_id> <message> [options]
```

**Options**:
- `--parse-mode`: Parse mode (Markdown/HTML)
- `--disable-web-page-preview`: Disable link previews
- `--disable-notification`: Send silently
- `--reply-to`: Reply to message ID
- `--keyboard`: Send custom keyboard (JSON)

**Example**:
```bash
python telegram.py send 123456789 "Choose an option:" --keyboard '[["Option 1", "Option 2"], ["Option 3"]]'
```

### Send Location

```bash
python telegram.py send-location <chat_id> <latitude> <longitude>
```

**Example**:
```bash
python telegram.py send-location 123456789 40.7128 -74.0060
```

### Send Contact

```bash
python telegram.py send-contact <chat_id> <phone_number> <first_name> [last_name]
```

**Example**:
```bash
python telegram.py send-contact 123456789 "+1234567890" "John" "Doe"
```

### Delete Message

```bash
python telegram.py delete-message <chat_id> <message_id>
```

**Example**:
```bash
python telegram.py delete-message 123456789 123
```

### Pin Message

```bash
python telegram.py pin-message <chat_id> <message_id> [options]
```

**Options**:
- `--disable-notification`: Pin silently

**Example**:
```bash
python telegram.py pin-message 123456789 123 --disable-notification
```

### Unpin Message

```bash
python telegram.py unpin-message <chat_id> [message_id]
```

**Example**:
```bash
python telegram.py unpin-message 123456789 123
```

## Use Cases

### Weather Notifications

Send weather updates to Telegram:

```bash
# Get weather and send to Telegram
python ../qweather/weather.py 北京 | python telegram.py send 123456789
```

### Travel Updates

Send travel plan updates:

```bash
python telegram.py send 123456789 "Your trip to Beijing starts tomorrow! Weather: Sunny, 25°C"
```

### System Alerts

Send system notifications:

```bash
python telegram.py send 123456789 "⚠️ System Alert: Server maintenance at 2:00 AM"
```

### Voice Messages (TTS)

Send voice messages for accessibility or convenience:

```bash
# Send voice message in Chinese
python telegram.py send-voice 123456789 "你好，这是一条语音消息" --voice zh-CN-XiaoxiaoNeural

# Send voice message in English
python telegram.py send-voice 123456789 "Hello, this is a voice message" --voice en-US-JennyNeural

# Send voice message with custom speed
python telegram.py send-voice 123456789 "This is a fast voice message" --rate "+20%"
```

### Voice Transcription (STT)

Transcribe received voice messages to text:

```bash
# Transcribe a specific voice message
python telegram.py transcribe-voice "AwACAgUAAxkBAAMRaa0-_uN54GquSrqjxU1frkB8j7gAAnIjAAKxFXBVHCMVawjXs6Q6BA" --language zh

# Process all updates and transcribe voice messages
python telegram.py process-voice-updates --transcribe --language zh
```

### Automated Voice Response

Create an automated voice response system:

```bash
# 1. Get user's voice message
python telegram.py get-updates

# 2. Transcribe the voice message
python telegram.py transcribe-voice <voice_file_id> --language zh

# 3. Process the text (e.g., with AI)
# 4. Send voice response
python telegram.py send-voice <chat_id> "<response_text>" --voice zh-CN-XiaoxiaoNeural
```

### Daily Reports

Send daily summaries:

```bash
python telegram.py send 123456789 "📊 Daily Report: 5 new users, 12 transactions completed"
```

## Error Handling

The bot provides clear error messages for common issues:

- **Invalid Token**: "Invalid bot token. Please check TELEGRAM_BOT_TOKEN in .env file"
- **Invalid Chat ID**: "Invalid chat ID. Please provide a valid chat ID"
- **File Not Found**: "File not found: <file_path>"
- **Network Error**: "Network error: <error_message>"
- **API Error**: "Telegram API error: <error_code> - <error_description>"

## Getting Chat ID

To send messages, you need a chat ID:

1. Start a conversation with your bot
2. Run: `python telegram.py get-updates`
3. Find your chat ID in the response (look for `"chat": {"id": 123456789}`)

## Best Practices

1. **Error Handling**: Always check for errors in API responses
2. **Rate Limiting**: Telegram has rate limits (30 messages per second)
3. **Message Length**: Keep messages under 4096 characters
4. **File Size**: Photos max 10MB, documents max 50MB
5. **Security**: Never expose your bot token
6. **Webhook**: For production, use webhooks instead of polling

## Related Skills

- `qweather` - Weather information for notifications
- `amap` - Location services for sending coordinates
- `travel` - Travel planning updates
- `bluesky` - Cross-platform social media posting
- `mastodon` - Cross-platform social media posting

## API Reference

### TelegramClient Class

Main client for interacting with Telegram Bot API.

#### Methods

- `send_message(chat_id: str, text: str, **kwargs) -> dict`: Send text message
- `send_photo(chat_id: str, photo: str, caption: str = None, **kwargs) -> dict`: Send photo
- `send_document(chat_id: str, document: str, caption: str = None, **kwargs) -> dict`: Send document
- `send_location(chat_id: str, latitude: float, longitude: float, **kwargs) -> dict`: Send location
- `send_contact(chat_id: str, phone_number: str, first_name: str, last_name: str = None, **kwargs) -> dict`: Send contact
- `delete_message(chat_id: str, message_id: int) -> dict`: Delete message
- `pin_chat_message(chat_id: str, message_id: int, **kwargs) -> dict`: Pin message
- `unpin_chat_message(chat_id: str, message_id: int = None) -> dict`: Unpin message
- `get_me() -> dict`: Get bot information
- `get_chat(chat_id: str) -> dict`: Get chat information
- `get_updates(**kwargs) -> dict`: Get updates

## Troubleshooting

### Common Issues

**"Invalid bot token"**:
- Verify TELEGRAM_BOT_TOKEN in .env file
- Get a new token from @BotFather if needed

**"Chat not found"**:
- Verify chat ID is correct
- Ensure user has started a conversation with the bot
- Check bot has permission to send messages

**"File too large"**:
- Compress images before sending
- Use document for files larger than 10MB
- Check Telegram file size limits

**"Rate limit exceeded"**:
- Implement rate limiting in your code
- Use delays between messages
- Consider using webhooks for high-volume messaging

## Multi-language Support

The skill supports multi-language messages. Send messages in any language supported by Telegram.

## Security Notes

- Never commit bot tokens to version control
- Use environment variables for sensitive data
- Implement proper error handling
- Validate user input
- Use HTTPS for webhook URLs

## License

This project is licensed under the GNU General Public License v3 - see the [LICENSE](../../../LICENSE) file for details.