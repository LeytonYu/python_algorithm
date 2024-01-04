from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = prices[0]
        maxv = 0
        for i in range(1, len(prices)):
            if prices[i] > temp:
                maxv += prices[i] - temp
            temp = prices[i]
        return maxv
