class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water = 0

        left, right = 0, n - 1

        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            water = w * h
            max_water = max(max_water, water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water