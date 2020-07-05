#Main function to solve problem
def compute():
    total = 0
    #For each number
    for i in range(1,1001):
        #Add then number to the total
        total += i**i
    #Return the last 10 digits
    return int(str(total)[-10:])
