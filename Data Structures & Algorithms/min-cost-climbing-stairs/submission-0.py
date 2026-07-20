class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cur = 0

        for i in range(2, len(cost) + 1):
            prev, cur = cur, min(prev + cost[i-2], cur + cost[i-1])
        
        return cur