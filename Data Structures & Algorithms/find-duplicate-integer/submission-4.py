class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [0] * n

        for num in nums:
            if seen[num-1] == 1:
                return num
            seen[num-1] = 1
        
        return -1