# input([prompt])
# password = input("请输入你的密码： ")

# print(*object, sep=' ',end='\n', file=sys.stdout)
# object: 表示输出的对象，输出多个对象时，对象之间需要用分隔符分隔
# sep:用于设定分隔符，默认使用空格作为分隔符
# end:用于设定输出以什么结尾，默认值为换行符\n.
# file:表示数据输出的文件对象

# name = '张三'
# print(password, name, sep='#', end='')
# print(password, name, sep='#')

file = open('a.txt', 'w', encoding='utf-8')
print('python', file=file)
