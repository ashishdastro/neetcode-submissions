"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for event in intervals:
            events.append((event.start, 1))            
            events.append((event.end, -1))
        
        events.sort()

        max_rooms = 0
        rooms = 0

        for _, delta in events:
            rooms += delta 
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms

