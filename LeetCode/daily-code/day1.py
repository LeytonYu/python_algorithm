class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        step = 0
        temp = pieces
        length = len(arr)
        while True:
            continue_flag = False
            for i, lst in enumerate(pieces):
                lt = len(lst)
                same = True
                for index, number in enumerate(lst):
                    if arr[index + step] != number:
                        same = False
                        break
                if same:
                    temp.pop(i)
                    continue_flag = True
                    step += lt
            print(step, length)
            if step == length:
                return True
            if not continue_flag:
                return False
            pieces = temp


if __name__ == '__main__':
    arr = [15,88]
    pieces = [[88],[15]]
    res = Solution().canFormArray(arr, pieces)
    print(res)