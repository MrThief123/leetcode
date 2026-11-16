"""
657. Robot Return to Origin  [Easy]

Approach:
  - The robot returns to the origin iff it moves as often up as down
    and as often left as right.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter

        count = Counter(moves)

        # Vertical and horizontal moves must each cancel out
        if count['U'] == count['D'] and count['L'] == count['R']:
            return True
        return False
