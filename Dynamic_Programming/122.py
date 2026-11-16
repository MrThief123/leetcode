"""
122. Best Time to Buy and Sell Stock II  [Medium]

Approach (greedy):
  - With unlimited transactions, capture every upward step between consecutive days.
  - The sum of all positive daily differences is the maximum profit.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0

        for i in range(len(prices) - 1):
            # Price rises tomorrow: bank the gain
            if prices[i+1] > prices[i]:
                out += prices[i+1] - prices[i]

        return out
