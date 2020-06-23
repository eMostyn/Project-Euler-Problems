#Function to generate the fractional part of the decimal
def generateDecimal():
    num = ""
    i = 1
    #0 based so only need to go to 999999
    while(len(num) < 1000000):
        #Add i to the string
        num += str(i)
        i += 1
    return num



#Main function for the problem
def expression():
    num = generateDecimal()
    nums = []
    i = 1
    #While i<1000000 add the number as an int then multiply it by 10
    while i < 1000000:
        nums.append(int(num[i-1]))
        i *= 10
    total = 1
    #Multiply the digits together
    for j in range(0,len(nums)):
        total *= nums[j]
    return total


print(expression())
