import itertools,eulerlib


#Function to check if the sequence meets the criteria
def checkSeq(n):
    #Generate list of permutations
    n = list(itertools.permutations(str(n)))
    #Turn into singular string per perm
    n = fixPerms(n)
    seq = []
    #For each number, up until the last but 2
    for i in range(0,len(n)-2):
        #If there are numbers in the list that meet the criteria
        if str(int(n[i]) + 3330) in n and str(int(n[i]) + 6660) in n:
            #Append the relevant nums
            seq.append(n[i])
            seq.append(str(int(n[i]) + 3330))
            seq.append(str(int(n[i]) + 6660))
    #Check all numbers are prime
    for j in range(0,len(seq)):
        if eulerlib.is_prime(int(seq[j])) == False:
            return []
    return seq


#Function to 'fix' the list of perms
def fixPerms(n):
    #For each of the items in the list of perms
    for i in range(0,len(n)):
        string = ""
        #Turn the individual characters into one string
        for j in range(0,len(n[i])):
            string += (n[i][j])
        #Set the item to the new string
        n[i] = string
    return n


#Main function to solve problem
def compute():
    i = 0
    #While its not found
    while True:
        #Increase i and then check that number sequence
        i += 1
        seq = checkSeq(i)
        #If its not empty, and isnt the already found one
        if seq != [] and seq[0] != "1487":
            #Return the string
            return seq[0]+seq[1]+seq[2]

