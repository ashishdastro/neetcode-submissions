class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == 0:
                return 0
            grid[r][c] = 0    
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        max_area = 0
        for r in range(m):
            for c in range(n):
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area