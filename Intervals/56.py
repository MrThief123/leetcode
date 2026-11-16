"""
56. Merge Intervals  [Medium]

Approach (sort by start, then sweep):
  - After sorting by start, only the last merged interval can overlap the next one.
  - If the next interval starts after the last one ends, append it; else extend the end.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # sorts by start, then end

        out = [intervals[0]]  # merged intervals so far

        for i in intervals[1:]:
            prev = out[-1]

            # not overlap
            if prev[1] < i[0]:
                out.append(i)
            # if overlap update the prev
            else:
                out[-1] = [min(i[0], prev[0]), max(i[1], prev[1])]

        return out
