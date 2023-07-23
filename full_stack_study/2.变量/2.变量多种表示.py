# 如果变量是一样的，那么无论变量名是什么，都是指向同一个变量
# 类似于备份数据

name1 = "列夫·托尔斯泰"
name2 = "列夫·托尔斯泰"
name3 = "列夫·托尔斯泰"

# 打印变量名所存的地址
print(id(name1))
print(id(name2))
print(id(name3))


# 多个变量赋值给一个变量名，结果所有变量被放在一个括号内(也叫元组)
name4 = "懒洋洋", "灰太狼"
name5 = ("懒洋洋", "灰太狼")
print(name4)
print(name5)

# 同一个变量名，被多个变量赋值，输出的值是最后一个赋值的变量，前面的值被覆盖
name6 = "喜羊羊"
print(id(name6))      # 查看地址
name6 = "熊二"
print(id(name6))      # 地址不一致
print(name6)
