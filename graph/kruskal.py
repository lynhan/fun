"""
makes mst
add smallest edge that doesn't form cycle
runtime O(ElogE) limited by sorting edges
space O(V)
"""

def k(E):  # (weight, node1, node2)
    E.sort()
    tree_nodes = set([])
    tree_edges = []
    for edge in E:
        if edge[1] in tree and edge[2] in tree_nodes:
            continue
        tree_edges.append(edge)
        tree_nodes.append(edge[1])
        tree_nodes.append(edge[2])
    return tree_edges
