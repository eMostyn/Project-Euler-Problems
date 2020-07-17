#Main function to solve problem
def compute():
    #Total number of nums > 1,000,000
    total = 0
    #For each number in the range
    for i in range(23,101):
        #For each possible r 
        for j in range(1,i):
            #Generate the number using the formula
            num = factorial(i)/(factorial(j)*(factorial(i-j))
            #If its over 1 million add 1 to the total
            if num > 1000000:
                total += 1
    return total




#Function to generate factorial
def factorial(n):
    #Total starts at n
    total = n
    #Multiply total by the num then decrease it till its 1
    while n > 1:
        n -= 1
        total *= n
    #Return the total 
    return total


print(compute())
