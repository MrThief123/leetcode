"""
2215. Find the Difference of Two Arrays  [Easy]

Approach (set difference):
  - Convert both arrays to sets to drop duplicates.
  - Answer is [elements only in nums1, elements only in nums2].

Complexity: O(n + m) time, O(n + m) space
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1.difference(set2)), list(set2.difference(set1))]
