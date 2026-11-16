"""
695. Max Area of Island  [Medium]

Approach (DFS flood fill):
  - From each land cell, DFS returns the island's area, sinking cells (set to 0) as it goes.
  - Track the maximum area.

Complexity: O(rows * cols) time, O(rows * cols) space (recursion)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        # Area of the island reachable from (r, c)
        def dfs(r, c):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or grid[r][c] == 0
            ):
                return 0  # out of bounds or water

            grid[r][c] = 0 # set as visited
            area = 1  # Current cell

            # Explore all four directions
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
