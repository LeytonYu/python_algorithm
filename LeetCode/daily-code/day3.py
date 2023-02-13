from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        length = len(s)
        m = length / 4
        if all(cnt[k] <= m for k in cnt):
            return 0
        left = 0
        res = length
        for right, x in enumerate(s):
            cnt[x] -= 1
            while all(cnt[k] <= m for k in cnt):
                res = min(res, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return res


if __name__ == '__main__':
    a = Solution().balancedString("QQQW")
    print(a)
