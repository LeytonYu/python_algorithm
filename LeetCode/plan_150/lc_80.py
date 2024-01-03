from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ln = len(nums)
        i = 0
        j = 1
        count = 0
        res = 1
        while j < ln:
            if nums[i] != nums[j]:
                if count <= 1:
                    nums[i + count + 1] = nums[j]
                    i = i + count + 1
                else:
                    nums[i+2] = nums[j]
                    i += 2
                j += 1
                res += 1
                count = 0
            elif nums[i] == nums[j]:
                if count == 0:
                    res += 1
                    if i + 1 < j:
                        nums[i + 1] = nums[j]
                count += 1
                j += 1
        while ln - res > 0:
            nums.pop()
            ln -= 1
        print(res)
        print(nums)
        return res

    def removeDuplicates_common(self, nums: List[int]) -> int:
        def solve(k):
            u = 0
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            print(u)
            print(nums)
            return u

        return solve(2)


if __name__ == '__main__':
    # Solution().removeDuplicates([1,1,1,2,2,2,3,3])
    Solution().removeDuplicates_common([1, 1, 1, 2, 2, 2, 3, 3])