"""
2706. Buy Two Chocolates  [Easy]

Approach:
  - Track the two cheapest prices in one pass.
  - If their sum fits the budget, return the leftover money, else return money unchanged.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a, b = float('inf'), float('inf')  # smallest, second smallest

        for i in prices:
            if i <= a:
                b = a  # old smallest becomes second smallest
                a = i
            elif i < b:
                b = i

        if a + b <= money:
            return money - a - b
        return money
