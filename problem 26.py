#DOESNT WORK, NEED TO CHANGE RECUSION IDENTIFICATION
def findLargest():
    largest = 0
    largestI = 0;
    for i in reversed(range(1,1000)):
        if largest > i:
            return largestI
        rec = findCyc(i)
        if rec> largest:
            largest = rec
            largestI = i
    
        


def findCyc(n):
    length = 0
    remainders = []
    x = 1
    #Loop keeps going until loop is found or it divides fully
    while(True):
        if x%n == 0:
            break
        elif x in remainders:
            break
        remainders.append(x)
        x = (x*10)%n
        length += 1
    return(length)




    
    
