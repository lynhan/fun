"""
Reverse bits of an 32 bit unsigned integer
Approach
    0 xor 0 = 0
    1 xor 1 = 1
    0 xor 1 = 1
    xor each bit with the xor of the pair
"""

def rev(n):
    for i in range(16):
        # fetch bits
        left = (n & (1 << (31-i))) >> (31-i)
        right = (n & (1 << i)) >> i

        # clear original bits
        n = n & (0 << (31 - i))
        n = n & (0 << i)

        # swap and position
        pair_xor = left ^ right
        left = (left ^ pair_xor) << (31-i)
        right = (right ^ pair_xor) << i
        n = n | left
        n = n | right

def alt(n):
    i = 31
    fin = 0
    while i >= 0:
        bit = ((n & 1<<i) >> i) & 1
        fin = fin | bit << (31-i)
        i -= 1
    return ret
