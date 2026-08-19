# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        height = {}

        stack = [(root, False)]

        while stack:
            cur, visited = stack.pop()

            if not cur:
                continue
            
            if visited:
                lh = height.get(cur.left, 0)
                rh = height.get(cur.right, 0)

                if abs(lh - rh) > 1: return False
            
                height[cur] = 1 + max(lh, rh)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))

        return True








