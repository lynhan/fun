"""
Given a binary tree
Return the preorder traversal of its nodes’ values without recursion
"""

def pre(node):
    order = []
    stack = [node]
    while stack:
        cur = stack.pop()
        order.append(cur)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return order
