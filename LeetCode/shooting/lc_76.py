class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, length = 0, float('inf')
        need = {}
        window = {}
        for c in t:
            need.setdefault(c, 0)
            need[c] += 1
        right = 0
        valid = 0
        start = 0
        nt = len(need)
        while right < len(s):
            tp = s[right]
            window.setdefault(tp, 0)
            window[tp] += 1
            if tp in need and window[tp] == need[tp]:
                valid += 1
            right += 1
            while valid == nt:
                if right - left < length:
                    length = right - left
                    start = left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    valid -= 1
                left += 1
        return '' if length > len(s) else s[start: start + length]


if __name__ == '__main__':
    print(Solution().minWindow(s = "cabwefgewcwaefgcf", t = "cae"))
