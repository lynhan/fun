"""
https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
longest path between two nodes has V-1 edges
    more than V-1 edges means cycle
"""

def f(V, E, W, source):
    dist = [float('inf')]* len(V)
    dist[0] = 0
    for i in range(len(E)):
        for node in V:
            if dist[node] != float('inf'):  # can get to this node
                for neighbor in E[node]:  # list of edges
                    dist[neighbor = min(dist[neighbor, dist[node] + W[edge])
    for node in V:
        for neighbor in E[node]:
            if dist[node] + W[edge] < dist[neighbor]:
                raise ValueError("graph has negative cycle")
