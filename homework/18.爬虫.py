# -*- coding:utf-8 -*-

# 目标网站
#
# http://www.beijingprice.cn/jfcx/sp/index.shtml?ItemCode=E000002
#
# 任务需求
#
# 将 序号    时间    批发价格    农贸零售价格    超市零售价格抓取


import requests
import json


url = "http://www.beijingprice.cn/jfcx/sp/index.shtml?ItemCode=E000002"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Cookie": "Hm_lvt_6722af973034eb7e801fff575580b361=1692871125; 122_vq=12; Hm_lpvt_6722af973034eb7e801fff575580b361=1692872832",
    "Host": "www.beijingprice.cn",
    "Upgrade-Insecure-Requests": "1"
}

data = {
    # "type": "1",
    "ItemCode": "E000002"
}

# 发送HTTP POST请求并获取响应
resp = requests.post(url, data=data)

json_data = json.loads(resp.text)

# 遍历JSON数据中的每个条目
for item in json_data:
    index = item["xh"]
    time = item["rq"]
    wholesale_price = item["pfjg"]
    farm_retail_price = item["nmlsjg"]
    supermarket_retail_price = item["cmlsjg"]

    print("序号:", index)
    print("时间:", time)
    print("批发价格:", wholesale_price)
    print("农贸零售价格:", farm_retail_price)
    print("超市零售价格:", supermarket_retail_price)
    print("-" * 30)


