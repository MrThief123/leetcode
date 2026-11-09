'''
169. Majority Element
Greedy approach to find the maximum profit from stock prices by tracking the minimum price so far and calculating potential profits.
Keep track of the minimum price encountered and update the maximum profit accordingly.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        out = 0

        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                out = max(out, price - min_so_far)
        return out