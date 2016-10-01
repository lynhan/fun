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
