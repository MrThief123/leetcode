"""
1221. Split a String in Balanced Strings  [Easy]

Approach (running balance):
  - +1 for 'L', -1 for 'R'.
  - Each time the balance returns to zero, a balanced substring ends; count it.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        out = 0    # balanced substrings found
        count = 0  # current balance (L minus R)

        for c in s:
            if c == 'L':
                count += 1
            else:
                count -= 1

            if not count:
                out += 1
                count = 0

        return out
