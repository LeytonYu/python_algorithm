class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeUtility:
    def __init__(self):
        self.treeHead = None

    def createTree(self):
        vals = [5, 7, 3, 1, 2, 6, 8, 4, 9, 0]
        for val in vals:
            self.insertTreeNode(val)
        return self.treeHead

    def insertTreeNode(self, val):
        if self.treeHead is None:
            self.treeHead = TreeNode(val)
            return
        node = self.treeHead
        # print(id(node), id(self.treeHead))
        while node is not None:
            if node.val > val and node.left is not None:
                node = node.left
                continue
            if node.val < val and node.right is not None:
                node = node.right
                continue
            temp = TreeNode(val)
            if node.val > val:
                node.left = temp
                break
            if node.val < val:
                node.right = temp
                break


def printTree(head):
    if head is None:
        return
    list = []
    list.append(head)
    while len(list) > 0:
        t = list[0]
        print(list[0].val,end=' ')
        del list[0]
        if t.left is not None:
            list.append(t.left)
        if t.right is not None:
            list.append(t.right)


tree = TreeUtility()
head = tree.createTree()
printTree(head)
