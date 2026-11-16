"""
62. Unique Paths  [Medium]

Approach (2D DP):
  - dp[i][j] = number of paths to cell (i, j) moving only right or down.
  - First row and column have exactly one path each.
  - Every other cell is the sum of the cell above and the cell to the left.

Complexity: O(m * n) time, O(m * n) space
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # A single row or column has exactly one route
        if m == 1 or n == 1:
            return 1

        dp = [[0] * n for _ in range(m)]

        # Edges: only one way to reach them
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Paths into (i, j) come from above or from the left
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
