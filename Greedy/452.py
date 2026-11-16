"""
452. Minimum Number of Arrows to Burst Balloons  [Medium]

Approach (greedy on overlapping groups):
  - Sort by start. Track the intersection [best_start, best_end] of the current group.
  - A balloon starting after best_end can't share the arrow: start a new arrow.
  - Otherwise shrink the shared region to the intersection with that balloon.

Complexity: O(n log n) time, O(1) extra space
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        out = 1  # arrows used (at least one)
        best_start = points[0][0]
        best_end = points[0][1]

        for start, end in points[1:]:
            # fully in front
            if start > best_end:
                out += 1
                best_start = start
                best_end = end
            else: # overlaps the current group: narrow the shared region
                best_start = min(start, best_start)
                best_end = min(end, best_end)

        return out
