"""
34. Find First and Last Position of Element in Sorted Array  [Medium]

Approach (binary search via bisect):
  - bisect_left gives the first index of target; bisect_right gives one past the last.
  - If they are equal the target is absent.

Complexity: O(log n) time, O(1) space
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        a = bisect.bisect_left(nums, target)    # first position >= target
        b = bisect.bisect_right(nums, target)   # first position > target

        if a == b:
            return [-1, -1]  # target not present
        return [a, b-1]
