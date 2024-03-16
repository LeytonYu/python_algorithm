class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        from collections import defaultdict
        need, window = defaultdict(int), defaultdict(int)
        for c in s1:
            need[c] += 1
        valid = 0
        nt = len(need)
        res = []
        while right < len(s2):
            tp = s2[right]
            window[tp] += 1
            if tp in need and window[tp] == need[tp]:
                valid += 1
            right += 1
            if right - left >= len(s1):
                if valid == nt:
                    res.append(left)
                cp = s2[left]
                if cp in need and window[cp] == need[cp]:
                    valid -= 1
                window[cp] -= 1
                left += 1
        return res


if __name__ == '__main__':
    print(Solution().checkInclusion(s1 = "trinitrophenylmethylnitramine", s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"))
