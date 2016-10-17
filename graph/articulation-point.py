"""
Articulation point
    root if dfs tree if more than two children
    any other vertex if there's no back edge stemming from subtree at that vertex
"""


def f(V, AL):
    order = [-1] * len(V)
    parent = [-1] * len(V)
    # parent[node] = back edge to earliest ancestor for some descendant of node

    count = 1
    def dfs(node):
        order[node] = count
        count += 1
        for neighbor in AL[node]:
            if order[neighbor] == -1:  # unvisited
                parent[neighbor] = node
                dfs(neighbor)
                parent[node] = min(parent[node], parent[neighbor])
            elif neighbor != parent[node]:  # back edge from node
                parent[node] = min(parent[node], neighbor)
    dfs(V[0])
    art = []
    for node in V:
        if node == 0 and len(AL[node]) > 1:  # root
            art.append(node)
        else:
            for neighbor in AL[node]:
                if parent[neighbor] == node:  # neighbor w/o back edge
                    art.append(node)
    return art
