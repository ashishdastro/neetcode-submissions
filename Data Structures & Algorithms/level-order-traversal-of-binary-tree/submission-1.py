# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        levels = {}

        stack = [(root, 1)]

        while stack:
            cur, level = stack.pop()

            if level in levels:
                levels[level].append(cur.val)
            else:
                levels[level] = [cur.val]
            
            if cur.right: stack.append((cur.right, level + 1))
            if cur.left: stack.append((cur.left, level + 1))

        return list(levels.values())

