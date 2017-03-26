def pal(A):
    if A < 0:
        return False

    if A < 10: 
        return True

    # 10 ** digits is just one more than actual digit count
    digits = 1
    while A // (10 ** digits) > 0:
        digits += 1

    import math
    for i in range(int( math.ceil(digits // 2) )):  # rounds up for odd numbers

        digits_from_right = 10 ** (digits - i - 1)
        left = (A // digits_from_right) % 10
        right_part =  A % (10 ** (i + 1))
        right = right_part // (10 ** i)
        if left != right:
            return False
    return True

print(pal(125421))