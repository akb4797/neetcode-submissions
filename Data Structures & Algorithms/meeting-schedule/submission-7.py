"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sortedList = sorted(intervals, key= lambda x:x.start)

        for elem in range(0, len(sortedList)-1):
            if(sortedList[elem].end > sortedList[elem+1].start):
                return False
            
        return True