class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        node = self
        for c in word:
            if not c in node.children:
                node.children[c] = Node()
            node = node.children[c]
        
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert all words into the trie
        trie = Node()
        for word in words:
            trie.insert(word)

        num_rows, num_cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == num_rows or c == num_cols or
                (r, c) in visited or board[r][c] not in node.children):
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            
            visited.remove((r,c))

        for r in range(num_rows):
            for c in range(num_cols):
                dfs(r, c, trie, "")

        return list(res)

            


