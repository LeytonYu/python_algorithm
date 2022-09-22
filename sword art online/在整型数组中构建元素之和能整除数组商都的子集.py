def findModuleSubSet(A):
    boxes = [0] * len(A)
    sum = 0
    subSet = []
    for k in range(len(A)):
        sum += A[k]
        subSet.append(k)
        t = sum % len(A)
        if t == 0:
            return subSet
        if boxes[t] != 0:
            preSum = 0
            for i in range(k + 1):
                preSum += A[i]
                if preSum % len(A) == t:
                    return subSet[i + 1:]
        boxes[t] = 1
    return []


import random

A = [random.randint(10, 999) for i in range(9)]
print(A)
subSet = findModuleSubSet(A)
print(subSet)
