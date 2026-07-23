class Node:
    def __init__ (self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # we have doubly ll as opposed to a deque bc we can store
        # addresses of nodes as opposed to indices
        # these wont get violated whenver new stuff comes in
        # heap is ytoo slow
        self.cap = capacity
        self.key_to_node = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # helpers
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert_at_head(self, node):
        prv = self.right.prev

        self.right.prev = node
        prv.next = node

        node.prev = prv
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
            self.insert_at_head(self.key_to_node[key])
            return self.key_to_node[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
            
        self.key_to_node[key] = Node(key, value)
        self.insert_at_head(self.key_to_node[key])

        if len(self.key_to_node) > self.cap:
            del self.key_to_node[self.left.next.key]
            self.remove(self.left.next)
        
