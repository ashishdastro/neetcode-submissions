class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for char in s:
                idx = ord(char) - ord('a')
                key[idx] += 1
            
            key = tuple(key)
            d[key].append(s)
        
        return list(d.values())