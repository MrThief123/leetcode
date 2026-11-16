"""
830. Positions of Large Groups  [Easy]

Approach (two pointers over runs):
  - `left` marks the start of a run; `right` extends while the next char is equal.
  - A run of length >= 3 is a large group; record [start, end].
  - Jump to the character after the run and repeat.

Complexity: O(n) time, O(1) extra space
"""

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        out = []
        n = len(s)

        if n < 3:
            return out

        left = 0
        right = 0

        while right < n:
            # Extend the run while the next character matches
            while right + 1 < n and s[left] == s[right+1]:
                right += 1

            if right - left >= 2:  # length >= 3
                out.append([left, right])
            # Start the next run right after this one
            left = right + 1
            right = left

        return out
