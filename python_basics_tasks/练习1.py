# -*- coding:utf-8 -*-
# 题目：
# 有一个列表 list_num = [1、2、3、4]，里面的数字能组成多少个互不相同且无重复数字的三位数？
# 各是多少？
# 使用while循环 + 迭代器完成

# while循环


# for循环完成
# list_num = [1, 2, 3, 4]
# count = 0    # 计数
# for a in range(1, len(list_num)+1):          # 遍历列表的到百位
#     for b in range(1, len(list_num)+1):      # 遍历列表得到十位
#         for c in range(1, len(list_num)+1):  # 遍历列表得到个位
#             if (a != b) and (a != c) and (b != c):    # 判断无重复数字
#                 count += 1
#                 print("%d%d%d" % (a, b, c), end=" ")
#     print()
# print(f"一共有{count}个")
