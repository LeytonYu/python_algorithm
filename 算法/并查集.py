class union_find(object):
    def __init__(self, data_list):
        # 保存节点的父节点
        self.father_dict = {}
        # 保存父节点的大小
        self.size_dict = {}
        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1
    def find(self, node):
        father = self.father_dict[node]
        # 递归查找父节点
        if(node != father):
            father = self.find(father)
        # 在查找父节点的时候，顺便把当前节点移动到父节点上面这个操作算是一个优化
        self.father_dict[node] = father
        return father
    def is_same_set(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)
    def union(self, node_a, node_b):
        # 对合并的两个节点做初步判断，判断是否为空
        if node_a is None or node_b is None:
            return
        # 分别查找两个节点的父节点
        a_head = self.find(node_a)
        b_head = self.find(node_b)
        # 当两个节点的父节点不一样时，才能做合并操作
        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            # 根据集合的大小做判断，尽量使小集合并到大集合
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size


if __name__ == '__main__':
    a = [1,2,3,4,5]
    union_find = union_find(a)
    union_find.union(1,2)
    union_find.union(3,5)
    union_find.union(3,1)
    print(union_find.is_same_set(2,5))  # True