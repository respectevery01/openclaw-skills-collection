# Bluesky CLI Tool

A powerful command-line tool for interacting with Bluesky social network API, including posting text, images, reading timelines, and searching content.

一个强大的命令行工具，用于与Bluesky社交网络API交互，包括发布文本、图片、阅读时间线和搜索内容。

## Features / 功能特性

- **Post Text**: Share text posts with automatic mention/link/hashtag detection / 发布文本：分享文本帖子，自动检测提及/链接/标签
- **Post Images**: Upload single or multiple images (up to 4) / 发布图片：上传单张或多张图片（最多4张）
- **Multi-language Support**: Specify post languages for better feed algorithms / 多语言支持：指定帖子语言以获得更好的推荐算法
- **Reply Controls**: Control who can reply to your posts (threadgate) / 回复控制：控制谁可以回复你的帖子
- **Profile Management**: Get profile information / 账户管理：获取账户信息
- **Timeline Reading**: Read your home timeline / 时间线阅读：阅读你的主页时间线
- **Content Search**: Search for posts and users / 内容搜索：搜索帖子和用户
- **Custom API Calls**: Make direct API calls to any Bluesky endpoint / 自定义API调用：直接调用任何Bluesky API端点

## Installation / 安装

### Prerequisites / 前置要求

- Python 3.7+
- Bluesky App Password (Get from Bluesky Settings → Privacy & Security → App Passwords)
- Bluesky App密码（从Bluesky设置 → 隐私与安全 → 应用密码获取）

### Setup / 设置

1. Clone the repository or navigate to the diary directory / 克隆仓库或导航到diary目录
2. Install dependencies / 安装依赖：
   ```bash
   pip install bsky-bridge requests python-dotenv
   ```
3. Configure credentials / 配置凭据：
   
   Create or edit `.env` file in the project root / 在项目根目录创建或编辑`.env`文件：
   ```env
   BLUESKY_API_URL=https://bsky.social
   BLUESKY_HANDLE_ID=your_handle.bsky.social
   BLUESKY_CLIENT_PASSWORD_SECRET=your_app_password
   ```

## Usage / 使用方法

### Basic Syntax / 基本语法

```bash
python bluesky.py [options]
```

### Options / 选项

| Option / 选项 | Description / 描述 |
|---------------|-------------------|
| `--post TEXT` | Post text to Bluesky / 发布文本到Bluesky |
| `--image PATH` | Post single image / 发布单张图片 |
| `--images PATHS` | Post multiple images (comma-separated) / 发布多张图片（逗号分隔） |
| `--alt TEXT` | Alt text for single image / 单张图片的alt文本 |
| `--alts TEXTS` | Alt texts for multiple images (comma-separated) / 多张图片的alt文本（逗号分隔） |
| `--langs LANGS` | Post languages (comma-separated, e.g., "en,zh") / 帖子语言（逗号分隔，如"en,zh"） |
| `--reply-to TYPE` | Reply controls (nobody/mentions/following/followers) / 回复控制 |
| `--profile` | Get profile information / 获取账户信息 |
| `--profile-handle HANDLE` | Get profile for specific handle / 获取指定handle的账户信息 |
| `--timeline` | Get home timeline / 获取主页时间线 |
| `--limit NUMBER` | Limit number of results (default: 20) / 限制结果数量（默认：20） |
| `--search QUERY` | Search content / 搜索内容 |
| `--type TYPE` | Search type (posts/actors) / 搜索类型（posts/actors） |
| `--api-call ENDPOINT` | Make custom API call / 自定义API调用 |
| `--method METHOD` | API call method (GET/POST) / API调用方法（GET/POST） |
| `--params JSON` | API call parameters (JSON string) / API调用参数（JSON字符串） |
| `--json-data JSON` | API call JSON data (JSON string) / API调用JSON数据（JSON字符串） |
| `--raw` | Show raw JSON output / 显示原始JSON输出 |
| `--help` | Show help message / 显示帮助信息 |

### Reply Control Options / 回复控制选项

- `nobody`: No one can reply / 没人可以回复
- `mentions`: Only mentioned users can reply / 只有被提及的用户可以回复
- `following`: Only people you follow can reply / 只有你关注的人可以回复
- `followers`: Only your followers can reply / 只有你的关注者可以回复
- Combinations: Combine multiple options with commas / 组合：用逗号组合多个选项

## Examples / 示例

### Post Text / 发布文本

Share a text post / 分享文本帖子：

```bash
# Simple post / 简单帖子
python bluesky.py --post "Hello Bluesky!"

# Post with mentions and links / 带提及和链接的帖子
python bluesky.py --post "Hey @friend.bsky.social check out https://example.com #coding"

# Multilingual post / 多语言帖子
python bluesky.py --post "Bonjour! Hello!" --langs "fr,en-US"
```

### Post Images / 发布图片

Share images with descriptions / 分享带描述的图片：

```bash
# Single image / 单张图片
python bluesky.py --post "Beautiful sunset!" --image "sunset.jpg" --alt "Orange and pink sunset over mountains"

# Multiple images / 多张图片
python bluesky.py --post "Trip highlights!" --images "photo1.jpg,photo2.jpg,photo3.jpg" --alts "Beach,Museum,Food"

# Image with language / 带语言的图片
python bluesky.py --post "Belle photo!" --image "photo.jpg" --alt "Landscape" --langs "fr,en-US"
```

### Reply Controls / 回复控制

Control who can reply to your posts / 控制谁可以回复你的帖子：

```bash
# No one can reply / 没人可以回复
python bluesky.py --post "This is a statement." --reply-to "nobody"

# Only mentioned users can reply / 只有被提及的用户可以回复
python bluesky.py --post "Hey @friend.bsky.social what do you think?" --reply-to "mentions"

# Only followers can reply / 只有关注者可以回复
python bluesky.py --post "Question for my followers" --reply-to "followers"

# Combine rules / 组合规则
python bluesky.py --post "Limited discussion" --reply-to "mentions,following"
```

