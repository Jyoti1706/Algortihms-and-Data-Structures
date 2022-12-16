def nonConstructibleChange1(coins):
    coins.sort()

    sum = 0
    for coin in coins:

        print(sum + 1, coin)
        if coin > sum + 1:
            return sum + 1
        sum = sum + coin
    return sum + 1

def nonConstructibleChange(coins):
    coins.sort()

    sum = 0
    i = 0
    while i < len(coins):

        print(sum + 1, coins[i])
        if coins[i] > sum + 1:
            return sum + 1
        sum = sum + coins[i]
        i=i+1
    return sum + 1


coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
print(nonConstructibleChange(coins))
