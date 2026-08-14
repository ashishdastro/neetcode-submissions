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
        visited = {}
        visited[node] = Node(node.val)

        while stack:
            cur = stack.pop()
            for nei in cur.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    stack.append(nei)
                visited[cur].neighbors.append(visited[nei])
        
        return visited[node]