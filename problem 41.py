import eulerlib

#Function to check if a number of length n is pandigital to n
def checkPan(n):
    #Convert it to string
    strN = str(n)
    numsReq = []
    #Add the numbers required to the list
    for i in range(1, len(strN)+1):
        numsReq.append(str(i))
    #If the 2 are equal then its pandigital
    if sorted(strN) == numsReq:
        return True
    return False

#Main function to answer q
def compute():
    largest = 0
    #Anything beyond runs out of memory...
    primes = eulerlib.primes(87654321)
    #For all the primes check if pan, is so update largest we've found
    for i in range(0,len(primes)):
        if checkPan(primes[i]):
            largest = primes[i]
    return largest



print(compute())
