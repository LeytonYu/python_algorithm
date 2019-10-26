class ArrayPermutation:
    def __init__(self, A, P):
        self.A = A
        self.P = P
        self.doPermutation()

    def doPermutation(self):
        for i in range(len(self.A)):
            change = self.relocate(i)
            temp = self.A[change]
            self.makeShift(i, change)
            self.A[i] = temp

    def relocate(self, i):
        change = self.P[i]
        k = 0
        j = 0
        while j < i:
            if self.P[j] > change:
                k += 1
            j += 1
        return change + k

    def makeShift(self, begin, end):
        i = end
        while i > begin:
            self.A[i] = self.A[i - 1]
            i -= 1

    def getPermutation(self):
        return self.A

A=[1,2,3,4,5,6]
B=[3,1,5,4,0,2]
ap=ArrayPermutation(A,B)

print(ap.getPermutation())