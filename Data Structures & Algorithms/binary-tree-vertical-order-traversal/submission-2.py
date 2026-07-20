# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        min_col = max_col = 0
        cols = defaultdict(list)

        q = deque([(root, 0)])

        while q:
            curr, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            cols[col].append(curr.val)

            if curr.left: q.append((curr.left, col - 1))
            if curr.right: q.append((curr.right, col + 1))
        
        result = []
        for col in range(min_col, max_col + 1):
            if col in cols:
                result.append(cols[col])

        return result






