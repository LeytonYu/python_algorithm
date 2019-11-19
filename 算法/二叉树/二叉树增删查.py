class Node(object):
    def __init__(self, item):
        self.item = item  # 表示对应的元素
        self.left = None  # 表示左子节点
        self.right = None  # 表示右子节点

    def __str__(self):
        # print 一个 Node 类时会打印 __str__ 的返回值
        return str(self.item)


class Tree(object):
    def __init__(self):
        # 根节点定义为 root 永不删除，作为哨兵使用。
        self.root = Node('root')

    def add(self, item):
        node = Node(item)
        # 如果二叉树为空，那么添加的点将插入 root 节点处
        if self.root is None:
            self.root = node
        else:
            # 在 q 列表中，添加二叉树的根节点
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                # 左子树为空则将点添加到左子树
                if pop_node.left is None:
                    pop_node.left = node
                    return
                # 右子树为空则将点添加到右子树
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, item):
        if self.root.item == item:
            # 根节点没有父节点
            return None
        # 在 tmp 列表中，添加二叉树的根节点
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            # 如果点的左子树为要寻找的点
            if pop_node.left and pop_node.left.item == item:
                # 返回这个点，即为寻找点的父节点
                return pop_node
            # 如果点的右子树为要寻找的点
            if pop_node.right and pop_node.right.item == item:
                # 返回这个点，即为寻找点的父节点
                return pop_node
            # 添加 tmp 列表里的元素
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def delete(self, item):
        # 如果根为空，就什么也不做
        if self.root is None:
            return False

        parent = self.get_parent(item)
        if parent:
            # 确定待删除节点
            del_node = parent.left if parent.left.item == item else parent.right
            # 待删除节点的左子树为空时
            if del_node.left is None:
                # 如果待删除节点是父节点的左孩子
                if parent.left.item == item:
                    parent.left = del_node.right
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = del_node.right
                # 删除变量 del_node
                del del_node
                return True
            # 待删除节点的右子树为空时
            elif del_node.right is None:
                # 如果待删除节点是父节点的左孩子
                if parent.left.item == item:
                    parent.left = del_node.left
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = del_node.left
                # 删除变量 del_node
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                # 待删除节点的右子树
                tmp_next = del_node.right

                # 寻找待删除节点右子树中的最左叶子节点并完成替代
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    # 让 tmp_next 指向右子树的最左叶子节点
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                # 如果待删除节点是父节点的左孩子
                if parent.left.item == item:
                    parent.left = tmp_next
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

    def preorder(self, node):  # 先序遍历
        if node is None:
            return []
        result = [node.item]
        left_item = self.preorder(node.left)
        right_item = self.preorder(node.right)
        return result + left_item + right_item

    def inorder(self, node):  # 中序遍历
        if node is None:
            return []
        result = [node.item]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + result + right_item

    def postorder(self, node):  # 后序遍历
        if node is None:
            return []
        result = [node.item]
        left_item = self.postorder(node.left)
        right_item = self.postorder(node.right)
        return left_item + right_item + result

if __name__=='__main__':
    tree=Tree()
    for i in range(20 ):
        tree.add(i)
    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))
