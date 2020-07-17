import eulerlib

#Function to generate numbers given then number and indexs to replace
def generateNums(n,toReplace):
    #Nums will be the list of numbers generated
    nums = []
    #Having the number as a string so as to index
    string = str(n)
    #For each digit 0-9
    for k in range(0,10):
        #For each position 
        for j in range(0,len(toReplace)):
            #We dont add the number if it is a prevailing 0 as they dont count
            if toReplace[j] == 0 and k == 0:
                continue
            #Create the new string which has the number replaced
            else:
                string = string[:toReplace[j]]+str(k)+string[toReplace[j]+1:]
        #Add the new string to the nums list as an int
        nums.append(int(string))
    return nums

#Function to find any repetition in a list
def findRep(n):
    #Convert it to a string but discount the last digit as if we replace the last digit there cannot be 8 primes
    string = str(n)[:-1]
    toReplace = []
    #For each number in the string
    for i in range(0,len(string)):
        indexs = [i]
        digit = string[i]
        #For each remaining digit
        for j in range(i+1,len(string)):
            #If the digit is equal to the number we are checking
            if string[j] == digit:
                indexs.append(j)
        #If this number is larger the current largest repetition found
        if len(indexs)> len(toReplace):
            toReplace = indexs
    return toReplace

#Function to see how many primes are in the list
def checkPrimes(n):
    num = 0
    #For each number in the list
    for i in range(0,len(n)):
        #If its prime add 1 to the counter
        if eulerlib.is_prime(n[i]):
            num += 1
    return num

#Main function to solve the problem
def compute():
    #Generate a list of all primes below 1 million
    primes = eulerlib.primes(1000000)
    #Starting 5000 in because a fairly large prime will be required
    for i in range(5000,len(primes)):
        #Get the index of where to replace
        repetition = findRep(primes[i])
        #If the list isnt empty
        if repetition != []:
            #Generate then nums
            nums = generateNums(primes[i],repetition)
            #Check how many are prime
            num = checkPrimes(nums)
            #If we have found the first one with 8
            if num == 8:
                #Find the first prime in the list
                return firstPrime(nums)
            
#Function to find the first prime in the sorted list
def firstPrime(n):
    #For each prime, if its prime return it
    for i in range(0,len(n)):
        if eulerlib.is_prime(n[i]):
            return n[i]



print(compute())
