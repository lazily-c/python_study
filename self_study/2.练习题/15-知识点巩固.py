# 题目：一辆汽车，把货物从城区运往山区，往返共用了20小时，
#      去的时候花的时间是来的时候的1.5倍；去时每小时比来时慢12公里
# 需求：这辆汽车往返共行驶了多少公里


def total_distance(x):
    t = 8
    d1 = x * t
    d2 = (x-12)*1.5*8
    d = d1 + d2
    return d

if __name__=="__main__":
    x = float(input("请输入汽车的行使速度："))
    distance = total_distance(x)
    print("这辆汽车往返共行驶了%.2f公里" % distance)
