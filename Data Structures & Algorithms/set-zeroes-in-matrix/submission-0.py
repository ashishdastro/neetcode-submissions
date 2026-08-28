class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_set = set()
        cols_set = set()

        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_set.add(r)
                    cols_set.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in rows_set or c in cols_set:
                    matrix[r][c] = 0
                    
        