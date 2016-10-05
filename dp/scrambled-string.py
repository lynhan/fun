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
    This bottom up approach starts with single character comparisons. We use a 3 dimensional table called memo, where memo[length][i][j] contains a boolean for whether s1[i:i+length] is a scramble of s2[j:j+length]. The order of table indicies is arbitrary.
    """
    if sorted(s1) != sorted(s2):
        return False
    size = len(s1)
    memo = [[[False for j in range(size)] for i in range(size)] for swapland in range(size + 1)]

    # init one char comparisons
    for i in range(size):
        for j in range(size):
            memo[1][i][j] = s1[i] == s2[j]

    # begin exhaustive search
    #   i and j take care of starting positions for the segment to swap
    #   swapland defines the length of the stretch of characters over which swaps happen
    #   ln is the length of the segment being swapped
    for swapland in range(2, size + 1):
        # swapland ranges from 2 to size inclusive

        for i in range(size + 1 - swapland):
            # i ranges from
            #   0 to size - 2 inclusive at the start
            #   0 at the end

            for j in range(size + 1 - swapland):
                # j ranges from
                #   0 to size - 2 inclusive at the start
                #   0 at the end

                for ln in range(1, swapland):
                    # ln ranges from
                    #   1 to 2 at the start
                    #   1 to size - 1 at the end
                    if memo[ln][i][j] and memo[swapland - ln][i + ln][j + ln]:
                        # segment did not move
                        # compare left segments in s1 and s2
                        # and right segments in s2 and s2
                        memo[swapland][i][j] = True
                    if memo[ln][i][j + swapland - ln] and memo[swapland - ln][i + ln][j]:
                        # segment moved to the other side of swap land
                        # compare s1 left to s2 right
                        # and s1 right to s2 left
                        memo[swapland][i][j] = True
    return memo[size][0][0]

print('With memoization:')
print(is_scramble_memo("rgtea", "great"))  # True
print(is_scramble_memo("rfeat", "great"))  # False
