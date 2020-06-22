import math


def generateNums():
    sums = 0
    for i in range(3,10000000):
        digs = [int(d) for d in str(i)]
        total = 0
        for j in range(0,len(digs)):
            total += math.factorial (digs[j])
        if total == i:
            sums += i
    return sums
