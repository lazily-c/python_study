# 井高10米，一只蜗牛白天爬3米，晚上滑下来2米，问多久可以爬出来，总共爬了多少米

# 上传代码+最终效果截图


# 井高10米
height = 10

# 白天爬的高度
up = 3

# 晚上下滑的高度
down = 2


def climb(height, up, down):
    distance = 0
    days = 0
    while distance < height:
        days += 1
        distance += up

        if distance >= height:
            break
        distance -= down
    total_distance = up * days

    return days, total_distance


days = climb(height, up, down)
total_distance = climb(height, up, down)

print(f"蜗牛爬出井口需要{days}")
print(f"蜗牛爬了多少米{total_distance}")

