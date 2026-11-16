"""
1431. Kids With the Greatest Number of Candies  [Easy]

Approach:
  - Find the current maximum.
  - A kid can be the greatest if candies + extraCandies reaches that maximum.

Complexity: O(n) time, O(n) space (output list)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        largest = max(candies)

        # One boolean per kid
        out = [i + extraCandies >= largest for i in candies]

        return out
