"""
20. Valid Parentheses  [Easy]

Approach (stack):
  - Push opening brackets.
  - For a closing bracket, the top of the stack must be its matching opener; pop it.
  - Valid only if every character was matched (count of matches == len / 2).

Complexity: O(n) time, O(n) space
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        # closing bracket -> its opening partner
        lookup = {

            ')': '(',
            '}': '{',
            ']': '['
        }

        count = 0  # number of matched pairs

        for i in s:
            # opening bracket
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if stack and lookup[i] == stack[-1]:
                    stack.pop()
                    count += 1
                else:
                    return False  # wrong or missing opener

        # All characters matched in pairs (this also rejects leftover openers)
        if len(s) / 2.0 == count:
            return True

        return False
