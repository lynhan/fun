"""
https://www.interviewbit.com/problems/arrange-ii/
"""

def f(horse, stable_num):
    stables = [[] for x in range(stable_num)]
    stables[0].append(horse[0])
    return assign(horse, stables, 1, 0)

def get_stables_sum(stable):
    total = 0
    for s in stable:
        product = 1
        for h in s:
            if h == "W":
                product *= 1
            else:
                product *= 0
        total += product
    return total
    
from copy import deepcopy
def assign(horse, stable, h, s):
    print(stable)
    if h == len(horse):
        return get_stables_sum(stable)
    stable1 = deepcopy(stable)
    stable1[s].append(horse[h])
    case1 = assign(horse, stable1, h+1, s)
    case2 = 0
    if s+1 < len(stable):
        stable2 = deepcopy(stable)
        stable2[s+1].append(horse[h])
        case2 = assign(horse, stable2, h+1, s+1)
    print(case1, case2)
    return min(case1, case2)

print(f("WWWB", 2))
