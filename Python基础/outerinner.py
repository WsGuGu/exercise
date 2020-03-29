# 闭包求两点之间的距离
import math


def getDisOut(x1, y1):
    def getDisIn(x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return getDisIn


def getDis(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if __name__ == '__main__':
    # 求点(1,1)距离原点的距离
    result = getDis(1, 1, 0, 0)
    print("距离：", result)
    # 使用闭包的方式
    getDisIn = getDisOut(0, 0)
    result = getDisIn(1, 1)
    print("距离：", result)