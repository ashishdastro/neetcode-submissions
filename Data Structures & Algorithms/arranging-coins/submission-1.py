class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n + 1

        while left < right:
            mid = left + (right - left) // 2
            if int(mid * (mid + 1) / 2) > n:
                right = mid 
            else:
                left = mid + 1
        
        return left - 1