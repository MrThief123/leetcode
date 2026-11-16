"""
151. Reverse Words in a String  [Medium]

Approach:
  - split() drops extra spaces; prepending each word to the output reverses the order.
  - Strip the trailing space at the end.

Complexity: O(n^2) worst case from repeated string prepends (O(n) with join/reversed), O(n) space
"""

class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()  # splits on any run of whitespace

        out = ""

        # Prepending acts like pushing onto a stack
        for word in words:

            out = word + " " + out

        return out.strip()
