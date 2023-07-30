# -*- coding:utf-8 -*-

# 练习：输入一个小数转化为整数

# 方法一：
# 输入一个小数
num = input("请输入一个小数：")

# 先把字符串num转化为浮点数
result = float(num)

print("转化后的浮点数保留两位小数：%.2f" % result)

# 再把转化后的浮点数result转化为整数
number = int(result)

print("转化后的整数是:%d" % number)


# 方法二：
# 使用eval()函数

# 输入一个小数
num1 = eval(input("请输入一个小数："))

print("转化后的浮点数保留两位小数：%.2f" % num1)
print("转化后的整数是:%d" % num1)
