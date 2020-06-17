spiral = [["-" for x in range(1001)] for y in range(1001)]

#Function to print out list nicely, used for testing
def printSpiral(n):
    for i in range(0,len(n)):
        print(n[i])
    print('\n')

#Function to move through spiral
def traverse(n):
    #Starting at the middle position
    mid = (len(n)-1)//2
    pos = [mid,mid]
    #Generate the sequences for y,x movement
    seqs = [generateYSequence(n),generateXSequence(n)]
    #Flips between 0,1
    choice = 1
    #Number counter
    counter = 1
    #Largest number is one higher than length of one side squared +1
    maxNum = len(n)**2 +1
    while(counter <maxNum):
        #The num is amount of times to move
        num = seqs[choice].pop(0)
        #Movement is - aka to left or up
        if(num<0):
            for j in range(0,num,-1):
                #Set that position to the number and move in the correct position 
                n[pos[0]][pos[1]] = counter
                counter += 1
                if num<0:
                    pos[choice] += -1
                else:
                    pos[choice] += +1
        else:
            for j in range(0,num,1):
                n[pos[0]][pos[1]] = counter
                counter += 1
                if num<0:
                    pos[choice] += -1
                else:
                    pos[choice] += +1
        #Flip choice to alternate
        choice = (choice +1)%2
    printSpiral(n)
    
        

#Generates the x movement sequence
def generateXSequence(n):
    seq = []
    #Flips between 1,-1
    multiplier = 1
    highest = len(n)+1
    #Appends the next number and flips multiplier
    for i in range(1,highest):
        seq.append(i*multiplier)
        multiplier *= -1
    return seq

#Generates the y movement sequence
def generateYSequence(n):
    seq = []
    multiplier = 1
    highest = len(n)
    for i in range(1,highest):
        seq.append(i*multiplier)
        multiplier *= -1
    return seq

#Calculates the diagonal sum
def calcDiag(n):
    mid = (len(n)-1)//2
    total = 0
    for i in range(0,len(n)):
        total += n[i][i]
        total += n[len(n)-i-1][i]
    #Minus 1 mid value as its been counted twice
    return total - n[mid][mid]

traverse(spiral)
print(calcDiag(spiral))
