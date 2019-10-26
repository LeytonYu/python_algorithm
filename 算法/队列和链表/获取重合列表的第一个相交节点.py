# +单项链表的奇偶排序
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class ListUtility:
    def __init__(self):
        self.head = None
        self.tail = None

    def createList(self, nodeNum):
        if nodeNum <= 0:
            return None
        head = None
        val = 0
        node = None
        while nodeNum > 0:
            if head is None:
                head = Node(val)
                node = head
            else:
                node.next = Node(val)
                node = node.next
                self.tail = node
            val += 1
            nodeNum -= 1
        self.head = head
        return head

    def getNodeById(self, num):
        node = self.head
        while num > 0:
            if node is not None:
                node = node.next
            num -= 1
        return node

    def printList(self, head):
        while head is not None:
            print("{0}->".format(head.val), end="")
            head = head.next
        print("null")


class ListReverse:
    def __init__(self, head):
        self.listHead = head
        self.newHead = None

    def recursiveReverse(self, node: Node):
        if node is None or node.next is None:
            self.newHead = node
            return node
        head = self.recursiveReverse(node.next)
        head.next = node
        node.next = None
        return node

    def getReverseList(self):
        self.recursiveReverse(self.listHead)
        return self.newHead


class ListIntersetFinder:
    def __init__(self, listHead1, listHead2):
        self.listHead1 = listHead1
        self.listHead2 = listHead2
        self.firstListLen = self.getListLen(self.listHead1)
        self.secondListLen = self.getListLen(self.listHead2)
        self.lenAfterReverse = 0

    def getListLen(self, head):
        len = 0
        while head is not None:
            head = head.next
            len += 1
        return len

    def getFirstIntersetNode(self):
        listReverse = ListReverse(self.listHead2)
        reverseHead = listReverse.getReverseList()
        self.lenAfterReverse = self.getListLen(self.listHead1)
        t3 = ((self.lenAfterReverse - self.firstListLen) + self.secondListLen - 1) / 2
        step = self.secondListLen - t3 - 1
        while step > 0:
            reverseHead = reverseHead.next
            step -= 1
        return reverseHead


class EvrnOddListSorter:
    def __init__(self, listHead: Node):
        self.listHead = listHead

    def sort(self):
        if self.listHead is None or self.listHead.next is None:
            return self.listHead
        evenHead = self.listHead
        oddHead = self.listHead.next
        oddHeadCopy = oddHead
        evenTail = evenHead

        while evenHead is not None and oddHead is not None:
            evenTail = evenHead
            evenHead.next = oddHead.next
            evenHead = evenHead.next
            if evenHead is not None:
                evenTail = evenHead
                oddHead.next = evenHead.next
                oddHead = oddHead.next
        evenTail.next = oddHeadCopy
        return self.listHead


def first():
    """
    获取重合列表的第一个相交节点
    """
    util_1 = ListUtility()
    util_2 = ListUtility()
    lst_1 = util_1.createList(9)
    lst_2 = util_2.createList(3)
    node = util_1.getNodeById(4)
    tail = util_2.getNodeById(2)
    tail.next = node
    util_1.printList(lst_1)
    util_2.printList(lst_2)

    checker = ListIntersetFinder(lst_1, lst_2)
    interset = checker.getFirstIntersetNode()
    print("The first interset node is", interset.val)


def second():
    """
    单项链表的奇偶排序
    """
    util = ListUtility()
    head = util.createList(10)
    sorter = EvrnOddListSorter(head)
    head = sorter.sort()
    util.printList(head)


if __name__ == '__main__':
    second()
