from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def op_calculate(opp, vs):
            aa = vs.pop()
            bb = vs.pop()
            cc = set()
            if opp == '*':
                for b in bb:
                    for a in aa:
                        cc.add(b + a)
            elif opp == '+':
                cc = aa | bb
            if cc:
                vs.append(cc)
        if '}' not in expression:
            return [expression]
        operate_stack = []
        value_stack = []
        pre = ''
        for s in expression:
            if s == '{':
                if pre.isalpha() or pre == '}':
                    operate_stack.append('*')
                operate_stack.append(s)
            elif s == ',':
                while operate_stack[-1] == '*':
                    op_calculate(operate_stack.pop(), value_stack)
                operate_stack.append('+')
            elif s.isalpha():
                if pre == '}' or pre.isalpha():
                    operate_stack.append('*')
                value_stack.append(set(s))
            elif s == '}':
                while operate_stack[-1] != '{':
                    op = operate_stack.pop()
                    op_calculate(op, value_stack)
                operate_stack.pop()
            else:
                print('nmd')
            pre = s

        for op in operate_stack:
            op_calculate(op, value_stack)
        return sorted(value_stack.pop())


if __name__ == '__main__':
    print(Solution().braceExpansionII(expression = "{a{x,ia,o}w,{n,{g,u,o},{a,x,ia,o,w}},er}"))