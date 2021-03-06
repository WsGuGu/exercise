# 装饰器
import time


def writeLog(func):
    print('访问了方法名:', func.__name__, '\t时间:', time.asctime())


def funOut(func):
    def funIn(a, b):
        writeLog(func)
        return func(a, b)

    return funIn


@funOut
def sum(a, b):
    return a + b


if __name__ == '__main__':
    result = sum(10, 20)
    print('两数的和:', result)