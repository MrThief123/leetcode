"""
605. Can Place Flowers  [Easy]

Approach (greedy planting):
  - Plant at index i if it and both neighbours are empty.
  - max/min clamp the neighbour indices so the edges act as if they have empty neighbours.
  - Planting as early as possible never reduces the total that fit.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        for i in range(0, len(flowerbed)):
            # Empty spot with empty neighbours (clamped at the ends)
            if flowerbed[i] == 0 and flowerbed[max(i-1, 0)] == 0 and flowerbed[min(i+1, len(flowerbed) - 1)] == 0:
                flowerbed[i] = 1  # plant

                n -= 1

                if n == 0:
                    return True

        return False
