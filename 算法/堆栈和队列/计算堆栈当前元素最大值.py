# 栈类（默认存储的元素都是整数）
class Stack():
    # 初始化
    def __init__(self):
        self.__stack = []

        self.__max2 = []  # 法二消耗的空间
        self.__max3 = []  # 法三消耗的空间

    # 入栈
    def append(self, item):
        self.__stack.append(item)

        # 法二
        if len(self.__max2) == 0:
            self.__max2.append(item)
        else:
            if self.__max2[-1] > item:
                self.__max2.append(self.__max2[-1])
            else:
                self.__max2.append(item)

        # 法三
        if len(self.__max3) == 0:
            self.__max3.append(0)
        else:
            if self.__stack[self.__max3[-1]] < item:
                self.__max3.append(len(self.__stack) - 1)
            else:
                pass

    # 出栈
    def pop(self):
        # 法二
        self.__max2.pop()
        # 法三
        if len(self.__stack) - 1 == self.__max3[-1]:
            self.__max3.pop()
        else:
            pass

        return self.__stack.pop()

    # 判断是否为空
    def isempty(self):
        return len(self.__stack) == 0

    # 返回栈的大小
    def length(self):
        return len(self.__stack)

    # 获取栈顶元素（不出栈）
    def getup(self):
        if self.isempty():
            raise IndexError
        else:
            return self.__stack[-1]

    # 获取栈内元素最大值（法一） 不建议用此方法，每次调用此方法都会查一遍站内元素，时间复杂度O（n）
    def getMax1(self):
        return max(self.__stack)

    # 获取栈内元素最大值（法二） 牺牲空间换时间，空间复杂度O（n），存储栈内每个元素对应的最大值
    def getMax2(self):
        if len(self.__max2) == 0:
            raise IndexError
        else:
            return self.__max2[-1]

    # 获取栈内元素最大值（法三，最优） 牺牲空间换时间，空间复杂度 < O（n），只存储最大值下标
    def getMax3(self):
        if len(self.__max3) == 0:
            raise IndexError
        else:
            return self.__stack[self.__max3[-1]]


# 测试
if __name__ == '__main__':
    s = Stack()
    s.append(1)
    s.append(2)
    assert s.length() == 2
    assert s.isempty() == False
    assert s.pop() == 2
    assert s.getup() == 1
    s.pop()
    assert s.isempty()
    try:
        s.getup()
        print("error")
    except IndexError:
        pass

    s.append(4)
    s.append(6)
    s.append(1)
    s.append(2)
    s.append(4)
    s.append(-1)
    s.append(10)
    assert s.getMax1() == 10
    assert s.getMax2() == 10
    assert s.getMax3() == 10
    s.pop()
    assert s.getMax1() == 6
    assert s.getMax2() == 6
    assert s.getMax3() == 6
