#Function to generate list of nums
def generateNums():
    nums = []
    #Double loop tries every combination
    for i in range(2,101):
        for j in range(2,101):
            num = i**j
            #If the num is unique it is added
            if num not in nums:
                nums.append(num)
    return len(nums)


