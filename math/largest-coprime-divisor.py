def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def f(A, B):
    while gcd(A, B) > 1:
        A = A/gcd(A, B)
    return A
    