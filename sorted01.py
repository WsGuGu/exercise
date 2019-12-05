"""
形成一个按value排序的队列，默认升序
"""
d = {'d1': 2, 'd2': 4, 'd4': 1, 'd3': 3}
print(sorted(d, key=d.__getitem__))
print(sorted(d.items(), key=lambda d: d[1]))