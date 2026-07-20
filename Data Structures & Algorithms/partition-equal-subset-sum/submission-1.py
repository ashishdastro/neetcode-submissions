class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        memo = {}
        def dfs(i, s):
            if s == target:
                return True
            if i == n or s > target:
                return False
            if (i, s) in memo:
                return memo[(i, s)]
            
            memo[(i, s)] = dfs(i+1, s) or dfs(i+1, s + nums[i])

            return memo[(i, s)]
        
        return dfs(0, 0)

