import eulerlib

#Function to check if number is a circular prime
def checkCircular(n, primes):
    strNum = str(n)
    #Generates the different perms of num
    for i in range(0,len(strNum)):
        newNum = strNum[i:]+strNum[:i]
        #If that perm isnt prime then return false
        if primes[int(newNum)] == False:
            return False
    #All perms are prime so return true
    return True

#Function to find the amount of circulars
def compute():
    #List all primes then generate the t/f list
    primes = eulerlib.primes(1000000)
    isPrime = listPrimes(primes)
    count = 0
    #For each prime, check if circular
    for i in range(0,len(primes)):
        if checkCircular(primes[i],isPrime):
            count += 1
    return count

#Function to create a true/false list of primes so as for easier lookup
def listPrimes(n):
    tfList = [False for i in range(1000000)]
    #Update list to True where its prime
    for i in range(0,len(n)):
        tfList[n[i]] = True
    return tfList


print(compute())
