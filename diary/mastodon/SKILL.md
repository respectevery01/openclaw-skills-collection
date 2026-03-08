---
name: mastodon
description: Interact with Mastodon social media API to post statuses, read timelines, and manage account
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# Mastodon Skill

## Quick Start

This skill provides interaction with the Mastodon social media platform API. Use it when users need to post statuses, read timelines, search content, or manage their Mastodon account.

## Basic Usage

### Post a Status (Toot)
```bash
python mastodon.py --post "{status_text}" --lang {language}
```
- `status_text`: The content of the status/toot to post
- `language`: zh_cn, en_us, zh_tw, jp (default: en_us)

### Read Home Timeline
```bash
python mastodon.py --timeline home --limit {count} --lang {language}
```
- `limit`: Number of statuses to retrieve (default: 20)

### Read Public Timeline
```bash
python mastodon.py --timeline public --limit {count} --lang {language}
```

### Get Account Information
```bash
python mastodon.py --account --lang {language}
```

### Search Statuses
```bash
python mastodon.py --search "{query}" --type statuses --limit {count} --lang {language}
```

### Search Accounts
```bash
python mastodon.py --search "{query}" --type accounts --limit {count} --lang {language}
```

### Get Status Details
```bash
python mastodon.py --status {status_id} --lang {language}
```

### Delete a Status
```bash
python mastodon.py --delete {status_id} --lang {language}
```

### Reply to a Status
```bash
python mastodon.py --reply {status_id} --post "{reply_text}" --lang {language}
```

### Boost (Reblog) a Status
```bash
python mastodon.py --boost {status_id} --lang {language}
```

### Unboost a Status
```bash
python mastodon.py --unboost {status_id} --lang {language}
```

### Favorite a Status
```bash
python mastodon.py --favorite {status_id} --lang {language}
```

### Unfavorite a Status
```bash
python mastodon.py --unfavorite {status_id} --lang {language}
```

## Language Matching

Match language to user's preference:
- Chinese: `--lang zh_cn`
- English: `--lang en_us`
- Traditional Chinese: `--lang zh_tw`
- Japanese: `--lang jp`

## Error Handling

### Missing API Credentials
```
Missing MASTODON_API_URL or MASTODON_ACCESS_TOKEN in .env file
```
Inform user they need to configure Mastodon API credentials in the root .env file.

### Authentication Failed
```
Authentication failed: Invalid access token
```
Check if the access token is valid and has the required permissions.

### Rate Limit Exceeded
```
Rate limit exceeded. Please wait before making more requests.
```
Inform user about rate limits and suggest waiting before retrying.

### Status Not Found
```
Status not found: {status_id}
```
The status may have been deleted or the ID is incorrect.

### Network Errors
```
Connection error: Unable to reach Mastodon instance
```
Check network connectivity and Mastodon instance availability.

## Best Practices

1. **Respect rate limits**: Mastodon instances have rate limits to prevent abuse
2. **Use appropriate content warnings**: For sensitive content, use CW (Content Warning)
3. **Keep posts concise**: Mastodon has a character limit (typically 500 characters)
4. **Use hashtags**: Add relevant hashtags for better discoverability
5. **Check instance rules**: Different instances may have different rules and policies
6. **Handle errors gracefully**: Always check API response status before processing
7. **Respect privacy**: Don't post private information without consent

## Response Format

### Status Object
```json
{
  "id": "1234567890",
  "content": "<p>Hello, Mastodon!</p>",
  "created_at": "2026-03-08T12:00:00.000Z",
  "account": {
    "id": "9876543210",
    "username": "username",
    "display_name": "Display Name",
    "url": "https://mastodon.social/@username"
  },
  "favourites_count": 10,
  "reblogs_count": 5,
  "replies_count": 3,
  "url": "https://mastodon.social/@username/1234567890"
}
```

### Account Object
```json
{
  "id": "9876543210",
  "username": "username",
  "display_name": "Display Name",
  "note": "Bio text",
  "followers_count": 100,
  "following_count": 50,
  "statuses_count": 200,
  "url": "https://mastodon.social/@username"
}
```

## Common Scenarios

### Post a Quick Update
User wants to share a quick thought or update.
```bash
python mastodon.py --post "{status_text}" --lang {user_language}
```
Post the status and provide the URL to the user.

### Read Recent Activity
User wants to see what's happening in their timeline.
```bash
python mastodon.py --timeline home --limit 20 --lang {user_language}
```
Display recent statuses from accounts they follow.

### Search for Content
User wants to find posts about a specific topic.
```bash
python mastodon.py --search "{query}" --type statuses --limit 20 --lang {user_language}
```
Present matching statuses with relevant information.

### Engage with Content
User wants to interact with a status (reply, boost, favorite).
```bash
# Reply
python mastodon.py --reply {status_id} --post "{reply_text}" --lang {user_language}

# Boost
python mastodon.py --boost {status_id} --lang {user_language}

# Favorite
python mastodon.py --favorite {status_id} --lang {user_language}
```
Perform the action and confirm success.

### Delete a Post
User wants to remove a status they posted.
```bash
python mastodon.py --delete {status_id} --lang {user_language}
```
Confirm deletion and provide feedback.

## Limitations

- **Rate limits**: Apply based on instance configuration
- **Character limits**: Typically 500 characters per post
- **Media uploads**: Not supported in current version
- **Polls**: Not supported in current version
- **Direct messages**: Not supported in current version
- **Instance-specific features**: Some features may vary between instances
- **API version**: Uses Mastodon REST API v1/v2

## Dependencies

- Python 3.7+
- requests
- python-dotenv
- Mastodon API credentials (set in root .env file):
  - `MASTODON_API_URL`: Mastodon instance URL (e.g., https://mastodon.social)
  - `MASTODON_ACCESS_TOKEN`: OAuth access token
  - `MASTODON_CLIENT_ID`: OAuth client ID (optional)
  - `MASTODON_CLIENT_SECRET`: OAuth client secret (optional)

## Authentication Setup

To obtain Mastodon API credentials:

1. Register an application on your Mastodon instance
2. Get the client ID and client secret
3. Obtain an access token using OAuth flow
4. Add credentials to the root .env file:
   ```
   MASTODON_API_URL=https://mastodon.social
   MASTODON_ACCESS_TOKEN=your_access_token
   MASTODON_CLIENT_ID=your_client_id
   MASTODON_CLIENT_SECRET=your_client_secret
   ```

## Security Considerations

- Never commit API credentials to version control
- Use environment variables or secure configuration files
- Rotate access tokens periodically
- Follow principle of least privilege for token permissions
- Be aware of instance-specific security policies
