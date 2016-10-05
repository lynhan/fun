"""
https://www.hackerrank.com/challenges/cut-the-tree
Given undirected graph
    removing an edge will result in two subgraphs
    graph diff = graph1_sum - graph_sum
Return
    min graph diff
"""

def get_input():
    node_num = input()
    node_val = input().split()
    VAL = [0] + list(map(lambda x: int(x), node_val))
    E = []
    for x in range(int(node_num)-1):
        edge = input().split()
        E.append( (int(edge[0]), int(edge[1]) ) )
    return VAL, E

def get_al(E):
    AL = {}  # adjacency list of node to list adjacent nodes
    for edge in E:
        if edge[0] in AL:
            AL[edge[0]].append(edge[1])
        else:
            AL[edge[0]] = [edge[1]]
        if edge[1] in AL:
            AL[edge[1]].append(edge[0])
        else:
            AL[edge[1]] = [edge[0]]
    return AL

def get_graph_sum(node, AL, VAL):
    s = 0
    stack = [node]
    visited = set([])
    while stack:
        cur = stack.pop()
        visited.add(cur)
        s += VAL[cur]
        for neighbor in AL[cur]:
            if neighbor not in visited:
                stack.append(neighbor)
    return s

def get_subgraph_sum(edge, AL, VAL):
    root = edge[0]
    other = edge[1]
    stack = [root]
    visited = set([])
    s = 0
    while stack:
        cur = stack.pop()
        visited.add(cur)
        s += VAL[cur]
        for neighbor in AL[cur]:
            if neighbor != other and neighbor not in visited:
                stack.append(neighbor)
    return s

def graph_diff():
    VAL, E = get_input()
    AL = get_al(E)
    graph_sum = get_graph_sum(1, AL, VAL)  # start with node 1

    min_diff = float('inf')
    for edge in E:
        part1 = get_subgraph_sum(edge, AL, VAL)
        part2 = graph_sum - part1
        min_diff = min(min_diff, abs(part1-part2))
    print(min_diff)

graph_diff()
