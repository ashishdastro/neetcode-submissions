class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        
        for char in t:
            idx = ord(char) - ord('a')
            if counts[idx] <= 0:
                return False
            else:
                counts[idx] -= 1
        
        return True