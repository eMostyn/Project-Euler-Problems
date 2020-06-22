import fractions
#Note: faction < 1 in value so numerator < denominator

#Function to generate all possible fracs
def generateFractions():
    fracs = []
    #Doesnt add multiples of 10
    for i in range(11,100):
        if i %10 != 0:
            for j in range(i+1,100):
                if j%10 != 0:
                    fracs.append([i,j])
    return fracs
    
#Removes all fracs where there isnt a common digit
def removeBad(n):
    newFracs = []
    for i in range(0,len(n)):
        dig1 = str(n[i][0])[0]
        dig2 = str(n[i][0])[1]
        num2 = str(n[i][1])
        if dig1 in num2 or dig2 in num2:
            newFracs.append([n[i][0],n[i][1]])
    return newFracs

#Removes the common digit from top/bottom
def simplify(n):
    num1 = n[0]
    num2 = n[1]
    dig1 = str(n[0])[0]
    dig2 = str(n[0])[1]
    dig3 = str(n[1])[0]
    dig4 = str(n[1])[1]
    if dig1 == dig3:
        num1 = dig2
        num2 = dig4
    elif dig1 == dig4:
        num1 = dig2
        num2 = dig3
    elif dig2 == dig3:
        num1 = dig1
        num2 = dig4
    elif dig2 == dig4:
        num1 = dig1
        num2 = dig3
    return [int(num1),int(num2)]

#Finds all suitable fracs and finds the product 
def findSuitable(n):
    numPro = 1
    decPro = 1
    for i in range(0,len(n)):
        num1 = n[i][0]
        num2 = n[i][1]
        simp1,simp2 = simplify([num1,num2])
        if (fractions.Fraction(simp1,simp2)) == (fractions.Fraction(num1,num2)):
            numPro *= num1
            decPro *= num2
    return fractions.Fraction(numPro,decPro)
            



print(findSuitable(removeBad(generateFractions())))
