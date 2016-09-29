"""
https://www.interviewbit.com/problems/sum-root-to-leaf-numbers/

Given
    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12
The root-to-leaf path 1->3 represents the number 13

Return 25
"""

def bfs(node):
    total = 0
    from collections import deque
    q = deque([(node, 0)])
    while q:
        cur = q.popleft()
        partial = cur[0] + cur[1]
        if cur.children:
            q.extend(map((lambda x: (x, partial)), cur.children))
        else:
            total += partial
    return total

def dfs_iterative(node):
    total = 0
    stack = [(node, 0)]
    while stack:
        cur = stack.pop()
        partial = cur[0] + cur[1]
        if cur.children:
            stack.extend(map((lambda x: (x, partial)), cur.children))
        else:
            total += partial
    return total

def dfs_recursive(node):
    total = 0
    def helper(item):
        partial = item[0] + item[1]
        if item[0].children:
            for c in item[0].children:
                helper((c, partial))
        else:
            total += partial
    helper((node, 0))
    return total
