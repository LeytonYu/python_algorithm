from typing import List


class Solution:
    """
    输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    输出：[1,2,2,3,5,6]
    解释：需要合并 [1,2,3] 和 [2,5,6] 。
    合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        start = 0
        ln = m + n
        for n_ in range(n):
            while nums2[n_] > nums1[start] and start < m:
                start += 1
            nums1.insert(start, nums2[n_])
            m += 1
            start += 1
            nums1.pop()
        # nums1 = nums1[:ln]
        print(nums1)

    def merge_v2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p2 >= 0:
            if nums1[p1] > nums2[p2] and p1 >= 0:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        print(nums1)


if __name__ == '__main__':
    Solution().merge_v2(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

