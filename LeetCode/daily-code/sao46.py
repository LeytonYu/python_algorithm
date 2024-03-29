from typing import List


class Solution:
    def maxValue0(self, grid: List[List[int]]) -> int:
        my_map = {}

        def inner(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            elif i == 0 and j > 0:
                my_map[f"{i},{j}"] = inner(i, j - 1) + grid[i][j]
            elif i > 0 and j == 0:
                my_map[f"{i},{j}"] = inner(i - 1, j) + grid[i][j]
            else:
                my_map[f"{i},{j}"] = max(inner(i - 1, j), inner(i, j - 1)) + grid[i][j]
            return my_map[f"{i},{j}"]

        row = len(grid)
        col = len(grid[0])
        return inner(row - 1, col - 1)

    def maxValue(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for __ in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                if dp[i][j] > res:
                    res = dp[i][j]
        return res

    def maxValue2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = grid[0]  # 这里没有拷贝，f 和 grid[0] 都持有同一段内存
        for j in range(1, n):
            f[j] += f[j - 1]
        for i in range(1, m):
            f[0] += grid[i][0]
            for j in range(1, n):
                f[j] = max(f[j - 1], f[j]) + grid[i][j]
        return f[-1]


print(Solution().maxValue([[1, 2], [5, 6], [1, 1]]))
