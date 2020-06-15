#Open the file and read the text, splitting the names into a list
file = open("names.txt","r")
names = file.read().split(",")
sortedNames = sorted(names)
#For each name remove the ""
for i in range(0,len(sortedNames)):
    sortedNames[i] = sortedNames[i].strip('\"')


#Dictionary for each letter correlating to its value 
alphabet = {"A": 1, "B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,
            "L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,
            "R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}



#Function to generate the alphabet score for a given name
def generateAlphScore(inp):
    score = 0
    for i in range(0,len(inp)):
        score += alphabet[inp[i]]
    return score

#Function to calculate the total scores, generating each individually and adding it to a total
def calculateScores():
    inp = sortedNames
    totalScore = 0
    for i in range(0,len(inp)):
        totalScore += generateAlphScore(inp[i]) * (i+1)
    print(totalScore)
        
    
calculateScores()
