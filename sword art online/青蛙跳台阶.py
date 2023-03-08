class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        a = 1
        b = 2
        for i in range(3, n + 1):
            a, b = b, (a + b) % 1000000007
        return b


for i in range(100):
    print(Solution().numWays(i))
