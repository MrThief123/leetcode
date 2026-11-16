"""
28. Find the Index of the First Occurrence in a String  [Easy]

Approach (brute-force window):
  - Slide a start index `left` across the haystack.
  - At each start, compare needle character by character with `right`.
  - A full match returns the start; otherwise reset and advance.

Complexity: O(n * m) time, O(1) space
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0   # start position in haystack
        right = 0  # how many needle characters have matched

        h_len = len(haystack)
        n_len = len(needle)

        while left <= h_len - n_len:

            # Extend the match as far as it goes
            while right < n_len and haystack[left+right] == needle[right]:
                right += 1

            if right == n_len:
                return left
            else:
                # Mismatch: restart matching from the next start position
                right = 0
                left += 1
        return -1
