#Function to check if n is a lychel number
def getLychel(n):
    num = n
    #Will count number of iterations
    its = 1
    #While the amount of iterations are below 0
    while its < 50:
        #Iterate the counter
        its += 1
        #Make num the sum of number + number reversed 
        num = num + int(str(num)[::-1])
        #If its a palindrome then its not a lychel number
        if str(num) == str(num)[::-1]:
            return False
    #Exceeded the amount of iterations so its a lychel number
    return True


#Main function to solve the problem
def compute():
    #Counts the amount of lychel numbers found
    total = 0
    #For each number 1 to 9999
    for i in range(1,10000):
        #If its a lychel number, add to the total 
        if getLychel(i):
            total += 1
    return total



print(compute())


