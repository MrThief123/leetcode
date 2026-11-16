"""
189. Rotate Array  [Medium]

Approach (copy to rotated position):
  - Element at index i belongs at (i + k) % n.
  - Write into a temp array, then copy back to modify nums in place.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [0 for i in range(n)]

        # Place each element at its rotated position
        for i in range(n):
            temp[(i+k)%n] = nums[i]

        # Copy back into the original list
        for i in range(n):
            nums[i] = temp[i]
