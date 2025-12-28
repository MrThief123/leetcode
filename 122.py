'''
Loop through the list of prices
If the price of the next day is greater than the current day,
add the difference to the output variable
Return the output variable
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0

        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                out += prices[i+1] - prices[i]

        return out