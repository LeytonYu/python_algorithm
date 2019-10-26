def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i not in "+-*/":
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == "/":
                num = b // a
                if (num < 0) and (b % a != 0):
                    stack.append(num + 1)
                # 注意这里，如果b不能整除a，且小于零，根据取整原理，
                # 要在b//a的基础上加1。
                # 如6/-100,取整的话应该等于0.但是6//-100是等于-1的，
                # 因此要在6//-100 的基础上加1.
                else:
                    stack.append(num)
            if i == "+":
                stack.append(b + a)
            if i == "-":
                stack.append(b - a)
            if i == "*":
                stack.append(b * a)
    return stack.pop()  # 理论上来说返回stack[0]应该也可以，但是返回有误。


ss = input()
print(evalRPN(ss))
