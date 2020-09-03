import math,time
#Dictionary which holds the amount of times a cubes smallest permutation has occurred
cubes = {}

#Main function to solve problem
def compute():
    #Starting at the first cube
    i = 0
    #Until we find a solution
    while(True):
        #Num will be a string representation of the smallest permutation
        num = ''.join(sorted(list(str(i**3))))
        #If that permutation has already been found 
        if num in cubes:
            #Increase the counter 
            cubes[num][0] += 1
        #It hasnt been found before
        else:
            #Set the counter to 1 as well as storing the i at which it was first found
            cubes[num] = [1,i]
        #If we have found the first cube
        if cubes[num][0] == 5:
            #Return the value i cubed, as this will be the smallest cube
            return cubes[num][1]**3
        #Increment i until its found
        i += 1

#Start used to calculate time taken
start = time.time()
print(compute(),time.time()-start)
