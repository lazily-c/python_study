# -*- coding:utf-8 -*-
import requests

# 发起目标请求的网站
url = "https://www.baidu.com"

# 向目标网站发起请求
response = requests.get(url)

# 解决文件中的乱码
response.encoding = "utf-8"

# print(response.text)
# print(response.status_code)
# print(response.url)
# print(response.request.headers)
