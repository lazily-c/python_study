# -*- coding:utf-8 -*-
import pymongo


class MongoData(object):
    def __init__(self):
        # 建立连接
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        self.db = self.client["13_class"]

    # 插入单条数据
    def add_data_one(self):
        self.db.student_data.insert_one({"student_id": 1301, "student_name": "李四", "student_love": "篮球"})

    # 插入多条数据
    def add_data_many(self, data_list):
        self.db.student_data.insert_many(data_list)

    # 查看一条数据
    def find_data_one(self):
        result = self.db.student_data.find_one()
        print(result)

    # 查看多条数据
    def find_data_many(self):
        result = self.db.student_data.find()
        for data in result:
            print(data)


if __name__ == '__main__':
    mongo =MongoData()
    data_list = [
        {"student_id": 1302, "student_name": "张三", "student_love": "足球"},
        {"student_id": 1303, "student_name": "王五", "student_love": "羽毛球"},
        {"student_id": 1304, "student_name": "赵六", "student_love": "排球"},
        {"student_id": 1305, "student_name": "懒洋洋", "student_love": "乒乓球"}
    ]
    # mongo.add_data_many(data_list)   # 添加多条数据
    # mongo.find_data_many()           # 查找多条数据
