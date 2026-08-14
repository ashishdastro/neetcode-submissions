class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                cur_r, cur_c = q.popleft()
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and(nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
            return area 

        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        return max_area