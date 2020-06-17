import math

#Function to check if num is prime 
def checkPrime(n):
    #Check every number from 2 -> square root of number
    for i in range(2,math.isqrt(abs(n)+1)):
        #If the number isnt prime return False
        if n%i == 0:
            return False
    #Number is prime
    return True

#Function to generate the amount of consecutive prime numbers
def generateConValues(a,b):
    #Number of con primes
    counter = 0;
    #While that num is prime
    while(checkPrime(counter**2 + a*counter + b)==True):
        #Increase the num
        counter += 1
    #Remove 1 to make correct amount
    return counter-1


#Function to find largest consecutive prime values
def findValues():
    largest = 0
    largestA = 0
    largestB = 0
    #Loops start from a= -1000 and loops b 
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            #Num of con primes
                num = generateConValues(a,b)
                if num>largest:
                    #Saves largest current num and a,b then caused it
                    largest = num
                    largestA = a
                    largestB = b
    return largestA*largestB
