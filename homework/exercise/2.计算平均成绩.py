# 问题:小坤本次语文成绩95.5、数学88、英语65、计算本次考试平均值，取整数

# 定义成绩变量
chinese = 95.5
mathematics = 88
English = 65
# 取整(//)
average = (chinese + mathematics + English) // 3
# 普通输出
print(average)
# 格式化输出
print("小坤本次考试平均值，取整后为{}".format(average))
