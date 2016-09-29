def max_depth(node):
    from collections import deque
    q = deque([(node, 0)])
    maxd = 0
    while q:
        cur = q.popleft()
        if node.children:
            for c in node.children:
                q.append((c, cur[1] + 1))
        else:
            maxd = max(cur[1], maxd)
    return maxd
