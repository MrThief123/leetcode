'''
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []

        for i in intervals:
            # Case 1: current interval completely before newInterval
            if i[1] < newInterval[0]:
                out.append(i)

            # Case 2: current interval completely after newInterval
            elif i[0] > newInterval[1]:
                out.append(newInterval)
                newInterval = i  # switch to processing remaining intervals

            # Case 3: overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])

        out.append(newInterval)
        return out