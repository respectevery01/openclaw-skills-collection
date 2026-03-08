# Amap CLI Tool

A powerful command-line tool for querying Amap (Gaode Map) API services, including geocoding, POI search, weather information, and route planning.

一个强大的命令行工具，用于查询高德地图API服务，包括地理编码、POI搜索、天气信息和路线规划。

## Features / 功能特性

- **Geocoding**: Convert addresses to coordinates / 地理编码：将地址转换为坐标
- **Reverse Geocoding**: Convert coordinates to addresses / 逆地理编码：将坐标转换为地址
- **POI Search**: Search for Points of Interest / POI搜索：搜索兴趣点
- **Weather Query**: Get weather information for cities / 天气查询：获取城市天气信息
- **Route Planning**: Get driving directions / 路线规划：获取驾车路线
- **Multi-language Support**: Chinese, English, Traditional Chinese, Japanese / 多语言支持：中文、英文、繁体中文、日语
- **Raw JSON Output**: View raw API responses / 原始JSON输出：查看原始API响应

## Installation / 安装

### Prerequisites / 前置要求

- Python 3.7+
- Amap API Key (Get from [Amap Open Platform](https://lbs.amap.com/))
- 高德地图API密钥（从[高德开放平台](https://lbs.amap.com/)获取）

### Setup / 设置

1. Clone the repository or navigate to the diary directory / 克隆仓库或导航到diary目录
2. Install dependencies / 安装依赖：
   ```bash
   pip install requests python-dotenv
   ```
3. Configure API key / 配置API密钥：
   
   Create or edit `.env` file in the project root / 在项目根目录创建或编辑`.env`文件：
   ```env
   AMAP_API_KEY=your_api_key_here
   ```

## Usage / 使用方法

### Basic Syntax / 基本语法

```bash
python amap.py [options]
```

### Options / 选项

| Option / 选项 | Description / 描述 |
|---------------|-------------------|
| `--geocode ADDRESS` | Geocode address to coordinates / 将地址地理编码为坐标 |
| `--regeocode COORDS` | Reverse geocode coordinates to address / 将坐标逆地理编码为地址 |
| `--poi KEYWORDS` | Search POI by keywords / 按关键字搜索POI |
| `--city CITY` | City for POI search / POI搜索的城市 |
| `--weather CITY` | Get weather information / 获取天气信息 |
| `--direction ORIGIN DEST` | Get driving directions / 获取驾车路线 |
| `--raw` | Show raw JSON output / 显示原始JSON输出 |
| `--lang LANGUAGE` | Set language (zh_cn, en_us, zh_tw, jp) / 设置语言 |
| `--help` | Show help message / 显示帮助信息 |

### Language Options / 语言选项

- `zh_cn`: Simplified Chinese (简体中文)
- `en_us`: English (英语)
- `zh_tw`: Traditional Chinese (繁体中文)
- `jp`: Japanese (日语)

## Examples / 示例

### Geocoding / 地理编码

Convert address to coordinates / 将地址转换为坐标：

```bash
# Chinese / 中文
python amap.py --geocode "北京天安门"

# English / 英语
python amap.py --lang en_us --geocode "Beijing Tiananmen"

# Traditional Chinese / 繁体中文
python amap.py --lang zh_tw --geocode "北京天安門"

# Japanese / 日语
python amap.py --lang jp --geocode "北京天安門"
```

**Output / 输出：**
```
地址: 北京市东城区天安门
坐标: 116.397463,39.909187
省份: 北京市
城市: 北京市
区县: 东城区
```

### Reverse Geocoding / 逆地理编码

Convert coordinates to address / 将坐标转换为地址：

```bash
python amap.py --regeocode "116.397463,39.909187"
```

**Output / 输出：**
```
地址: 北京市东城区东华门街道天安门
省份: 北京市
城市: 北京市
区县: 东城区
乡镇: 东华门街道
```

### POI Search / POI搜索

Search for Points of Interest / 搜索兴趣点：

```bash
# Search coffee shops in Beijing / 在北京搜索咖啡厅
python amap.py --poi "咖啡厅" --city 北京

# Search restaurants in Shanghai / 在上海搜索餐厅
python amap.py --lang en_us --poi "restaurant" --city Shanghai
```

**Output / 输出：**
```
找到POI: 406
糖房咖啡(什刹海店) - 北京城区什刹海街道前海东沿22号3层-4层 - 116.394115,39.938976
JM Cafe咖啡(白塔寺店) - 北京城区宫门口东岔29号 - 116.362449,39.925763
...
```

### Weather Query / 天气查询

Get weather information for a city / 获取城市天气信息：

```bash
# Beijing weather / 北京天气
python amap.py --weather 北京

# Shanghai weather in English / 上海天气（英文）
python amap.py --lang en_us --weather Shanghai

# Taipei weather in Traditional Chinese / 台北天气（繁体中文）
python amap.py --lang zh_tw --weather 台北
```

**Output / 输出：**
```
城市: 北京市
天气: 霾
温度: 6°C
风向: 东南
风力: ≤3
湿度: 46%
报告时间: 2026-03-08 00:33:09
```

### Route Planning / 路线规划

Get driving directions / 获取驾车路线：

```bash
# Route from Beijing to Shanghai / 从北京到上海的路线
python amap.py --direction "116.397463,39.909187" "121.473701,31.230416"

# Route with raw output / 原始输出格式的路线
python amap.py --direction "116.397463,39.909187" "121.473701,31.230416" --raw
```

### Raw JSON Output / 原始JSON输出

View raw API responses / 查看原始API响应：

```bash
python amap.py --raw --weather 北京
```

**Output / 输出：**
```json
{
  "status": "1",
  "count": "1",
  "info": "OK",
  "infocode": "10000",
  "lives": [
    {
      "province": "北京",
      "city": "北京市",
      "adcode": "110000",
      "weather": "霾",
      "temperature": "6",
      "winddirection": "东南",
      "windpower": "≤3",
      "humidity": "46",
      "reporttime": "2026-03-08 00:33:09"
    }
  ]
}
```

## API Reference / API参考

### AmapClient Class / AmapClient类

The tool uses the `AmapClient` class to interact with Amap API services.

该工具使用`AmapClient`类与高德地图API服务交互。

#### Methods / 方法

- `geocode(address: str) -> dict`: Geocode address to coordinates / 地理编码
- `regeocode(location: str) -> dict`: Reverse geocode coordinates to address / 逆地理编码
- `search_poi(keywords: str, city: str = None) -> dict`: Search POI by keywords / 搜索POI
- `get_weather(city: str) -> dict`: Get weather information / 获取天气信息
- `get_direction(origin: str, destination: str) -> dict`: Get driving directions / 获取驾车路线

## Error Handling / 错误处理

The tool provides clear error messages for common issues:

该工具为常见问题提供清晰的错误消息：

- **Missing API Key**: "Missing AMAP_API_KEY in .env file"
- **Invalid City**: "No results found"
- **API Errors**: Displayed with error code and message / 显示错误代码和消息

## Project Structure / 项目结构

```
diary/
├── amap/
│   ├── amap_cli.py          # Main CLI tool / 主CLI工具
│   └── amap_client.py       # API client / API客户端
├── i18n/
│   ├── common/              # Common translations / 通用翻译
│   │   ├── zh_cn.json
│   │   ├── en_us.json
│   │   ├── zh_tw.json
│   │   └── jp.json
│   └── amap/               # Amap-specific translations / Amap专用翻译
│       ├── zh_cn.json
│       ├── en_us.json
│       ├── zh_tw.json
│       └── jp.json
├── amap.py                 # Launch script / 启动脚本
└── README.md               # This file / 本文件
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

- [Amap Open Platform Documentation](https://lbs.amap.com/api/)
- [GitHub Issues](https://github.com/yourusername/yourrepo/issues)

## Changelog / 更新日志

### Version 1.0.0 / 版本1.0.0

- Initial release / 初始版本
- Support for geocoding, reverse geocoding, POI search, weather, and routing / 支持地理编码、逆地理编码、POI搜索、天气和路线规划
- Multi-language support (zh_cn, en_us, zh_tw, jp) / 多语言支持
- Raw JSON output option / 原始JSON输出选项
- Comprehensive error handling / 全面的错误处理

## Acknowledgments / 致谢

- [Amap (Gaode Map)](https://lbs.amap.com/) for providing API services
- [高德地图](https://lbs.amap.com/) 提供API服务

---

Made with ❤️ by the development team
由开发团队用❤️制作

## 👨‍💻 作者

**Jask**

- **个人网站**: https://jask.dev
- **GitHub**: https://github.com/respectevery01
- **Twitter**: [@jaskdon](https://twitter.com/jaskdon)

## 📄 许可证

本项目仅供教育和个人使用。