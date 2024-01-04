from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = None
        maxv = 0
        for p in prices:
            if temp is None:
                temp = p
            elif temp < p:
                maxv = max(maxv, p - temp)
            else:
                temp = p
        return maxv