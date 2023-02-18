from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for x in range(1, 1001):
            for y in range(1, 1001):
                if customfunction.f(x, y) == z:
                    res.append([x, y])
                    break
                if customfunction.f(x, y) > z:
                    break
        return res