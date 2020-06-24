#Main dictionary to convert letter to number
dictt = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#Open the file
f = open("p042_words.txt","r")
#Read the contents
text = f.read()
#Split the contents into a list of words 
words = text.split(",")
#For each word, remove the beginning and end "" to make it easier to count score
for i in range(0,len(words)):
    words[i] = words[i].strip('\"')

#Function to return score of given string
def alphScore(n):
    total = 0
    #Puts to lower case so works with dict
    n = n.lower()
    #For each letter in the word, add the dictionary position to total
    for i in range(0,len(n)):
        total += dictt[n[i]]
    return total

#Main function to solve problem
def compute():
    #List holding all triangular numbers
    tris = [1]
    num = 0
    #For each word
    for i in range(0,len(words)):
        #Calc score of the word
        score = alphScore(words[i])
        #If the score is less than the largest calculated and isnt in there, then not a tri word
        if score <= tris[-1]:
            if score in tris:
                num += 1
        else:
            #Set i to next unfound tri number
            i = len(tris)+1
            #While score is still greater than largest found tri num
            while score>tris[-1]:
                #Append the new num
                tris.append(generateTriNum(i))
                i+=1
                #If its equal add to number found
                if score == tris[-1]:
                    num += 1
                    break;      
    return num

#Function that returns the ith tri number
def generateTriNum(n):
    return int(0.5*n*(n+1))