### Get Profile / 获取账户信息

Get profile information / 获取账户信息：

```bash
# Get your profile / 获取你的账户信息
python bluesky.py --profile

# Get specific user's profile / 获取指定用户的账户信息
python bluesky.py --profile --profile-handle "someone.bsky.social"
```

**Output / 输出：**
```
Handle: @jaskdon
Display Name: Jask
Bio: Gambling is gambling after all, reality is reality after all, only the ideal is eternal.
Followers: 100
Following: 50
Posts: 200
```

### Read Timeline / 阅读时间线

Get your home timeline / 获取你的主页时间线：

```bash
# Get timeline / 获取时间线
python bluesky.py --timeline

# Get limited number of posts / 获取有限数量的帖子
python bluesky.py --timeline --limit 10
```

### Search Content / 搜索内容

Search for posts and users / 搜索帖子和用户：

```bash
# Search posts / 搜索帖子
python bluesky.py --search "python" --type posts --limit 10

# Search users / 搜索用户
python bluesky.py --search "john" --type actors --limit 5
```

### Custom API Calls / 自定义API调用

Make direct API calls to any Bluesky endpoint / 直接调用任何Bluesky API端点：

```bash
# GET request / GET请求
python bluesky.py --api-call "app.bsky.actor.getProfile" --method GET --params '{"actor": "someone.bsky.social"}'

# POST request / POST请求
python bluesky.py --api-call "com.atproto.repo.createRecord" --method POST --json-data '{"repo": "...", "collection": "...", "record": {...}}'
```

### Raw JSON Output / 原始JSON输出

View raw API responses / 查看原始API响应：

```bash
python bluesky.py --profile --raw
```

**Output / 输出：**
```json
{
  "did": "did:plc:xxx",
  "handle": "jaskdon.bsky.social",
  "displayName": "Jask",
  "description": "Bio text",
  "followersCount": 100,
  "followsCount": 50,
  "postsCount": 200
}
```

## API Reference / API参考

### BlueskyClient Class / BlueskyClient类

The tool uses the `BlueskyClient` class to interact with Bluesky API services.

该工具使用`BlueskyClient`类与Bluesky API服务交互。

#### Methods / 方法

- `post_text(text: str, langs: List[str] = None, reply_to: str = None) -> dict`: Post text / 发布文本
- `post_image(text: str, image_path: str, alt_text: str = "", langs: List[str] = None, reply_to: str = None) -> dict`: Post single image / 发布单张图片
- `post_images(text: str, image_paths: List[str], alt_texts: List[str], langs: List[str] = None, reply_to: str = None) -> dict`: Post multiple images / 发布多张图片
- `get_profile(handle: str = None) -> dict`: Get profile information / 获取账户信息
- `get_timeline(limit: int = 20, cursor: str = None) -> dict`: Get timeline / 获取时间线
- `search(query: str, search_type: str = "posts", limit: int = 20) -> dict`: Search content / 搜索内容
- `api_call(endpoint: str, method: str = "GET", json_data: dict = None, params: dict = None) -> dict`: Make custom API call / 自定义API调用
- `logout()`: Logout and clear session / 登出并清除会话

## Error Handling / 错误处理

The tool provides clear error messages for common issues:

该工具为常见问题提供清晰的错误消息：

- **Missing Credentials**: "Missing BLUESKY_HANDLE_ID or BLUESKY_CLIENT_PASSWORD_SECRET in .env file"
- **Authentication Failed**: "Authentication failed: Invalid handle or app password"
- **Rate Limit Exceeded**: "Rate limit exceeded. Please wait before making more requests"
- **Image Upload Failed**: "Image upload failed: Image too large or invalid format"
- **Network Errors**: Displayed with connection details / 显示连接详情

## Image Processing / 图片处理

Images are automatically processed before upload:

图片在上传前会自动处理：

- **Max size**: 1 MB (auto-compressed if larger) / 最大大小：1MB（超过会自动压缩）
- **Max dimensions**: 3840x2160 (auto-resized if larger) / 最大尺寸：3840x2160（超过会自动调整）
- **EXIF data**: Automatically stripped for privacy / EXIF数据：自动删除以保护隐私
- **Formats**: JPEG, PNG (transparency preserved) / 格式：JPEG、PNG（保留透明度）

## Project Structure / 项目结构

```
diary/
├── bluesky/
│   ├── bluesky_cli.py       # Main CLI tool / 主CLI工具
│   └── bluesky_client.py    # API client / API客户端
├── bluesky.py               # Launch script / 启动脚本
└── references/
    └── README.md            # This file / 本文件
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

- [Bluesky Documentation](https://docs.bsky.app/)
- [AT Protocol Documentation](https://atproto.com/)
- [GitHub Issues](https://github.com/yourusername/yourrepo/issues)

## Changelog / 更新日志

### Version 1.0.0 / 版本1.0.0

- Initial release / 初始版本
- Support for posting text and images / 支持发布文本和图片
- Multi-language support / 多语言支持
- Reply controls (threadgate) / 回复控制
- Timeline reading / 时间线阅读
- Content search / 内容搜索
- Custom API calls / 自定义API调用
- Automatic image processing / 自动图片处理

## Acknowledgments / 致谢

- [Bluesky](https://bsky.social/) for providing the social network platform
- [bsky-bridge](https://pypi.org/project/bsky-bridge/) for the Python library
- [AT Protocol](https://atproto.com/) for the underlying protocol

---

Made with ❤️ by the development team
由开发团队用❤️制作
