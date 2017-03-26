"""
Given two positive ints
Return greatest common divisor
    largest positive integer that divides the numbers without a remainder
Approach
    euclidean
"""

def gcd(a, b):
    print(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(6, 15))