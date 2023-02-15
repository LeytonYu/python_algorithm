from typing import List
from math import gcd


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return gcd(*nums) == 1


if __name__ == '__main__':
    print(Solution().isGoodArray([1, 2, 3]))