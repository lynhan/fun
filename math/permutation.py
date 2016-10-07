"""
Generate all permutations of string
"""

def permute(s):
    if len(s) == 1:
        yield s
    for i in range(len(s)):
        for partial in permute(s[:i]+s[i+1:]):
            yield s[i] + partial

def f(s):
    l = []
    for p in permute(s):
        l.append(p)
    return l

print(f("abc"))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def permute_without_yield(s):
    if len(s) == 1:
        return [s]
    p = []
    for i in range(len(s)):
        partials = permute_without_yield(s[:i]+s[i+1:])
        p.extend(map(lambda part: s[i] + part, partials))
    return p

print(permute_without_yield("abc"))
