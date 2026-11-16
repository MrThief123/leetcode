"""
69. Sqrt(x)  [Easy]

Approach (binary search on the answer):
  - Search 0..x for the largest integer whose square is <= x.
  - When the loop ends, `right` is that largest value (floor of the root).

Complexity: O(log x) time, O(1) space
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2  # avoids overflow in other languages
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right  # floor(sqrt(x))
