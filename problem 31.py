def waysToMake():
    #List of all possible coins
    coins = [1,2,5,10,20,50,100,200]
    #Each way has 1 to begin
    ways = {i:1 for i in range(201)}
    #For each coin the number of ways to make a specific amount 1-200 is amount of k-coin + 1 
    for coin in coins[1::]:
        for k in range(coin,201):
            ways[k] += ways[k-coin]
    #Ways to make 200 pence
    return ways[200]
