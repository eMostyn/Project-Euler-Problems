import itertools

#Set of nums allowed
nums = ["1","2","3","4","5","6","7","8","9"]
#Perms will be a list all the permutations of 
perms = list(itertools.permutations(nums))

def generateProducts():
    #List of all products already found
    products = []
    #Total = current sum of all products
    total = 0
    #For each different permutation
    for i in range(0,len(perms)):
        #Product will be 1,2 * 3,4,5
        product = int(perms[i][0]+perms[i][1]) * int(perms[i][2]+perms[i][3]+perms[i][4])
        #Convert the product into a list
        product = [int(d) for d in str(product)]
        #Sort the list but keep the original
        sortPro = sorted(product)
        #If the product sorted is equal to the remaining number sorted eg 6789 == 6789
        if sortPro == sorted(strToInt(perms[i][5:])):
            #If the product hasnt already been found
            if product not in products:
                #Add it to the total and the products list
                total += listToInt(product)
                products.append(product)
    #Same loop but for 1,2,3,4 * 5
    for i in range(0,len(perms)):
        product = int(perms[i][0]+perms[i][1]+perms[i][2]+perms[i][3]) * int(perms[i][4])
        product = [int(d) for d in str(product)]
        sortPro = sorted(product)
        if sortPro == sorted(strToInt(perms[i][5:])):
            if product not in products:
                total += listToInt(product)
                products.append(product)
    return total

#Function to convert list of string to list of int
def strToInt(n):
    n = list(n)
    for i in range(0,len(n)):
        n[i] = int(n[i])
    return n

#Function to convert list or seperate digits to int 
def listToInt(n):
    total = ""
    for i in range(0,len(n)):
        total += str(n[i])
    return int(total)


print(generateProducts())

