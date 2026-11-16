"""
441. Arranging Coins  [Easy]

Approach (simulation):
  - Fill row 1 with 1 coin, row 2 with 2 coins, ...
  - Stop when the remaining coins can't complete the next row; the number of
    complete rows is the answer.
  - (Binary search or the quadratic formula would be O(log n) / O(1).)

Complexity: O(sqrt(n)) time, O(1) space
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0  # current row number
        while n >= 0:
            i += 1
            n = n - i  # spend i coins on row i
        return i - 1   # the last row went negative, so it wasn't completed
