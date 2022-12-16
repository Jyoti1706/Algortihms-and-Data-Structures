def nonConstructibleChange(coins):
    # Write your code here.
    coins = sorted(coins)

    output = set(coins)
    print(coins)
    max_sum = 0
    p = 0

    k = 0
    overall_sum=0

    while k < len(coins):

        i = k

        sum = overall_sum
        while i < len(coins):
            sum = sum + coins[i]
            j = i + 1
            while j < len(coins):
                temp = sum + coins[j]
                print(f"sum:: {sum} +coins[{j}] :: {coins[j]} = {temp}")
                output.add(temp)
                if temp > max_sum:
                    max_sum = temp
                j = j + 1
            i = i + 1

        #overall_sum = overall_sum + coins[k]
        k = k + 1
    print(f"max :: {max_sum}")
    for i in range(1,max_sum):
        if not(i in output):
            return i
    return max_sum+1


coins = [5, 7, 1, 1, 2, 3,22]
#coins = [1,1,5]
print(nonConstructibleChange(coins))
