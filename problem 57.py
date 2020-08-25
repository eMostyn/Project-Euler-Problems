#Main function to solve problem
def compute():
    #Keeps track of numerator and denominator, 3/2 is 1st iteration
    numer = 3
    denom = 2
    total = 0
    #For each iteration 1,1000
    for i in range(1,1000):
        #Add 2*denominator to the numerator and the numerator to the denominator
        #This is done at the same time so that the initial numerator is added, not the new one
        numer,denom = numer + 2*denom, denom + numer
        #If the numerator has more digits than the denominator then increment the counter
        if len(str(numer)) > len(str(denom)):
            total += 1
    #Return the total found cases
    return total



print(compute())
