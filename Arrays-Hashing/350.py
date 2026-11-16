"""
350. Intersection of Two Arrays II  [Easy]

Approach:
  - Count each element in both arrays.
  - For every shared element, include it min(count1, count2) times.

Complexity: O(n + m) time, O(n + m) space
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        out = []

        count1 = Counter(nums1)
        count2 = Counter(nums2)

        for key in count1.keys():
            if key in count2:
                best = min(count1[key], count2[key])  # shared copies
                out.extend([key for i in range(best)])

        return out
