'''
1937. Maximum Number of Points with Cost
Use dp with left and right sweeps to optimize the transition.

If we have row 1 1 10 1 1 
Then the best we can do for the next row is:
- from left to right: 1 1 10 9 8
- from right to left: 8 9 10 1 1
Taking the max of these two gives us the best possible previous row values for each column in the current row.
'''

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