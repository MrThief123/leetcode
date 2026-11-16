"""
1266. Minimum Time Visiting All Points  [Easy]

Approach:
  - Each second you can move one step horizontally, vertically or diagonally.
  - Between two points the time is max(|dx|, |dy|): go diagonally for min(|dx|, |dy|)
    steps, then straight for the remaining difference.
  - Sum this for every consecutive pair of points.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        out = 0

        if n < 2:
            return 0

        # prev = points[n], curr = the next point to reach
        for n, prev in enumerate(points[:-1]):
            curr = points[n+1]
            x_diff = abs(curr[0] - prev[0])
            y_diff = abs(curr[1] - prev[1])

            # check if either x or y difference is zero aka same row or column
            if not x_diff or not y_diff:
                out += max(x_diff, y_diff)
            else:
                out += min(x_diff, y_diff)                    # diagonal steps
                out += max(x_diff - y_diff, y_diff - x_diff)  # remaining straight steps = |x_diff - y_diff|

        return out
