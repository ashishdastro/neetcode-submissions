class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                s = board[r][c]
                if s == ".":
                    continue
                
                if s in rows[r] or s in cols[c] or s in squares[(r//3, c//3)]:
                    return False
                
                cols[c].add(s)
                rows[r].add(s)
                squares[(r//3, c//3)].add(s)
        
        return True