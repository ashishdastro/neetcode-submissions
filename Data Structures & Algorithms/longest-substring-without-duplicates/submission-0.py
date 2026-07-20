class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            length = right - left + 1
            ans = max(ans, length)
        
        return ans