class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        s_map = defaultdict(int)
        length = 0
        left, right = 0, 0
        while right < len(s):
            temp = s[right]
            s_map[temp] += 1
            right += 1
            while s_map[temp] > 1:
                dif = s[left]
                s_map[dif] -= 1
                left += 1
            if right - left > length:
                length = right - left
        return length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s = "abcabcbb"))

