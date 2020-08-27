import itertools,eulerlib,time

#Function to check if 2 numbers are concatenating  primes
def checkNums(a,b):
    #Generate a list of all permutations of a,b
    perms = list(itertools.permutations([a,b],2))
    #For each permutation 
    for i in range(0,len(perms)):
        num = ""
        #Converts each permutation from list to a string
        for j in range(0,len(perms[i])):
            num += str(perms[i][j])
        #Sets that position to new int to be tested
        perms[i] = int(num)
        #If the permutation is not a prime then return False, theyre not concatenating  primes
        if eulerlib.is_prime(perms[i]) == False:
            return False
    #All perms were prime
    return True

#Main function to solve problem 
def compute():
    #List of primes, set cap of 10000 for now
    primes = eulerlib.primes(10000)
    #Pick a prime as the first number in the chain
    #Chain will be [a,b,c,d,e] as 5 primes
    for a in primes:
        #Pick a prime as second number in the chain
        for b in primes:
            #Only continue in the code is b is larger than a 
            if b<a:
                continue;
            #If a,b are concatenating  primes then move to find next number in chain
            if checkNums(a,b):
                #For each c, which is larger than b and therefore larger than a
                for c in primes:
                    if c<b:
                        continue;
                    #Check if it forms a concatenating chain with a,b
                    if checkNums(a,c) and checkNums(b,c):
                        #Find 4th number where d is larger than c,b,a
                        for d in primes:
                            if d<c:
                                continue;
                            #Check if it forms a concatenating chain with a,b,c
                            if checkNums(a,d) and checkNums(b,d) and checkNums(c,d):
                                #Find 5th number in chain
                                for e in primes:
                                    if e<d:
                                        continue;
                                    #If it forms a chain then return the sum
                                    if checkNums(a,e) and checkNums(b,e) and checkNums(c,e) and checkNums(d,e):
                                        return a,b,c,d,e,a+b+c+d+e
            

start = time.time()
print(compute())
end = time.time() - start
print(end)
