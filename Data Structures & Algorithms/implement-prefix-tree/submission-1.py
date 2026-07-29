class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]

        node.is_end = True

    def search(self, word: str) -> bool:
        # its a word if we can go through and find the word
        # and it has a * at the end
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True
        
        