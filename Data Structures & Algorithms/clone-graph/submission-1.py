"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stack = [node]
        visited = set()
        visited.add(node)
        old_to_new = {}

        while stack:
            curr_node = stack.pop()
            old_to_new[curr_node] = Node(val=curr_node.val)

            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        for key, val in old_to_new.items():
            for neighbor in key.neighbors:
                val.neighbors.append(old_to_new[neighbor])

        return old_to_new[node]

