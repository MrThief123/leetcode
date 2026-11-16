"""
435. Non-overlapping Intervals  [Medium]

Approach (greedy, keep the interval that ends earliest):
  - Sort by start and track the end of the last kept interval.
  - No overlap: keep the interval and move prevEnd.
  - Overlap: one interval must be removed; remove the one with the later end
    (keep min(end, prevEnd)) so future intervals have the most room.

Complexity: O(n log n) time, O(1) extra space
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0  # intervals removed

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # not overlap
            if start >= prevEnd:
                prevEnd = end
            # if overlap
            else:
                res += 1                   # remove one of the two
                prevEnd = min(end, prevEnd)  # keep the one that ends sooner
        return res
