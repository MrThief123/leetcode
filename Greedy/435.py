'''
435. Non-overlapping Intervals
Keep track of the end time of the last added interval. 
If the start time of the current interval is greater than or equal to 
the end time of the last added interval, then there is no overlap and we can add this interval to our count. 
Otherwise, we need to remove one of the intervals. 
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # not overlap
            if start >= prevEnd:
                prevEnd = end
            # if overlap
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res