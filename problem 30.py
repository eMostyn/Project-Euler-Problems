import math

def fifthPowers():
    total = 0
    for i in range(2,1000000):
        iTotal = 0
        num = i
        while(num > 0):
            iTotal += (num%10)**5
            num = num//10
        if iTotal == i:
            total += iTotal
    return total 
        
            
