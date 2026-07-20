class Solution:
    from collections import Counter
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        result = []
        for bucket in buckets[::-1]:
            result += bucket
            if len(result) == k:
                return result
