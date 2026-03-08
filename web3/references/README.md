# Web3 Tools

Web3 工具提供全面的区块链数据查询功能，包括代币信息查询和多链钱包余额追踪。工具支持多个区块链网络，包括以太坊、BSC、Solana、比特币和各种 EVM 兼容链。

## 功能

### 代币查询 (token_query.py)

查询详细的代币信息，包括：
- 实时价格数据
- 代币名称和符号
- 市值
- 24小时交易量
- 总供应量和最大供应量
- 代币小数位数
- Logo 和官方网站
- 社交媒体链接

**支持的链：**
- Ethereum
- BSC (币安智能链)
- Solana

### 钱包余额 (wallet_balance.py)

查询多链钱包余额：
- 每条链的原生代币余额
- 使用实时价格计算美元价值
- 自动检测地址类型
- 支持 EVM 链、比特币和 Solana
- ERC20 代币余额查询（仅限 EVM 链）

**支持的链：**
- EVM 链：Ethereum、BSC、Polygon、Arbitrum、Optimism、Avalanche、Base、Linea、Fantom、Cronos
- 非 EVM：Bitcoin、Solana

## 使用方法

### 代币查询

```bash
python scripts/token_query.py <链> <合约地址>
```

**示例：**
```bash
# Ethereum 代币
python scripts/token_query.py ethereum 0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683

# BSC 代币
python scripts/token_query.py bsc 0x...

# Solana 代币
python scripts/token_query.py sol So11111111111111111111111111111111111111112
```

### 钱包余额

```bash
python scripts/wallet_balance.py <钱包地址>
```

**示例：**
```bash
# EVM 钱包地址
python scripts/wallet_balance.py 0x53A0Fc074E31068CFdBD73B756458546274fEa97

# 比特币地址
python scripts/wallet_balance.py bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh

# Solana 地址
python scripts/wallet_balance.py 9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM
```

## 环境配置

在 `.env` 文件中设置环境变量：

```
OKX_API_KEY=your_api_key
OKX_API_SECRET=your_api_secret
OKX_API_PASSPHRASE=your_passphrase
ETHERSCAN_API_KEY=your_etherscan_api_key
```

## 依赖安装

```bash
pip install python-dotenv requests okx
```

## 多语言支持

工具支持多种语言：
- 英语 (en_us) - 默认
- 中文 (zh_cn)
- 日语 (jp)
- 繁体中文 (zh_tw)

可以通过命令行参数或环境变量指定语言。

## 错误处理

工具实现了全面的错误处理：
- 无效的链名称
- 无效的钱包地址
- API 请求失败
- 网络超时
- 缺少环境变量

错误响应包含描述性消息，帮助识别和解决问题。

## 地址类型检测

钱包余额工具自动检测地址类型：
- **比特币**：以 `1`、`3` 或 `bc1` 开头的地址
- **Solana**：Base58 编码的地址（32-44 个字符）
- **EVM**：以 `0x` 开头且长度为 42 个字符的地址

## 高级功能

### 多链查询

同时查询所有支持链的余额：
```python
from scripts.wallet_balance import wallet_balance

result = wallet_balance(wallet_address, show_zero=False)
```

### ERC20 代币余额

查询 EVM 链的 ERC20 代币余额：
```python
from scripts.wallet_balance import wallet_balance_with_tokens

result = wallet_balance_with_tokens(
    wallet_address,
    chain='ethereum',
    token_addresses=['0x...', '0x...']
)
```

### 自定义链选择

指定要查询的链：
```python
from scripts.wallet_balance import wallet_balance

result = wallet_balance(
    wallet_address,
    chains=['ethereum', 'bsc'],
    show_zero=True
)
```

## 数据结构

### 代币查询响应

```json
{
  "chain": "ethereum",
  "token_address": "0xEa9Bb54fC76BfD5DD2FF2f6dA641E78C230bB683",
  "price_usd": "123.45",
  "name": "Token Name",
  "symbol": "TKN",
  "market_cap": "1000000000",
  "volume_24h": "50000000",
  "total_supply": "1000000000",
  "max_supply": "1000000000",
  "decimals": "18",
  "logo_url": "https://...",
  "official_website": "https://...",
  "social_urls": {},
  "timestamp": "1700000000000"
}
```

### 钱包余额响应

```json
{
  "wallet_address": "0x53A0Fc074E31068CFdBD73B756458546274fEa97",
  "balances": [
    {
      "chain": "ethereum",
      "chain_id": "1",
      "balance": "1.5",
      "balance_raw": "1500000000000000000",
      "decimals": "18",
      "unit": "ETH",
      "price_usd": "2000.00",
      "value_usd": "3000.00"
    }
  ],
  "total_value_usd": "3000.00",
  "chain_count": 1,
  "timestamp": "1700000000000"
}
```

## 性能考虑

- 代币查询使用 OKX API 并有速率限制
- 钱包余额查询使用并行请求进行优化
- 尽可能缓存价格数据以减少 API 调用
- 超时设置防止在无响应端点上挂起

## 安全注意事项

- API 密钥仅从环境变量加载
- 不记录或存储敏感数据
- 所有 API 请求使用 HTTPS
- 查询前验证钱包地址

## 限制

- 代币查询需要 OKX API 凭证
- 某些链可能有速率限制
- 价格数据可能有轻微延迟
- 并非所有代币都有完整的元数据
- 比特币查询依赖公共 API

## 故障排除

### 常见问题

**"不支持的链"错误：**
- 验证链名称在支持的链列表中
- 检查链名称拼写（区分大小写）

**"无效的钱包地址"错误：**
- 验证地址格式符合预期的区块链
- 检查地址中的拼写错误

**API 请求失败：**
- 验证 API 密钥配置正确
- 检查网络连接
- 验证 API 端点可访问

**缺少价格数据：**
- 某些代币可能没有可用的价格数据
- 检查 CoinGecko API 状态
- 验证代币符号映射正确

## 最佳实践

1. **API 密钥管理**：保持 API 密钥安全并定期轮换
2. **错误处理**：始终检查响应中的错误
3. **速率限制**：遵守 API 速率限制以避免被阻止
4. **数据验证**：查询前验证地址
5. **缓存**：适当时缓存结果以减少 API 调用
6. **监控**：监控 API 使用率和错误率

## 相关技能

- `qweather` - 旅行规划天气信息
- `amap` - 路线规划和位置服务
- `travel` - 旅行规划集成

## 👨‍💻 作者

**Jask**

- **个人网站**: https://jask.dev
- **GitHub**: https://github.com/respectevery01
- **Twitter**: [@jaskdon](https://twitter.com/jaskdon)

## 📄 许可证

本项目基于MIT许可证开源 - 详见 [LICENSE](../../LICENSE) 文件。
