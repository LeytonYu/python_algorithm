def mergeSort(A):
    if len(A) <= 1:
        return A
    half = int(len(A) / 2)
    first = mergeSort(A[:half])
    second = mergeSort(A[half:])
    i = 0
    j = 0
    newA = []
    while i < len(first) or j < len(second):
        if i < len(first) and j < len(second):
            if first[i] <= second[j]:
                newA.append(first[i])
                i += 1
            else:
                newA.append(second[j])
                j += 1
        else:
            if i < len(first):
                newA.append(first[i])
                i += 1
            if j < len(second):
                newA.append(second[j])
                j += 1
    return newA




def merge_sort(A):
    if len(A)<=1:
        return A
    half=int(len(A)/2)
    f=merge_sort(A[:half])
    s=merge_sort(A[half:])
    i=0
    j=0
    new=[]
    while i<len(f) or j <len(s):
        if i<len(f) and j<len(s):
            if f[i]<s[j]:
                new.append(f[i])
                i+=1
            else:
                new.append(s[j])
                j+=1
        else:
            if i<len(f):
                new.append(f[i])
                i+=1
            else:
                new.append(s[j])
                j+=1
    return new

A = [int(i) for i in input('请输入一些数字：').split()]
print(merge_sort(A))