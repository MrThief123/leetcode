"""
2124. Check if All A's Appears Before All B's  [Easy]

Approach (track latest 'a' and earliest 'b'):
  - s is beautiful (only 'a's and 'b's with all 'a's before all 'b's) as
    long as the earliest 'b' doesn't come before the latest 'a'.
  - Scan once, tracking the last index seen with 'a' and the first index
    seen with 'b'; compare them at the end (either missing means trivially
    true).

Complexity: O(n) time, O(1) space
"""

class Solution:
    def checkString(self, s: str) -> bool:
        if not s:
            return True

        earliest_b = -1
        latest_a = -1

        for n, i in enumerate(s):
            if i == 'a':
                latest_a = n
            elif earliest_b == -1:
                earliest_b = n

        if latest_a == -1 or earliest_b == -1:
            return True

        if earliest_b > latest_a:
            return True

        return False
