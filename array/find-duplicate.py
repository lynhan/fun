"""
Given
    array of n ints
    int range from 1 to n-1 inclusive
    we are guaranteed at least one duplicate
Return
    the duplicate
Approach
    we match int to index (1 goes to index 1)
        encountering a duplicate means that
            we are trying to put an int at index i but array[i] is already the same as index i
        if we use a zero indexed array, indices range from 0 to n-1
            since ints range from 1 to n-1, we will never match an int to index 0
                so we can use index 0 as holder for the next index to examine
"""

def find_duplicate(array):
    i = array[0]
    while array[i] != i:
        array[0] == array[i]  # save next
        array[i] = i  # match value to index
        i = array[0]  # go to next
    return i
