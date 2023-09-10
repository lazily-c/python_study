# -*- coding:utf-8 -*-
import pymysql

# 建立连接
coon = pymysql.connect(
    host="127.0.0.1",           # 127.0.0.1代表本机地址
    port=3306,                  # mysql默认端口3306
    user="root",                # root最高权限用户名
    password="15096962415",     # 密码
    db="13_class"               # 指定数据库进行连接
)


# 建立游标，传递python给mysql的命令
cursor = coon.cursor()
