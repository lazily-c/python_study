# -*- coding:utf-8 -*-
import requests

# 发起目标请求的网站
url = "https://www.baidu.com"

# 添加伪装
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

# 向目标网站发起请求
response = requests.get(url, headers=headers)

# 解决文件中的乱码
response.encoding = "utf-8"

print(response.text)
