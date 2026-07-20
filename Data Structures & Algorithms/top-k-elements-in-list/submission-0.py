class Solution:
    from collections import Counter
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)        
        sorted_elements = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        return sorted_elements[:k]
