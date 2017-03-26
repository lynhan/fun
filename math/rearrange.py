# A[i] + Arr[Arr[i]] * n
# old = A[i] % n
# new = a[i] / n

def re(A):
    for i in range(len(A)):
        if A[i] > i:
            A[i] += A[A[i]] * len(A)
        else:
            old = A[A[i]] % len(A)
            A[i] += old * len(A)
    for i in range(len(A)):
        A[i] = A[i] // len(A)
    print(A)
        
    
re([5,4,0,3,1,2])