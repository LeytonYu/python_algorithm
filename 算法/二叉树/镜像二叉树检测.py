def isMirror(l, r):
    if not l and not r:
        return True
    if not l or not r:
        return False
    if l.val != r.val:
        return False
    return isMirror(l.left, r.right) and isMirror(l.right, r.left)
