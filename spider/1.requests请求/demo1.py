# -*- coding:utf-8 -*-
import requests

# 发起目标请求的网站
url = "https://www.baidu.com"


# 向目标网站发起请求
response = requests.get(url)

# 解决文件中的乱码
response.encoding = "utf-8"

# 输出源代码，类型为字符串，非字节码
# print(response.text)

# 获取字节，媒体数据 使用此参数
# print(response.content)

# 状态码，200就代表成功
# print(response.status_code)

# 响应的url
# print(response.url)       # https://www.baidu.com/

# 请求头
# print(response.request.headers)



