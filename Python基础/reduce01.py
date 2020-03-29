from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0


def sam(c, b):
    return c + b


sum = reduce(sam, a)
print(sum)