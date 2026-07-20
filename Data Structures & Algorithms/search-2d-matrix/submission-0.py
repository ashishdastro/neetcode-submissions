class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m*n - 1

        while left < right:
            mid = left + (right - left) // 2
            r, c = mid // n, mid % n
            if matrix[r][c] >= target:
                right = mid
            else:
                left = mid + 1
        
        r, c = left // n, left % n

        return matrix[r][c] == target