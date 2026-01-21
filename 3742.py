'''
3742. Maximum Path Score in a Grid
Use dynamic programming to track the maximum score achievable at each cell given the cost constraints.
Keep a 3D DP array where dp[i][j][c] represents the maximum score at cell (i, j) using cost c.
'''

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

        return max(dp[m - 1][n - 1])
