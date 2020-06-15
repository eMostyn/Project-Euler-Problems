def factorial(n):
    total = 1;
    for i in reversed(range(1,n+1)):
        total *= i
    return total

def sumDigits():
    total = 0
    numStr = str(factorial(100))
    for i in range(len(numStr)):
        total += int(numStr[i])
    print(total)
        
