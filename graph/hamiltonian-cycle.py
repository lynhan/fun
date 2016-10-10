"""
given unweighted graph
visit all nodes once and end with starting node
backtrack when no more new nodes reachable and have not visited all nodes
"""

def ham(V, AL):
    path = [0]*(len(V)+1)
    def f(path, index):  # index of last added node
        if index == len(V)-1:
            if 0 in AL[path[index]]:
                return True
            else:
                return False
        for neighbor in AL[path[index]]:
            if neighbor not in path[:index+1]:
                path[index+1] = neighbor
                if f(path, index+1):
                    return True
    if f(path, 0):  # pass by reference
        return path
    return "no ham cycle"

V = [0,1,2,3,4]
AL = {
    0: set([1, 3]),
    1: set([0, 2, 3, 4]),
    2: set([1, 4]),
    3: set([0, 1, 4]),
    4: set([1, 2, 3]),
}

print(ham(V, AL))  # [0, 1, 2, 4, 3, 0]
