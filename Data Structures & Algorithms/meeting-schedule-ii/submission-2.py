"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = []
        for interval in intervals:
            points.append((interval.start, 1))            
            points.append((interval.end, -1))
        
        points.sort()
        max_overlap = 0
        active = 0

        for point in points:
            if point[1] == 1:
                active += 1
            else:
                active -= 1
            max_overlap = max(max_overlap, active)
        
        return max_overlap

