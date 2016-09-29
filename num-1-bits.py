"""
Given unsigned integer
Return the number of 1 bits it has
"""

def num_ones(n):
    count = 0
    while n:  # num ones > 0
        if n & 1:  # right most bit is 1
            count += 1
        n >> 1
    return count
