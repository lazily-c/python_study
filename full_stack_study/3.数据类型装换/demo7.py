# -*- coding:utf-8 -*-
num1 = 100                       # int
num2 = "123"                     # str
result1 = 123.456                # float
result2 = "178.567"              # str


# 整数转化为浮点数
test1 = float(num1)
print(test1)
print(type(test1))

test2 = int(result1)
print(test2)
print(type(test2))

# 字符串转整数
test3 = int(num2)
print(test3)
print(type(test3))

# 字符串转小数
test4 = float(result1)
print(test4)
print(type(test4))

test5 = float(result2)
print(test5)
print(type(test5))

# 这个会报错，看第二点
# test6 = int(result2)
# print(test6)
# print(type(test6))

"""
1、长得向整数的字符串，可以转化为整数,也可以转化为浮点数。
2、长的像小数的字符串可以转化为浮点数，不可以转化为整数。
# eval 将字符串的引号去掉，转化成原本类型。
"""

list1 = [1, 2, 3, 4, 5, 5]         # list
list2 = "[1, 2, 3, 4, 5]"       # str
test7 = eval(list2)
print(test7)
print(type(test7))

tu1 = (1, 2, 3, 4, 5)           # tuple
tu2 = "(1, 2, 3, 4, 5)"         # str
test8 = eval(tu2)
print(test8)
print(type(test8))

set1 = {1, 2, 3, 4, 5}          # set
set2 = "{1, 2, 3, 4, 5}"        # str
test9 = eval(set2)
print(test9)
print(type(test9))

# 列表转元组和集合
test10 = tuple(list1)
test11 = set(list1)
print(test10)
print(test11)

# 集合特点:无序不重复

