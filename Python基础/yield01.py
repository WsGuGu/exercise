def foo():
    print('starting')
    while True:
        res = yield 4
        print('res:', res)


if __name__ == '__main__':
    g = foo()
    print(type(g))
    print(next(g))
    print(next(g))