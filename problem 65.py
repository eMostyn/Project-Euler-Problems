#Function to generate the values for a
def generateVals():
    seq = []
    k = 0
    #In groups of 3
    for i in range(1,10000,3):
        #Using formula provided append numbers
        k+= 1
        seq.append(1)
        seq.append(2*k)
        seq.append(1)
    return seq

#Function to calculate sum from final integer
def calculateSum(num):
    total = 0
    while num > 0:
        #Take the last digit, and then remove it
        total += num%10
        num = num//10
    return total

#Function to solve problem
def compute():
    #Get the values for a 
    vals = generateVals()
    #Starting at 
    numerators = [3,8]
    #For the correct amount of times
    for i in range(2,99):
        #Using the formula a*nk-1 + nk-2
        newNum = vals[i] * numerators[1] + numerators[0]
        #Set the numerators to be used for next calculation
        numerators = [numerators[1],newNum]
    #Return the sum of that integer
    return(calculateSum(numerators[1]) )
          
print(compute())
