file = open("p059_cipher.txt", "r")
encryptedMessage = file.read().split(",")
encryptedMessage = [ int(x) for x in encryptedMessage ]

#Function to check if a given character produces solely valid characters
def checkValid(digit,testChar):
    #Gets xor value of digit from message and current character being tested
    xor = digit ^ testChar
    #2 checks to see if the value is in the range of valid ascii characters
    if 32 <= xor <= 93:
        return True
    elif 97 <= xor <= 122:
        return True
    #Not in valid region
    return False

#Main function to calculate answer
def compute(encrypted):
    #Holds current key1 valids
    key1 = []
    #Goes through the alphabet
    for a in range(97,123):
        key1.append(a)
        #Check every character which key1 must work on
        for j in range(0,len(encrypted),3):
            #If its not valid then remove that character from the valid list and move to the next character
            if checkValid(encrypted[j],a) == False:
                key1.remove(a)
                break;
    #Same approach for key2 and key3
    key2 = []
    for b in range(97,123):
        key2.append(b)
        for k in range(1,len(encrypted),3):
            if checkValid(encrypted[k],b) == False:
                key2.remove(b)
                break;
    key3 = []
    for c in range(97,123):
        key3.append(c)
        for l in range(2,len(encrypted),3):
            if checkValid(encrypted[l],c) == False:
                key3.remove(c)
                break;

    #For every section to use the found key one, aka every 3 chars        
    for i in range(0,len(encrypted),3):
        #Use each character of the key on the corresponding character
        encrypted[i] = encrypted[i] ^ key1[0]
        encrypted[i+1] = encrypted[i+1] ^ key2[0]
        encrypted[i+2] = encrypted[i+2] ^ key3[0]
    #Return the sum of each decrypted aswell as the decrypted message in plaintext
    return sum(encrypted),convertMessage(encrypted)

#Converts into plaintext so the message can be read
def convertMessage(toConvert):
    newMessage = ""
    for i in range(0,len(toConvert)):
      newMessage += (chr(toConvert[i]))
    return newMessage


print(compute(encryptedMessage))


