class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        right_max = [0] * n
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        left_max = 0
        res = 0

        for i, h in enumerate(height):
            water = min(left_max, right_max[i]) - height[i]
            res += max(0, water)
            left_max = max(left_max, h)

        return res