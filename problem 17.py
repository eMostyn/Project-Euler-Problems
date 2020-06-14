onetoTwenty = ["","one","two","three","four","five","six","seven","eight","nine",
               "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
               "seventeen","eighteen","nineteen"]
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def printNum(num):
    #If number is less than 20 then use the array above
    if num<20:
        return onetoTwenty[num]
    #Num is 20-99 so use 'tens' then add the value of 'ones' digit if not 0 
    elif num>=20 and num<100:
        return tens[num//10] + (onetoTwenty[num%10] if(num%10 != 0) else "")
    #Num is 100-999 so use first digit + hundred, then recurse for the remaining 2 digits if they aren't 0
    elif num >= 100 and num<1000:
        return onetoTwenty[num//100] +"hundred" + (("and" + printNum(num%100)) if (num%100 != 0) else "")
    else:
        return "onethousand"
def getLength():
    length = 0
    for i in range(1, 1001):
        length += len(printNum(i))
    print(length)

getLength()
