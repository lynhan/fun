"""
https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
"""
def path(V, D):
    for middle in range(len(V)):
        for start in range(len(V)):
            for end in range(len(V)):
                D[start][end] = min(D[start][end], \
                                D[start][middle] + D[middle][end])
