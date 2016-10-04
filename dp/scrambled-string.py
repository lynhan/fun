"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively. To scramble the string, we may choose any non-leaf node and swap its two children.
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""

def is_scramble(s1, s2):  # s1 is scrambled, s2 is original
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    for i in range(1, len(s1)):
        if is_scramble(s1[i:], s2[:len(s2)-i]) and is_scramble(s1[:i], s2[len(s2)-i:]):
            return True
        if is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:]):
            return True
    return False

print('Just recursion:')
print(is_scramble("rgtea", "great"))  # True
print(is_scramble("rfeat", "great"))  # False

def is_scramble_memo(s1, s2):
    """
    This approach uses a bottom up approach by starting with single character comparisons. We use a 3 dimensional table called memo, where memo[i][j][length] contains a boolean for whether s1[i:i+length] is a scramble of s2[j:j+length].
    """
    if sorted(s1) != sorted(s2):
        return False
    size = len(s1)
    memo = [[[False for j in range(size)] for i in range(size)] for k in range(size + 1)]

    # init one char comparisons
    for i in range(size):
        for j in range(size):
            memo[1][i][j] = s1[i] == s2[j]

    for length in range(2, size + 1):
        # length ranges from 2 to size inclusive
        # to encompass whole word

        for i in range(size + 1 - length):
            # i ranges from
            #   0 to size - 2 inclusive at the start
            #   0 at the end

            for j in range(size + 1 - length):
                # j ranges from
                #   0 to size - 2 inclusive at the start
                #   0 at the end

                for k in range(1, length):
                    # k ranges from
                    #   1 to 2 at the start
                    #   1 to size - 1 at the end
                    if (memo[k][i][j] and memo[length - k][i + k][j + k]) \
                    or (memo[k][i][j + length - k] and memo[length - k][i + k][j]):
                        memo[length][i][j] = True
                        break
    return memo[size][0][0]

print('With memoization:')
print(is_scramble_memo("rgtea", "great"))  # True
print(is_scramble_memo("rfeat", "great"))  # False
