
def temp_test(lst: list):
    ln = len(lst)
    if ln < 1:
        return 0
    dp = [1] * ln
    res = 1
    for i in range(ln):
        for j in range(i):
            if lst[i] > lst[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j]+1
        if dp[i] > res:
            res = dp[i]
    return res


print(temp_test([10,9,2,5,3,7,101,18]))
