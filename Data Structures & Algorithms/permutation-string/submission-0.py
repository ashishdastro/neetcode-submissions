class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts1 = [0] * 26
        for char in s1:
            counts1[ord(char) - ord('a')] += 1
        
        counts2 = [0] * 26
        left = 0
        for right in range(len(s2)):
            if right - left + 1 > len(s1):
                counts2[ord(s2[left]) - ord('a')] -= 1
                left += 1
            counts2[ord(s2[right]) - ord('a')] += 1
            if tuple(counts1) == tuple(counts2):
                return True
        
        return False