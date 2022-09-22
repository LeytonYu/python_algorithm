def in_order(root):
    # 中序遍历
    if root is None:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.rigth)


def pre_order(root):
    # 先序遍历
    if root is None:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def bac_order(root):
    '''后序打印'''
    if root is None:
        return
    bac_order(root.left)
    bac_order(root.right)
    print(root.val, end=' ')


"""Morris遍历"""


def preorder(root):
    if not root: return
    p = root
    prenode = None
    while p:
        if p.left:
            prenode = p.left
            while prenode.right and prenode.right != p:
                prenode = prenode.right
            if not prenode.right:  # 建立链接方便回溯
                print(p.val)  # 打印
                prenode.right = p
                p = p.left
                continue
            if prenode.right == p:
                prenode.right = None  # 回溯完成删除多余链接
        if not p.left: print(p.val)  # 打印
        p = p.right


def inorder(root):
    if not root: return
    p = root
    prenode = None
    while p:
        if p.left:
            prenode = p.left
            while prenode.right and prenode.right != p:
                prenode = prenode.right
            if not prenode.right:  # 建立链接方便回溯
                prenode.right = p
                p = p.left
                continue
            if prenode.right == p:
                print(p.val)  # 打印
                prenode.right = None  # 回溯完成删除多余链接
        if not p.left: print(p.val)  # 打印
        p = p.right


def ReverseAndPrint(root):
    if not root: return
    node = root
    t = None
    while node:
        p = node.right
        node.right = t
        t = node
        node = p
    node = t
    t = None
    while node:
        p = node.right
        print(node.val)
        node.right = t
        t = node
        node = p


def postorder(root):
    if not root: return
    p = root
    prenode = None
    while p:
        if p.left:
            prenode = p.left
            while prenode.right and prenode.right != p:
                prenode = prenode.right
            if not prenode.right:  # 建立链接方便回溯
                prenode.right = p
                p = p.left
                continue
            else:  # prenode.right == p
                prenode.right = None  # 回溯完成删除多余链接
                ReverseAndPrint(p.left)
        p = p.right
    ReverseAndPrint(root)
