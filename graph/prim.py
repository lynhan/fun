"""
minimum spanning tree (prim)
    spanning tree: subgraph that is a tree and connects all the vertices together
    mst: weight less than or equal to the weight of every other spanning tree
    greedily creates min weight connected graph with no cycles
    by connecting tree constructed so far to min weight edge with unvisited neighbor
"""

def prim_matrix_helper(newnodes, tree, M):
    nearest_node = None
    min_edge = float('inf')
    for node in tree:
        for neighbor in M[node]:
            if neighbor not in tree and M[node][neighbor] < min_edge:
                min_edge = M[node][neighbor]
                nearest_node = neighbor
    if nearest_node:
        newnodes.remove(nearest_node)
        tree.add(nearest_node)
    return nearest_node

def prim_matrix(V, M):
    """
    this approach iterates through neighbors of every node in the tree
    to find the min edge neighbor until no neighbor is found
    time: O(V^2)
    """
    newnodes = set(V)
    node = newnodes.pop()
    tree = set([node])
    found_neighbor = prim_matrix_helper(newnodes, tree, M)
    while found_neighbor:
        found_neighbor = prim_matrix_helper(newnodes, tree, M)
    return tree

def prim_heap(V, AL): # AL[node] = [(neighbor, weight)]
    """
    this approach tracks a frontier of nodes to explore, ordered by edge weight
    from current tree
    time: O(ElogE)
    space: O(E)
    """
    import heapq as h
    tree = set([])
    frontier = [(0, (V[0], V[0]) )]
    while len(tree) < len(V):
        node = h.heappop(frontier)
        tree.add(node)
        for nb in AL[node]:
            h.heappush(frontier, (nb[1], (node, nb[0]) ))
    return tree
