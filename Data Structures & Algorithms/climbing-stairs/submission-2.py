class Solution:   
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(n):
            if n  <= 2:
                return n
            
            if n not in memo:
                memo[n] = dfs(n-1) + dfs(n-2)

            return memo[n]
        
        return dfs(n)