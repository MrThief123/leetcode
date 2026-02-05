'''
You are given a 0-indexed 2D integer array grid of size m x n, where grid[i][j] represents the number of fish in the cell (i, j). A fisher can start at any cell and can repeatedly perform the following operations:
- Catch all the fish at cell (i, j), or
- Move to any adjacent cell (i + 1, j), (i - 1, j), (i, j + 1), or (i, j - 1) that has at least one fish. The fisher can only move to a cell if it has at least
'''

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j):
            total = grid[i][j]
            grid[i][j] = 0

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