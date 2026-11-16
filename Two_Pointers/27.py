"""
27. Remove Element  [Easy]

Approach:
  - Replace every occurrence of val with infinity and count the survivors.
  - Sorting then pushes the infinities to the back, leaving the kept values in front.
  - (A true two-pointer overwrite would be O(n); this version is O(n log n).)

NOTE: the print() is leftover debug output and `inf` relies on LeetCode's
      pre-imported math.inf.

Complexity: O(n log n) time, O(1) space
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        out = len(nums)  # count of elements that remain
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = inf  # mark for removal
                out -= 1

        print(nums.sort())  # sorts in place; print shows None (debug leftover)
        return out
