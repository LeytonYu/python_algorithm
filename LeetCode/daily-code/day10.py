from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        st = 0
        ss = suits[0]
        for s in suits:
            if s == ss:
                st += 1
        if st == 5:
            return 'Flush'
        my_map = {}
        for r in ranks:
            my_map.setdefault(r, 0)
            my_map[r] += 1
        order_values = sorted(my_map.values(), reverse=True)
        if 3 <= order_values[0]:
            return 'Three of a Kind'
        elif order_values[0] == 2:
            return 'Pair'
        else:
            return 'High Card'


if __name__ == '__main__':
    print(Solution().bestHand([1, 2, 4, 4, 5], suits=["d", "a", "a", "b", "c"]))
