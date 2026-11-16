"""
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts  [Medium]

Approach:
  - The biggest piece uses the biggest horizontal gap and the biggest vertical gap.
  - Sort the cuts, add the cake edges (0 and h / w), and find each max gap.
  - Return the product mod 1e9 + 7.

Complexity: O(n log n + m log m) time, O(n + m) space
"""

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        # Add the cake borders so the first/last gaps are counted
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        max_w = 0  # widest vertical gap
        max_h = 0  # tallest horizontal gap

        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i-1])

        return max_w*max_h % (pow(10, 9) + 7)
