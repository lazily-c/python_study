# 1、数值类型

# 查看类型函数type()
"""
a、整数类型  int
b、浮点数类型   float
"""

num_1 = 520
print(type(num_1))

num_2 = 10.5
print(type(num_2))

# 2、布尔值  True  False 判断


# 3、字符串类型  str
val_1 = 'hello world'
val_2 = "你好世界"
val_3 = """你好世界"""
print(type(val_1))
print(type(val_2))

# 4、列表类型 list
list_1 = [val_1, val_2]
print(list_1)
print(type(list_1))

# 5、元组类型 tuple
tul = (val_1, val_2)
print(tul)
print(type(tul))

# 6、集合类型 set
# 无序 不重复
set_1 = {1, 2, 3, 4, 5, 6, 6, 6, val_2, tul}
print(set_1)
print(type(set_1))

# 7、字典类型 dict 键值对
# "name": "李华"   name是键(key)，李华是值(value)
dict_1 = {"name": "李华", "age": "23", "sex": "男"}
print(dict_1)
print(type(dict_1))
