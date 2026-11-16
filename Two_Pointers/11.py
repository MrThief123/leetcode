"""
11. Container With Most Water  [Medium]

Approach (two pointers from both ends):
  - Area = width * min(left height, right height).
  - Move the shorter wall inward: moving the taller one can only shrink the area.

Complexity: O(n) time, O(1) space
"""

# Version 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        point1 = 0                    # left wall
        point2 = len(height) - 1      # right wall

        max_cap = 0

        while point1 < point2:
            area = (point2 - point1) * min(height[point1], height[point2])
            max_cap = max(area, max_cap)

            # Advance the shorter wall in search of a taller one
            if height[point1] < height[point2]:
                point1 += 1
            else:
                point2 -= 1

        return max_cap


# Version 2: same logic, different variable names
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:
            maximum = max(min(height[left], height[right]) * (right - left), maximum)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum
