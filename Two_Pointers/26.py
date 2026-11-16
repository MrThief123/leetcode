"""
26. Remove Duplicates from Sorted Array  [Easy]

Approach (slow/fast pointers):
  - unique_index marks the last unique value written.
  - When the scan finds a different value, write it just after unique_index.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer for the position of unique elements
        unique_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        # The number of unique elements is unique_index + 1
        return unique_index + 1
