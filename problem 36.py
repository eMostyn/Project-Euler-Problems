#Function to check if n is a palindrome
def checkPal(n):
    #Convert it to string to allow subscript
    strN = str(n)
    rev = ""
    #Create new string starting from last to first
    for i in reversed(range(len(strN))):
        rev += strN[i]
    #If equal then is a palindrome
    if strN == rev:
        return True
    return False

#Function to answer the Q
def compute():
    total = 0
    #For each number
    for i in range(0,1000000):
        #If both the base 10 and base 2 representations are palindrome and it to total
        if checkPal(i) == True and checkPal(int(bin(i)[2:])) == True:
            total += i
    return total
                    


print(compute())
