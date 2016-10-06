"""
https://www.hackerrank.com/challenges/cut-the-tree
O(E^2)
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
    visited_nodes = set([])
    DIFF = {}
    import heapq as h
    q = []  # nodes ordered by min edge count
    for node in AL:
        h.heappush(q, (len(AL[node]), node))
    while len(q) > 1:  # O(edges)
        cur = h.heappop(q)
        cur_node = cur[1]
        visited_neighbors = []
        new_neighbor = []  # will only have 1 node
        for neighbor in AL[cur_node]:  # O(max neighbor)
            if neighbor in visited_nodes:
                visited_neighbors.append(neighbor)
            else:
                new_neighbor.append(neighbor)
        edge_neighbor = new_neighbor[0]
        cur_node_graph_sum = VAL[cur_node]
        for n in visited_neighbors:
            d = DIFF[tuple(sorted((cur_node, n)))]
            cur_node_graph_sum += d[n]
        DIFF[tuple(sorted((cur_node, edge_neighbor)))] = {
            cur_node: cur_node_graph_sum,
            edge_neighbor: graph_sum - cur_node_graph_sum}
        # update edge count for node in heap : O(edges)
        q.remove((EC[edge_neighbor], edge_neighbor))
        EC[edge_neighbor] = EC[edge_neighbor] - 1
        q.append((EC[edge_neighbor], edge_neighbor))
        h.heapify(q)
        visited_nodes.add(cur_node)
        min_diff = min(min_diff, abs(graph_sum - 2*cur_node_graph_sum))
    print(min_diff)

graph_diff()
