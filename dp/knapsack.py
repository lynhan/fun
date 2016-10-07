
def top_down(C, V, W):
    # case1 = knapsack(i-1, C)
    # case2 = V[i] + knapsack(i-1, C-W[i])
    # knapsack = max(case1, case2)
    pass

def tab(C, V, W):
    # 2d array (i, C) storing max value
    memo = [[0 for capacity in range(C+1)] for i in range(len(V))]
    for i in range(len(V)):
        for capacity in range(1, C+1):  # max value for capacity 0 is 0
            if i == 0:
                memo[i][capacity] = V[i] if capacity >= W[i] else 0
            else:
                case1 = memo[i-1][capacity]
                case2 = V[i] + memo[i-1][capacity-W[i]] if W[i] <= capacity else 0
                memo[i][capacity] = max(case1, case2)
    return memo[len(V)-1][C-1]

print(tab(6, [4,1,2,7,3], [3,1,4,5,3]))
