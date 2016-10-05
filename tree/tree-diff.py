"""
Given directed tree
    removing an edge will result in two subtrees
    tree diff = tree1_sum - tree_sum
Return
    min tree diff
"""

def set_tree_sum(node):  # assumes node has value
    if not node.children:
        node.tree_sum = node.val
        return node.val
    node.sum = node.val
    for child in node.children:
        node.sum += set_tree_sum(child)
    return node.sum

def min_tree_diff(node):
    set_tree_sum(node)  # in place
    min_diff = float('inf')
    stack = [node]
    while stack:
        cur = stack.pop()
        min_diff = min(min_diff, node.tree_sum - cur.tree_sum)
        for child in node.children:
            stack.append(child)
    return min_diff
