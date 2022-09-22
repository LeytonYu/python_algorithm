def findSushu(n):
    lst = [True] * (n + 1)
    for i in range(2, n + 1):
        if lst[i]:
            p = i
            j = 2
            while p * j <= n:
                lst[p * j] = False
                j += 1
    count = 0
    for i in range(2, n + 1):
        if lst[i]:
            count += 1
            if count % 10 == 0:
                print(i)
            else:
                print(i, end=' ')
    print('一共有%d个素数'%count)

n = int(input('请输入一个整数：'))
findSushu(n)
