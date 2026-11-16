"""
57. Insert Interval  [Medium]

Approach (single pass over sorted, non-overlapping intervals):
  - Intervals entirely before newInterval are copied unchanged.
  - On reaching one entirely after it, emit newInterval and carry on with that interval.
  - Overlapping intervals are absorbed into newInterval by widening its bounds.

Complexity: O(n) time, O(n) space
"""

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

            # Case 3: overlapping intervals: merge into newInterval
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])

        out.append(newInterval)  # the final (possibly merged) interval
        return out
