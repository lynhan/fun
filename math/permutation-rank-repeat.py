def mult_duplicates(s):  # O(n)
    import math
    product = 1
    cur = ""
    count = 1
    for char in s:
        if char != cur:
            product *= math.factorial(count)
            count = 1
            cur = char
        else:
            count += 1
    product *= math.factorial(count)
    return product

import math

def get_num_before(s):  # O(n^2)
    count = 0
    current = s[0]
    unique = sorted(set(s))

    for char in unique:   # O(n)
        if char == current:
            return count
        right_part = [x for x in sorted(s)] 
        right_part.remove(char)
        numer = math.factorial(len(s)-1)
        denom = mult_duplicates(right_part)  # O(n)
        count += numer / denom
    return count

def f(s):  # O(n^3)
    rank = 0
    for i in range(len(s)): # O(n)
        rank += get_num_before(s[i:]) # O(n^2)
    return (rank + 1) % 1000003

print(f('cbaa'))