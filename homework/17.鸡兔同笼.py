# -*- coding:utf-8 -*-
# 题目：鸡兔同笼，笼子里面总共36条腿和10个头
# 要求：求有多少只鸡，多少只兔，使用python求解

def solve_chicken_rabbit(total_count, total_legs):
    for x in range(total_count + 1):       # 遍历鸡的数量
        y = total_count - x                # 兔的数量
        if 2 * x + 4 * y == total_legs:    # 判断腿的数量是否相等
            return x, y
    return None


total_count = 10  # 头的总数量为10
total_legs = 36  # 总脚数为36

result = solve_chicken_rabbit(total_count, total_legs)

if result:
    chicken_count, rabbit_count = result
    print("鸡的数量为:", chicken_count)          # 返回鸡得到数量
    print("兔的数量为:", rabbit_count)           # 返回兔的数量
else:
    print("无法求解鸡兔的数量")
