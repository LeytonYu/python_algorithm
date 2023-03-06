class Solution:
    def minimumDeletions(self, s: str) -> int:
        leftb, righta = 0, s.count('a')
        res = righta
        for c in s:
            if c == 'a':
                righta -= 1
            else:
                leftb += 1
            res = min(res, leftb + righta)
        return res


if __name__ == '__main__':
    print(Solution().minimumDeletions(s = "aababbab"))