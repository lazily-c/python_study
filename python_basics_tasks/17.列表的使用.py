# -*- coding:utf-8 -*-
#   函数接受一个列表def func(data:list)
# 例如：
#     传递实参  ：[1,2,3,4,5]
#     输出返回值：[1,5,2,4,3]
#
#     传入实参  ：[1,2,3,4,5,6]
#     输出返回值：[1,6,2,5,3,4]
#
#     传入实参  ：["张三","李四","王五"]
#     输出返回值：["张三","王五","李四"]
#
#
#     [第一个，倒数第一个，第二个，倒数第二个，第三个，倒数第三个]

# 代码实现：
def func_one(data_list):
    new_list = []
    length = len(data_list)    # 求出长度
    # 传入列表长度是偶数，执行的程序
    if length % 2 == 0:
        for num in range(0, length // 2):  # 循环次数
            new_list.append(data_list[num])
            new_list.append(data_list[length - 1 - num])

    # 传入列表长度是奇数，执行的程序
    else:
        for num in range(0, length // 2 + 1):    # 长度奇数循环次数多一次
            new_list.append(data_list[num])       # 将传入的列表第一个，添加进新列表
            if data_list[num] != data_list[length - 1 - num]:
                new_list.append(data_list[length - 1 - num])    # 最后一个，添加进新列表
    return new_list


data1 = func_one([1, 2, 3, 4, 5])
data2 = func_one([1, 2, 3, 4, 5, 6])
data3 = func_one(["张三", "李四", "王五"])
print(data1)
print(data2)
print(data3)
