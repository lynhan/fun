"""
https://www.interviewbit.com/problems/word-ladder-i/
"""

def get_word_dist(w1, w2):
    diff_char_count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff_char_count += 1
    return diff_char_count

def get_word_distances(w1, d):
    distances = [[] for x in range(len(w1))]
    for w in d:
        dist = get_word_dist(w1, w)
        distances[dist - 1].append(w)
    return distances

def get_words_near_w2(w2, d):
    w = set([])
    for word in d:
        if get_word_dist(word, w2) == 1:
            w.add(word)
    return w

def f(w1, w2, d):
    distances = get_word_distances(w1, d)
    words_near_w2 = get_words_near_w2(w2, d)
    from collections import deque
    from copy import deepcopy
    q = deque([[w1]])
    while q:
        curpath = q.popleft()
        for w in distances[len(curpath)-1]:
            if get_word_dist(curpath[-1], w) == 1:
                newpath = deepcopy(curpath)
                newpath.append(w)
                if w in words_near_w2:
                    newpath.append(w2)
                    return newpath
                q.append(newpath)
    return "no path found"

print(f("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
