"""
Given a sorted linked list, delete all duplicates such that each element appears only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

def rmdup(node):
    prev = None
    while node:
        if node == prev:
            prev.next = node.next
        prev = node
        node = node.next
