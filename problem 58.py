import eulerlib

#Main function to compute problem
def compute():
    #Current numbers in each corner
    nums = [3,5,7,9]
    #Start side length
    sideLength = 3
    #Total = number of diagonal numbers
    total = 5
    #Number of found primes in the spiral
    primes = 3
    #While the ratio is above 10%
    while primes/total > 0.1:
        #Increase the side length by 2
        sideLength += 2
        #Total of diagonals will be this formula
        total = (sideLength * 2) - 1
        #Update nums to change the diagonal numbers
        nums = updateNums(nums,sideLength)
        #Check for amount of primes in the new numbers
        primes += checkPrimes(nums)
    return sideLength



#Function to check how many primes in the list nums
def checkPrimes(nums):
    primes = 0
    #For each number in the list, if its prime increment the counter
    for i in range(0,len(nums)):
        if eulerlib.is_prime(nums[i]):
            primes += 1
    return primes

#Function to update the numbers in each corner
def updateNums(nums,sideLength):
    #The smallest corner number will be sidelength - 1 greater than the previous max number (sidelength - 2) squared
    nums[0] = (sideLength-2)**2+sideLength - 1
    #For the remaining numbers their value will be the previous + sidelength - 1
    for i in range(1,len(nums)):
        nums[i] = nums[i-1] + sideLength - 1
    #Return the new nums
    return nums


print(compute())
