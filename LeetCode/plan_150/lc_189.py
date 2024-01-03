from typing import List


def gcd(x, y) -> int:
    return x if y == 0 else gcd(y, x % y)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        g = gcd(n, k)
        cnt = n // g
        for i in range(0, g):
            j, pre = i, nums[i]
            for _ in range(0, cnt):
                j = (j + k) % n
                nums[j], pre = pre, nums[j]     # 交互


if __name__ == '__main__':

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Solution().rotate(nums = [0,1,2,3,4,5,6,7,8,9], k = 3)
    print(nums[3:])
    print(nums[:3])