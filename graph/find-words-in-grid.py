"""
Given a dictionary of words and a M x N board where every cell has one character.
Find all possible words that can be formed by a sequence of adjacent characters.
"""

# time O(n * m * num words * len(longest word))
# space O(words)
def f(words, board):  # words: {starting letter: [words]}
    res = []
    current_char = None
    current_word = None

    def search(r, c, i): # len(longest word)
        if current_word[0] != board[r][c]:
            return False
        found = []
        if r > 0:
            up = search(r-1, c, i+1)
            if up: found.extend(up)
        if c > 0:
            left = search(r, c-1, i+1)
            if left: found.extend(left)
        if r < len(board)-1:
            down = search(r+1, c, i+1)
            if down: found.extend(down)
        if c < len(board[0])-1:
            right = search(r, c+1, i+1)
            if right: found.extend(right)
        return found

    for r in range(len(board)): # n
        for c in range(len(board[0])): # m
            if char in words:
                current_char = char
                for word in words[char]: # num words
                    current_word = word
                    found = search(r, c, 0):
                    if found: res.extend(found)
    return res
