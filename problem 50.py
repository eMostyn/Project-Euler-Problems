import eulerlib

#Main function to solve problem
def compute():
    #Generate list of all primes under 1 million
    primes = eulerlib.primes(999999)
    #Will store the current largest result and consecutive length
    result = 0
    largestConsec = 0
    #For each prime in the list
    for i in range(0,len(primes)):
        #Start the sum at that prime and the consecutive number at 1
        Sum = primes[i]
        consec = 1
        #For each prime above that prime
        for j in range(i+1,len(primes)):
            #Add it to the sum and increment consec
            Sum += primes[j]
            consec += 1
            #If the prime is too large already then stop
            if Sum >= 1000000:
                break
            #If the sum is prime and its a longer consec than the current largest
            if eulerlib.is_prime(Sum) and consec > largestConsec:
                #Set the result and largestConsec to current sum and consec
                result = Sum
                largestConsec = consec
    #Return largest found
    return result
            
