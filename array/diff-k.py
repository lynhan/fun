"""
Given
    array ‘A’ of sorted integers and another non negative integer k
Return
    if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
    linear space complexity
"""

def f(array, k):
    i = 0
    j = 1
    while i < len(array):
        diff = array[j] - array[i]
        if diff == k:
            return True
        elif diff > k:
            i += 1
        elif diff < k:
            j += 1
    return False
