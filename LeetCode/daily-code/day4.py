from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ln = len(hours)
        fuck_map = {}
        res = 0
        sm = 0
        for i, h in enumerate(hours, 1):
            sm += 1 if h > 8 else -1
            if sm > 0:
                res = i
            else:
                if fuck_map.get(sm - 1):
                    res = max(res, i - fuck_map.get(sm - 1))
                else:
                    fuck_map.setdefault(sm, i)
        return res