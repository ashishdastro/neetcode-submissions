# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (0, True)
            
            lh, lb = dfs(root.left)
            rh, rb = dfs(root.right)

            h = 1 + max(lh, rh)
            b = lb and rb and abs(lh - rh) <= 1

            return (h, b)

        _ , b = dfs(root)

        return b