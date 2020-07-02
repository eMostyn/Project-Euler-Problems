import math

#Function to check if n is a pent number using inverse function
def isPent(n):
    num = (1+math.sqrt(1+24*n))/6
    return num == int(num)

#Function to check if n is a hex number using inverse function
def isHex(n):
    num = (1+math.sqrt(1+8*n))/4
    return num == int(num)

#Main function to compute
def compute():
    i = 40755
    #Keep increasing i until found
    while(True):
        i +=1
        #Generate the trinum then checkf if also pent and hex
        triNum = i*(i+1)/2
        if isPent(triNum) and isHex(triNum):
            return triNum



print(compute())
