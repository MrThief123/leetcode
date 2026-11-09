'''
452. Minimum Number of Arrows to Burst Balloons
Sort the balloons by their start position. 
Then, iterate through the balloons and keep track of the best start and end positions for the current arrow. 
If the next balloon is fully in front of the current arrow, we need to shoot a new arrow and update the best start and end positions. 
If the next balloon is in between, we update the best start and end positions to be the intersection of the current arrow 
and the next balloon.
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        out = 1
        best_start = points[0][0]
        best_end = points[0][1]

        for start, end in points[1:]:
            # fully in front
            if start > best_end:
                out += 1
                best_start = start
                best_end = end
            else: # in between
                best_start = min(start, best_start)
                best_end = min(end, best_end)

        return out
