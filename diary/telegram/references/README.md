# Telegram Bot Tool

A powerful command-line tool for interacting with Telegram Bot API, including sending messages, managing channels, and handling notifications.

一个强大的命令行工具，用于与Telegram Bot API交互，包括发送消息、管理频道和处理通知。

## Features / 功能特性

- **Send Messages**: Send text with Markdown/HTML formatting / 发送消息：发送带Markdown/HTML格式的文本
- **Send Media**: Upload photos and documents / 发送媒体：上传照片和文档
- **Send Location**: Share GPS coordinates / 发送位置：分享GPS坐标
- **Send Contact**: Share phone contacts / 发送联系人：分享电话联系人
- **Text-to-Speech (TTS)**: Convert text to voice messages / 文本转语音：将文本转换为语音消息
- **Speech-to-Text (STT)**: Transcribe voice messages to text / 语音转文本：将语音消息转录为文本
- **Message Management**: Delete, pin, and unpin messages / 消息管理：删除、置顶和取消置顶消息
- **Bot Info**: Get bot information / Bot信息：获取机器人信息
- **Chat Info**: Get chat details / 聊天信息：获取聊天详情
- **Real-time Updates**: Receive messages and updates / 实时更新：接收消息和更新
- **File Download**: Download received files / 文件下载：下载接收的文件
- **Auto Organization**: Organize files by type automatically / 自动组织：按类型自动组织文件

## Installation / 安装

### Prerequisites / 前置要求

