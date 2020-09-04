#Main function to solve problem 
def compute():
    #Counter records how many currently found
    total = 0
    #For i 1-9 where i^j
    for i in range(1,10):
        #For j 1-29, set as 29 as any larger will probably not be fitting
        for j in range(1,30):
            #Generate num
            num = i ** j
            #Check if the length of the number is equal to the power
            if len(str(num)) == j:
                #Increment counter if so
                total += 1
    return total



print(compute())
