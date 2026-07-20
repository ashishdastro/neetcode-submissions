class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        min_heap = []

        for num in counts.keys():
            heapq.heappush(min_heap, (counts[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [item[1] for item in min_heap]