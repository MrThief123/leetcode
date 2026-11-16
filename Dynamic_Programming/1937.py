"""
1937. Maximum Number of Points with Cost  [Medium]

Approach (DP with left/right sweeps):
  - dp[i][j] = points[i][j] + max over k of (dp[i-1][k] - |j - k|).
  - Computing that max naively is O(n^2) per row, so split by direction:
      * left sweep: best from columns to the left, losing 1 per step
      * right sweep: best from columns to the right, losing 1 per step
  - Example, previous row 1 1 10 1 1:
      left to right: 1 1 10 9 8
      right to left: 8 9 10 1 1
    The max of the two is the best value reachable from the previous row at each column.

Complexity: O(m * n) time, O(m * n) space
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        dp = [[0] * n for _ in range(m)]

        # base case: first row, no movement cost
        for j in range(n):
            dp[0][j] = points[0][j]

        for i in range(1, m):
            left = [0] * n
            right = [0] * n

            # left to right sweep
            left[0] = dp[i - 1][0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, dp[i - 1][j])

            # right to left sweep
            right[n - 1] = dp[i - 1][n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, dp[i - 1][j])

            # fill current row
            for j in range(n):
                dp[i][j] = points[i][j] + max(left[j], right[j])

        return max(dp[-1])
