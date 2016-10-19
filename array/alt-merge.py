"""
http://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/
"""

from copy import deepcopy
def f(a, b):
    res = []
    def help(part, aturn, ai, bi):
        if aturn:
            while ai < len(a) and a[ai] < b[bi]:
                ai += 1
            while ai < len(a):
                newpart = deepcopy(part)
                newpart.append(a[ai])
                if len(newpart) > 1 and ai != len(a) - 1:
                    res.append(newpart)
                help(newpart, False, ai, bi)
                ai += 1
        elif bi < len(b):
            while bi < len(b) and b[bi] < a[ai]:
                bi += 1
            while bi < len(b):
                newpart = deepcopy(part)
                newpart.append(b[bi])
                if len(newpart) > 1:
                    res.append(newpart)
                help(newpart, True, ai, bi)
                bi += 1
    help([], True, 0, 0)
    return res

from pprint import pprint as p
p(f([10, 15, 25], [1, 5, 20, 30]))

# 10 20
# 10 20 25 30
# 10 30
# 15 20
# 15 20 25 30
# 15 30
# 25 30
