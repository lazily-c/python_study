# -*- coding:utf-8 -*-
import requests
import warnings
warnings.filterwarnings('ignore')

url = "https://ssr2.scrape.center/"

response = requests.get(url, verify=False)
print(response.text)
