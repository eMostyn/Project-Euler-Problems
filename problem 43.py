import itertools

#The numbers the substring will need to divide by
divs = [2,3,5,7,11,13,17]
nums = [0,1,2,3,4,5,6,7,8,9]
#Will generate a list of permutations
perms  = list(itertools.permutations(nums))

#Function to turn list of nums into actual number
def getPerm(i):
    num = ''
    for j in range(0,len(perms[i])):
        num += str(perms[i][j])
    return int(num)

#Main function to solve problem
def compute():
    total = 0
    #For each permutation
    for i in range(0,len(perms)):
        num = getPerm(i)
        #If it works add it to total
        if checkSub(num):
            total += num
    return total

#Function to check if substring property is met
def checkSub(n):
    #Starting at position 0, used for divs
    pos = 0
    #Turn it to string
    string = str(n)
    #If only 9 long then starting 0 was removed, add it back to string
    if len(string) != 10:
        string = '0' + string
    #Loop to check property
    for j in range(1,8):
        #Generate number to check
        num = int(string[j]+string[j+1]+string[j+2])
        #If it isnt divisible then return false
        if num % divs[pos] != 0:
            return False
        #Move to next divisor
        else:
            pos += 1
    return True


print(compute())
