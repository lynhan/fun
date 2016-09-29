"""
Given
    array where array[i] is the price of a stock on day i.
    you buy and sell once
Return
    max profit
Approach
    go from right to left, memoize max num so far and max profit so far
    linear time and constant space
"""

def profit(array):
    max_profit = 0
    max_num = array[-1]
    i = len(array) - 2
    while i >= 0:
        max_num = max(array[i], max_num)
        max_profit = max(max_num - array[i], max_profit)
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
    so we can modify the above approach such that
        when max profit so far changes, we add it to total profit
"""

def more_profit(array):
    total_profit = 0
    max_profit = 0
    max_num = array[-1]
    i = len(array) - 2
    while i >= 0:
        max_num = max(array[i], max_num)
        if max_num - array[i] > max_profit:
            total_profit += max_profit
            max_profit = max_num - array[i]
        i -= 1
    return max_profit
