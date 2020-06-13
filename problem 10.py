import math


def isPrime(num):
    for j in range(2, math.isqrt(num)+1):
        if(num % j == 0):
            return False
    return True

sum = 2
for i in range(3,2000000,2):
        sum += i
        
print(sum)
