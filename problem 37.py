import eulerlib

#Function to check if number is trunctable l>r and r>l
def checkTrunc(n):
    num = n
    while num>=1:
        #Check if number is prime
        if eulerlib.is_prime(num) == False:
            return False
        #Remove last digit
        num = num//10
    num = n
    #Pos is to find largest power of 10
    pos = len(str(n))-1
    while num>=1:
        #Check prime
        if eulerlib.is_prime(num) == False:
            return False
        #Remove last digit
        num = num%10**pos
        pos -= 1
    return True


def compute():
    total = 0
    count = 0
    #Generate a large amount of primes
    primes = eulerlib.primes(1000000)
    #Iterate through the list
    for i in range(4,len(primes)):
        #If the number is prime add it to total
        if(checkTrunc(primes[i]) == True):
            total += primes[i]
            count += 1
        #Break if found all trunc primes
        if count == 11:
            return total


