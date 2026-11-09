'''
42. Trapping Rain Water
Use two-pointer technique to calculate trapped water.
Track maximum heights from both ends
Move smaller height pointer inward and calculate trapped water at each step.
    = min(max_left, max_right) - height[current]
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        out = 0

        # Initialize max heights from both ends
        max_left = height[0]
        max_right = height[-1]

        # Two-pointer traversal
        while left < right:
            # Move the pointer with the smaller height
            if max_left < max_right:
                left += 1

                # Update max_left and calculate trapped water
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    out += min(max_left, max_right) - height[left]
            else:
                right -= 1

                if height[right] > max_right:
                    max_right = height[right]
                else:
                    out += min(max_left, max_right) - height[right]

        return out