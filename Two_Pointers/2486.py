"""
2486. Append Characters to String to Make Subsequence  [Medium]

Approach (greedy two pointers):
  - Match as many leading characters of t as possible as a subsequence of s.
  - Whatever is left of t must be appended.

Complexity: O(n + m) time, O(1) space
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        i = 0  # pointer in s
        j = 0  # pointer in t (characters of t matched so far)

        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i += 1

        return m - j  # unmatched tail of t
