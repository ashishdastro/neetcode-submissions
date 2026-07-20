class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += (row + 1 >= rows or grid[row+1][col] == 0)
                    perimeter += (row - 1 < 0 or grid[row-1][col] == 0)
                    perimeter += (col + 1 >= cols or grid[row][col+1] == 0)
                    perimeter += (col - 1 < 0 or grid[row][col-1] == 0)

        return perimeter