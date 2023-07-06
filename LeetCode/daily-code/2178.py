from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        st = []
        idx = 1
        while finalSum >= 2 * idx:
            finalSum -= 2 * idx
            st.append(2 * idx)
            idx += 1
        if finalSum > 0:
            st.append(st.pop() + finalSum)
        return st


if __name__ == '__main__':
    print(Solution().maximumEvenSplit(32))

