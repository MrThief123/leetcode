"""
322. Coin Change  [Medium]

Approach (unbounded knapsack DP):
  - dp[i] = fewest coins needed to make amount i.
  - For each coin, dp[i] = min(dp[i], dp[i - coin] + 1).
  - Amount unreachable -> -1.

Complexity: O(amount * len(coins)) time, O(amount) space
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0  # zero coins make amount 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
