"""
http://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/
"""

def f(array):
    for i, n in enumerate(array):
        if i & 1 and n < array[i+1] \
        or not i & 1 and n > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
