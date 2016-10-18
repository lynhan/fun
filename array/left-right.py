"""
https://www.hackerrank.com/challenges/sherlock-and-array
"""

test_cases = int(input())

def process():
    L = int(input())
    A = map(lambda x: int(x), input().split())
    if L == 1:
        print("YES")
        return
    if L < 3:
        print("NO")
        return

    left = [0]*L
    left_sum = 0
    for i in range(L):
        left_sum += A[i]
        left[i] = left_sum

    right = [0]*L
    right_sum = 0
    for i in range(L-1, -1, -1):
        right_sum += A[i]
        right[i] = right_sum

    for i in range(L):
        if left[i] == right[i]:
            print("YES")
    print("NO")


for x in range(test_cases):
    process()
