# 1) num % 10 gives you the last digit of a number.
# 2) num / 10 gives you the number after removing the last digit.
# 3) num * 10 + digit appends the digit at the end of the number.

def reverse(A):
    if abs(A) < 10:
        return A
    pos = abs(A)
    digits = 1
    while pos // (10 ** digits) > 0:
        digits += 1
    res = 0
    for i in range(digits):
        last = pos % 10
        res = res * 10 + last
        pos = pos / 10
    if len(bin(res))-2 >= 32:  # overflow
        return 0
    if A < 0:
        return res * -1
    return res

print(reverse(-1146467285))