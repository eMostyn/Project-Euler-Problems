import eulerlib


#Function to check if the num fits the criteria
def checkNum(n):
    #Generate a list of squares and primes lower than n 
    squares = generateSquares(n)
    primes = eulerlib.primes(n)
    #For each prime number
    for i in range(0,len(primes)):
        #For each square number
        for j in range(0,len(squares)):
            #Check if the criteria is met for this combination
            if primes[i] + 2*squares[j] == n:
                return True
    return False


#Function that generates a list of squares smaller than n
def generateSquares(n):
    squares = []
    i = 0
    while(i**2 < n):
        i += 1
        squares.append(i**2)
    return squares

#Main function
def compute():
    #Starts at 3, checks every odd number 
    i = 1
    while(True):
        i += 2
        #If i is not prime
        if(eulerlib.is_prime(i) == False):
            #If the conditions is not met return the num
            if checkNum(i) == False:
                return i

