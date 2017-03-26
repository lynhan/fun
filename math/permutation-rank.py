def get_chars_before(char, order):
    for i, c in enumerate(order):
        if c == char:
            return i
    return 0

def rank(A):
    import math
    r = 0
    order = sorted(A)
    for i, char in enumerate(A):
        r += get_chars_before(char, order) * math.factorial(len(order)-1)
        order.remove(char)
    return r + 1

print(rank('acb'))