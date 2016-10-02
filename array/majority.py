"""
Given
    array of size n
    array is non-empty and the majority element always exist in the array
Return
    majority element, which appears more than floor(n/2) times
Approach
    cancel out each non-majority element with the majority element
    the majority element will be left over
    linear space, constant time
"""

def check_majority(array, num):
    count = 0
    for n in array:
        if num == n:
            count += 1
    return count > len(array) // 2

def majority(array):
    pair = None  # previously canceled pair
    num = None  # current num
    count = 0
    for n in array:
        if not num:
            num = n
            count = 1
        elif n != num:
            if count > 1:
                count -= 1
            else:
                pair = (num, n)
                num = None
                count = 0
        elif n == num:
            count += 1
    if num and check_majority(array, num):
        return num
    if check_majority(array, pair[0]):
        return pair[0]
    return pair[1]

print(majority([2,2,2,4,1]))
