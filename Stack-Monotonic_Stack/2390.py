"""
2390. Removing Stars From a String  [Medium]

Approach (stack):
  - Push normal characters.
  - A star removes the closest non-star character to its left, i.e. pops the stack.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()  # delete the nearest character on the left
            else:
                stack.append(char)

        return "".join(stack)
