def decode(A):
    ret = ""
    while A != 0:
        A = A-1  # account for A = 1
        temp = A % 26  # multiple for current digit
        A /= 26  # go left
        ret += chr(temp+ord('A')) # convert multiple to letter
    return ret[::-1]

print(decode(53))