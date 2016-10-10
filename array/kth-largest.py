"""
Given
    array of unique numbers, number k where k is smaller than size of array
Return
    kth smallest element in the given array.
"""

# time O(nlogn)
def f(A, k):
    A.sort()
    return A[k-1]

# time O(n + klogn)
def f2(A, k):
    import heapq as h
    h.heapify(A)  # O(n)
    res = None
    for i in range(k):  # O(klogn)
        res = h.heappop(A)
    return res

# make max heap from A[:k]
# A[k:], if el < max heap root, max heap root does not belong in first k smallest
# replace root with el and heapify
# time: O(n + (n-k)*logk)
# space: O(k)
def f3(A, k):
    import heapq as h
    B = list(map(lambda x: -x, A))[:k]
    h.heapify(B)  # O(k)
    for i in range(k, len(A)): # O((n-k)*logk)
        if -A[i] > B[0]:
            B[0] = -A[i]
            h.heapify(B)
    return -B[0]

def partition(A, left, right, pivot):
    pivot_val = A[pivot]
    A[pivot], A[right] = A[right], A[pivot]
    border = left
    for i in range(left, right):
        if A[i] < pivot_val:
            A[border], A[i] = A[i], A[border]
            border += 1
    A[right], A[border] = A[border], A[right]
    return border

# quick select
# worse case O(n^2), avg O(n)
def f4(A, k):
    import random
    left = 0
    right = len(A)-1
    while left != right:
        pivot = random.randint(left, right)
        pivot = partition(A, left, right, pivot)
        if pivot == k:
            return A[k]
        if k < pivot:
            right = pivot-1
        else:
            left = pivot+1
    return A[left-1]

print(f4([2,4,6,3,7], 2))  # 3
