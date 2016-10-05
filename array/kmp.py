"""
Knuth–Morris–Pratt algorithm
Check for substring with runtime O(len(string)) and space O(len(substring));

We parse the substring to make a table, which is an array of len(sub).
Each index i has a number n, which refers to the length of the longest matching prefix (segment from the start of the substring) and suffix (segment ending at index i, inclusive). This value tells us how much we need to backtrack when there is a mismatch.

When there is a mismatch at string index j and substring index i
    The next index to examine in the string is:
        j - table[i - 1]
    The next index to examine in the substring is:
        i - table[i - 1]
In order words, we skip checking the current prefix because the current prefix was the suffix that we just checked.

This is how we find n.
    prefix_end starts at 0
    suffix_end starts at 1
    Our invariant is that
        the left segment from index 0 to prefix_end (the prefix)
        is always the same as the right segment ending at suffix_end (the suffix)
        and matches the right segment maximally
            that is, if the substring ending at suffix end is "ababa"
            prefix and suffix are both "aba", not just "a"
    Base case
        table[0] is always 0
            because if string[j] does not match substring[1], then we reexamine string[j] (string[j-table[1-1]]) and substring[0]
    Induction
        sameness
            prefix and suffix are built up with the same characters at the same time
        maximal matching
            we always increment prefix and suffix when their next chars match
    Termination
        We track length of longest prefix and suffix until the end of the substring, so every character in the substring has the correct value.
"""

def make_table(sub):
    table = [0] * len(sub)
    prefix_end = 0
    suffix_end = 1
    while suffix_end < len(sub):
        if sub[suffix_end] == sub[prefix_end]:
            table[suffix_end] = table[suffix_end-1] + 1
            prefix_end += 1
        else:
            table[suffix_end] = 0
            prefix_end = 0
        suffix_end += 1
    return table

def has_substring(string, sub):
    if not sub:
        return None
    table = make_table(sub)
    i, j = 0, 0
    while i < len(string):
        if string[i] != sub[j]:
            if table[j] > 1:
                j = table[j-1]
            else:
                i += 1
                j = 0
        elif string[i] == sub[j]:
            i += 1
            j += 1
        if j == len(sub):
            return True
    return False
