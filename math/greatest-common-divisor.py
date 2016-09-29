"""
Given two positive ints
Return greatest common divisor
    largest positive integer that divides the numbers without a remainder
Approach
    euclidean
"""

def gcd(a, b):
    while a != b:
        diff = abs(a-b)
        if a > b:
            a = diff
        else:
            b = diff
    return a
