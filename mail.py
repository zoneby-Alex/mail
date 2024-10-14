import smtplib
import requests
import json
from email.mime.text import MIMEText
from email.header import Header
import weather

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "wiliamperez@163.com"  # 用户名
mail_pass = "VAH8Xa2N9XHSJdDw"  # 授权码

sender = mail_user  # 确保发件人邮箱与授权用户一致
receivers = ['qwy@myft.onmicrosoft.com', 
             'frankfurtlin@sina.com'
             ]  # 接收邮件的邮箱。

def get_weather():
    url = "https://api.seniverse.com/v3/weather/daily.json"
    params = {
        "key": "SrvH56GvqkG9FE6ht",
        "location": "beijing",
        "language": "zh-Hans",
        "unit": "c",
        "start": 0,
        "days": 3
    }
    
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    
    weather_info = ""
    for daily in data['results'][0]['daily']:
        date = daily['date']
        text_day = daily['text_day']
        high = daily['high']
        low = daily['low']
        weather_info += f"{date}: {text_day}, 最高气温 {high}°C, 最低气温 {low}°C\n"
    
    return weather_info

# 获取天气信息
    weather_content = get_weather()

email_content = f"""
Hello, Frankfurtlin

Here is the weather forecast for today:

{weather.get_weather()}

Have a nice day!

Alex
"""

message = MIMEText(email_content, 'plain', 'utf-8')
message['From'] = Header(sender)
message['To'] = Header("收件人", 'utf-8')
subject = '每日天气预报'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("错误：无法发送邮件", e)