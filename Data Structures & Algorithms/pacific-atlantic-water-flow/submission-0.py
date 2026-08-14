class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set() 
        atlantic = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(r, c, reachable):
            reachable.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    not 0 <= nr < rows or 
                    not 0 <= nc < cols or 
                    (nr, nc) in reachable or 
                    heights[nr][nc] < heights[r][c]
                ):
                    continue

                dfs(nr, nc, reachable)
        
        # Top and bottom borders
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        # Left and right borders
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)
        
        return [[r, c] for r,c in pacific & atlantic]