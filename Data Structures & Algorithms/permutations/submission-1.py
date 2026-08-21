class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        perms = self.permute(nums[1:])

        result = []

        for p in perms:
            for i in range(len(p) + 1):
                result.append(p[:i] + [nums[0]] + p[i:])
        
        return result