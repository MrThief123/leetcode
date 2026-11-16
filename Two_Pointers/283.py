"""
283. Move Zeroes  [Easy]

Approach (two pointers, stable partition):
  - `left` is where the next non-zero belongs.
  - Scan with i; swap each non-zero into position `left` and advance it.
  - Zeros end up at the back, order of non-zeros preserved.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        left = 0  # next slot for a non-zero value

        if n == 1:
            return

        for i in range(n):
            if nums[i] != 0:
                # Swap the non-zero forward
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1
