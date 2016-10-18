"""
Reverse a singly linked list.
"""

def f(node):
    prev = node
    head = node.next
    rest = head.next
    prev.next = None
    while head:
        head.next = prev
        prev = head
        head = rest
        if head:
            rest = rest.next
