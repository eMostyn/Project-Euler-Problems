#Requires working for larger spiral + diagonal sum calculation + commentation
spiral = [["-" for x in range(1001)] for y in range(1001)]

testSpiral = [[0 for x in range(5)] for y in range(5)]

def printSpiral(n):
    for i in range(0,len(testSpiral)):
        print(testSpiral[i])
    print('\n')

def traverse(n):
    testSpiral[2][2] = "n"
    pos = [2,2]
    seqs = [generateYSequence(),generateXSequence()]
    print(seqs)
    choice = 1
    counter = 1
    while(counter <26):
        num = seqs[choice].pop(0)
        if(num<0):
            for j in range(0,num,-1):
                print(seqs,num,j)
                testSpiral[pos[0]][pos[1]] = counter
                counter += 1
                if num<0:
                    pos[choice] += -1
                else:
                    pos[choice] += +1
        else:
            for j in range(0,num,1):
                print(seqs,num,j)
                testSpiral[pos[0]][pos[1]] = counter
                counter += 1
                if num<0:
                    pos[choice] += -1
                else:
                    pos[choice] += +1
            
        choice = (choice +1)%2
        printSpiral(testSpiral)
    printSpiral(testSpiral)
    
        


def generateXSequence():
    seq = []
    multiplier = 1
    for i in range(1,6):
        seq.append(i*multiplier)
        multiplier *= -1
##    seq[-1] = seq[-1]-1
    return seq


def generateYSequence():
    seq = []
    multiplier = 1
    for i in range(1,5):
        seq.append(i*multiplier)
        multiplier *= -1
    return seq


print(traverse(testSpiral))
