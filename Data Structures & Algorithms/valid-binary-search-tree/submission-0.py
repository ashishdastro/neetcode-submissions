# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lower, upper = float('-inf'), float('inf')
        stack = [(root, lower, upper)]

        while stack:
            cur, lower, upper = stack.pop() 
            if not lower < cur.val < upper:
                return False
            
            if cur.right: stack.append((cur.right, cur.val, upper))
            if cur.left: stack.append((cur.left, lower, cur.val))
        
        return True