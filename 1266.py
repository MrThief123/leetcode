'''
1266. Minimum Time Visiting All Points
Calculate the minimum time to visit all points in order, considering diagonal and straight moves.
'''

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        out = 0

        if n < 2:
            return 0

        for n, prev in enumerate(points[:-1]):
            curr = points[n+1]
            x_diff = abs(curr[0] - prev[0])
            y_diff =  abs(curr[1] - prev[1])
    
            # check if either x or y difference is zero aka same row or column
            if not x_diff or not y_diff:
                out += max(x_diff, y_diff)
            else:
                out += min(x_diff, y_diff)
                out += max(x_diff - y_diff, y_diff - x_diff)

        return out