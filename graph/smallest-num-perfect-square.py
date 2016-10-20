"""
Given int n
Return smallest number of perfect squares that sum to n
"""

def get_perfect_squares(n):
    s = []
    num = 1
    while num ** 2 <= n:
        s.append(num ** 2)
        num += 1
    return s

def f(n):
    perfect_squares = get_perfect_squares(n)
    def dfs(n, depth):
        if n < 0:
            return False
        if n == 0:
            return depth
        for j in range(len(perfect_squares)-1, -1, -1):
            new_n = n - perfect_squares[j]
            res_depth = dfs(new_n, depth+1)
            if res_depth: return res_depth
    return dfs(n, 0)

print(f(16))
