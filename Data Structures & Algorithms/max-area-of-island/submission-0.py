class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        area = 0
        for r in range(m):
            for c in range(n):
                area = max(area, dfs(r, c))
        
        return area