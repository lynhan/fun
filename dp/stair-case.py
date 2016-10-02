"""
Given
    you are climbing a stair case with n steps
    each time you can either climb 1 or 2 steps.
Return
    all distinct ways to climb to the top
"""

def steps(n):
    stairs = [0]*n
    stairs[0] = 1
    stairs[1] = 2
    for i in range(2, n):
        stairs[i] = stairs[i-1] + stairs[i-2]
    return stairs[n-1]
