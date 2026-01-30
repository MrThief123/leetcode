'''
1496. Path Crossing
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west respectively. You start at the origin (0, 0) on a 2D plane and walk according to the directions in path.
Return true if the path crosses itself at any point, that is, if at any time you
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()

        direction = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}

        curr = (0, 0)

        seen.add(curr)

        for i in path:
            curr = (curr[0] + direction[i][0], curr[1] + direction[i][1])
            
            if curr in seen:
                return True
            seen.add(curr)
        return False