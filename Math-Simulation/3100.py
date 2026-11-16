"""
3100. Water Bottles II  [Medium]

Approach (simulation):
  - Unlike problem 1518, every exchange makes the required numExchange grow by 1.
  - Drink all full bottles. While empties >= numExchange, trade them for one full
    bottle at a time (bumping numExchange after each trade).
  - Drink the new bottles (they become empties) and repeat.

Complexity: O(sqrt(n)) time, O(1) space
"""

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        out = numBottles  # bottles drunk so far

        while numBottles >= numExchange:
            temp = 0  # bottles gained this round
            while numBottles >= numExchange:
                temp += 1
                out += 1                       # drink the new bottle
                numBottles = numBottles - numExchange
                numExchange += 1               # price goes up after each exchange

            # Newly drunk bottles are now empty and can be exchanged next round
            numBottles += temp

        return out
