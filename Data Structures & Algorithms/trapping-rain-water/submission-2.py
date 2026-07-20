class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()

                if not stack:
                    break
                
                left = stack[-1]
                w = i - left - 1
                ans += w * (min(height[left], h) - height[bottom])

            stack.append(i)
        
        return ans