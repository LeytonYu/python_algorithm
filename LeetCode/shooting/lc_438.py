class Solution:
    def findAnagrams(self, s: str, p: str) -> bool:
        left, right = 0, 0
        from collections import defaultdict
        need, window = defaultdict(int), defaultdict(int)
        for c in p:
            need[c] += 1
        valid = 0
        nt = len(need)
        res = []
        while right < len(s):
            tp = s[right]
            window[tp] += 1
            if tp in need and window[tp] == need[tp]:
                valid += 1
            right += 1
            if right - left >= len(p):
                if valid == nt:
                    res.append(left)
                cp = s[left]
                if cp in need and window[cp] == need[cp]:
                    valid -= 1
                window[cp] -= 1
                left += 1
        return res


if __name__ == '__main__':
    print(Solution().findAnagrams(s = "abab", p = "ab"))
