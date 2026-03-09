# RSS Feed Reader Tool

A powerful command-line tool for fetching, searching, and managing RSS feeds from various sources.

一个强大的命令行工具，用于获取、搜索和管理来自各种来源的RSS订阅源。

## Features / 功能特性

- **Fetch Feeds**: Get RSS feed content with full details / 获取订阅源：获取RSS订阅源的完整内容
- **Search Entries**: Search for specific keywords in feeds / 搜索条目：在订阅源中搜索特定关键词
- **Latest Entries**: Get the most recent entries / 最新条目：获取最新的条目
- **Feed Info**: Get feed metadata and statistics / 订阅源信息：获取订阅源元数据和统计信息
- **Multiple Feeds**: Fetch and combine multiple feeds / 多个订阅源：获取和合并多个订阅源
- **Flexible Output**: JSON or text format / 灵活输出：JSON或文本格式
- **Save to File**: Export feed data to JSON files / 保存到文件：将订阅源数据导出到JSON文件

## Installation / 安装

### Prerequisites / 前置要求

- Python 3.7+

### Setup / 设置

1. Navigate to diary/rss directory / 导航到diary/rss目录
2. Install dependencies / 安装依赖：
   ```bash
   pip install feedparser>=6.0.0
   ```

## Basic Usage / 基本用法

### Fetch RSS Feed / 获取RSS订阅源

```bash
python rss_cli.py fetch <rss_url>
```

**Example / 示例**:
```bash
# Fetch BBC News / 获取BBC新闻
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml

# Fetch with limit / 限制条目数量
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml --limit 5

# Fetch and save to JSON / 获取并保存为JSON
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml --output news.json

# Fetch in JSON format / 以JSON格式获取
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml --format json
```

### Get Latest Entries / 获取最新条目

```bash
python rss_cli.py latest <rss_url> [options]
```

**Options / 选项**:
- `--count`: Number of latest entries (default: 5) / 最新条目数量（默认：5）

**Examples / 示例**:
```bash
# Get latest 5 entries / 获取最新5条
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml

# Get latest 10 entries / 获取最新10条
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 10
```

### Search Entries / 搜索条目

```bash
python rss_cli.py search <rss_url> <keyword> [options]
```

**Options / 选项**:
- `--limit`: Limit number of results / 限制结果数量

**Examples / 示例**:
```bash
# Search for keyword / 搜索关键词
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "technology"

# Search with limit / 限制搜索结果
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "climate" --limit 3
```

### Get Feed Information / 获取订阅源信息

```bash
python rss_cli.py info <rss_url>
```

**Example / 示例**:
```bash
python rss_cli.py info http://feeds.bbci.co.uk/news/rss.xml
```

### Fetch Multiple Feeds / 获取多个订阅源

```bash
python rss_cli.py fetch-multiple <url1> <url2> ... [options]
```

**Options / 选项**:
- `--limit`: Limit number of entries per feed / 每个订阅源的条目数量限制
- `--output`: Output file path (JSON) / 输出文件路径（JSON）

**Examples / 示例**:
```bash
# Fetch multiple feeds / 获取多个订阅源
python rss_cli.py fetch-multiple http://feeds.bbci.co.uk/news/rss.xml https://www.reddit.com/r/technology/.rss

# Fetch with limit and save / 限制数量并保存
python rss_cli.py fetch-multiple http://feeds.bbci.co.uk/news/rss.xml https://www.reddit.com/r/technology/.rss --limit 5 --output feeds.json
```

## Advanced Features / 高级功能

### Output Formats / 输出格式

```bash
# JSON output for programmatic use / JSON格式输出（程序化使用）
python rss_cli.py fetch <rss_url> --format json

# Text output for human reading / 文本格式输出（人类阅读）
python rss_cli.py fetch <rss_url> --format text
```

### Save to File / 保存到文件

```bash
# Save feed data to JSON file / 保存订阅源数据到JSON文件
python rss_cli.py fetch <rss_url> --output feed_data.json

# Save multiple feeds / 保存多个订阅源
python rss_cli.py fetch-multiple <url1> <url2> --output all_feeds.json
```

## Popular RSS Feeds / 热门RSS订阅源

