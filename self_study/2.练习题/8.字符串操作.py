# 将字符串var1 = "1a2b3c4d5e6f"中的数字提取，并且累加

# 方法一
# 定义字符串
var1 = "1a2b3c4d5e6f"

# 提取字符串中的数字
num = var1[::2]

#  测试是否拿到了字符串中的数字
# print(num)

#  定义一个变量用来接收累加值

sum = 0

# 遍历字符串，每次取一个字符，转成整型相加
for i in num:
    sum += int(i)
print("提取字符串后,并累加的结果是{}".format(sum))
