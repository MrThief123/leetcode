"""
1162. As Far from Land as Possible  [Medium]

Approach (multi-source BFS):
  - Start from all land cells at once and expand outward one layer at a time.
  - The number of layers needed to cover all water is the largest distance to land.
  - All land or all water -> -1.

Complexity: O(rows * cols) time, O(rows * cols) space
"""

from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        # 1. Add all land cells to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i, j))

        # Edge cases: all land or all water
        if not q or len(q) == rows * cols:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = -1  # becomes the number of layers expanded minus the land layer

        # 2. Multi-source BFS
        # expand from all land cells simultaneously
        while q:
            distance += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 2  # mark visited water as "processed"
                        q.append((nr, nc))

        return distance
