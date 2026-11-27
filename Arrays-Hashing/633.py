"""
633. Sum of Square Numbers  [Medium]

Approach (hash set of squares):
  - Precompute every perfect square up to c into a set.
  - c is expressible as a^2 + b^2 iff some square i in the set has its
    complement (c - i) also in the set.

Complexity: O(sqrt(c)) time, O(sqrt(c)) space
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c in (0,1):
            return True

        i = 0
        square = 0
        temp = set()

        while square < c:
            square = i*i
            temp.add(square)
            i += 1

        for i in temp:
            if c-i in temp:
                return True
        return False
