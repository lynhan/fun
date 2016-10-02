"""
Given an array of integers, every element appears twice except for one.
Return that single one.
Approach
    track number of 0 and 1 in each bit position
    each position will either have an odd 1 or odd 0 count
    assemble number
"""

def single(array):
    bits = len(bin(max(array))) - 2
    zero = [0]*bits
    one = [0]*bits
    for num in array:
        i = 0
        while num:
            if num & 1:
                one[i] += 1
            else:
                zero[i] += 1
            num = num >> 1
            i += 1
        print(one, zero)
    binary = []
    for i in range(bits):
        if zero[i] & 1:  # odd number of zeros
            binary.append('0')
        elif one[i] & 1:
            binary.append('1')
    binary_str = ''.join(binary)[::-1]
    return int(binary_str, 2)

print(single([1,2,2,1,3,3,4]))
