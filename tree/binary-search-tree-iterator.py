class BSTIterator:
    def __init__(self, root):
        self.root = root
        self.next_path = []
        self.prev_path = []

        # get smallest element
        node = self.root
        while node:
            self.next_path.append(node)
            node = node.left

        # get biggest element
        node = self.root
        while node:
            self.prev_path.append(node)
            node = node.right

    def has_next(self): # O(1) time, O(h) memory
        return bool(self.next_path)

    def has_prev(self):  # O(1) time, O(h) memory
        return bool(self.prev_path)

    def get_next(self):
        next = self.next_path.pop()
        # update stack
        if next.right:
            node = next.right
            while node:
                self.next_path.append(node)
                node = node.left
        return next.val

    def get_prev(self):
        prev = self.prev_path.pop()
        # update stack
        if prev.left:
            node = prev.left
            while.node:
                self.prev_path.append(node)
                node = node.right
        return prev.val
