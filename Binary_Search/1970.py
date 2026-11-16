"""
1970. Last Day Where You Can Still Cross  [Hard]

Approach (reverse time + Union-Find):
  - Instead of flooding cells, process days backwards and "un-flood" them.
  - Union each new land cell with adjacent land cells.
  - Two virtual nodes represent the top and bottom edges; the first time (going
    backwards) they connect is the last day a crossing is possible.

Complexity: O(row * col * alpha) time, O(row * col) space
"""

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        # Helper functions for Union-Find
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])  # path compression
            return parents[x]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            if ua != ub:
                parents[ua] = ub

        # Total nodes = grid cells + 2 virtual nodes
        N = row * col + 2
        # (named LEFT/RIGHT, but they stand for the TOP and BOTTOM edges)
        LEFT, RIGHT = row * col, row * col + 1
        parents = [i for i in range(N)]

        # Water array: True = flooded, False = land
        water = [True] * (row * col)  # start all flooded, will un-flood backward

        # Directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Convert 2D coordinate to DSU index
        def idx(r, c):
            return r * col + c

        # Start from the last day and go backwards
        for day in range(len(cells)-1, -1, -1):
            r, c = cells[day]
            r -= 1  # convert to 0-indexed
            c -= 1

            water[idx(r, c)] = False  # make this cell land

            # Union with neighbors if they are land
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and not water[idx(nr, nc)]:
                    uunion(idx(r, c), idx(nr, nc))

            # Union with virtual nodes if on top/bottom row
            if r == 0:
                uunion(idx(r, c), LEFT)
            if r == row - 1:
                uunion(idx(r, c), RIGHT)

            # Check if top is connected to bottom
            if ufind(LEFT) == ufind(RIGHT):
                return day  # day cells[0..day-1] are flooded, so day is the last crossable day

        return 0
