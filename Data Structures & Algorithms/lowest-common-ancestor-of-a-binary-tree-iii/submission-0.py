"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set()
        parent = p
        while parent:
            parents.add(parent)
            parent = parent.parent
        
        parent = q
        while parent:
            if parent in parents:
                return parent
            parent = parent.parent
        
        return None