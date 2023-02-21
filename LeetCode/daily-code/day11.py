from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        right_most = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(i - ranges[i], 0)
            right_most[left] = max(right_most[left], i + ranges[i])

        ans = 0
        cur_right = 0  # 已建造的桥的右端点
        next_right = 0  # 下一座桥的右端点的最大值
        for i in range(n):  # 注意这里没有遍历到 n，因为它已经是终点了
            next_right = max(next_right, right_most[i])
            if i == cur_right:  # 到达已建造的桥的右端点
                if i == next_right:  # 无论怎么造桥，都无法从 i 到 i+1
                    return -1
                cur_right = next_right  # 造一座桥
                ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().minTaps(n=6, ranges=[1, 1, 1, 2, 1, 1, 1]))
