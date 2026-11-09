'''
Using Dynamic Programming to find the number of unique paths in an m x n grid
Set up a 2D array to store the number of unique paths to each cell
Initialize the first row and first column to 1 since there's only one way to reach those cells
Iterate through the grid starting from cell (1,1) and fill in the number of unique paths to each cell
The number of unique paths to reach cell (i,j) 
is the sum of the unique paths to reach the cell directly above it and the cell directly to the left of it
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
