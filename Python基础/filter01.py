a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = ['1', '2', '3', '   ', 'a  b']


def not_empty(s):
    return s.strip()


def odd(n):
    return n % 2 == 1


L = filter(odd, a)
print(list(L))
print(list(filter(not_empty, b)))