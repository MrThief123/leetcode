"""
1518. Water Bottles  [Easy]

Approach (simulation):
  - Drink all full bottles; empties are exchanged numExchange-for-1.
  - Each round: new full bottles = empties // numExchange; leftover empties
    carry over, plus the newly emptied bottles after drinking them.
  - Stop when no exchange is possible.

Complexity: O(log n) time, O(1) space
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        out = numBottles  # bottles drunk so far (all initial ones)

        while numBottles // numExchange > 0:
            out += numBottles // numExchange  # drink the exchanged bottles
            # Empties now = those just drunk + leftovers that couldn't be exchanged
            numBottles = numBottles // numExchange + numBottles % numExchange

        return out
