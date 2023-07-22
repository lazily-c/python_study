# 计算机(奴隶)
# 机器语言(0000011111)
# python语言 ==> python解释器 ==> 机器语言
# 计算 ！= 运算


# 程序 = 数据结构 + 算法
# 尼古拉斯·沃斯


# 编程题(解决某个问题)


"""
定义一个变量(可以变的)
name_1 变量名(标识符)
"李华" 值
"""

# 赋值语句
name_1 = "李华"
name_2 = "李逍遥"


# id()用来查看地址
# print()打印输出
print(id(name_1))
print(id(name_2))


name_1 = name_2 = name_3 = "韩信"  # 变量名指向同一个内存空间
print(id(name_1))
print(id(name_2))
print(id(name_3))


# 黄色 ：警告(提醒)(并不会报错)
# 红色的波浪线：报错


# 此时没有变量名指向韩信，python的垃圾回收机制，过了一段时间会释放"韩信"(删除)
name_1 = name_2 = name_3 = "企鹅"


print(name_1)
print(name_2)


# 标识符命名：见名知意
class_name = "13班"

# 注释：
"""
    1、注释分为：单行注释 和 多行注释
    2、注释的好处：(不执行)方便别的程序员更好的理解代码，提高可读性
    3、在python中，使用 # 号进行单行注释，使用（“”“   ”“”）进行多行注释
"""

# 多行注释：
"""
用python写程序题：每天道歉一次，并买三束花束花 总共持续10天
当我在第四天，买了第2束花后，女朋友不生气了，整个循环都会退出
"""

# 运算符
a = 100
b = 200

# 加、减、乘、除
print(a+b)
print(a-b)
print(a*b)
print(a/b)

num_1 = 9
num_2 = 4
# 取整(//)
print(num_1//num_2)
# 取余(求模)(%)
print(num_1 % num_2)


# 幂运算(**)
print(2**2)    # 2的平方
print(2**3)    # 2的3次方
print(2**4)    # 2的4次方

# 优先级
var_1 = 10
var_2 = 20
var_3 = 30
num = (var_1+var_2+var_3) * 10
print(num)


# =：赋值
# ==：等于

# 复合赋值运算符
a = 0
a = a+1  # 等价与a += 1
print(a)


# 比较运算符
c = 10
d = 20
# c == d  # 表达式(有一个结果)
print(a == b)
print(a != b)


# 逻辑运算符
# and: 什么与什么(前后表达式都为真 才真)
# or: 什么或什么(有一个为真，就为真)
# not：不是什么(取反)

g = 100
z = 200
q = 300

print(a != b and a != c)    # 两个表达式都为真，即为真
print(a == b or a == c)     # 两个表达式都为假，即为假
print(not a == b)

print("-----------------")
a = 100

# print() 具有输出功能
print(id(a))

# 数值
# 列表 list
# 字符串 str

str = "亚连"
print(str)
