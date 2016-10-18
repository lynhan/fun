"""
http://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
"""

def f(array, k):
    s = 0
    start = 0
    min_len = float('inf')
    for i, n in enumerate(array):
        s += n
        if s > k:
            while s > k:
                s -= array[start]
                start += 1
            start -= 1
            s += array[start]
            min_len = min(min_len, i - start)

            s -= array[start]
            start += 1
    return min_len + 1

print(f([1, 4, 45, 6, 0, 19], 51))  # 3
print(f([1, 10, 5, 2, 7], 9))  # 1
print(f([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))  # 4
