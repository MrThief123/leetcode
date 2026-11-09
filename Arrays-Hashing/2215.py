'''
Find the distinct elements in two arrays using set operations
Convert both arrays to sets to remove duplicates
Use set difference to find elements unique to each array
Return the results as lists
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1.difference(set2)), list(set2.difference(set1))]