# python是严格遵循缩进的语言

# if判断

sex = input("请输入你的性别：")  # male female
age = int(input("请输入你的年龄："))

# 当需要判断多个条件的时候
# if sex == "male":
#     print('你是男孩')
# elif sex == "female":
#     print('你是女孩')
# else:
#     print("你不是女孩，也不是男孩")

# 练习：输入性别和年龄，判断这个人是否可以结婚
# if嵌套
if sex == "male":
    if age >= 22:
        print("可以结婚")
    else:
        print("不可以结婚")
else:
    if age >= 20:
        print("可以结婚")
    else:
        print("不可以结婚")
