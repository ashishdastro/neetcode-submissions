class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1]
        prod = 1

        for i in range(n-1, 0, -1):
            prod *= nums[i]
            right.append(prod)
        
        prod = 1
        result = []
        right = right[::-1]

        for i in range(n):
            result.append(prod * right[i])
            prod *= nums[i]
        
        return result