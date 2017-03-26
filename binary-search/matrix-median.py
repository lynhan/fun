# https://www.interviewbit.com/problems/matrix-median/

def get_max(A):
    m = float('-inf')
    for row in A:
        for col in row:
            m = max(m, col)
    return m
import math

# edge case: empty, 1 thing, 2 things
def binary_search(num, array):
    left = 0
    right = len(array)-1
    mid = (left + right) // 2 
    while left != right:
        if array[mid] == num:
            return True
        if array[mid] < num:
            left = mid
            mid = math.ceil( (left + right) / 2 )
        else:
            right = mid
            mid = math.floor( (left + right) / 2 )
    return False
        
def get_num_less_than(num, row):
    left = 0
    right = len(row) - 1
    mid = (left + right) // 2
    if num <= row[0]: 
        return 0
    if num > row[-1]:
        return len(row)
    while not (row[mid] >= num and row[mid-1] < num):
        if row[mid] < num:
            left = mid
            mid = int(math.ceil( (left + right) / 2 ))
        elif row[mid] > num:
            right = mid
            mid = int(math.floor( (left + right) / 2 ))
    print('num smaller than', num, 'in', row, mid)
    return mid

def median(A):
    left = 0
    right = get_max(A)
    half = math.ceil( len(A) * len(A[0]) / 2)
    while left < right - 1:  # [1,2,2,2,2,2,4]
        print(left, right)
        median = math.ceil((left + right) / 2)
        count = 0 
        for row in A:
            count += get_num_less_than(median, row) # log(row)
        print('count', count, 'half', half, 'left', left, 'right', right, 'med', median)
        if count >= half:
            right = median
        if count < half:
            left = median
        input()
    return right




print(median(
    [
        [1,3,5],
        [2,6,9],
        [3,6,9]
        ]))

"""
0, maxnum
mid value 

median: first time count less than median is less than half
while right and left are not next to each other
12333334459

true median value: 3
num before 3: 2
num before next number (4): 7

total count: 11
halfcount = 5

[1, 9]
median = 1+9 / 2 = 5
num before median: 9
    9 > half (5) so median is too big

[1, 5]
median = 1+5 / 2 = 3
num before median: 2
since 2 < half(5) we return median

edge cases
    nonrep num (3) right of median (2): count always greater than half 
    12245
    nonrep num (3) left of median: count always smaller than half JK 
    12445
    [1, 5]
    median val = 3
    num less than 3: 2, which is less than half
    [3, 5] 
    median val = 4
    num less than 4: 2, which is less than half
    [4, 5]
    
    
"""
