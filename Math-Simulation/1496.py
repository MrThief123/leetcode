"""
1496. Path Crossing  [Easy]

Approach (set of visited points):
  - Walk the path from (0, 0), recording every position.
  - Revisiting any position means the path crosses itself.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()  # all positions visited so far

        # direction letter -> (dx, dy)
        direction = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}

        curr = (0, 0)  # start at the origin

        seen.add(curr)

        for i in path:
            curr = (curr[0] + direction[i][0], curr[1] + direction[i][1])

            if curr in seen:
                return True  # been here before
            seen.add(curr)
        return False
