class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        right_heights = [0]
        max_r = 0
        for i in range(n-2, -1, -1):
            max_r = max(max_r, height[i+1])
            right_heights.append(max_r)
        
        right_heights = right_heights[::-1]

        max_l = 0
        ans = 0
        for i in range(n):
            water = min(max_l, right_heights[i]) - height[i]
            ans += max(0, water)
            max_l = max(max_l, height[i])
        return ans
