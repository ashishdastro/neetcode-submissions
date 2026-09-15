class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        res = n + 1
        for i in range(n):
            left, right = i, n
            while left < right:
                mid = left + (right - left) // 2
                cur_sum = prefix_sum[mid + 1] - prefix_sum[i]
                if cur_sum >= target:
                    right = mid
                else:
                    left = mid + 1
                
            if left != n:
                res = min(res, left - i + 1)
        
        return res % (n + 1)
