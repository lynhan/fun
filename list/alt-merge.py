"""
http://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/
"""

def f(one, two):
    one_next = None
    two_next = None
    while one and two:
        one_next = one.next
        two_next = two.next
        one.next = two
        if one_next:
            two.next = one_next
        one = one_next
        two = two_next
