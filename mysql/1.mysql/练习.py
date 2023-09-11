# -*- coding:utf-8 -*-
# 成功创建一个13_class数据库，并且创建student_data的数据表
# 表字段包含：student_id，student_name，student_age，student_gender，student_love
# 需求：实现基于MySQL的学员管理系统
#   增加学员信息
#   删除学员信息

import pymysql


# 建立数据库的连接
class StudentData(object):
    def __init__(self):
        self.coon = pymysql.connect(
            host="127.0.0.1",  # 127.0.0.1代表本机地址
            port=3306,  # mysql默认端口3306
            user="root",  # root最高权限用户名
            password="15096962415",  # 密码
            db="13_class"  # 指定数据库进行连接
        )

        # 建立游标
        self.cursor = self.coon.cursor()

    def add_student(self):
        while True:
            student_id = int(input("请输入学员的学号："))
            student_name = (input("请输入学员的姓名："))
            student_age = (input("请输入学员的年龄："))
            student_gender = (input("请输入学员的性别："))
            student_love = (input("请输入学员的爱好："))
            sql = "insert into student_info(student_id,student_name,student_age,student_gender,student_love) values (%s,%s,%s,%s,%s)"
            params = [(student_id, student_name, student_age, student_gender, student_love)]
            self.cursor.executemany(sql, params)
            self.coon.commit()
            number = input("是否继续添加：")
            if number == "否":
                break

    def del_student_data(self):
        student_id = int(input("请输入需要删除的学员学号："))
        sql = f"select student_name from student_info where student_id={student_id}"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        self.cursor.execute(f"delete from student_info where student_id={student_id}")
        self.coon.commit()
        print(result[0], "删除成功")

    def main(self):
        while True:
            print("1、增加学员信息")
            print("2、删除学员信息")
            print("3、退出系统")
            number = int(input("请输入数字选择功能："))
            if number == 1:
                self.add_student()
            elif number == 2:
                self.del_student_data()
            elif number == 3:
                print("欢迎下次使用")
                break


if __name__ == '__main__':
    student = StudentData()
    student.main()
