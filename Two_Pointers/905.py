"""
905. Sort Array By Parity  [Easy]

Approach (partition with two pointers):
  - `left` is the boundary of the even section.
  - Each even number found is swapped into `left`, then the boundary advances.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0  # next slot for an even number

        for i in range(len(nums)):
            temp = nums[i]
            if nums[i] % 2 == 0:
                # Swap the even number into the front section
                nums[i] = nums[left]
                nums[left] = temp
                left += 1

        return nums
