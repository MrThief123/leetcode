'''
350. Intersection of Two Arrays II
keep track of the counts of each element in both arrays using hash maps,
then find the common elements and their minimum counts.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        out = []

        count1 = Counter(nums1)
        count2 = Counter(nums2)

        for key in count1.keys():
            if key in count2:
                best = min(count1[key], count2[key])
                out.extend([key for i in range(best)])

        return out