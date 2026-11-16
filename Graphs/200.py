"""
200. Number of Islands  [Medium]

Approach (flood fill):
  - Scan the grid; each unvisited land cell starts a new island.
  - Flood-fill the island (the helper is named bfs but is a recursive DFS) so its
    cells aren't counted again.

Complexity: O(rows * cols) time, O(rows * cols) space
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        out = 0  # islands found

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Explore the island containing (x, y)
        def bfs(x, y):
            visited[x][y] = True

            for d in directions:
                nx = x + d[0]
                ny = y + d[1]

                # Check bounds and if the cell is land and unvisited
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    bfs(nx, ny)

        # Main loop to find islands
        for i in range(rows):
            for j in range(cols):
                # If we find an unvisited land cell, it's a new island
                if grid[i][j] == '1' and visited[i][j] == False:
                    bfs(i, j)
                    out += 1

        return out
