"""
Given house values on a street
Return max profit if you can't rob adjacent houses
"""

def rob(house):
    profits = [house[0], max(house[0], house[1])]
    for i in range(1, len(house)):
        profits.append( max( profits[-1], house[i] + profits[-2] ) )
    return house[-1]
