# 定义两个函数
#
# 调用第一个函数可以录入学员
#
#  输入学员姓名，并将学员姓名添加到列表
#
# 调用第二个函数可以查询学员
#
#  输入学员姓名，可查询学员是否录入


# 全局变量
List_name = []


def func1():
    student_name = input("请输入录入学生名字： ")
    global List_name
    # 把输入的学生名字放入列表
    List_name.append(student_name)


def func2():
    student_name = input("请输入查询学生名字： ")
    global List_name
    # 判断学员是否在里面
    if student_name in List_name:
        print("录入成功")
        return True
    else:
        print("录入失败")
        return False


func1()
func2()
