class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]
        
        cur = nums[0]
        ans = nums[0]

        for i in range(1, n):
            cur = max(nums[i], nums[i] + cur)
            ans = max(ans, cur)

        return ans    
