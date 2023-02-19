from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ln = len(classes)
        add_func = lambda p, t: (p+1)/(t+1) - p/t
        nc = [(-add_func(p, t), p, t) for p, t in classes]

        heapq.heapify(nc)   # 小顶堆
        while extraStudents:
            _, p, t = heapq.heappop(nc)
            p += 1
            t += 1
            heapq.heappush(nc, (-add_func(p, t), p, t))
            extraStudents -= 1

        return sum(p / t for _, p, t in nc) / ln


if __name__ == '__main__':
    print(Solution().maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))

