#Function to check if the condition is met
def checkCondition(n):
    #Convert it to string so that we can 'sort' the string 
    string = sorted(str(n))
    #For each multiplier
    for i in range(2,7):
        #Create the new string
        newString = sorted(str(n*i))
        #If the strings dont match, return False 
        if newString != string:
            return False
    #All multipliers work so return True
    return True

#Main function to solve problem
def compute():
    num = 1
    #Keep increasing the number until the smallest that meets the condition is found
    while(checkCondition(num) == False):
        num += 1
    return num
