import math

#Function to check if a given number is a pent number 
def isPent(n):
    #Uses inverse function to calculate, if penTest is an int then its a pent number
    penTest = (math.sqrt(24*n+1) +1)/6
    return penTest == int(penTest)

#Main function to solve problem
def compute():
    i =1
    while(True):
        #Increase i then generate k as a pent number
        i += 1
        k = i*(3*i-1)/2
        #For all pent numbers smaller than k 
        for a in range(i-1,0,-1):
            #Let j be pent number
            j  = a*(3*a-1)/2
            #Check if difference and sum conditions are met
            if isPent(k-j) and isPent(k+j):
                #If so its be found so return the difference
                return k-j


print(compute())
