"""
Given
    k sorted lists
Return
    merged, sorted list
Approach
    Keep a pointer for each list
    Append min pointer to new list and increment pointer until old list is empty
        Track min pointer with min heap (logk per push)
        Runtime is nlogk total where n is total number of elements and k is total number of lists
"""

def merge(array):
    import heapq
    fin = []
    h = []
    # populate heap
    for i, a in enumerate(array):
        heapq.heappush(h, (a[0], (0, i)))
    while h:
        cur = heapq.heappop(h)
        fin.append(cur[0])
        item_index, list_index = cur[1][0], cur[1][1]
        if item_index < len(array[list_index]) - 1:
            heapq.heappush(h, (array[list_index][item_index+1], (item_index+1, list_index)))
    return fin

print(merge([[1,3,4],[2,5,6]]))
