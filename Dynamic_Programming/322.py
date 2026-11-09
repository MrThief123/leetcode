'''
322. Coin Change
Use dynamic programming to find the minimum number of coins needed to make up a given amount.
Maintain a dp array where dp[i] represents the minimum coins needed for amount i.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
