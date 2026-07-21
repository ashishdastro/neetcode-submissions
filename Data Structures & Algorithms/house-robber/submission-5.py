class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = {}

        def rob_(i):
            if i == 0:
                return nums[0]

            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in memo:
                memo[i] = max(rob_(i-1), nums[i] + rob_(i-2))
            
            return memo[i]
        
        return rob_(len(nums) - 1)