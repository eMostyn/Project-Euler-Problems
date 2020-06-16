#Function to generate the sum of all divisors of n
def sumOfDivisors(n):
    total = 0
    for i in range(1,n):
        if n%i == 0:
            total+= i
    return total

#Generates the list of abundants 
def generateAbundant():
    abundant = []
    for i in range(1,28123):
        #If the sum is greater add it
        if sumOfDivisors(i) > i:
            abundant.append(i)
    return abundant

#Function to generate True/False for whether can be represented 
def generateTF():
    #Create a list all false
    nums = [False] * 28123 
    abundant = generateAbundant()
    #Generate all the sums
    for i in range(0,len(abundant)-1):
        for j in range(i,len(abundant)):
            if(abundant[i] + abundant[j] < 28123):
                #Set that position to True as it can be represented
                nums[abundant[i] + abundant[j]] = True
    return nums

#Summation goes through and adds all False to total
def summation():
    sums = generateSums()
    total = 0
    for i in range(0,len(sums)):
        if sums[i] == False:
            total += i
    return total


print(summation())
