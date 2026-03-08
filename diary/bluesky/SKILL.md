---
name: bluesky
description: Interact with Bluesky social network API to post text, images, and manage account
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# Bluesky Skill

## Quick Start

This skill provides interaction with the Bluesky social network API. Use it when users need to post content, read timelines, search content, or manage their Bluesky account.

## Basic Usage

### Post Text
```bash
python bluesky.py --post "Hello Bluesky!"
```
- Mentions, links, and hashtags are automatically detected

### Post with Languages
```bash
python bluesky.py --post "Bonjour! Hello!" --langs "fr,en-US"
```
- Helps Bluesky's feed algorithms understand multilingual content

### Post Image
```bash
python bluesky.py --post "Check out this photo!" --image "/path/to/image.jpg" --alt "A beautiful sunset"
```

### Post Multiple Images
```bash
python bluesky.py --post "My photo gallery!" --images "/path/to/image1.jpg,/path/to/image2.jpg" --alts "First image,Second image"
```
- Up to 4 images per post

### Get Profile
```bash
python bluesky.py --profile
```

### Get Timeline
```bash
python bluesky.py --timeline --limit 20
```

### Search
```bash
python bluesky.py --search "python" --type posts --limit 10
```

### Reply Controls (Threadgate)
```bash
# No one can reply
python bluesky.py --post "This is a statement." --reply-to "nobody"

# Only mentioned users can reply
python bluesky.py --post "Hey @friend.bsky.social what do you think?" --reply-to "mentions"

# Only people you follow can reply
python bluesky.py --post "Question for my friends" --reply-to "following"

# Only your followers can reply
python bluesky.py --post "Followers only discussion" --reply-to "followers"

# Combine multiple rules
python bluesky.py --post "Limited discussion" --reply-to "mentions,following"
```

### Custom API Call
```bash
python bluesky.py --api-call "app.bsky.actor.getProfile" --method GET --params '{"actor": "someone.bsky.social"}'
```

## Authentication

The skill uses Bluesky credentials from the root .env file:
- `BLUESKY_API_URL`: Bluesky instance URL (e.g., https://bsky.social)
- `BLUESKY_HANDLE`: Your Bluesky handle (e.g., username.bsky.social)
- `BLUESKY_APP_PASSWORD`: Your App Password (not your main password)

To create an App Password:
1. Go to Settings → Privacy & Security → App Passwords
2. Create a new password with a descriptive name
3. Use this password instead of your main password

## Error Handling

### Missing Credentials
```
Missing BLUESKY_API_URL, BLUESKY_HANDLE, or BLUESKY_APP_PASSWORD in .env file
```
Inform user they need to configure Bluesky credentials.

### Authentication Failed
```
Authentication failed: Invalid handle or app password
```
Check if the handle and app password are correct.

### Rate Limit Exceeded
```
Rate limit exceeded. Please wait before making more requests.
```
The library automatically handles rate limits with exponential backoff.

### Image Upload Failed
```
Image upload failed: Image too large or invalid format
```
Images are automatically processed:
- Max size: 1 MB (auto-compressed if larger)
- Max dimensions: 3840x2160 (auto-resized if larger)
- Formats: JPEG, PNG (transparency preserved)
- EXIF data: Automatically stripped for privacy

## Best Practices

1. **Use App Passwords**: Never use your main Bluesky password
2. **Specify Languages**: Help feed algorithms by specifying post languages
3. **Use Alt Text**: Always provide descriptive alt text for images
4. **Respect Rate Limits**: The library handles them automatically, but be mindful
5. **Threadgate Wisely**: Use reply controls to manage conversation flow
6. **Image Optimization**: Images are automatically optimized, but start with reasonable sizes
7. **Mention Format**: Use full handle format (username.bsky.social) for mentions

## Response Format

### Post Response
```json
{
  "uri": "at://did:plc:xxx/app.bsky.feed.post/xxx",
  "cid": "bafyrei...",
  "record": {
    "text": "Hello Bluesky!",
    "createdAt": "2026-03-08T12:00:00.000Z"
  }
}
```

### Profile Response
```json
{
  "did": "did:plc:xxx",
  "handle": "username.bsky.social",
  "displayName": "Display Name",
  "description": "Bio text",
  "followersCount": 100,
  "followsCount": 50,
  "postsCount": 200
}
```

## Common Scenarios

### Quick Status Update
User wants to share a quick thought.
```bash
python bluesky.py --post "Just deployed my new app! 🚀"
```

### Share Photo
User wants to share an image with description.
```bash
python bluesky.py --post "Beautiful sunset today" --image "sunset.jpg" --alt "Orange and pink sunset over mountains"
```

### Multilingual Post
User wants to post in multiple languages.
```bash
python bluesky.py --post "Hello World! 你好世界!" --langs "en,zh"
```

### Limited Discussion
User wants to control who can reply.
```bash
python bluesky.py --post "Question for my followers" --reply-to "followers"
```

### Photo Gallery
User wants to share multiple photos.
```bash
python bluesky.py --post "Trip highlights!" --images "photo1.jpg,photo2.jpg,photo3.jpg" --alts "Beach,Museum,Food"
```

## Limitations

- **Image limit**: Maximum 4 images per post
- **Image size**: 1 MB max (auto-compressed)
- **Image dimensions**: 3840x2160 max (auto-resized)
- **Rate limits**: Apply based on Bluesky's policies
- **Session persistence**: Sessions are saved to .bsky_sessions/ directory
- **Custom API calls**: Requires knowledge of AT Protocol endpoints

## Dependencies

- Python 3.7+
- bsky-bridge
- python-dotenv
- Bluesky credentials (set in root .env file):
  - `BLUESKY_API_URL`: Bluesky instance URL
  - `BLUESKY_HANDLE`: Your Bluesky handle
  - `BLUESKY_APP_PASSWORD`: Your App Password

## Advanced Features

### Automatic Mentions, Links, and Hashtags
The library automatically detects and formats:
- Mentions: @username.bsky.social
- Links: https://example.com
- Hashtags: #coding

### Image Processing
Images are automatically processed before upload:
- Compression to 1 MB max
- Resize to 3840x2160 max
- EXIF data removal for privacy
- Aspect ratio preservation

### Rate Limit Handling
The library automatically handles rate limits:
- Detects HTTP 429 responses
- Reads Retry-After and RateLimit-Reset headers
- Exponential backoff (1s, 2s, 4s...)
- Retries up to 3 times before raising an error

### Session Persistence
Sessions are automatically saved and reused:
- Stored in .bsky_sessions/ directory
- Automatic token refresh
- Logout clears tokens and deletes session file

## Security Considerations

- Never commit App Passwords to version control
- Use environment variables or secure configuration files
- Rotate App Passwords periodically
- Use App Passwords instead of main password
- Be aware of Bluesky's security policies
- EXIF data is automatically stripped from images for privacy
