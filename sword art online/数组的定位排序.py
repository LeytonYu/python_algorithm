# 给定数组A以及下标i，调整数组，比A[i]小的在前面，接着是所有等于A[i]的元素，最后是比A[i]大的元素
def rearrangeByPiovt(array, begin, end, pivot, checkEqual):
    if end <= begin:
        return
    while begin < end:
        if (checkEqual is True and array[begin] >= pivot) or \
                (checkEqual is False and array[begin] > pivot):
            temp = array[begin]
            array[begin] = array[end]
            array[end] = temp
            end -= 1
        else:
            begin += 1
    return array


def rearrangeArray(array, i):
    if (len(array) <= 1):
        return array
    pivot = array[i]
    array = rearrangeByPiovt(array, 0, len(array) - 1, pivot, True)
    for j in range(len(array)):
        if array[j] >= pivot:
            break
    array = rearrangeByPiovt(array, j, len(array) - 1, pivot, False)
    return array


S = [6, 5, 5, 7, 9, 4, 3, 3, 4, 6, 8, 4, 7, 9, 2, 1]
i = 5
# print(rearrangeByPiovt(S,0,len(S)-1,S[i],True))
print(rearrangeArray(S, i))
