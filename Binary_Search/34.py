'''
Use binary search to find the first and last positions of a target value in a sorted array
Utilize bisect module to find the leftmost and rightmost indices of the target
Return [-1, -1] if the target is not found, otherwise return the found indices
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        a = bisect.bisect_left(nums, target)
        b = bisect.bisect_right(nums, target)

        if a == b :
            return [-1, -1]
        return [a, b-1]        