"""
5. Longest Palindromic Substring  [Medium]

Approach (expand around centre):
  - Every palindrome has a centre: a character (odd length) or a gap between
    two characters (even length).
  - Expand outward from each centre while both ends match, keeping the longest.

Complexity: O(n^2) time, O(1) extra space
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = 0   # length of the best palindrome so far
        out = ""
        n = len(s)

        for i in range(n):
            # check odd length (centre at i)
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > best:
                    best = right - left + 1
                    out = s[left:right+1]
                left -= 1
                right += 1

            # check even length (centre between i and i+1)
            left = i
            right = i+1

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > best:
                    best = right - left + 1
                    out = s[left:right+1]
                left -= 1
                right += 1

        return out
