"""
521. Longest Uncommon Subsequence I  [Easy]

Approach:
  - If a == b, every subsequence of one is also a subsequence of the
    other, so no uncommon subsequence exists -> -1.
  - Otherwise, the longer of the two strings (or either, if equal length)
    can't be a subsequence of the other: a shorter string can't contain a
    longer one as a subsequence, and two distinct equal-length strings
    can't be subsequences of each other either (a subsequence of the same
    length as its source must equal the source). So the answer is simply
    max(len(a), len(b)).

Complexity: O(n) time, O(1) space
"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        return max(len(a), len(b))
