"""
392. Is Subsequence  [Easy]

Approach (two pointers):
  - Walk through t; each time it matches s[curr], advance curr.
  - If curr reaches the end of s, every character was found in order.

NOTE: `n` is never defined (should be len(s)), so this raises NameError on a
      match. Left unchanged here; the fix is `if curr == len(s)`.

Complexity: O(len(t)) time, O(1) space
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        curr = 0  # next character of s to match
        i = 0     # position in t

        while i < len(t):
            if s[curr] == t[i]:
                curr += 1
                if curr == n:  # BUG: `n` undefined (see NOTE)
                    return True
            i += 1
        return False
