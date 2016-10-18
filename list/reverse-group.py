def iter(node, k):
    left = None
    right = node
    for x in range(k):
        right = right.next

    while head:
        prev = node
        head = node.next
        rest = node.next.next

        while head != right:
            head.next = prev
            prev = head
            head = rest
            if rest:
                rest = rest.next

        # connect left and right
        left.next = head
        for x in range(k-1): # last element of sequence
            head = head.next
        head.next = right

        # update left, node, right for new sequence
        left = head
        node = head.next
        for x in range(k):
            right = right.next

def chunk(node, k):
    prev = node
    head = node
    for x in range(k):
        head = head.next
    rest = head
    for x in range(k):
        rest = rest.next

    def link(head, prev, rest):
        if not head:
            return
        head_end = head  #
        for x in range(k-1):
            head_end = head_end.next
        head_end.next = prev
        prev = head
        head = rest
        k_ = 0
        while k_ < k and rest:
            rest = rest.next
            k_ += 1
        link(head, prev, rest)

    link(head, prev, rest)

def rec(node, k):
    chunk(node, 1)
    chunk(node, k)