### News / 新闻
- BBC News: http://feeds.bbci.co.uk/news/rss.xml
- CNN: http://rss.cnn.com/rss/edition.rss
- Reuters: https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best

### Technology / 技术
- TechCrunch: https://techcrunch.com/feed/
- Hacker News: https://news.ycombinator.com/rss
- Ars Technica: https://feeds.arstechnica.com/arstechnica/index

### Science / 科学
- Nature: https://www.nature.com/nature.rss
- Science Daily: https://www.sciencedaily.com/rss/top.xml
- NASA: https://www.nasa.gov/rss/dyn/breaking_news.rss

### Social Media / 社交媒体
- Reddit (Technology): https://www.reddit.com/r/technology/.rss
- Reddit (Programming): https://www.reddit.com/r/programming/.rss

## Use Cases / 使用场景

### News Monitoring / 新闻监控

Monitor news from multiple sources:

监控来自多个来源的新闻：

```bash
# Fetch latest news / 获取最新新闻
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 10

# Search for specific topics / 搜索特定主题
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "AI" --limit 5
```

### Blog Updates / 博客更新

Track blog updates:

跟踪博客更新：

```bash
# Get latest blog posts / 获取最新博客文章
python rss_cli.py latest https://example.com/blog/feed.xml --count 5

# Get feed information / 获取订阅源信息
python rss_cli.py info https://example.com/blog/feed.xml
```

### Aggregated Feeds / 聚合订阅源

Combine multiple feeds:

合并多个订阅源：

```bash
# Fetch from multiple sources / 从多个来源获取
python rss_cli.py fetch-multiple \
  http://feeds.bbci.co.uk/news/rss.xml \
  https://www.reddit.com/r/technology/.rss \
  https://example.com/blog/feed.xml \
  --limit 5 \
  --output aggregated.json
```

### Automated Monitoring / 自动化监控

Create automated monitoring scripts:

创建自动化监控脚本：

```bash
#!/bin/bash
# Monitor RSS feeds and send alerts / 监控RSS订阅源并发送警报

# Fetch latest entries / 获取最新条目
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 5 > latest_news.txt

# Search for keywords / 搜索关键词
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "urgent" --limit 3 > urgent_news.txt

# Send notifications (integrate with Telegram) / 发送通知（集成Telegram）
if [ -s urgent_news.txt ]; then
  python ../telegram/scripts/telegram_cli.py send <chat_id> "$(cat urgent_news.txt)"
fi
```

## Integration with Other Tools / 与其他工具集成

### RSS + Telegram

Send news updates to Telegram:

向Telegram发送新闻更新：

```bash
news=$(python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 5)
python ../telegram/scripts/telegram_cli.py send <chat_id> "$news"
```

### RSS + AI Aggregator

Summarize news with AI:

使用AI总结新闻：

```bash
news=$(python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 5 --format json)
summary=$(python ../ai_aggregator/scripts/ai_aggregator_cli.py analyze "$news")
echo "$summary"
```

## Error Handling / 错误处理

If a feed fails to load:

如果订阅源加载失败：

1. Check RSS URL is correct / 检查RSS URL是否正确
2. Verify feed is accessible / 验证订阅源是否可访问
3. Check network connectivity / 检查网络连接
4. Some feeds may require user-agent headers / 某些订阅源可能需要user-agent头（已自动处理）

## Best Practices / 最佳实践

1. **Rate Limiting**: Don't fetch feeds too frequently / 速率限制：不要过于频繁地获取订阅源
2. **Caching**: Cache feed data to reduce requests / 缓存：缓存订阅源数据以减少请求
3. **Error Handling**: Handle feed parsing errors gracefully / 错误处理：优雅地处理订阅源解析错误
4. **Validation**: Validate feed URLs before fetching / 验证：在获取前验证订阅源URL
5. **Storage**: Save feed data for offline access / 存储：保存订阅源数据以供离线访问

## Getting Help / 获取帮助

```bash
python rss_cli.py --help
python rss_cli.py fetch --help
python rss_cli.py search --help
```

## License / 许可证

This project is licensed under the GNU General Public License v3 - see the [LICENSE](../../../../LICENSE) file for details.

本项目基于GNU General Public License v3许可证开源 - 详见 [LICENSE](../../../../LICENSE) 文件。
