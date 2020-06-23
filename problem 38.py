#Function to check if number is pandigital
def checkPan(n):
    pan = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    sort = sorted(str(n))
    #If when the string is sorted it is equal to 1-9 then its pandigital
    if sort != pan:
        return False
    return True

#Function to generate the product given a list and a number it multiplies then number by each in the list
#and concatenates it
def generateProduct(n,mults):
    output = ""
    for i in range(0,len(mults)):
        newNums = str(n*mults[i])
        output += newNums
    return int(output)

#Main function, tries every combination 
def compute():
    largest = 0
    mults = [1]
    #Tries 1-9 as 10 would create a 0
    for i in range(2,10):
        mults.append(i)
        #Upper bound for j changes depending on i 
        for j in range(1,10**(9 // i) ):
            num = generateProduct(j,mults)
            if checkPan(num):
                if largest < num:
                    largest = num
    return largest
