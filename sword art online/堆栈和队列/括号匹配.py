class ParenMatch:
    def __init__(self, parens):
        self.parens = parens
        self.stack = []

    def isMatch(self):
        for c in self.parens:
            if c == '(':
                self.stack.append(c)
            elif c == ')':
                self.stack.pop()
            else:
                raise RuntimeError("Illegal character")
        if len(self.stack) != 0:
            return False
        return True


s = '((())(()))'
pm = ParenMatch(s)
print("the matching result is :", pm.isMatch())
