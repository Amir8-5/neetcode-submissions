"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = {}

        def rec(node):
            if node in res:
                return res[node]
            
            res[node] = Node(node.val)
            for nei in node.neighbors:
                res[node].neighbors.append(rec(nei))
            return res[node]
        
        return rec(node) if node else None

            
