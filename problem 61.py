import itertools,time
start = time.time()

#Function to generate the valid number
def generateNums():
    #Empty lists
    tris = []
    squares = []
    pents = []
    hexs = []
    hepts = []
    octs = []
    #Starting at n = 1, the while loop increments it, only adding the the number to the list if its 4 digits long, stopping when 5 digits
    a = 1
    while a*(a+1)//2 <= 9999:
        if a*(a+1)//2 >= 1000:
            tris.append((a*(a+1))//2)
        a+= 1
    b = 1
    while b**2 <= 9999:
        if b**2 >= 1000:
            squares.append(b**2)
        b+= 1
    c = 1
    while c*((3*c)-1)//2 <= 9999:
        if c*((3*c)-1)//2 >= 1000:
            pents.append(c*((3*c)-1)//2)
        c+= 1
    d = 1
    while d*((2*d)-1) <= 9999:
        if d*((2*d)-1) >= 1000:
            hexs.append(d*((2*d)-1))
        d+= 1
    e = 1
    while e*((5*e)-3)//2 <= 9999:
        if e*((5*e)-3)//2 >= 1000:
            hepts.append(e*((5*e)-3)//2)
        e+= 1
    f = 1
    while f*((3*f)-2) <= 9999:
        if f*((3*f)-2) >= 1000:
            octs.append(f*((3*f)-2))
        f+= 1
    return [tris,squares,pents,hexs,hepts,octs]
        
        
        
        
#Function to solve problem
def compute():
    #Call generate nums to generate list startNums off all the numbers as a list of lists
    startNums = generateNums()
    #Perms is a list of permutations of the lists, eg triangle then square and square then triangle. Required as we dont know the order of the final list
    perms = list(itertools.permutations(startNums))
    #Chain will represent the current chain found, which will be returned if we reach the bottom of the loops
    chain = []
    #For each different ordering of the nums
    for i in range(0,len(perms)):
        #The numbers this time
        nums = perms[i]
        #For each number in the first list, which may be any of the types of num depending on the permuation
        for a in range(0,len(nums[0])):
                #Set the starting num and add it to the chain
                num = nums[0][a]
                chain = [num]
                #End will represent the end 2 digits
                end = str(nums[0][a])[-2:]
                #For each number in the 2nd list 
                for b in range(0,len(nums[1])):
                    #If that number has the correct first 2 digits and the number has not currently been used
                    if str(nums[1][b])[0:2] == str(nums[0][a])[-2:] and nums[1][b] not in chain:
                        #Set the new num, and add it to the chain
                        num = nums[1][b]
                        chain = [chain[0],num]
                        end = str(num)[-2:]
                        #For each 3rd number, repeating same process for each number
                        for c in range(0,len(nums[2])):
                            #If the conditions are met
                            if str(nums[2][c])[0:2] == end and nums[2][c] not in chain:
                                num = nums[2][c]
                                chain = [chain[0],chain[1],num]
                                end = str(num)[-2:]
                                #Find 4th number in chain
                                for d in range(0,len(nums[3])):
                                    if str(nums[3][d])[0:2] == end and nums[3][d] not in chain :
                                        num = nums[3][d]
                                        chain = [chain[0],chain[1],chain[2],num]
                                        end = str(num)[-2:]
                                        #Find 5th number in chain
                                        for e in range(0,len(nums[4])):
                                            if str(nums[4][e])[0:2] == end and nums[4][e] not in chain:
                                                num = nums[4][e]
                                                chain = [chain[0],chain[1],chain[2],chain[3],num]
                                                end = str(num)[-2:]
                                                for f in range(0,len(nums[5])):
                                                    #For 6th number check if the looping condition is met
                                                    if str(nums[5][f])[0:2] == end and nums[5][f] not in chain and str(nums[5][f])[-2:] == str(chain[0])[0:2]:
                                                        chain.append(nums[5][f])
                                                        #Return the full chain to check validity as well as the sum for the answer
                                                        return chain,sum(chain)



print(compute())
print(time.time()-start)
