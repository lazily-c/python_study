# 题目：做一个猜字游戏
#
# 要求：1、从1-100生成一个随机数
#
#      2、总共有5次机会
#
#      3、若中途猜对，循环就要终止
#
# 提示：生成了一个56，但是我也输入了一个56，即为过关，循环终止

import random

# 从1-100生成一个随机数
num = random.randint(1, 6)

for i in range(5):
    value = int(input("请输入一个你猜的数： "))
    if value == num:
        print("猜对了")
        break
    else:
        print("猜错了请重新输入")











