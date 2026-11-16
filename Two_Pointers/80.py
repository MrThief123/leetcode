"""
80. Remove Duplicates from Sorted Array II  [Medium]

Approach:
  - Count occurrences, then write each value back at most twice.
  - Insertion-ordered Counter keeps the sorted order of the input.
  - (A pure two-pointer version would avoid the extra Counter memory.)

Complexity: O(n) time, O(n) space
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)

        k = 0  # write position / length of the result

        for i, c in count.items():

            # Keep at most two copies of each value
            for j in range(min(c, 2)):
                nums[k] = i
                k += 1

        return k
