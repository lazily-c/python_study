# 变量的命名规则
"""
命名以数字、字母、下划线组成

注意:1、不能以数字&纯数字开头
    2、不能使用python内置关键字
    3、严格区分大小写
    4、不能用python的类型


命名习惯：
    1、大驼峰：每个单词首字母都大写。例如：MyName
    2、小驼峰：第二个(含)以后的单词首字母都大写。例如：myName
    3、下划线命名法：例如：my_name
"""

# 从某种角度来讲，变量名可以随便写

# 查看python关键字
# import keyword
# print(keyword.kwlist)

# 例：
name = "熊二"
print(name)
My_Favorite = "deng_xue_mei"

_animal = "熊猫"  # 下划线命名法，在后面知识有特殊意义
