import random


class Node():
    def __init__(self, val):
        self.next = None
        self.val = val
        self.visited = False
        self.jump = None


class ListUtility:
    def __init__(self):
        self.head = None
        self.tail = None
        self.map = {}

    def createList(self, nodeNum):
        if nodeNum <= 0:
            return None
        self.listLength = nodeNum
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
            self.map[val] = node
            val += 1
            nodeNum -= 1
        self.head = head
        return head

    def createJumpNode(self, head):
        while head is not None:
            n = random.randint(0, self.listLength - 1)
            head.jump = self.map[n]
            head = head.next

    def printPostingList(self, head):
        while head is not None:
            print("(node val: {0} jump val: {1})->".format(head.val, head.jump.val), end="")
            head = head.next
        print("null")

class PostingListCopy:
    def __init__(self,head):
        self.originalHead=head
        self.copyHead=None
    def copyPostingList(self):
        self.createPostingNodes()
        self.createJumpNodes()
        self.adjustNextPointer()
        return self.copyHead
    def createPostingNodes(self):
        node=None
        tempHead=self.originalHead
        while tempHead is not None:
            node=Node(tempHead.val)
            node.next=tempHead.next
            tempHead.next=node
            tempHead=node.next
    def createJumpNodes(self):
        temp=self.originalHead
        self.copyHead=temp.next
        while temp is not None:
            cpNode=temp.next
            cpNode.jump=temp.jump.next
            temp=cpNode.next
    def adjustNextPointer(self):
        temp=self.originalHead
        while temp is not None:
            cpNode=temp.next
            temp.next=cpNode.next
            temp=temp.next
            if temp is not None:
                cpNode=temp.next
            else:
                cpNode.next=None

util = ListUtility()
head = util.createList(10)
util.createJumpNode(head)
util.printPostingList(head)
pc=PostingListCopy(head)
copyHead=pc.copyPostingList()
print("print copied posting list:")
util.printPostingList(copyHead)
