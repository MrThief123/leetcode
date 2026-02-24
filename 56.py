'''
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        out = [intervals[0]]

        for i in intervals[1:]:
            prev = out[-1]

            # not overlap
            if prev[1] < i[0]:
                out.append(i)
            # if overlap update the prev
            else:
                out[-1] = [min(i[0], prev[0]), max(i[1], prev[1])]
                
        return out