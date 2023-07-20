# 1、使用input输入一个小数，并转化为整数
# var = float(input("请输入一个小数："))
# print(int(var))

# 2、使用三次input输入三个数，然后相加求和
# 方法一：能够确保精度
# 使用decimal模块
from decimal import *
num_1 = Decimal(input("请输入一个数："))
num_2 = Decimal(input("请输入一个数："))
num_3 = Decimal(input("请输入一个数："))

# 字符串的相加，就是拼接
print(num_1 + num_2 + num_3)

# 方法二：精度不是很准确
num_1 = eval(input("请输入一个数："))
num_2 = eval(input("请输入一个数："))
num_3 = eval(input("请输入一个数："))
value = num_1 + num_2 + num_3
print(value)
