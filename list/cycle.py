"""
Given
    head of a singly linked list with a cycle
Return
    start node of the cycle
Approach
    use two pointers, one twice as fast as the other
    if length before cycle is k
        a is fast pointer
        b is slow pointer
        when b is at k (start of cycle)
            a is at 2k, or k into cycle
            a is cycle length (L) - k behind b
            let x = L - k
                when b travels x, a will travel 2x
                if a is x behind b, a and b will meet after
                    a travels 2x and b travels x
            a and b will meet at 2x = 2(L - k) = 2L - 2k
            since a is at k
                adding 2L means a will be in the same spot
                subtracking 2k means a will be k before start
            so when a and b meet, travel k more to start of cycle
                put one at start of list and increment both by single steps
"""

def get_cycle(start):
    slow, fast = start.next, start.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    slow = start
    while slow != fast
        slow = slow.next
        fast = fast.next
    return fast
