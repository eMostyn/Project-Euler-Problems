#DOESNT WORK, NEED TO CHANGE RECUSION IDENTIFICATION
def printDec(n):
    count = 0
    numerator = 1
    denominator = n
    result = 0
    while count <(2*n)-2 and "00000" not in str(result):
        if(denominator > numerator):
            numerator *= 10
            result *= 10
        else:
            result += (numerator // denominator)
            numerator = (numerator % denominator)
            count += 1
    return str(result).strip('0.')



def findRec(n):
    largest = 0
    for j in range(0,len(n)):
        for i in range(1,len(n)):
            recString = n[j:j+i]
            if recString == n[j+i:j+i+i]:
                if len(recString) > largest:
                    largest = len(recString)
    return largest

def longestRec(): 
    largest = 0
    num = 0
    for i in reversed(range(2,1000)):
        rec = findRec((printDec(i)))
        print(i,rec)
        if(rec>largest):
            largest = rec
            num = i
        if(largest>i):
            return num




print(longestRec())


    
    
