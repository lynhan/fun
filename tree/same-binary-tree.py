"""
Given root nodes of two binary trees
Return if the trees are the same
"""

def is_same(a, b):
    if a != b:
        return False
    if not a and not b:
        return True
    l = is_same(a.left, b.left)
    r = is_same(a.right, b.right)
    return l and r
