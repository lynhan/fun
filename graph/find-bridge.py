"""
Return all bridges in graph. Assume nodes are numbered from 0.
"""

def bridge(V, AL):
    bridges = []
    visited = {}  # node: dfs parents
    def dfs(node):
        for neighbor in AL[node]:
            if neighbor in visited:
                visited[neighbor].append(node)
            else:
                visited[neighbor] = [node]
                dfs(neighbor)
    dfs(0)
    for node in visited:
        if len(visited[node]) == 1:
            bridges.append((node, visited[node][0]))
    return bridges
