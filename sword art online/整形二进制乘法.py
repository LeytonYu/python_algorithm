def binaryAdd(x, y):
    # x，y是进行二进制相加的两个整数，v表示最终结果，
    # advance表示进位，r表示当前相加的比特位在二进制中的位置。
    v = 0
    advance = 0
    r = 0
    while x > 0 or y > 0:
        # 获取当前最低位的比特位值
        i = x & 1
        j = y & 1
        x = x >> 1
        y = y >> 1
        b = i ^ j
        if b == 1:
            if advance == 1:
                b = 0
        else:
            if i & j == 1:
                if advance == 1:
                    b = 1
                else:
                    b = 0
                    advance = 1
            else:
                if advance == 1:
                    b = 1
                    advance = 0
        b = b << r
        v |= b
        r += 1
    if advance == 1:
        v |= (advance << r)
    return v


def binaryMutiply(a, b):
    stack = []
    s = 0
    while b > 0:
        if b & 1 == 1:
            stack.append(a << s)
        else:
            stack.append(0)
        b = b >> 1
        s += 1

    while (len(stack) > 1):
        x = stack.pop()
        y = stack.pop()
        z = binaryAdd(x, y)
        stack.append(z)
    return stack.pop()


a, b = [int(i) for i in input().split()]
v = binaryMutiply(a, b)
print(v)
