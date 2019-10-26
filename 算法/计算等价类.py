class Number:
    def __init__(self,val):
        self.val=val
        self.set=[]
        self.visited=False
        self.set.append(val)

class EquivalClass:
    def __init__(self,n,A,B):
        self.numArray=[]
        for i in range(n):
            self.numArray.append(Number(i))
        for i in range(len(A)):
            a=A[i]
            b=B[i]
            self.makeSet(self.numArray[a],self.numArray[b])

    def makeSet(self,numberA,numberB):
        numberA.set.extend(numberB.set)
        numberB.set=numberA.set

    def printAllEquivalSet(self):
        i=len(self.numArray)-1
        while i>=0:
            self.printEquvalSet(self.numArray[i])
            i-=1

    def printEquvalSet(self,number):
        if number.visited is True:
            return
        number.visited=True
        print("{",end="")
        dd=len(number.set)-1
        while dd>=0:
            print("{0}".format(number.set[dd]),end=" ")
            self.numArray[number.set[dd]].visited=True
            dd-=1
        print("}")

n=7
A=[1,5,3,6]
B=[2,1,0,5]
equival=EquivalClass(n,A,B)
equival.printAllEquivalSet()
