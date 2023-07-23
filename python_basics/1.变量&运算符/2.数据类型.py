# 数据类型(数值、布尔、列表、元组、字典、集合)
# type()-----检测数据类型

# 1、数值型
"""
1、int
2、float
"""

# 整型(int)
var_1 = 10
print(type(var_1))      # 打印类型

# 浮点型(float)------就是小数
var_2 = 10.5
print(type(var_2))       # 打印类型


# 2、字符串类型(str)  特点：数据都要 带引号，可以是单引号、双引号、三引号。
# 注意：三引号在没有变量名时，表示多行注释
name_1 = "李白"
print(type(name_1))  # 打印类型


# 3、bool类型    通常判断时使用。   布尔值有两个取值分别是：True 和 False
a = True
print(type(a))

# 4、list -- 列表
b = [10, 20, 30]
print(type(b))

# 5、tuple -- 元组
c = (10, 20, 30)
print(type(c))

# 6、set -- 集合
d = {10, 20, 30}
print(type(d))

# 7、dict -- 字典 -- 键值对
e = {"name": "TOM", "age": 18}
print(type(e))
