"""
1137. N-th Tribonacci Number  [Easy]

Approach (bottom-up DP):
  - T(0) = 0, T(1) = 1, T(2) = 1, and T(n) = T(n-1) + T(n-2) + T(n-3).
  - Fill a table up to n (n <= 37 by the constraints, hence the 38 slots).

Complexity: O(n) time, O(1) space (fixed-size table)
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0 for i in range(38)]  # indices 0..37

        # Base cases
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]
