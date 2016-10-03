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
"""

memo = {}
def interleave(s1, s2, s3):
    if not s2 and not s2 and not s3:
        return True
    if (len(s1),len(s2),len(s3)) in memo:
        return memo[(len(s1),len(s2),len(s3))]
    if s1 and s3[0] == s1[0] and interleave(s1[1:], s2, s3[1:]):
        memo[(len(s1),len(s2),len(s3))] = True
        return True
    if s2 and s3[0] == s2[0] and interleave(s1, s2[1:], s3[1:]):
        memo[(len(s1),len(s2),len(s3))] = True
        return True
    memo[(len(s1),len(s2),len(s3))] = False
    return False

print(interleave("aabcc", "dbbca", "aadbbcbcac"))  # True
memo = {}
print(interleave("aabcc", "dbbca", "aadbbbaccc"))  # False
memo = {}
print(interleave("ab", "bc", "abcb"))  # True
