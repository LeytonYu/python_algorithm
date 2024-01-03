from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        current = None
        count = 0
        for m in nums:
            if count == 0:
                current = m
            if m == current:
                count += 1
            else:
                count -= 1
        return current
