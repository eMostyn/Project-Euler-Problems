import math

def generateTriNums():
    numOfFacs = 0
    i= 7
    triNum = 28
    while(numOfFacs < 500):
        i+= 1
        triNum += i
        numOfFacs = getFacs(triNum)
    return triNum


def getFacs(num):
    amount = 0
    for i in range(1, math.isqrt(num)+1):
        if(num % i == 0):
            amount += 1
    return amount*2

print(generateTriNums())
