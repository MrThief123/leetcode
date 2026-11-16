"""
2414. Longest Continuous Increasing Substring  [Easy]

Approach:
  - Build the current substring one character at a time.
  - If the new character isn't exactly one more than the last, drop characters
    from the end until it is (or the substring is empty), then append.
  - Track the longest length reached.

Complexity: O(n) amortised time, O(n) space
"""

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        out = 0
        substring = ""  # current alphabetical run

        for i in s:
            # Not a valid continuation: shrink until it is
            while substring and ord(i) - ord(substring[-1]) != 1:
                substring = substring[:-1]
            substring += i
            out = max(out, len(substring))

        return out
