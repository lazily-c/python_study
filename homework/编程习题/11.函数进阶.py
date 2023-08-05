# 递归完成斐波拉契前20项。关键代码加上注释。
# 斐波拉契数列：1 1 2 3 5 8 13……


# 定义
def feibolaqi(n):
    if n <= 1:
        return 1
    else:
        # 计算公式
        return feibolaqi(n-1) + feibolaqi(n-2)

# 遍历输出


for i in range(20):
    print("斐波拉契的第{}项,是{}".format(i, feibolaqi(i)))
