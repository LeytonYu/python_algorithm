from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        ln = len(nums)
        if ln == 1:
            return 1
        while j < ln:
            if nums[i] != nums[j]:
                if i < j:
                    nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1