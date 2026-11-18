"""
2914. Minimum Number of Changes to Make Binary String Beautiful  [Medium]

Approach (pairwise check):
  - A beautiful string splits into blocks of equal consecutive characters,
    each of even length -> every adjacent pair (s[0], s[1]), (s[2], s[3]), ...
    can be made equal independently.
  - For each pair that differs, one change fixes it, so count mismatched
    pairs.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def minChanges(self, s: str) -> int:
        out = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                out += 1

        return out
