# 任务：
# 每天道歉一次，并买三束花束花 总共持续10天
# 当我在第四天，买了第2束花后，女朋友不生气了，整个循环都会退出
# 疑问：在嵌套循环当中，内部循环执行到break它是退内部，还是整体？
# 提示：如何才能让条件循环停止

# 记录道歉天数
day = 1
while day <= 10:    # 1 2 3 4 5 6 7 8 9 10

    # 进行格式化输出，第几天道歉
    print(f"今天是第{day}天，道歉")

    # 记录买鲜花的次数
    flower_count = 1

    while flower_count <= 3:

        # 格式化输出，第几天，买了几束鲜花
        print("今天是第{}天，买{}几束鲜花".format(day, flower_count))

        # 判断同时满足在第四天，买了第2束花，这两个条件
        if day == 4 and flower_count == 2:
            print("女朋友不生气了")

            # 退出的只是内循环
            break

        # 买鲜花循环结束的出口
        flower_count += 1

    # 再退出内循环后，加同时满足在第四天，买了第2束花，这两个条件
    if day == 4 and flower_count == 2:

        # 执行break,退出整个循环
        break

    # 道歉循环结束的出口
    day += 1
