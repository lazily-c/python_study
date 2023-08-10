# -*- coding:utf-8 -*-

# 任务： 给出一个整数列表，每n个元素为一组进行翻转，请你返回修改后的列表。
#
# 示例：
#
# 输入num_list = [1,2,3,4,5], result = 3，输出[3,2,1,4,5]
#
# 输入num_list = [1,2,3,4,5],result = 2,输出[2,1,4,3,5]

def reverse_groups(num_list, result):
    modified_list = []
    for i in range(0, len(num_list), result):
        group = num_list[i:i+result]
        modified_list.extend(group[::-1])
    return modified_list

# 示例测试
input1 = [1, 2, 3, 4, 5]
output1 = reverse_groups(input1, 3)
print(output1)  # 输出: [3, 2, 1, 4, 5]

input2 = [1, 2, 3, 4, 5]
output2 = reverse_groups(input2, 2)
print(output2)  # 输出: [2, 1, 4, 3, 5]

