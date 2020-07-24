import itertools

file = open("p054_poker.txt", "r")

#Function to split the inputted text file into each individual hand
def splitHands(text):
    #Split the file by lines
    lines = text.split('\n')
    hands = []
    #For each line
    for i in range(0,len(lines)):
        #Split each card by removing whitespace
        cards = lines[i].split(" ")
        #Append 5 cards at a time
        for j in range(0,len(cards)-4,5):
            hand = []
            hand.append(cards[j])
            hand.append(cards[j+1])
            hand.append(cards[j+2])
            hand.append(cards[j+3])
            hand.append(cards[j+4])
            hands.append(hand)
    return hands

hands = splitHands(file.read())

#Lists containing the suits and also the possible values
suits = ["H","C","S","D"]
vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

#Converts the hand into just a list of the card values
def getVals(hand):
    vals = []
    for i in range(0,len(hand)):
        vals.append(hand[i][0])
    return vals

#Converts the hand into justa list of suits 
def getSuits(hand):
    suits = []
    for i in range(0,len(hand)):
        suits.append(hand[i][1])
    return suits

#Function to calculate what a hand is and assign a relative socre to it
def checkHand(hand):
    values = getVals(hand)
    suits = getSuits(hand)
    #If the values are equal and the list of the set is 1 (converting to a set removes duplicates)
    if sorted(values) == ['A', 'J', 'K', 'Q', 'T'] and len(set(suits)) == 1:
        #Sets the score to 10 and the highest card will be an ace
        return 10,"A"
    #If there is a straight and there are of the same suit
    elif checkStraight(values) and len(set(suits)) == 1:
        #Sets the score to 9 and finds the highest card within the hand
        return 9,findLargestCard(values)
    #If there is a four of the same card
    elif checkSameVal(values)[0] == 4:
        #Sets the score to 8 and finds the number which appeared 4 times
        return 8,checkSameVal(values)[1]
    #Checks if there is a three of a kind as well as a pair
    elif checkSameVal(values)[0] == 3 and checkPairs(values)[0] == 1:
        #Sets score to 7 and finds value of number which appeared 3 times
        return 7,checkSameVal(values)[1]
    #Checks if all cards are of same set
    elif len(set(suits)) == 1:
        #Sets score to 6 and finds largest card in hand
        return 6,findLargestCard(values)
    #Checks if there is a straight
    elif checkStraight(values):
        #Sets the score to 5 and finds the largest card in the hand
        return 5,findLargestCard(values)
    #Checks if there is a three of a kind
    elif checkSameVal(values)[0] == 3:
        #Sets the score to 4 and finds the number which occurred 3 times
        return 4,checkSameVal(values)[1]
    #Checks if a 2 pairs has occurred
    elif checkPairs(values)[0] == 2:
        #Sets the score to 3 and gets the value of the largest pair
        return 3,checkPairs(values)[1]
    #Checks if a pair has occured
    elif checkPairs(values)[0] == 1:
        #Sets the score to 3 and gets the value of the pair
        return 2,checkSameVal(values)[1]
    else:
        #Sets the score to 1 and gets the largest card in the hand
        return 1,findLargestCard(values)

#Checks if a straight has occurred
def checkStraight(values):
    #Generates a list of permutations, as cannot straight sort the list
    perms = list(itertools.permutations(values))
    #For each permutation
    for i in range(0,len(perms)):
        #For each number in vals - 5
      for j in range(0,len(vals)-5):
          #Check if the permutation matches that "strip" for the vals list
          if list(perms[i]) == vals[j:j+5]:
            return True
    return False

#Checks for the largest amount of repeated values
def checkSameVal(values):
    largest = 0
    largestVal = "-"
    #For each number in the list
    for i in range(0,len(values)):
        amount = 1
        #For the rest of the numbers
        for j in range(i+1,len(values)):
            #If the numbers are equal increment the counter
            if values[j] == values[i]:
                amount += 1
        #IF that amount was larger than the largest found, replace it
        if amount >= largest:
            largest = amount
            largestVal = values[i]
    return largest,largestVal

#Checks if a pair has occurred
def checkPairs(values):
    found = []
    highestPair = "2"
    num = 0
    #For each number
    for i in range(0,len(values)):
        #If we havent already checked that number
        if values[i] not in found:
            #Add it to found
            found.append(values[i])
            amount = 1
            #For each remaining number
            for j in range(i+1,len(values)):
                #If the values are the same incremement the counter
                if values[j] == values[i]:
                    amount += 1
            #If the number was a pair incremement the counter for amount of pairs  
            if amount == 2:
                num += 1
                #If the pair number is larger than the current largest, replace it
                if vals.index(highestPair) <  vals.index(values[i]):
                    highestPair = values[i]
    return num,highestPair

#Calculates the largest card
def findLargestCard(values):
    largestIndex = 0
    #For each number 
    for i in range(0,len(values)):
        #If the value is larger than the current largest, replace it
        if(vals.index(values[i]) > largestIndex):
           largestIndex = vals.index(values[i])
    return vals[largestIndex]


#Function to find the largest card given 2 hands
def highestCard(hand1,hand2):
    hand1 = getVals(hand1)
    hand2 = getVals(hand2)
    hand1Card = findLargestCard(hand1)
    hand2Card = findLargestCard(hand2)
    #Keeps going until a winner is found
    while hand1Card == hand2Card:
        hand1 = removeItem(hand1,hand1Card)
        hand2 = removeItem(hand2,hand2Card)
        hand1Card = findLargestCard(hand1)
        hand2Card = findLargestCard(hand2)
    if vals.index(hand1Card) > vals.index(hand2Card):
        return True
    return False

#Function to remove an item from a list
def removeItem(hand,toRemove):
    newList = []
    #Only appends items which are not what we're trying to remove
    for i in range(0,len(hand)):
        if hand[i] != toRemove:
            newList.append(hand[i])
    return newList
        
   
def compute():
    player1Vics = 0
    #For each hand
    for i in range(0,len(hands),2):
        #Get the score of each hand
        player1 = checkHand(hands[i])[0]
        player2 = checkHand(hands[i+1])[0]
        #If player1 has a higher score than player2
        if player1 > player2:
            player1Vics += 1
        #Else if they have the same hand score
        elif player1 == player2:
            #If player1 has a better version of the same outcome, aka pair of 3s > pair of 2s
            if vals.index(checkHand(hands[i])[1]) >  vals.index(checkHand(hands[i+1])[1]):
                player1Vics += 1
            #If they're the same outcome but player1 has a higher remaining card
            elif vals.index(checkHand(hands[i])[1]) ==  vals.index(checkHand(hands[i+1])[1]) and highestCard(hands[i],hands[i+1]):
                player1Vics += 1
    return player1Vics
                                        
            

