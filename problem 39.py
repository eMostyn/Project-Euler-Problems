def generateOps(p):
    results = 0
    for a in range(1,p+1):
        #a<b and b<=c so it cannot be greater than half the remaining number aka (p-a)
        for b in range(a,(p-a)//2 +1):
            #C will be the reminaing number aka p-a-b
            c = p-a-b
            #Check to see if sum works
            if a*a + b*b == c*c:
                results += 1
    return results


def compute():
    #Returns number from 1-1000 which when used as p gives the largest num of results
    return max(range(1,1001), key = generateOps)
    
