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

def get_edge_count(AL):
    EC = {}
    for node in AL:
        EC[node] = len(AL[node])
    return EC

def graph_diff():
    VAL, E = get_input()
    AL = get_al(E)
    EC = get_edge_count(AL)
    graph_sum = get_graph_sum(1, AL, VAL)
    min_diff = float('inf')
    done = set([]) # nodes whose edges have all been examined
    DIFF = {}

    import heapq as h
    q = []  # nodes ordered by min edge count
    for node in AL:
        h.heappush(q, (len(AL[node]), node))
    # print("queue", q)

    while len(q) > 1:
        cur = h.heappop(q)
        cur_node = cur[1]
        # print('cur_node', cur_node)
        others_done = []
        others_not_done = []  # will only have 1 node
        for other in AL[cur_node]:
            if other in done:
                others_done.append(other)
            else:
                others_not_done.append(other)
        buddy = others_not_done[0]
        # print('buddy', buddy)

        this_sum = VAL[cur_node]
        for other_node in others_done:
            d = DIFF[tuple(sorted((cur_node, other_node)))]
            this_sum += d[other_node]
        other_sum = graph_sum - this_sum
        # print('this_sum', this_sum)

        DIFF[tuple(sorted((cur_node, buddy)))] = {cur_node: this_sum, buddy: other_sum}
        q.remove((EC[buddy], buddy))
        EC[buddy] = EC[buddy] - 1
        q.append((EC[buddy], buddy))
        h.heapify(q)
        done.add(cur_node)
        # print('diff', DIFF)
        # print('done', done)
        # print('ec', EC)
        # print('new queue', q)
        # import pdb; pdb.set_trace()
        min_diff = min(min_diff, abs(this_sum - other_sum))
    print(min_diff)

graph_diff()
