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

def fhfNew(head):
    if head is None or head.next is None:
        return head
    nhead=fhfNew(head.next)
    head.next.next=head
    head.next=None
    return nhead


utility = ListUtility()
head = utility.createList(10)
utility.printList(head)
# reverse = ListReverse(head)
# utility.printList(reverse.getReverseList())
utility.printList(fhfNew(head))
