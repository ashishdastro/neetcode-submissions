class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(idx):
            if idx < 0:
                return 0
            if idx in memo:
                return memo[idx]

            memo[idx] = max(nums[idx] + helper(idx-2), helper(idx-1))
            return memo[idx]
            
        return helper(len(nums) - 1)