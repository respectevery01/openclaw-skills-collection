---
name: ai_aggregator
description: AI API aggregator for intelligent routing to different AI services based on task requirements and cost optimization
author: Jask
author_url: https://jask.dev
github: https://github.com/respectevery01
twitter: jaskdon
---

# AI Aggregator Skill

## Overview

AI Aggregator provides intelligent routing to different AI services based on task requirements, cost optimization, and performance considerations. This skill helps AI agents choose the most appropriate API for each task while minimizing token usage and costs.

## Available AI APIs

### 1. DeepSeek API
**Environment Variable**: `DEEPSEEK_API_KEY`

**Best For**:
- Chinese language tasks
- Code generation and debugging
- Technical documentation
- Mathematical reasoning
- Cost-sensitive tasks (very affordable)

**Strengths**:
- Excellent Chinese language understanding
- Strong coding capabilities
- Very cost-effective
- Fast response times

**Use When**:
- User requests in Chinese
- Need code generation or debugging
- Budget is a concern
- Simple to moderate complexity tasks

**Avoid When**:
- Complex multi-step reasoning
- Highly creative tasks
- Need for advanced reasoning

### 2. OpenAI API (GPT-4)
**Environment Variable**: `OPENAI_API_KEY`

**Best For**:
- Complex reasoning tasks
- Multi-step problem solving
- Advanced code generation
- Creative writing
- High-quality output requirements

**Strengths**:
- Superior reasoning capabilities
- Excellent code generation
- Strong creative abilities
- Wide range of capabilities

**Use When**:
- Complex problem solving required
- Need highest quality output
- Budget is not a constraint
- Multi-step reasoning needed

**Avoid When**:
- Simple tasks (overkill)
- Cost is a major concern
- Chinese language tasks (other APIs may be better)

### 3. Gemini API
**Environment Variable**: `GEMINI_API_KEY`

**Best For**:
- Multimodal tasks (text + images)
- Google ecosystem integration
- Balanced performance and cost
- General-purpose tasks

**Strengths**:
- Good multimodal capabilities
- Balanced performance
- Competitive pricing
- Strong integration with Google services

**Use When**:
- Need image analysis with text
- General-purpose tasks
- Balanced cost-performance needed
- Google ecosystem integration

**Avoid When**:
- Pure text tasks (other APIs may be more specialized)
- Need for absolute highest quality

### 4. Minimax API
**Environment Variable**: `MINIMAX_API_KEY`

**Best For**:
- Chinese language tasks
- Conversational AI
- Real-time interactions
- Cost-effective Chinese processing

**Strengths**:
- Good Chinese language support
- Fast response times
- Cost-effective for Chinese
- Real-time capabilities

**Use When**:
- Chinese conversations
- Real-time chat applications
- Budget-conscious Chinese tasks
- Simple to moderate complexity

**Avoid When**:
- Complex reasoning
- Need for advanced capabilities
- Non-Chinese languages

### 5. GLM API
**Environment Variable**: `GLM_API_KEY`

**Best For**:
- Chinese language tasks
- General-purpose AI
- Balanced cost-performance
- Enterprise applications

**Strengths**:
- Strong Chinese understanding
- Enterprise-grade reliability
- Balanced performance
- Good for business applications

**Use When**:
- Chinese language tasks
- Enterprise applications
- Need for reliability
- Balanced requirements

**Avoid When**:
- Need for cutting-edge capabilities
- Highly creative tasks
- Non-Chinese languages

### 6. Qwen API
**Environment Variable**: `QWEN_API_KEY`

**Best For**:
- Chinese language tasks
- Code generation
- Technical documentation
- Cost-effective processing

**Strengths**:
- Excellent Chinese support
- Good coding abilities
- Very cost-effective
- Fast response times

**Use When**:
- Chinese language tasks
- Code generation needed
- Budget is a concern
- Technical documentation

**Avoid When**:
- Complex multi-step reasoning
- Highly creative tasks
- Non-Chinese languages

### 7. Claude API
**Environment Variable**: `CLAUDE_API_KEY`

**Best For**:
- Complex reasoning tasks
- Long-form content generation
- Detailed analysis
- High-quality output requirements

**Strengths**:
- Excellent reasoning capabilities
- Strong long-form generation
- High-quality output
- Good at following complex instructions

**Use When**:
- Need detailed analysis
- Long-form content required
- Complex reasoning needed
- Quality is paramount

