from typing import List


class Solution:

    def ggj(self, i, nums, ln, aim_list):
        aim_list[i] = 1
        if nums[i] == 0:
            return False
        if nums[i] + i >= ln - 1:
            return True
        else:
            temp = False
            for j in range(nums[i], 0, -1):
                if aim_list[i + j] == 0 and self.ggj(i + j, nums, ln, aim_list):
                    temp = True
            return temp

    def canJump(self, nums: List[int]) -> bool:
        ln = len(nums)
        if ln == 1:
            return True
        aim_list = [0] * ln
        return self.ggj(0, nums, ln, aim_list)


if __name__ == '__main__':
    print(Solution().canJump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))