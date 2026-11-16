"""
2658. Maximum Number of Fish in a Grid  [Medium]

A fisher starts anywhere on a water cell (value > 0) and can move between
adjacent water cells, catching all fish along the way.

Approach (DFS over connected water components):
  - DFS sums the fish in each connected component, zeroing cells as it goes.
  - The answer is the largest component sum.

Complexity: O(rows * cols) time, O(rows * cols) space (recursion)
"""

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Total fish in the component containing (i, j)
        def dfs(i, j):
            total = grid[i][j]
            grid[i][j] = 0  # mark visited

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != 0:
                    total += dfs(ni, nj)

            return total

        out = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    out = max(out, dfs(i, j))

        return out
