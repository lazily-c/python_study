# -*- coding:utf-8 -*-
import requests

class Novel_Data(object):
    def __init__(self):
        self.url = "https://www.17k.com/all/book/2_0_0_0_0_0_0_0_{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }

    # 构建前三页的url地址
    def get_url_list(self):
        url_list = []
        for num in range(1, 4):
            url_list.append(self.url.format(num))

        return url_list

    # 发起请求，并且获取响应数据
    def get_page_index(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        if response.status_code == 200:
            return response.text
        else:
            return None

    # 将html数据存储在html文件当中
    def write_html_data(self, response, index):
        file_name = f"第{index}页的数据.html"
        with open("./17k/" + file_name, "a") as file:
            file.write(response)
            print(f"第{index}页的数据保存成功")


    # 实现整个代码的业务逻辑
    def main(self):
        url_list = self.get_url_list()
        for url in url_list:
            response = self.get_page_index(url)
            index = url_list.index(url) + 1
            self.write_html_data(response, index)


if __name__ == '__main__':
    novel = Novel_Data()
    novel.main()
