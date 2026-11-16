"""
17. Letter Combinations of a Phone Number  [Medium]

Approach (backtracking):
  - Map each digit to its keypad letters.
  - Build a combination one position at a time: for the current digit, try each
    of its letters and recurse on the next digit.
  - When the path has one letter per digit, record it.

Complexity: O(4^n * n) time, O(n) recursion depth (plus output)
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        # Digit -> letters on a phone keypad
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []
        n = len(digits)

        # index = which digit we're choosing a letter for, path = letters so far
        def backtrack(index, path):
            if index == n:
                result.append(path)  # one letter chosen per digit
                return

            for letter in phone[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result
