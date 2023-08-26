# -*- coding:utf-8 -*-
# 设置代理
import requests

url = "http://httpbin.org/ip"
proxy = {
    "http": "http://123.169.34.83"   # ip不能用
}


response = requests.get(url, proxies=proxy)
print(response.text)