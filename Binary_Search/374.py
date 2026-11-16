"""
374. Guess Number Higher or Lower  [Easy]

Approach (classic binary search):
  - guess(mid) returns 0 if correct, -1 if the pick is lower, 1 if higher.
  - Narrow the range accordingly.

Complexity: O(log n) time, O(1) space
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)  # provided by LeetCode

            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1  # pick is lower than mid
            else:
                left = mid + 1   # pick is higher than mid
