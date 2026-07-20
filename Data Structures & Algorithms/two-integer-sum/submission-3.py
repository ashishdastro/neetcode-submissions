class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        
        for i, num in enumerate(nums):
            required = target - num
            if required in idx_map:
                return [idx_map[required], i]
            idx_map[num] = i
        
        