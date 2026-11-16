"""
455. Assign Cookies  [Easy]

Approach (sort + two pointers):
  - Sort children by greed and cookies by size.
  - Offer the smallest remaining cookie to the least greedy remaining child;
    if it's too small, try the next bigger cookie.

Complexity: O(n log n + m log m) time, O(n + m) space
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)  # children's greed factors
        s = sorted(s)  # cookie sizes

        left, right = 0, 0  # left: child, right: cookie

        out = 0

        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                out += 1    # child satisfied
                right += 1
                left += 1
            else:
                right += 1  # cookie too small, try a larger one

        return out
