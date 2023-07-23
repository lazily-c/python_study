# 多变量赋值，最后一个等号左边的，全部都是变量名

# 例如：
a = b = c = 123
print(a)
print(b)
print(c)

# 如果变量内容是一样的，不管变量名是什么，地址都是同一个
print(id(a))
print(id(b))
print(id(c))

