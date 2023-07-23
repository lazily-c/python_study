# 重键盘获取用户输入的信息

# 程序
# 进程(正在运行的程序)
# 进程的状态(等待、执行、阻塞)
# 时间片轮转法

# 阻塞：程序停止执行，直到某个特定的条件触发，才继续执行

# input输入的数据类型是str类型
num = input("请输入你要输入的信息：")

# 打印输入信息的类型
print(type(num))

# 进行计算，由于num是str类型，要对num进行强制换
# 注意：所有的数值型都可以转成str型，但不是所有的str型都可以转换成数值型

value_1 = int(num) - 50

# 打印输出计算结果
print(value_1)

# type() 查看数据类型

print("----------------------")

# 元组
tu = (1, 2, 4)
print(list(tu))       # 转化为列表

# 列表
li = [1, 2, 4]
print(tuple(li))      # 转化为元组


# 数据类型转换的常用场景
# 列表和元组
# 字符串和数值

value_2 = eval(input("请输入："))
print(type(value_2))

# 使用场景
# 请输入一个列表，并计算这个列表中所有元素的的和
Li = eval(input("请输入："))
sum = 0

for i in Li:
    sum += i

print(sum)
