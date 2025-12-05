def max_profit(prices):

    max_profit = 0

    left = 0
    right = 1

    while right < len(prices):
        if prices[right] > prices[left]:
            diff = prices[right] - prices[left]
            max_profit += diff
            left += 1
            right += 1
        else:
            left += 1
            right += 1
    return max_profit




            














