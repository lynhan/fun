"""
https://www.interviewbit.com/problems/interleaving-strings/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
Approach
    If s3 char matches s1 char, recurse with new strings
    If s3 char matches s2 char, recurse with new strings
    Return true if s1, s2, s3 are all empty
    Return false if s3 cannot be matched with s1 or s2
    Can memoize indicies to results in hash table ( len(s1)*len(s2) space)
    Runtime: 2^n
    Runtime with memo: len(s1)*len(s2)
"""

memo = {}
def interleave(s1, s2, s3):
    if not s2 and not s2 and not s3:
        return True
    if (len(s1),len(s2),len(s3)) in memo:
        memo[(len(s1),len(s2),len(s3))]['hit'] += 1
        return memo[(len(s1),len(s2),len(s3))]['result']
    case1 = s1 and s3[0] == s1[0] and interleave(s1[1:], s2, s3[1:])
    case2 = s2 and s3[0] == s2[0] and interleave(s1, s2[1:], s3[1:])
    if case1:
        memo[(len(s1),len(s2),len(s3))] = {
            'result': True,
            'hit': 0,
        }
        return True
    if case2:
        memo[(len(s1),len(s2),len(s3))] = {
            'result': True,
            'hit': 0,
        }
        return True
    elif not case1 and not case2:
        memo[(len(s1),len(s2),len(s3))] = {
            'result': False,
            'hit': 0,
        }
        return False

# each parameter combination will be checked at most twice
# the first time to compute its value
# the second time to check its cached value
#   left: used s1 char in string checked so far? true if s2 match
#   up: used s2 char in string checked so far? true if s1 match
# can visualize topdown approach as starting from the bottom right of the table
print('topdown:')
print(interleave("abc", "def", "abcdef"))  # True


def tab(s1, s2, s3):
    table = [[False for c in range(len(s2) + 1)] for r in range(len(s1) + 1)]
    # set up
    for r in range(1, len(s1) + 1):
        table[r][0] = ( s1[r-1] == s3[r-1] )
    for c in range(1, len(s1) + 1):
        table[0][c] = ( s2[c-1] == s3[c-1] )
    # fill table
    for r in range(1, len(s1)+1):
        for c in range(1, len(s2)+1):
            if table[r-1][c]:
                table[r][c] = (s3[r+c-1] == s1[r-1])
            if table[r][c-1]:
                table[r][c] = (s3[r+c-1] == s2[c-1])
    return table[len(s2)][len(s1)]

print('\ntab:')
print(tab("bc", "ab", "abcb"))  # True
