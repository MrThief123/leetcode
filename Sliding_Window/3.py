"""
3. Longest Substring Without Repeating Characters  [Medium]

Approach (sliding window + set):
  - Grow the window by moving `right`.
  - If s[right] is already in the window, shrink from `left` until it is removed.
  - Track the longest window length.

Complexity: O(n) time, O(min(n, alphabet)) space
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0

        charSet = set()  # characters currently in the window

        if len(s) <= 1:
            return len(s)

        left = 0

        for right in range(len(s)):

            # Duplicate found: shrink from the left until it's gone
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])

            best = max(best, right - left + 1)

        return best
