"""
Articulation point
    subtree root with no back edge
"""

def f(V, AL):
    # low[root] = back edge to earliest ancestor for node in subtree, including root
    low = [float('inf') for x in range(len(V))]
    order = [-1 for x in range(len(V))]
    parent = [-1 for x in range(len(V))]
    count = 0
    def dfs(node):
        nonlocal count
        order[node] = count
        low[node] = count
        count += 1
        for neighbor in AL[node]:
            if order[neighbor] == -1:  # unvisited
                parent[neighbor] = node
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])
            elif neighbor != parent[node]:  # back edge from node
                low[node] = min(low[node], order[neighbor])
    dfs(V[0])
    art = []
    for node in V:
        for neighbor in AL[node]:
            if low[neighbor] > order[node]:  # neighbor w/o back edge
                art.append(node)
    return art

V = [0,1,2,3]
AL = {
    0: [3, 1],
    1: [2, 3, 0],
    2: [1],
    3: [1, 0],
}
print(f(V, AL))  # [1]
