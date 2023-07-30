# format()     占位符

num = 10086
result = 180.25
var1 = "坤哥"
love = "篮球"
# format方法
print("全名制作人，大家好，我是：{},我的电话好码是：{},我的爱好是：{}" .format(var1, num, love))
# {2} 索引值  从0开始
print("全名制作人，大家好，我是：{2},我的电话好码是：{0},我的爱好是：{1}" .format(num, love, var1))
print("全名制作人，大家好，我是：{var1},我的电话好码是：{num},我的爱好是：{love}" .format(num=num, love=love, var1=var1))

# f"xxx"{}"xxx" 方法
print(f"全名制作人，大家好，我是：{var1},我的电话好码是：{num},我的爱好是：{love}")
