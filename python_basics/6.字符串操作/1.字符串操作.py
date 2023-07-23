# 格式化字符串
name = "耀"
age = 19

# 格式化输出的三种方法
str_1 = "我叫{},我{}岁".format(name, age)
str_2 = "我叫%s,我%d岁" % (name, age)
str_3 = f"我叫{name},我{age}岁"

print(str_1)
print(str_2)
print(str_3)

name_1 = "大江东去浪涛尽"

# 遍历一个序列(字符串、列表、元组)
# 序列：有顺序的排列

for i in name_1:
    print(i)

# print() 语句是默认换行的

# 根据下标和索引进行访问
print(name_1[0])   # 大
print(name_1[1])   # 江
print(name_1[2])   # 东
print(name_1[3])   # 去
print(name_1[4])   # 浪
print(name_1[5])   # 涛


print(name_1, end="+")
print(name_1, end="+")
print(name_1, end="+")
print(name_1)


# 九九乘法表
for i in range(1, 10):  # 1 2 3 4 5 6 7 8 9
    for j in range(1, i+1):
        print("{}*{}={}".format(i, j, i*j), end=" ")
    print()      # 换行操作
