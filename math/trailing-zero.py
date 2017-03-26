def zero(num):
    count = 0
    mult = 1
    while num // (5**mult) > 0:
        count += num // (5**mult)
        mult += 1
    mult -= 1
    return count

print(zero(4617))
