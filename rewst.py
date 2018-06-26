lists = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7]
]

l =[3, 4, 5, 6, 7]

y=(sum(x) for x in zip(*lists))

res = list((sum(x * x) for x in l))

print(res)

print(list(y))