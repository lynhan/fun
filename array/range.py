"""
What a delicious problem.
"""

class Node:
    def __init__(self, val, p = None, l = None, r = None):
        self.val = val
        self.p = p
        self.l = l
        self.r = r

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

class BST:
    def __init__(self, root):
        self.root = root

    def add(self, node):
        pass

    def delete(self, node):
        pass

class AVL(BST):
    def add(self, node):
        pass

    def delete(self, node):
        pass
