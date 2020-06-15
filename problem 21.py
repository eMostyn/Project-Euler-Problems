#Function to find sum of divisors
def d(n):
    total = 0
    for i in range(1,n):
        if n%i == 0:
            total += i
    return total



def amiNum():
    #Records list of amicable numbers
    amiNums = []
    total = 0
    #For each number 
    for i in range(1,10000):
        #Num1 represents the sum of divisors of i
        num1 = d(i)
        #Num2 represents the sum of divisors of num1
        num2 = d(num1)
        #If i and num2 are the same but a!=b 
        if i == num2 and i != num1:
            #Add the i/num2 aka a/b to the list of aminums and the total if not already present
            if i not in amiNums:
                amiNums.append(i)
                total += i
            if num2 not in amiNums:
                amiNums.append(num2)
                total += num2
    print(amiNums)
    return total


print(amiNum())
                
