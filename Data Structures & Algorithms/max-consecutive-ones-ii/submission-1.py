class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        flip = 0
        count = 0
        ans = 0

        for num in nums:
            if num == 0 and flip == 1:
                ans = max(ans, count)
                count = 0
                flip = 0
            else:
                if num == 0:
                    flip = 1
                count += 1
            
        return max(ans, count)