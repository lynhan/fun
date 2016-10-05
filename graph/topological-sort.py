"""
https://en.wikipedia.org/wiki/Topological_sorting
This is all very much pseodo-python, sans actual node objects and helper methods
"""

def khan(S):
    """
    S is set of start nodes with no incoming edges
    Approach: follow the signs
        start with a set of nodes with no incoming edges
        pop node from set and add to final list
        remove edge from node to children, add children to set if no incoming edge (set only contains nodes with no incoming edges)
    """
    L = []
    while S:
        node = S.pop()
        L.append(node)
        for child in node.children:
            child.remove_edge_to_parent()
            if not child.parents:
                S.add(c)
    if E:
        print('error: has cycle')
    else:
        return L

def dfs(unmarked):
    """
    Append nodes to L bottom up (leaf nodes first), return reverse.
    """
    L = [] # list that will contain the sorted nodes
    visited = set([]) # nodes visited by existing visit calls (diamonds are ok!)
    def visit(node):
        if node in visited:
            raise ValueError("graph not DAG")
        visited.append(node)
        if node in unmarked:
            # we are recursing, so node wasn't popped from the while loop
            unmarked.remove(node)
        for child in node.children:
            visit(child)
        visited.remove(node)
        L.append(node)  # done traversing from this node
    while unmarked:  # nodes we haven't started traversing from
        node = unmarked.pop()
        visit(node)
    return L[::-1]
