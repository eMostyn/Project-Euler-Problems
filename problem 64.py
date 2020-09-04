import math
#Main function to solve problem
def compute():
    #Num of odd periods
    total = 0
    #For each num N<= 10000
    for i in range(2,10001):
        #If its not a square num
        if math.isqrt(i) ** 2 != i:
            #Holds nums found
            nums = []
            #Initial a and r value where a is the int and r the remainder
            a = math.isqrt(i)
            r = (math.sqrt(i) % 1)
            #The initial a, used for finding when its looped
            a0 = a
            #Initial m and d values, used for the formulas I found
            m = 0
            d = 1
            #While a is not half the original a
            while a != a0 * 2:
                #Use the formulas found in order to calculate new values
                m = d*a - m
                d = (i-(m**2))/d
                a = int((a0+m)/d)
                #Append new a to nums, used to track length
                nums.append(a)
            #If the length is odd, increment counter
            if len(nums) % 2 != 0:
                total += 1
    return total


print(compute())
