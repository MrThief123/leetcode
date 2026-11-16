"""
3760. Maximum Substrings With Distinct Start  [Medium]

Approach:
  - Each substring needs a distinct first character, so there can be at most one
    substring per distinct letter, and that many is always achievable.
  - The answer is the number of distinct characters in s.

Complexity: O(n) time, O(1) space (26 letters)
"""

class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
