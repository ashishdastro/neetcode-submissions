class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord("a")] += 1
            key = tuple(key)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        return list(groups.values())
