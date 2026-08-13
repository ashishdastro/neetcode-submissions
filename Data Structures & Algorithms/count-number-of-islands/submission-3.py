class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                cur_r, cur_c = q.popleft()

                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"


        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    result += 1
                    bfs(r, c)
        
        return result                        

