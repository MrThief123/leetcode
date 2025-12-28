'''
Using Backtracking to generate all possible letter combinations for a given digit string
Create a mapping of digits to their corresponding letters on a phone keypad
Use a helper function to perform backtracking, building combinations one letter at a time
When the current combination reaches the length of the input digits, add it to the result list'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []
        n = len(digits)

        def backtrack(index, path):
            if index == n:
                result.append(path)
                return

            for letter in phone[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result
