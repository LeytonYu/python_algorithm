from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        my_map = {}
        res = []
        for name in names:
            tp = name
            k = my_map.get(tp, 1)
            while my_map.get(tp):
                tp = f"{name}({k})"
                k += 1
            my_map[tp] = 1
            if tp != name:
                my_map[name] += 1
            res.append(tp)
        return res


if __name__ == '__main__':
    print(Solution().getFolderNames(names = ["wano","wano","wano","wano"]))


