ct=0
def insert(stack, val):
    global ct
    ct+=1
    if len(stack) == 0 or val <= stack[-1]:
        stack.append(val)
        return stack
    t=stack.pop()
    insert(stack,val)
    stack.append(t)
    return stack


def sortByRecursion(stack):
    global ct
    ct += 1
    if len(stack) == 0:
        return stack
    v = stack.pop()
    stack = sortByRecursion(stack)
    stack = insert(stack, v)
    return stack


stack = [3, 2, 5, 6, 1, 4]
st = sortByRecursion(stack)
print(st,ct)
