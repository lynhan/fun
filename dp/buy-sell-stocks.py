"""
Given
    array where array[i] is the price of a stock on day i.
    buy and sell once
Return
    max profit
Approach
    go from right to left, memoize max num so far and max profit so far
    linear time and constant space
    time: O(n)
    space: O(n)
"""
def once(price):
    max_profit = 0
    max_num = price[-1]
    i = len(price) - 2
    while i >= 0:
        max_num = max(price[i], max_num)
        max_profit = max(max_num - price[i], max_profit)
        i -= 1
    return max_profit

"""
Alt
    can buy and sell more than once
    must sell current stock before buying another
Approach
    if we visualize the prices as a line graph over time
        and divide the graph into sections by local maximums
        we can get the max profit by summing the difference between local max and min
    so we can modify the original approach such that
        when max profit so far changes, we add it to total profit
    time: O(n)
    space: O(n)
"""
def flexible(price):
    total_profit = 0
    max_profit = 0
    max_num = price[-1]
    i = len(price) - 2
    while i >= 0:
        max_num = max(price[i], max_num)
        if max_num - price[i] > max_profit:
            total_profit += max_profit
            max_profit = max_num - price[i]
        i -= 1
    return max_profit

"""
Alt
    can buy and sell AT MOST k times
    assumes can sell and buy on same day
Approach
    consider two factors in dp solution:
        num transactions
        time (past day to buy, present day to sell)
        ...3 for loops
    store two factors in 2d array
        profit[tr][day] stores max profit
            with AT MOST n transactions up to today, inclusive
        case1: no transaction
            profit[tr][day-1]
        case2: sell
            this means buying on past day
            price[now] – price[past] + profit[tr-1][past]
                ...for all past days in range (0...day-1)
        base cases:
            tr = 0, profit = 0
            day = 0, profit = 0
    time: O(k*n)
    space: O(k*n)
"""
def at_most(price, k):
    profit = [[0 for i in range(len(price))] for n in range(k + 1)]
    for tr in range(1, k+1):
        profit_after_lowest_buy = -price[0]
        for day in range(1, len(price)):
            # days range from 0 to current day - 1
            profit_after_lowest_buy = max(profit_after_lowest_buy, \
                                    profit[tr-1][day-1] - price[day-1]);
            case1 = profit[tr][day-1] # don't sell, no transaction today
            case2 = price[day] + profit_after_lowest_buy  # sale + optimal previous earnings
            profit[tr][day] = max(case1, case2)
    return profit[k][len(price)-1]

"""
Alt
    buy and sell EXACTLY 2 times
Approach
    find max profit if we sell on each day
    find max profit if we buy on each day
"""
def exact(price, k):
    max_if_buy = [0]*len(price)
    cur_max = float('-inf')
    for i in range(len(price)-1, -1, -1):
        cur_max = max(cur_max, price[i])
        max_if_buy[i] = cur_max - price[i]
    max_profit = 0
    cur_min = float('inf')
    for i in range(len(price)):
        cur_min = min(cur_min, price[i])
        max_profit = max(max_profit, price[i] - cur_min + max_if_buy[i])
    return max_profit
