a = ['a', 2, 'c', 'd']
for i, n in enumerate(a):
    if n == 2:
        a.pop(i)
    print(n)
