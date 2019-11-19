class TreeNode:
    def __init__(self,val):
        self.value=val
        self.right=None
        self.left=None

class TreeUtil:
    def __init__(self):
        self.root=None

    def addTreeNode(self,node):
        if self.root is None:
            self.root=node
            return
        currentNode=self.root
        while currentNode is not None:
            prevNode=currentNode
            if currentNode.value>node.value:
                currentNode=currentNode.left
            else:
                currentNode=currentNode.right
        if prevNode.value>node.value:
            prevNode.left=node
        else:
            prevNode.right=node

    def get_root(self):
        return self.root

    def getDeepth(self, Root):
        if Root is None:
            return 0
        nright = self.getDeepth(Root.right)
        nleft = self.getDeepth(Root.left)
        return max(nright, nleft) + 1

    def IsBalance_solution(self, pRoot):
        if pRoot is None:
            return True
        right = self.getDeepth(pRoot.right)
        left = self.getDeepth(pRoot.left)
        if abs(right - left) > 1:
            return False
        return self.IsBalance_solution(pRoot.right) and self.IsBalance_solution(pRoot.left)

array=[6,4,9,2,5,7,10,1,3,8]
util=TreeUtil()
for node in array:
    n=TreeNode(node)
    util.addTreeNode(n)
root=util.get_root()
if util.IsBalance_solution(root):
    print("It is balanced")
else:
    print("It is not balanced")
