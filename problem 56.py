#Function to compute problem
def compute():
    #Holds maximal digit sum so far
    maxi = 0
    #For each a <100
    for i in range(0,100):
        #For each b <100
        for j in range(0,100):
            #Generate number
            num = i**j
            #Set maxi to be the largest of the current maxi and the digit sum of num
            maxi = max(maxi,getDigiSum(num))
    return maxi



#Function to compute digit sum of n
def getDigiSum(n):
    #Convert to string to substring
    num = str(n)
    #Total will keep track of current sum
    total = 0
    #For each number in num
    for i in range(0,len(num)):
        #Add it to total
        total += int(num[i])
    #Return total
    return total


print(compute())
