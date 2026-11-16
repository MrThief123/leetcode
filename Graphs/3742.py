"""
3742. Maximum Path Score in a Grid  [Medium]

Approach (DP over cell + cost used):
  - Walk from the top-left to the bottom-right moving only right or down.
  - Cell values: 0 -> +0 score / 0 cost, 1 -> +1 score / 1 cost, 2 -> +2 score / 1 cost.
  - dp[i][j][c] = best score reaching (i, j) having spent exactly cost c (-1 = unreachable).
  - Push each state forward to the cell below and the cell to the right, staying within budget k.

Complexity: O(m * n * k) time, O(m * n * k) space
"""

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # score gained from each cell value
        score_add = {0: 0, 1: 1, 2: 2}

        # cost incurred by each cell value
        cost_add = {0: 0, 1: 1, 2: 1}

        # dp[i][j][c] = max score at (i, j) using cost c
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for cost_used in range(k + 1):

                    # Unreachable state
                    if dp[i][j][cost_used] == -1:
                        continue

                    cur_score = dp[i][j][cost_used]

                    # move down
                    if i + 1 < m:
                        new_cost = cost_used + cost_add[grid[i + 1][j]]
                        if new_cost <= k:
                            new_score = cur_score + score_add[grid[i + 1][j]]
                            dp[i + 1][j][new_cost] = max(
                                dp[i + 1][j][new_cost],
                                new_score
                            )

                    # move right
                    if j + 1 < n:
                        new_cost = cost_used + cost_add[grid[i][j + 1]]
                        if new_cost <= k:
                            new_score = cur_score + score_add[grid[i][j + 1]]
                            dp[i][j + 1][new_cost] = max(
                                dp[i][j + 1][new_cost],
                                new_score
                            )

        # Best over every cost level at the destination
        return max(dp[m - 1][n - 1])
