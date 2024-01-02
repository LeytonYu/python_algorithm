from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        ln = 0
        while start <= end:
            if nums[start] != val:
                ln += 1
                start += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        return ln


if __name__ == '__main__':
    print(Solution().removeElement(nums = [3,2,2,3], val = 3))