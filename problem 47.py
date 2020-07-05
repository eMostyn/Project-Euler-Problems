import math, eulerlib

#Function to return amount of distinct prime factors
def generateFacs(n):
    #If the number is prime then it has only 2 facs
    if eulerlib.is_prime(n):
        return 1
    count = 0
    while n >1:
        count += 1
        #For each possible factor
        for i in range(2,math.isqrt(n)+1):
            #If it is a factor
            if n % i == 0:
                while True:
                    #Divide the number by the factor as many times as possible
                    n //= i
                    if n %i != 0:
                        break
                break
        else:
            break
    return count


#Main function to solve problem
def compute():
    #Holds amount of consecutive ints
    consecutive = 0
    i = 0
    #While the num is not 4
    while consecutive != 4:
        #Increase i
        i += 1
        #Check if the number has 4 distinct prime factors
        if generateFacs(i) == 4:
            consecutive += 1
        #If its not that reset consecutive
        else:
            consecutive = 0
    return i -3
