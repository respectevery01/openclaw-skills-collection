# 和风天气查询工具

基于和风天气API的天气查询工具，支持实时天气、天气预报、空气质量查询等功能。

## 功能特性

- 🌤️ 实时天气查询
- 📅 3天/7天天气预报
- 🌫️ 空气质量监测
- 📊 生活指数查询
- 🔍 城市搜索功能

## 配置要求

在 `.env` 文件中配置以下参数：

```bash
QWEATHER_API_KEY=your_api_key
QWEATHER_API_URL=your_api_url
QWEATHER_PROJECT_ID=your_project_id
```

## 使用方法

### 1. 基础查询

```bash
# 查询北京天气
python weather_cli.py 北京

# 使用城市ID查询
python weather_cli.py --location-id 101010100
```

### 2. 完整天气信息

```bash
# 显示完整天气信息（实时+预报+空气质量）
python weather_cli.py 北京 --all
```

### 3. 特定功能

```bash
# 只显示3天预报
python weather_cli.py 北京 --forecast 3

# 只显示7天预报
python weather_cli.py 北京 --forecast 7

# 只显示空气质量
python weather_cli.py 北京 --air
```

### 4. 城市搜索

```bash
# 搜索城市
python weather_cli.py --search 北京
```

### 5. 编程方式使用

```python
from qweather_client import QWeatherClient

client = QWeatherClient()

# 获取实时天气
weather = client.get_current_weather("101010100")

# 获取3天预报
forecast = client.get_3day_forecast("101010100")

# 获取空气质量
air_quality = client.get_air_quality("101010100")

# 搜索城市
search_result = client.search_location("北京")
```

## 示例输出

```
查询地点: 北京

🌤️  实时天气信息
温度: 15°C
体感温度: 14°C
天气状况: 晴
风向: 西北风
风力等级: 2级
湿度: 45%
能见度: 15公里

📅 未来3天天气预报

11月15日:
  白天: 晴 8°C ~ 18°C
  夜晚: 多云
  风向: 西北风 2级

11月16日:
  白天: 多云 10°C ~ 20°C
  夜晚: 阴
  风向: 东南风 1级

🌫️  空气质量信息
AQI指数: 45
空气质量: 优
主要污染物: PM2.5
PM2.5: 25 μg/m³
PM10: 35 μg/m³
```

## 文件说明

- `qweather_client.py` - 核心API客户端类
- `weather_cli.py` - 命令行工具
- `README.md` - 使用说明文档

## 注意事项

1. 确保 `.env` 文件中的API配置正确
2. 网络连接正常
3. API调用有频率限制，请合理使用
4. 城市ID可以通过搜索功能获取

## 👨‍💻 作者

**Jask**

- **个人网站**: https://jask.dev
- **GitHub**: https://github.com/respectevery01
- **Twitter**: [@jaskdon](https://twitter.com/jaskdon)

## 📄 许可证

本项目基于GNU General Public License v3许可证开源 - 详见 [LICENSE](../../../../LICENSE) 文件。