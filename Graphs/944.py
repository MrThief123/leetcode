"""
944. Rotting Oranges  [Medium]

Approach (multi-source BFS):
  - Start the queue with every rotten orange; each BFS layer is one minute.
  - Rot adjacent fresh oranges and count down the fresh total.
  - If none are left fresh, the answer is the number of layers - 1 (the last
    layer rots nothing new); otherwise some are unreachable -> -1.

Complexity: O(rows * cols) time, O(rows * cols) space
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()  # rotten oranges to spread from
        fresh = 0        # fresh oranges remaining
        seen = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Seed the BFS with all rotten oranges and count the fresh ones
        for i in range(rows):
            for j in range(columns):
                curr = (i, j)
                if grid[i][j] == 2:
                    seen.add(curr)
                    queue.append(curr)
                elif grid[i][j] == 1:
                    fresh += 1

        # Nothing to rot
        if fresh == 0:
            return 0

        minutes = 0

        while queue:
            minutes += 1

            # mutli source bfs: process the whole current layer
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for nx, ny in directions:
                    nx = x + nx
                    ny = y + ny

                    if 0 <= nx < rows and 0 <= ny < columns and grid[nx][ny] == 1 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
                        fresh -= 1

        # All fresh oranges rotted; the final layer added nothing, hence minutes - 1
        if fresh <= 0:
            return minutes - 1
        return -1
