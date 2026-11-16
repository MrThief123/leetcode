"""
345. Reverse Vowels of a String  [Easy]

Approach (two pointers from both ends):
  - Move each pointer inward until it sits on a vowel, then swap them.
  - Strings are immutable, so work on a list and join at the end.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        s_list = list(s)  # mutable copy

        left = 0
        right = len(s_list) - 1

        while left < right:
            # Skip non-vowels from each side
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1

            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        return "".join(s_list)
