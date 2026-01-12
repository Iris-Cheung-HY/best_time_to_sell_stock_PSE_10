def max_profit(prices):
    max_profit = 0

    l = 0
    r = l + 1

    while r < len(prices):
        a = prices[l]
        b = prices[r]
        if prices[l] < prices[r]:
            max_profit += b - a
            l += 1
            r += 1
        else:
            l += 1
            r += 1
    return max_profit



    # max_profit = 0

    # left = 0
    # right = 1

    # while right < len(prices):
    #     if prices[right] > prices[left]:
    #         diff = prices[right] - prices[left]
    #         max_profit += diff
    #         left += 1
    #         right += 1
    #     else:
    #         left += 1
    #         right += 1
    # return max_profit




            














