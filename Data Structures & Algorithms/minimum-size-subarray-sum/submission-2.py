class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0

        ans = n + 1
        cur_sum = 0
        for right in range(n): 
            cur_sum += nums[right]
            while cur_sum >= target:
                ans = min(ans, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return ans if ans != n + 1 else 0
