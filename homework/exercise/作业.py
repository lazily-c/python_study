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

# 方法一 
def func(data):
    result = []
    length = len(data)

    for i in range(length // 2 + 1):
        result.append(data[i])
        if i != length - i - 1:
            result.append(data[length - i - 1])

    return result


# 示例测试
input1 = [1, 2, 3, 4, 5]
output1 = func(input1)
print(output1)  # 输出: [1, 5, 2, 4, 3]

input2 = [1, 2, 3, 4, 5, 6]
output2 = func(input2)
print(output2)  # 输出: [1, 6, 2, 5, 3, 4]

input3 = ["张三", "李四", "王五"]
output3 = func(input3)
print(output3)