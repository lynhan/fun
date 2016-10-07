"""
Given a string of integers
Return number of encodings
A -> 1
Z -> 26
12 decodes to AB and L
"""
memo = {}
def top_down(s):
    if not s:
        return 1
    try: return memo[s]
    except KeyError:
        total = 0
        if int(s[:1]) > 0 and int(s[:1]) <= 26:
            total += top_down(s[1:])
        if len(s) > 1 and int(s[:2]) > 0 and int(s[:2]) <= 26:
            total += top_down(s[2:])
        memo[s] = total
        return total

print(top_down("12"))
