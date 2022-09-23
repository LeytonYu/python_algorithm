class Solution(object):
    def removeDuplicates(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        q = 1
        while q < len(nums):
            if nums[p] != nums[q]:
                p += 1
                if p < q:
                    nums[p] = nums[q]
            q += 1
        return p + 1


if __name__ == '__main__':
    nums = [1,2,2,2,2,2,2,2,3,3,4,5,66,66]
    res = Solution().removeDuplicates(nums)
    print(res)