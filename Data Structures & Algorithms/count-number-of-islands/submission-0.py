class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r+dr, c+dc)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count 