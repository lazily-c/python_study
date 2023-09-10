# -*- coding:utf-8 -*-
import pymysql


# 建立连接
class MysqlData():
    def __init__(self):
        self.coon = pymysql.connect(
            host="127.0.0.1",           # 127.0.0.1代表本机地址
            port=3306,                  # mysql默认端口3306
            user="root",                # root最高权限用户名
            password="15096962415",     # 密码
            db="13_class"               # 指定数据库进行连接
        )

        # 建立游标，传递python给mysql的命令
        self.cursor = self.coon.cursor()

    def add_data(self):
        # 方法一
        # sql = "insert into student_data(student_id, student_name, student_gender, student_age) values (1307,'懒洋洋','男','四十五')"
        # self.cursor.execute(sql)
        # 方法二  多用第二种方法，效率更高
        sql = "insert into student_data(student_id, student_name, student_gender, student_age) values (%s, %s, %s, %s)"
        params = [(1309, '灰太狼', '男', '五十五')]
        self.cursor.executemany(sql, params)
        # 提交事务
        self.coon.commit()

    def show_data(self):
        # 根据指定的student_id, 查找姓名
        sql = "select student_name from student_data where student_id=1309"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result[0])

    def delect_data(self):
        # 根据指定的student_id，删除数据
        sql = "delete from student_data where student_id=1309"
        self.cursor.execute(sql)
        self.coon.commit()

    def update_data(self):
        # 根据指定的student_id,修改数据
        sql = "update student_data set student_name='灰太狼' where student_id=1307"
        self.cursor.execute(sql)
        self.coon.commit()


if __name__ == '__main__':
    data = MysqlData()
    data.update_data()

