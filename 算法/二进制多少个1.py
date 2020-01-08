def countOnes(x):
    # count=0;
    # while x>0:
    #     count+=1
    #     print(bin(x), bin(x - 1))
    #     x&=(x-1)
    # return count
    return sum(map(eval,list(bin(x)[2:])))  # More pythonic
x=int(input())
c=countOnes(x)
print('binary form of {0} is {1}'.format(x,bin(x)))
print('binary form of {0} contains {1} 1'.format(x,c))