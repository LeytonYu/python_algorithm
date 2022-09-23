class MyIndex:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.header = MyIndex(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index + 1 > self.size:
            return -1
        tp = self.header.next
        for i in range(index):
            tp = tp.next
        return tp.val

    def addAtHead(self, val: int) -> None:
        first = self.header.next
        new_index = MyIndex(val)
        if first:
            new_index.next = first
        self.header.next = new_index
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_index = MyIndex(val)
        tp = self.header.next
        if tp:
            while tp.next:
                tp = tp.next
            tp.next = new_index
        else:
            self.header.next = new_index
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        else:
            index -= 1
            tp = self.header.next
            for i in range(index):
                tp = tp.next
            new_index = MyIndex(val)
            new_index.next = tp.next
            tp.next = new_index
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            tp = self.header.next
            pre = self.header
            for i in range(index):
                pre = tp
                tp = tp.next
            pre.next = tp.next
            self.size -= 1

    def my_print(self):
        tp = self.header.next
        while tp:
            print(tp.val)
            tp = tp.next
        print('----------')


if __name__ == '__main__':
    obj = MyLinkedList()
    # param_1 = obj.get(0)
    # print(param_1, 'xixi')
    # obj.addAtHead(1)
    # obj.my_print()
    # obj.addAtTail(3)
    # obj.my_print()
    obj.addAtIndex(1, 0)
    # obj.my_print()
    # obj.deleteAtIndex(1)
    # obj.my_print()
    print(obj.get(0), 'xixi')
