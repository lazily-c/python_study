# -*- coding:utf-8 -*-
# 任务： 给出一个整数列表，每n个元素为一组进行翻转，请你返回修改后的列表。
#
# 示例：
#
# 输入num_list = [1,2,3,4,5], result = 3，输出[3,2,1,4,5]
#
# 输入num_list = [1,2,3,4,5],result = 2,输出[2,1,4,3,5]

def func_one(data_list):
    new_list_one = []               # 用来处理传入的列表
    new_list_two = []               # 存最后的结果
    num = int(input("请输入分组的元素个数："))
    for result in range(0, len(data_list), num):          # 根据传入的分组元素个数，划分循环的步长
        new_list_one.extend(data_list[result: result + num])    # 将传入的列表，根据输入的组数,进行切片后添加到new_list_one
        # print(new_list_one)       # 查看每次循环，对传入列表切片后，得到的结果
        if len(new_list_one) == num:        # 切片后的列表长度与分组的元素个数是否相等
            new_list_one.sort(reverse=True)         # 进行逆序排序
        new_list_two.extend(new_list_one)           # 直接添加，不进行逆序
        new_list_one.clear()                        # 每次循环后，把new_list_one置为空
        # print(new_list_one)
    print(new_list_two)


data_list = [1, 2, 3, 4, 5]
func_one(data_list)