**Avoid When**:
- Simple tasks (overkill)
- Cost is a major concern
- Need for speed (can be slower)

## API Selection Strategy

### Decision Tree

```
1. Is the task in Chinese?
   YES → Use DeepSeek, GLM, or Qwen (most cost-effective)
   NO  → Go to step 2

2. Is the task simple or moderate complexity?
   YES → Use DeepSeek (most cost-effective)
   NO  → Go to step 3

3. Does the task require complex reasoning?
   YES → Use OpenAI GPT-4 or Claude
   NO  → Go to step 4

4. Is cost a major concern?
   YES → Use DeepSeek, Minimax, or Qwen
   NO  → Use OpenAI or Claude for best quality

5. Does the task involve images?
   YES → Use Gemini
   NO  → Use text-optimized API (DeepSeek, OpenAI, etc.)
```

### Cost Optimization Guidelines

**Most Cost-Effective to Most Expensive**:
1. **DeepSeek** - Very affordable, good for most tasks
2. **Minimax** - Affordable for Chinese tasks
3. **Qwen** - Affordable for Chinese and code
4. **GLM** - Balanced cost-performance
5. **Gemini** - Moderate cost, good for multimodal
6. **Claude** - Higher cost, excellent quality
7. **OpenAI GPT-4** - Highest cost, best quality

### Token Usage Optimization

**To minimize token usage**:
- Use more concise prompts
- Choose the right API for the task (don't over-engineer)
- Use streaming responses when possible
- Cache results when appropriate
- Use system prompts efficiently

## Task-Specific Recommendations

### Code Generation
**Primary**: DeepSeek, Qwen
**Fallback**: OpenAI GPT-4
**Reason**: Strong coding capabilities at lower cost

### Chinese Language Tasks
**Primary**: DeepSeek, GLM, Qwen
**Fallback**: Minimax
**Reason**: Best Chinese understanding, cost-effective

### Complex Reasoning
**Primary**: OpenAI GPT-4, Claude
**Fallback**: Gemini
**Reason**: Superior reasoning capabilities

### Creative Writing
**Primary**: Claude, OpenAI GPT-4
**Fallback**: Gemini
**Reason**: Strong creative abilities

### Multimodal Tasks
**Primary**: Gemini
**Fallback**: OpenAI GPT-4 (if available)
**Reason**: Best multimodal support

### Technical Documentation
**Primary**: DeepSeek, Qwen
**Fallback**: GLM
**Reason**: Good technical understanding, cost-effective

### Real-time Conversations
**Primary**: Minimax, DeepSeek
**Fallback**: GLM
**Reason**: Fast response times, cost-effective

### Enterprise Applications
**Primary**: GLM, OpenAI GPT-4
**Fallback**: Claude
**Reason**: Reliability and quality

## API Key Configuration

Ensure the following environment variables are set in `.env` file:

```env
# AI API Keys
DEEPSEEK_API_KEY=your_deepseek_api_key
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
MINIMAX_API_KEY=your_minimax_api_key
GLM_API_KEY=your_glm_api_key
QWEN_API_KEY=your_qwen_api_key
CLAUDE_API_KEY=your_claude_api_key
```

## Error Handling

If an API key is missing or invalid:
1. Check the `.env` file
2. Verify the API key is correctly set
3. Try alternative APIs if available
4. Provide clear error message to user

## Best Practices

1. **Start with cost-effective APIs**: Try DeepSeek, Qwen, or Minimax first
2. **Upgrade only when needed**: Use more expensive APIs only for complex tasks
3. **Monitor token usage**: Track which APIs work best for which tasks
4. **Fallback strategies**: Have backup APIs ready in case of failures
5. **User preferences**: Consider user's language and requirements

## Example Usage

```python
# Simple Chinese task - use DeepSeek
if task_language == 'chinese' and task_complexity == 'simple':
    use_api = 'deepseek'

# Complex reasoning - use OpenAI or Claude
elif task_complexity == 'complex':
    use_api = 'openai'  # or 'claude'

# Multimodal task - use Gemini
elif has_images:
    use_api = 'gemini'

# Code generation - use DeepSeek or Qwen
elif task_type == 'code_generation':
    use_api = 'deepseek'  # or 'qwen'
```

## Related Skills

- `qweather` - Weather information
- `amap` - Map services
- `travel` - Travel planning
- `web3` - Blockchain and financial analysis
