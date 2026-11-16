"""
9. Palindrome Number  [Easy]

Approach:
  - Compare the string form of x with its reverse.
  - (A numeric version could reverse half the digits to avoid the string.)

Complexity: O(d) time, O(d) space (d = digits)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
