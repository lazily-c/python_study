# -*- coding:utf-8 -*-
# 逻辑运算符
# (and(与) or(或) not(非))

num1 = 0
num2 = 1
num3 = 2
# and运算符，只要有一个值为0，则结果为零，否则结果为最后一个非0数字
print(num1 and num2)
print(num2 and num3)
print(num3 and num2)


# or运算符，只有所有值为0结果才为0,否则结果为第一个非零数字
print(num1 or num2)
print(num2 or num1)
print(num2 or num3)


print(2 and 0 or 4)
print(3 or 4 and 2)
# 先执行and 在执行or
print(5 and 6 or 0 and 5 or 8)


