class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = delete = s.count('a')
        for c in s:
            delete -= 1 if c == 'a' else -1
            if delete < ans:
                ans = delete
        return ans


if __name__ == '__main__':
    print(Solution().minimumDeletions(s = "aabaabbab"))