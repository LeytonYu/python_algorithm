from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sa = sorted(zip(scores, ages))
        smax = [0] * len(scores)
        print(sa)
        for i, (s, a) in enumerate(sa):
            for j in range(i):
                if a >= sa[j][1]:
                    smax[i] = max(smax[i], smax[j])
            smax[i] += s
        print(smax)
        return max(smax)

    def bestTeamScoreV2(self, scores: List[int], ages: List[int]) -> int:
        max_sum = [0] * (max(ages) + 1)
        for score, age in sorted(zip(scores, ages)):
            max_sum[age] = max(max_sum[:age + 1]) + score
            print(max_sum)
        return max(max_sum)

    def bestTeamScoreV3(self, scores: List[int], ages: List[int]) -> int:
        u = max(ages)
        t = [0] * (u + 1)

        # 返回 max(max_sum[:i+1])
        def query(i: int) -> int:
            mx = 0
            while i:
                mx = max(mx, t[i])
                i &= i - 1
            return mx

        # 更新 max_sum[i] 为 mx
        def update(i: int, mx: int) -> None:
            while i < len(t):
                t[i] = max(t[i], mx)
                i += i & -i

        for score, age in sorted(zip(scores, ages)):
            update(age, query(age) + score)
        return query(u)


if __name__ == '__main__':
    a = Solution().bestTeamScoreV2([1,2,3,15], ages = [8,9,10,1])
    print(a)