- Python 3.7+
- Telegram Bot Token (Get from [@BotFather](https://t.me/botfather))
- Telegram Bot令牌（从[@BotFather](https://t.me/botfather)获取）

### Setup / 设置

1. Clone or navigate to diary/telegram directory / 克隆或导航到diary/telegram目录
2. Install dependencies / 安装依赖：
   ```bash
   # Basic dependencies / 基础依赖
   pip install requests python-dotenv
   
   # For TTS (text-to-speech) / 文本转语音
   pip install edge-tts>=6.1.0
   
   # For STT (speech-to-text) / 语音转文本
   pip install openai>=1.0.0
   ```
3. Configure bot token / 配置Bot令牌：
   
   Create or edit `.env` file in project root / 在项目根目录创建或编辑`.env`文件：
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   # Optional for STT / STT可选
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Getting Bot Token / 获取Bot令牌

1. Open Telegram and search for @BotFather / 打开Telegram并搜索@BotFather
2. Send `/newbot` command / 发送`/newbot`命令
3. Follow the instructions to create your bot / 按照说明创建你的bot
4. Copy the bot token / 复制bot令牌

### Getting Chat ID / 获取聊天ID

To send messages, you need a chat ID:

要发送消息，你需要聊天ID：

1. Start a conversation with your bot / 与你的bot开始对话
2. Run the following command / 运行以下命令：
   ```bash
   python telegram.py get-updates
   ```
3. Find your chat ID in the response / 在响应中找到你的聊天ID：
   ```json
   {
     "message": {
       "chat": {
         "id": 123456789,
         "type": "private"
       }
     }
   }
   ```

## Usage / 使用方法

### Basic Syntax / 基本语法

```bash
python telegram.py [command] [options]
```

### Commands / 命令

#### Send Text Message / 发送文本消息

```bash
python telegram.py send <chat_id> <message> [options]
```

**Options / 选项**:
- `--parse-mode`: Parse mode (Markdown/HTML) / 解析模式
- `--disable-web-page-preview`: Disable link previews / 禁用链接预览
- `--disable-notification`: Send silently / 静默发送
- `--reply-to`: Reply to message ID / 回复消息ID
- `--keyboard`: Custom keyboard (JSON) / 自定义键盘（JSON）

**Examples / 示例**:
```bash
# Simple message / 简单消息
python telegram.py send 123456789 "Hello from Telegram Bot!"

# With Markdown formatting / 带Markdown格式
python telegram.py send 123456789 "*Bold text* and _italic text_" --parse-mode Markdown

# With HTML formatting / 带HTML格式
python telegram.py send 123456789 "<b>Bold</b> and <i>italic</i>" --parse-mode HTML

# With custom keyboard / 带自定义键盘
python telegram.py send 123456789 "Choose an option:" --keyboard '[["Option 1", "Option 2"], ["Option 3"]]'

# Reply to message / 回复消息
python telegram.py send 123456789 "This is a reply" --reply-to 123
```

#### Send Photo / 发送照片

```bash
python telegram.py send-photo <chat_id> <photo_path> [caption] [options]
```

**Options / 选项**:
- `--parse-mode`: Parse mode for caption / 标题解析模式
- `--disable-notification`: Send silently / 静默发送
- `--reply-to`: Reply to message ID / 回复消息ID

**Examples / 示例**:
```bash
# Send photo / 发送照片
python telegram.py send-photo 123456789 "path/to/photo.jpg"

# Send photo with caption / 发送带标题的照片
python telegram.py send-photo 123456789 "path/to/photo.jpg" "Beautiful sunset!"

# Send photo with formatting / 发送带格式的照片
python telegram.py send-photo 123456789 "path/to/photo.jpg" "*Beautiful sunset!*" --parse-mode Markdown
```

#### Send Document / 发送文档

```bash
python telegram.py send-document <chat_id> <document_path> [caption] [options]
```

**Options / 选项**:
- `--parse-mode`: Parse mode for caption / 标题解析模式
- `--disable-notification`: Send silently / 静默发送
- `--reply-to`: Reply to message ID / 回复消息ID

**Examples / 示例**:
```bash
# Send document / 发送文档
python telegram.py send-document 123456789 "path/to/file.pdf"

# Send document with caption / 发送带标题的文档
python telegram.py send-document 123456789 "path/to/file.pdf" "Important document"
```

#### Send Location / 发送位置

```bash
python telegram.py send-location <chat_id> <latitude> <longitude> [options]
```

**Options / 选项**:
- `--disable-notification`: Send silently / 静默发送
- `--reply-to`: Reply to message ID / 回复消息ID

**Examples / 示例**:
```bash
# Send location / 发送位置
python telegram.py send-location 123456789 40.7128 -74.0060

# Send location silently / 静默发送位置
python telegram.py send-location 123456789 40.7128 -74.0060 --disable-notification
```

#### Send Contact / 发送联系人

```bash
python telegram.py send-contact <chat_id> <phone_number> <first_name> [last_name] [options]
```

**Options / 选项**:
- `--disable-notification`: Send silently / 静默发送
- `--reply-to`: Reply to message ID / 回复消息ID

**Examples / 示例**:
```bash
# Send contact / 发送联系人
python telegram.py send-contact 123456789 "+1234567890" "John"

# Send contact with last name / 发送带姓氏的联系人
python telegram.py send-contact 123456789 "+1234567890" "John" "Doe"
```

#### Delete Message / 删除消息

```bash
python telegram.py delete-message <chat_id> <message_id>
```

**Example / 示例**:
```bash
python telegram.py delete-message 123456789 123
```

#### Pin Message / 置顶消息

```bash
python telegram.py pin-message <chat_id> <message_id> [options]
```

**Options / 选项**:
- `--disable-notification`: Pin silently / 静默置顶

**Examples / 示例**:
```bash
# Pin message / 置顶消息
python telegram.py pin-message 123456789 123

# Pin silently / 静默置顶
python telegram.py pin-message 123456789 123 --disable-notification
```

#### Unpin Message / 取消置顶

```bash
python telegram.py unpin-message <chat_id> [message_id]
```

**Examples / 示例**:
```bash
# Unpin specific message / 取消置顶特定消息
python telegram.py unpin-message 123456789 123

# Unpin all messages / 取消置顶所有消息
python telegram.py unpin-message 123456789
```

#### Get Bot Information / 获取Bot信息

```bash
python telegram.py bot-info
```

**Output / 输出**:
```json
{
  "id": 123456789,
  "is_bot": true,
  "first_name": "My Bot",
  "username": "my_bot",
  "can_join_groups": true,
  "can_read_all_group_messages": false,
  "supports_inline_queries": false
}
```

#### Get Chat Information / 获取聊天信息

```bash
python telegram.py chat-info <chat_id>
```

**Example / 示例**:
```bash
python telegram.py chat-info 123456789
```

#### Get Updates / 获取更新

```bash
python telegram.py get-updates [options]
```

**Options / 选项**:
- `--offset`: Offset for updates / 更新偏移量
- `--limit`: Limit number of updates / 限制更新数量
- `--timeout`: Timeout for long polling / 长轮询超时

**Examples / 示例**:
```bash
# Get all updates / 获取所有更新
python telegram.py get-updates

# Get limited updates / 获取有限更新
python telegram.py get-updates --limit 10

# Get updates with timeout / 获取带超时的更新
python telegram.py get-updates --timeout 30
```

#### Download File / 下载文件

```bash
python telegram.py download-file <file_id> [options]
```

**Options / 选项**:
- `--save-path`: Save path (default: current directory) / 保存路径（默认：当前目录）

**Examples / 示例**:
```bash
# Download file / 下载文件
python telegram.py download-file "AgACAgUAAxkDAAMMaa08NVZvZLYnYKheatwcO_7oXtcAAvwMaxuxFXBVqo0RpyylgeEBAAMCAANzAAM6BA"

# Download file with custom path / 下载文件到指定路径
python telegram.py download-file "AgACAgUAAxkDAAMMaa08NVZvZLYnYKheatwcO_7oXtcAAvwMaxuxFXBVqo0RpyylgeEBAAMCAANzAAM6BA" --save-path "./downloaded_photo.jpg"
```

#### Process Updates and Download Files / 处理更新并下载文件

```bash
python telegram.py process-updates [options]
```

**Options / 选项**:
- `--download-dir`: Download directory (default: assets/telegram_downloads) / 下载目录（默认：assets/telegram_downloads）
- `--offset`: Update offset to start from / 更新偏移量

**Examples / 示例**:
```bash
# Process all pending updates and download files / 处理所有待处理的更新并下载文件
python telegram.py process-updates

# Process updates from specific offset / 从特定偏移量处理更新
python telegram.py process-updates --offset 584268297

# Use custom download directory / 使用自定义下载目录
python telegram.py process-updates --download-dir "./my_downloads"
```

**File Organization / 文件组织**:
Files are automatically organized by type in the download directory:
文件会自动按类型在下载目录中组织：

- `photos/` - Photos sent as messages / 作为消息发送的照片
- `images/` - Image documents / 图片文档
- `videos/` - Videos / 视频
- `audio/` - Audio files and voice messages / 音频文件和语音消息
- `archives/` - Archive files (zip, rar, 7z) / 压缩文件（zip, rar, 7z）
- `documents/` - Documents (pdf, doc, docx, txt, xls, xlsx) / 文档（pdf, doc, docx, txt, xls, xlsx）
- `other/` - Other file types / 其他文件类型

**Example file structure / 示例文件结构**:
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

#### Send Voice Message (TTS) / 发送语音消息（文本转语音）

```bash
python telegram.py send-voice <chat_id> <text> [options]
```

**Options / 选项**:
- `--voice`: Voice name (default: zh-CN-XiaoxiaoNeural) / 语音名称（默认：zh-CN-XiaoxiaoNeural）
- `--rate`: Speech rate (default: +0%) / 语速（默认：+0%）
- `--pitch`: Speech pitch (default: +0Hz) / 音调（默认：+0Hz）
- `--disable-notification`: Send silently / 静默发送
- `--reply-to`: Reply to message ID / 回复消息ID

**Examples / 示例**:
```bash
# Send voice message with default voice / 使用默认语音发送语音消息
python telegram.py send-voice 123456789 "Hello, this is a voice message!"

# Send voice message with custom voice / 使用自定义语音发送语音消息
python telegram.py send-voice 123456789 "你好，这是语音消息" --voice zh-CN-YunxiNeural

# Send voice message with faster rate / 发送更快的语音消息
python telegram.py send-voice 123456789 "This is a fast message" --rate "+20%"

# Send voice message with higher pitch / 发送高音调的语音消息
python telegram.py send-voice 123456789 "This is a high pitch message" --pitch "+10Hz"
```

#### List Available Voices / 列出可用语音

```bash
python telegram.py list-voices
```

This command lists all available TTS voices with their names, languages, and genders.
此命令列出所有可用的TTS语音及其名称、语言和性别。

**Popular Chinese Voices / 热门中文语音**:
- `zh-CN-XiaoxiaoNeural` - Female, standard / 女性，标准（默认）
- `zh-CN-YunxiNeural` - Male, standard / 男性，标准
- `zh-CN-XiaoyiNeural` - Female, child / 女性，儿童
- `zh-CN-YunjianNeural` - Male, standard / 男性，标准

**Popular English Voices / 热门英语语音**:
- `en-US-JennyNeural` - Female, standard / 女性，标准
- `en-US-GuyNeural` - Male, standard / 男性，标准
- `en-GB-SoniaNeural` - Female, UK English / 女性，英式英语

#### Transcribe Voice Message (Speech-to-Text) / 转录语音消息（语音转文本）

```bash
python telegram.py transcribe-voice <file_id> [options]
```

**Options / 选项**:
- `--api-key`: OpenAI API key (default: OPENAI_API_KEY env var) / OpenAI API密钥（默认：OPENAI_API_KEY环境变量）
- `--language`: Language code (e.g., zh, en, ja) / 语言代码（例如：zh, en, ja）

**Examples / 示例**:
```bash
# Transcribe voice message / 转录语音消息
python telegram.py transcribe-voice "AwACAgUAAxkDAAMPaa0-nkc_5jH0lIL1UoZ62yDCj-AAAm8jAAKxFXBVisMQTEPHEbg6BA"

# Transcribe with language specified / 指定语言转录
python telegram.py transcribe-voice "AwACAgUAAxkDAAMPaa0-nkc_5jH0lIL1UoZ62yDCj-AAAm8jAAKxFXBVisMQTEPHEbg6BA" --language zh

# Transcribe with custom API key / 使用自定义API密钥转录
python telegram.py transcribe-voice "AwACAgUAAxkDAAMPaa0-nkc_5jH0lIL1UoZ62yDCj-AAAm8jAAKxFXBVisMQTEPHEbg6BA" --api-key "your-api-key"
```

#### Process Voice Updates with Transcription / 处理语音更新并转录

```bash
python telegram.py process-voice-updates [options]
```

**Options / 选项**:
- `--download-dir`: Download directory (default: assets/telegram_downloads) / 下载目录（默认：assets/telegram_downloads）
- `--offset`: Update offset to start from / 更新偏移量
- `--transcribe`: Transcribe voice messages / 转录语音消息
- `--api-key`: OpenAI API key (default: OPENAI_API_KEY env var) / OpenAI API密钥（默认：OPENAI_API_KEY环境变量）
- `--language`: Language code for transcription (e.g., zh, en, ja) / 转录语言代码（例如：zh, en, ja）

**Examples / 示例**:
```bash
# Process updates and transcribe voice messages / 处理更新并转录语音消息
python telegram.py process-voice-updates --transcribe

# Process with language specified / 指定语言处理
python telegram.py process-voice-updates --transcribe --language zh

# Process from specific offset / 从特定偏移量处理
python telegram.py process-voice-updates --transcribe --offset 584268298
```

**Note / 注意**: This command processes all pending updates, downloads voice messages, and optionally transcribes them to text using OpenAI's Whisper model.
此命令处理所有待处理的更新，下载语音消息，并可选择使用OpenAI的Whisper模型将其转录为文本。

## Use Cases / 使用场景

### Weather Notifications / 天气通知

Send weather updates to Telegram:

向Telegram发送天气更新：

```bash
# Get weather and send to Telegram / 获取天气并发送到Telegram
python ../qweather/weather.py 北京 | python telegram.py send 123456789
```

### Travel Updates / 旅行更新

Send travel plan updates:

发送旅行计划更新：

```bash
python telegram.py send 123456789 "Your trip to Beijing starts tomorrow! Weather: Sunny, 25°C"
```

### System Alerts / 系统警报

Send system notifications:

发送系统通知：

```bash
python telegram.py send 123456789 "⚠️ System Alert: Server maintenance at 2:00 AM"
```

### Daily Reports / 每日报告

Send daily summaries:

发送每日摘要：

```bash
python telegram.py send 123456789 "📊 Daily Report: 5 new users, 12 transactions completed"
```

## Error Handling / 错误处理

The tool provides clear error messages for common issues:

该工具为常见问题提供清晰的错误消息：

- **Invalid Token**: "TELEGRAM_BOT_TOKEN not found in environment variables"
- **Invalid Chat ID**: "Chat not found"
- **File Not Found**: "File not found: <file_path>"
- **Network Error**: "Network error: <error_message>"
- **API Error**: "Telegram API error: <error_code> - <error_description>"

## Limitations / 限制

- **Message Length**: Maximum 4096 characters / 消息长度：最多4096字符
- **Photo Size**: Maximum 10MB / 照片大小：最多10MB
- **Document Size**: Maximum 50MB / 文档大小：最多50MB
- **Rate Limit**: 30 messages per second / 速率限制：每秒30条消息

## Best Practices / 最佳实践

1. **Error Handling**: Always check for errors in API responses / 始终检查API响应中的错误
2. **Rate Limiting**: Implement delays between messages / 在消息之间实现延迟
3. **Security**: Never expose bot token / 永远不要暴露bot令牌
4. **Validation**: Validate user input / 验证用户输入
5. **Testing**: Test with personal chat first / 先在个人聊天中测试

## Project Structure / 项目结构

```
diary/telegram/
├── SKILL.md              # AI skill documentation / AI技能文档
├── README.md             # This file / 本文件
├── assets/              # Asset modules / 资产模块
│   └── telegram_client.py  # API client / API客户端
└── scripts/             # Scripts / 脚本
    ├── telegram_cli.py   # Main CLI tool / 主CLI工具
    └── telegram.py      # Launch script / 启动脚本
```

## Contributing / 贡献

Contributions are welcome! Please feel free to submit a Pull Request.

欢迎贡献！请随时提交Pull Request。

## License / 许可证

This project is licensed under the MIT License - see the [LICENSE](../../../../LICENSE) file for details.

本项目基于MIT许可证开源 - 详见 [LICENSE](../../../../LICENSE) 文件。

## Support / 支持

For issues and questions, please visit:

如有问题和疑问，请访问：

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [BotFather](https://t.me/botfather)
- [GitHub Issues](https://github.com/yourusername/yourrepo/issues)

## Acknowledgments / 致谢

- [Telegram](https://telegram.org/) for providing the platform
- [BotFather](https://t.me/botfather) for bot management

---

Made with ❤️ by the development team
由开发团队用❤️制作

## 👨‍💻 作者

**Jask**

- **个人网站**: https://jask.dev
- **GitHub**: https://github.com/respectevery01
- **Twitter**: [@jaskdon](https://twitter.com/jaskdon)