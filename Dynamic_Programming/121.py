"""
121. Best Time to Buy and Sell Stock  [Easy]

Approach (one pass):
  - Track the lowest price seen so far (the best day to have bought).
  - At each price, the best profit if we sell today is price - min_so_far.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]  # cheapest buy price seen
        out = 0                 # best profit so far

        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                out = max(out, price - min_so_far)
        return out
