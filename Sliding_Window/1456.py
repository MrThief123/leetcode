"""
1456. Maximum Number of Vowels in a Substring of Given Length  [Medium]

Approach (fixed-size sliding window):
  - Count vowels in the first k-1 characters.
  - Each step adds the new character, records the count, then removes the oldest.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0  # vowels in the current window
        out = 0

        # Prime the window with the first k-1 characters
        for i in range(k-1):
            if s[i] in vowels:
                count += 1

        out = count

        left = 0       # oldest character
        right = k - 1  # newest character

        while right < n:
            if s[right] in vowels:
                count += 1

            out = max(out, count)

            # Slide: drop the oldest character
            if s[left] in vowels:
                count -= 1
            left += 1
            right += 1

        return out
