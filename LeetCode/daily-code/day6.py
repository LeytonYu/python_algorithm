from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        my_map = Counter(nums)
        ou = ji = 0
        for key, value in my_map.items():
            if value % 2 == 0:
                ou += value // 2
            else:
                ou += value // 2
                ji += 1
        return [ou, ji]


if __name__ == '__main__':
    print(Solution().numberOfPairs([1,3,2,1,3,2,2]))