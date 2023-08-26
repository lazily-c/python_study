# -*- coding:utf-8 -*-
import requests
from urllib.parse import urlencode

# 伪装
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

"""
# first：url与参数不分离，直接发起请求，简便，但是不易修改
url = "https://www.duitang.com/search/?kw=%E5%B0%91%E5%A5%B3&type=feed"


response = requests.get(url, headers=headers)
print(response.text)
"""

# second：将参数单独取出来存放至一个字典当中，在发送请求的时候可携带参数
# url = "https://www.duitang.com/search/?"
# params = {
#     "kw": "帅哥",
#     "type": "feed"
# }
#
# response = requests.get(url, params=params, headers=headers)
# print(response.text)


# third：和第二种一致，只不过采用拼接的方式来做
url = "https://www.duitang.com/search/?"
params = {
    "kw": "帅哥",
    "type": "feed"
}

# urlencode 将字典对象转化为url的请求参数
new_url = url + urlencode(params)
response = requests.get(new_url, headers=headers)
print(response.text)
