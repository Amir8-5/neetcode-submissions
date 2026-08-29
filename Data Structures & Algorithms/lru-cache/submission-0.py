class Node:
    def __init__(self, key:int, val: int):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.values = {}
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key in self.values:
            node = self.values[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.remove(self.values[key])
        node = Node(key, value)
        self.insert(node)
        self.values[key] = node
        if len(self.values) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.values[lru.key]


    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next = nxt
        nxt.prev = pre

    def insert(self, node):
        # insert at right
        pre, nxt = self.right.prev, self.right
        pre.next = nxt.prev = node
        node.prev, node.next = pre, nxt
        



        
