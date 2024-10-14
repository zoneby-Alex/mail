import requests
import json

def get_weather(city="Nanshan"):
    # 替换成你的 API 密钥
    api_key = "b0337b4877524f55ac5231831241310"

    # 构造 API 请求 URL
    base_url = "http://api.weatherapi.com/v1"
    current_weather_endpoint = "/current.json"
    url = f"{base_url}{current_weather_endpoint}?key={api_key}&q={city}"
    # 或者
    # url = f"{base_url}{current_weather_endpoint}?key={api_key}&q={lat},{lon}"

    # 发送 HTTP GET 请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 JSON 数据
        data = json.loads(response.text)

        # 提取所需的天气信息
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        wind_speed = data["current"]["wind_kph"]

        return f"当前 {city}的温度为 {temperature} ℃，天气状况为 {condition}，风速为 {wind_speed} km/h"
    else:
        return f"请求失败，错误代码：{response.status_code}"

# 示例调用
print(get_weather())