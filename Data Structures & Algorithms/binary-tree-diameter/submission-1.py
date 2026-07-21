# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, False)]
        height = {}
        diameter = 0

        while stack:
            cur, visited = stack.pop()

            if not cur:
                continue
            
            if visited:
                left = height.get(cur.left, 0)
                right = height.get(cur.right, 0)
                diameter = max(diameter, left+right)
                height[cur] = 1 + max(left, right)
            else:
                stack.append((cur, True))
                stack.append((cur.left, False))
                stack.append((cur.right, False))
        
        return diameter
        














