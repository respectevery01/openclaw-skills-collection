---
name: rss
description: RSS feed reader for fetching, searching, and managing RSS feeds from various sources
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# RSS Feed Reader Skill

## Overview

RSS Feed Reader skill provides comprehensive integration with RSS feeds for fetching, searching, and managing content from various sources. Use this skill when users need to read news, blog posts, podcasts, or any RSS-based content.

## Quick Start

### Prerequisites

- Python 3.7+
- Required dependencies: `feedparser`

### Installation

1. Install dependencies:
   ```bash
   pip install feedparser>=6.0.0
   ```

## Basic Usage

### Fetch RSS Feed

```bash
python rss_cli.py fetch <rss_url>
```

**Example**:
```bash
# Fetch BBC News RSS feed
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml

# Fetch with limit
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml --limit 5

# Fetch and save to JSON
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml --output news.json

# Fetch in JSON format
python rss_cli.py fetch http://feeds.bbci.co.uk/news/rss.xml --format json
```

### Get Latest Entries

```bash
python rss_cli.py latest <rss_url> [options]
```

**Options**:
- `--count`: Number of latest entries (default: 5)

**Examples**:
```bash
# Get latest 5 entries
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml

# Get latest 10 entries
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 10
```

### Search Entries

```bash
python rss_cli.py search <rss_url> <keyword> [options]
```

**Options**:
- `--limit`: Limit number of results

**Examples**:
```bash
# Search for keyword
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "technology"

# Search with limit
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "climate" --limit 3
```

### Get Feed Information

```bash
python rss_cli.py info <rss_url>
```

**Example**:
```bash
python rss_cli.py info http://feeds.bbci.co.uk/news/rss.xml
```

### Fetch Multiple Feeds

```bash
python rss_cli.py fetch-multiple <url1> <url2> ... [options]
```

**Options**:
- `--limit`: Limit number of entries per feed
- `--output`: Output file path (JSON)

**Examples**:
```bash
# Fetch multiple feeds
python rss_cli.py fetch-multiple http://feeds.bbci.co.uk/news/rss.xml https://www.reddit.com/r/technology/.rss

# Fetch with limit and save
python rss_cli.py fetch-multiple http://feeds.bbci.co.uk/news/rss.xml https://www.reddit.com/r/technology/.rss --limit 5 --output feeds.json
```

## Advanced Features

### Custom Output Formats

```bash
# JSON output for programmatic use
python rss_cli.py fetch <rss_url> --format json

# Text output for human reading (default)
python rss_cli.py fetch <rss_url> --format text
```

### Save to File

```bash
# Save feed data to JSON file
python rss_cli.py fetch <rss_url> --output feed_data.json

# Save multiple feeds
python rss_cli.py fetch-multiple <url1> <url2> --output all_feeds.json
```

### Search and Filter

```bash
# Search in feed
python rss_cli.py search <rss_url> "keyword"

# Limit search results
python rss_cli.py search <rss_url> "keyword" --limit 5
```

## Use Cases

### News Monitoring

Monitor news from multiple sources:

```bash
# Fetch latest news from BBC
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 10

# Search for specific topics
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "AI" --limit 5
```

### Blog Updates

Track blog updates:

```bash
# Get latest blog posts
python rss_cli.py latest https://example.com/blog/feed.xml --count 5

# Get feed information
python rss_cli.py info https://example.com/blog/feed.xml
```

### Podcast Feeds

Fetch podcast episodes:

```bash
# Fetch podcast RSS
python rss_cli.py fetch https://example.com/podcast/feed.xml --limit 10

# Search episodes
python rss_cli.py search https://example.com/podcast/feed.xml "interview"
```

### Aggregated Feeds

Combine multiple feeds:

```bash
# Fetch from multiple sources
python rss_cli.py fetch-multiple \
  http://feeds.bbci.co.uk/news/rss.xml \
  https://www.reddit.com/r/technology/.rss \
  https://example.com/blog/feed.xml \
  --limit 5 \
  --output aggregated.json
```

### Automated Monitoring

Create automated monitoring scripts:

```bash
#!/bin/bash
# Monitor RSS feeds and send alerts

# Fetch latest entries
python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 5 > latest_news.txt

# Search for keywords
python rss_cli.py search http://feeds.bbci.co.uk/news/rss.xml "urgent" --limit 3 > urgent_news.txt

# Send notifications (integrate with Telegram)
if [ -s urgent_news.txt ]; then
  python ../telegram/scripts/telegram_cli.py send <chat_id> "$(cat urgent_news.txt)"
fi
```

## Popular RSS Feeds

### News
- BBC News: http://feeds.bbci.co.uk/news/rss.xml
- CNN: http://rss.cnn.com/rss/edition.rss
- Reuters: https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best

### Technology
- TechCrunch: https://techcrunch.com/feed/
- Hacker News: https://news.ycombinator.com/rss
- Ars Technica: https://feeds.arstechnica.com/arstechnica/index

### Science
- Nature: https://www.nature.com/nature.rss
- Science Daily: https://www.sciencedaily.com/rss/top.xml
- NASA: https://www.nasa.gov/rss/dyn/breaking_news.rss

### Podcasts
- Example: https://example.com/podcast/feed.xml

### Social Media
- Reddit (Technology): https://www.reddit.com/r/technology/.rss
- Reddit (Programming): https://www.reddit.com/r/programming/.rss

## Error Handling

If a feed fails to load:
1. Check the RSS URL is correct
2. Verify the feed is accessible
3. Check network connectivity
4. Some feeds may require user-agent headers (automatically handled)

## Best Practices

1. **Rate Limiting**: Don't fetch feeds too frequently
2. **Caching**: Cache feed data to reduce requests
3. **Error Handling**: Handle feed parsing errors gracefully
4. **Validation**: Validate feed URLs before fetching
5. **Storage**: Save feed data for offline access

## Integration with Other Skills

### RSS + Telegram
```bash
# Send news updates to Telegram
news=$(python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 5)
python ../telegram/scripts/telegram_cli.py send <chat_id> "$news"
```

### RSS + AI Aggregator
```bash
# Summarize news with AI
news=$(python rss_cli.py latest http://feeds.bbci.co.uk/news/rss.xml --count 5 --format json)
summary=$(python ../ai_aggregator/scripts/ai_aggregator_cli.py analyze "$news")
echo "$summary"
```

## Getting Help

```bash
python rss_cli.py --help
python rss_cli.py fetch --help
python rss_cli.py search --help
```
