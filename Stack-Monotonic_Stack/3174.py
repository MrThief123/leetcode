"""
3174. Clear Digits  [Easy]

Approach (stack):
  - Letters are pushed.
  - A digit deletes the closest non-digit to its left, i.e. pops the last letter.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        out = []  # acts as the stack

        for i in s:
            if i.isalpha():
                out.append(i)
            else:
                # Digit: remove the nearest letter on its left
                if out and out[-1].isalpha():
                    out.pop()
        return ''.join(out)
