def binaryfind(A, m):
    if len(A) == 0:
        return -1
    i = int(len(A) / 2)
    if A[i] == m:
        return i
    if A[i] < m and i + 1 < len(A):
        return binaryfind(A[i:], m)
    if A[i] > m and i - 1 >= 0:
        return binaryfind(A[:i], m)
    return -1


A = [int(i) for i in input().split()]
A.sort()
M = int(input())
flag = False
for i in range(len(A)):
    m = M - A[i]
    j = binaryfind(A, m)
    if j != -1 and j != i:
        flag = True
        print('存在i，j')
        break
if not flag:
    print('不存在i，j')
