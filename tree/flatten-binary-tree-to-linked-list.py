"""
Given a binary tree, flatten it to a linked list in place
Approach
    Base case
        if node has no children, return node as reference to end of linked list
    Recurse
        flatten left subtree, get end of linked list
        save right child
        set left child as right child of parent
        connect right child to end of left linked list
        then flatten right subtree
"""

def flatten(node):
    if not node.left and not node.right:
        return node
    list_end = None
    if node.left:
        list_end = flatten(node.left)
        original_right = node.right
        node.right = node.left
        list_end.right = original_right
        if original_right:
            flatten(original_right)
    elif node.right:
        list_end = flatten(node.right)
    return list_end
