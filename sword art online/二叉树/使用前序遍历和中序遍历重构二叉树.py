# 树的定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree2(self, preorder, inorder):
    if len(preorder) == 0:
        return None
    i, j = 1, 0
    root = TreeNode(preorder[0])
    stack = [root]
    while i < len(preorder):
        node = TreeNode(preorder[i])
        tmp = None
        while stack and stack[-1].val == inorder[j]:
            tmp = stack.pop()
            j += 1
        if tmp:
            tmp.right = node
        else:
            stack[-1].left = node
        stack.append(node)
        i += 1
    return root
