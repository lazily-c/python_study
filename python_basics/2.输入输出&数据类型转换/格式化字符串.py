name_1 = "李元芳"
age = 16
height = 1.60

# 要求：请以我叫李元芳，我的年龄是16，我的身高是1.9米，进行输出
# 普通输出
print(name_1, age, height)

# 格式化(方法一)
# 使用格式符号(%s %d %f)
print("我叫%s，我的年龄是%d，我的身高是%.2f米" % (name_1, age, height))
print("我叫%s" % name_1)

print("---------------------------------")

# 格式化(方法二)
# 使用format()函数进行格式化

# python内置的函数
# print()函数：输出
# id()函数:返回变量的地址

str_1 = "黄河之水天上来"
name = "李白"
like = "作诗"

# python中一切皆对象
print('我叫{},我喜欢{},有诗句{}'.format(name, like, str_1))

print("----------------------------------")

# 格式化(方式三)
# 在字符串前加f,如：f"xxx"{}"xxx"，大括号内传变量名
print(f"我叫{name},我喜欢{like},有诗句{str_1}")

# 换行
print("天生我材必有用，\n千金散尽还复来")
# 制表符：tab键
print("天生我材必有用\t\t千金散尽还复来")

# 输出\n
print("i \\nlove python")

# 原始字符串：去掉转义效果
print(r"i \nlove python")

# 开发、研发
# 网站(登录、注册的功能)
# 开源(开放源代码)的项目
